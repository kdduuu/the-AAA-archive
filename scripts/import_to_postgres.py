# ==========================================================
# The AAA Archive
# Arquivo: import_to_postgres.py
#
# Objetivo:
# Importar os dados dos arquivos CSV do projeto para o PostgreSQL.
#
# Fluxo:
#
# data/games.csv
# data/awards.csv
#        ↓
# Python + Pandas
#        ↓
# scripts/database.py
#        ↓
# PostgreSQL
#        ↓
# tabelas games e awards
#
# Este script NÃO altera a API.
# Este script NÃO altera o dashboard.
# Ele apenas sincroniza os CSVs editoriais com o banco.
#
# Autor: Kadu Almeida
# ==========================================================


# ==========================================================
# IMPORTAÇÃO DOS MÓDULOS
# ==========================================================

from pathlib import Path

import pandas as pd

# A conexão com o PostgreSQL fica centralizada em database.py.
#
# Dessa forma, este script usa as mesmas configurações do:
#
# - test_database.py;
# - api/main.py;
# - dashboard/dashboard_helpers.py.
#
# O database.py lê as credenciais do arquivo .env.
from database import conectar_postgres


# ==========================================================
# CONFIGURAÇÃO DOS CAMINHOS DO PROJETO
# ==========================================================

# Este arquivo está dentro da pasta scripts/.
#
# Por isso, a raiz do projeto é a pasta anterior.
PROJECT_ROOT = Path(__file__).resolve().parent.parent

GAMES_CSV_PATH = PROJECT_ROOT / "data" / "games.csv"
AWARDS_CSV_PATH = PROJECT_ROOT / "data" / "awards.csv"


# ==========================================================
# COLUNAS ESPERADAS
# ==========================================================

# Essas listas funcionam como uma validação básica do contrato
# definido nos dicionários de dados.
COLUNAS_GAMES = [
    "id",
    "nome",
    "ano_lancamento",
    "genero",
    "developer",
    "franchise",
    "descricao",
    "metacritic",
    "nota_kadu",
    "nota_pavam",
    "historico_importante",
    "historico_influente",
]

COLUNAS_AWARDS = [
    "ano",
    "premiacao",
    "jogo",
    "status",
]


# ==========================================================
# CONSULTAS FIXAS DE CONTAGEM
# ==========================================================

# Evitamos montar nomes de tabelas diretamente com f-string.
#
# Como o script só precisa contar duas tabelas conhecidas,
# mantemos as consultas permitidas em um dicionário fixo.
CONSULTAS_CONTAGEM = {
    "games": "SELECT COUNT(*) FROM games;",
    "awards": "SELECT COUNT(*) FROM awards;",
}


# ==========================================================
# FUNÇÕES AUXILIARES DE TRATAMENTO DE DADOS
# ==========================================================

def tratar_valor(valor):
    """
    Trata valores vazios antes de inserir no PostgreSQL.

    Valores vazios do Pandas, como NaN, são convertidos para None.

    No PostgreSQL:
        None do Python vira NULL.
    """

    if pd.isna(valor):
        return None

    return valor


def converter_int(valor):
    """
    Converte um valor para inteiro.

    Se o valor estiver vazio, retorna None.
    """

    valor = tratar_valor(valor)

    if valor is None:
        return None

    return int(valor)


def converter_float(valor):
    """
    Converte um valor para número decimal.

    Se o valor estiver vazio, retorna None.
    """

    valor = tratar_valor(valor)

    if valor is None:
        return None

    return float(valor)


def converter_texto(valor):
    """
    Converte um valor para texto.

    Se o valor estiver vazio, retorna None.
    """

    valor = tratar_valor(valor)

    if valor is None:
        return None

    return str(valor).strip()


def converter_booleano(valor):
    """
    Converte diferentes representações para booleano.

    Valores verdadeiros aceitos:
        True, "true", "sim", "s", "yes", "y", "1"

    Valores falsos aceitos:
        False, "false", "não", "nao", "n", "no", "0"

    Se o valor estiver vazio, retorna None.

    Se o conteúdo não for reconhecido, gera um erro para impedir
    que um valor inválido seja importado silenciosamente.
    """

    valor = tratar_valor(valor)

    if valor is None:
        return None

    if isinstance(valor, bool):
        return valor

    valor_texto = str(valor).strip().lower()

    valores_verdadeiros = {
        "true",
        "1",
        "sim",
        "s",
        "yes",
        "y",
    }

    valores_falsos = {
        "false",
        "0",
        "não",
        "nao",
        "n",
        "no",
    }

    if valor_texto in valores_verdadeiros:
        return True

    if valor_texto in valores_falsos:
        return False

    raise ValueError(
        f"Valor booleano não reconhecido: {valor!r}. "
        "Use TRUE, FALSE ou deixe o campo vazio."
    )


# ==========================================================
# FUNÇÕES DE VALIDAÇÃO DOS CSVs
# ==========================================================

def validar_arquivo_csv(caminho):
    """
    Verifica se o arquivo CSV existe antes da leitura.
    """

    if not caminho.exists():
        raise FileNotFoundError(
            f"Arquivo CSV não encontrado: {caminho}"
        )


def validar_colunas(df, colunas_esperadas, nome_arquivo):
    """
    Verifica se o CSV possui todas as colunas exigidas.

    Colunas adicionais são permitidas, mas todas as colunas
    esperadas precisam existir.
    """

    colunas_ausentes = [
        coluna
        for coluna in colunas_esperadas
        if coluna not in df.columns
    ]

    if colunas_ausentes:
        raise ValueError(
            f"O arquivo {nome_arquivo} não possui as colunas "
            f"obrigatórias: {', '.join(colunas_ausentes)}"
        )


def validar_games(df_games):
    """
    Executa validações básicas da Foundation Collection.
    """

    validar_colunas(
        df_games,
        COLUNAS_GAMES,
        "games.csv",
    )

    if df_games["id"].isna().any():
        raise ValueError(
            "games.csv possui registros sem id."
        )

    if df_games["id"].duplicated().any():
        ids_duplicados = (
            df_games.loc[
                df_games["id"].duplicated(keep=False),
                "id",
            ]
            .astype(int)
            .tolist()
        )

        raise ValueError(
            f"games.csv possui ids duplicados: {ids_duplicados}"
        )

    if df_games["nome"].isna().any():
        raise ValueError(
            "games.csv possui registros sem nome."
        )


def validar_awards(df_awards):
    """
    Executa validações básicas da Awards History.
    """

    validar_colunas(
        df_awards,
        COLUNAS_AWARDS,
        "awards.csv",
    )

    colunas_com_nulos = [
        coluna
        for coluna in COLUNAS_AWARDS
        if df_awards[coluna].isna().any()
    ]

    if colunas_com_nulos:
        raise ValueError(
            "awards.csv possui valores vazios nas colunas "
            f"obrigatórias: {', '.join(colunas_com_nulos)}"
        )

    status_permitidos = {
        "Vencedor",
        "Indicado",
    }

    status_encontrados = set(
        df_awards["status"]
        .astype(str)
        .str.strip()
    )

    status_invalidos = (
        status_encontrados - status_permitidos
    )

    if status_invalidos:
        raise ValueError(
            "awards.csv possui valores inválidos na coluna "
            f"status: {', '.join(sorted(status_invalidos))}"
        )


# ==========================================================
# FUNÇÕES DE LEITURA DOS CSVs
# ==========================================================

def carregar_csv_games():
    """
    Carrega e valida data/games.csv.
    """

    validar_arquivo_csv(GAMES_CSV_PATH)

    print(f"Lendo arquivo: {GAMES_CSV_PATH}")

    df_games = pd.read_csv(GAMES_CSV_PATH)

    validar_games(df_games)

    return df_games


def carregar_csv_awards():
    """
    Carrega e valida data/awards.csv.
    """

    validar_arquivo_csv(AWARDS_CSV_PATH)

    print(f"Lendo arquivo: {AWARDS_CSV_PATH}")

    df_awards = pd.read_csv(AWARDS_CSV_PATH)

    validar_awards(df_awards)

    return df_awards


# ==========================================================
# FUNÇÃO DE LIMPEZA DAS TABELAS
# ==========================================================

def limpar_tabelas(cursor):
    """
    Limpa as tabelas antes de uma nova importação.

    RESTART IDENTITY reinicia o id automático da tabela awards.

    As alterações fazem parte da mesma transação da importação.

    Portanto, se alguma inserção falhar, o PostgreSQL desfaz
    também a limpeza das tabelas.
    """

    cursor.execute(
        "TRUNCATE TABLE awards RESTART IDENTITY;"
    )

    cursor.execute(
        "TRUNCATE TABLE games RESTART IDENTITY;"
    )


# ==========================================================
# FUNÇÃO PARA IMPORTAR GAMES
# ==========================================================

def importar_games(cursor, df_games):
    """
    Importa os registros de games.csv para a tabela games.
    """

    sql = """
        INSERT INTO games (
            id,
            nome,
            ano_lancamento,
            genero,
            developer,
            franchise,
            descricao,
            metacritic,
            nota_kadu,
            nota_pavam,
            historico_importante,
            historico_influente
        )
        VALUES (
            %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s
        );
    """

    dados = []

    for _, linha in df_games.iterrows():
        registro = (
            converter_int(
                linha["id"]
            ),
            converter_texto(
                linha["nome"]
            ),
            converter_int(
                linha["ano_lancamento"]
            ),
            converter_texto(
                linha["genero"]
            ),
            converter_texto(
                linha["developer"]
            ),
            converter_texto(
                linha["franchise"]
            ),
            converter_texto(
                linha["descricao"]
            ),
            converter_int(
                linha["metacritic"]
            ),
            converter_float(
                linha["nota_kadu"]
            ),
            converter_float(
                linha["nota_pavam"]
            ),
            converter_booleano(
                linha["historico_importante"]
            ),
            converter_booleano(
                linha["historico_influente"]
            ),
        )

        dados.append(registro)

    cursor.executemany(
        sql,
        dados,
    )


# ==========================================================
# FUNÇÃO PARA IMPORTAR AWARDS
# ==========================================================

def importar_awards(cursor, df_awards):
    """
    Importa os registros de awards.csv para a tabela awards.

    O id não é informado porque o PostgreSQL gera
    automaticamente.
    """

    sql = """
        INSERT INTO awards (
            ano,
            premiacao,
            jogo,
            status
        )
        VALUES (
            %s, %s, %s, %s
        );
    """

    dados = []

    for _, linha in df_awards.iterrows():
        registro = (
            converter_int(
                linha["ano"]
            ),
            converter_texto(
                linha["premiacao"]
            ),
            converter_texto(
                linha["jogo"]
            ),
            converter_texto(
                linha["status"]
            ),
        )

        dados.append(registro)

    cursor.executemany(
        sql,
        dados,
    )


# ==========================================================
# FUNÇÕES DE CONFERÊNCIA
# ==========================================================

def contar_registros(cursor, nome_tabela):
    """
    Conta registros de uma tabela permitida.

    Apenas as tabelas presentes em CONSULTAS_CONTAGEM
    podem ser utilizadas.
    """

    consulta = CONSULTAS_CONTAGEM.get(
        nome_tabela
    )

    if consulta is None:
        raise ValueError(
            f"Tabela não permitida para contagem: "
            f"{nome_tabela}"
        )

    cursor.execute(
        consulta
    )

    return cursor.fetchone()[0]


def validar_quantidades_importadas(
    total_games,
    total_awards,
    quantidade_games_csv,
    quantidade_awards_csv,
):
    """
    Confirma que as quantidades importadas são iguais
    às quantidades presentes nos CSVs.
    """

    if total_games != quantidade_games_csv:
        raise RuntimeError(
            "A quantidade importada em games não "
            "corresponde ao CSV. "
            f"CSV: {quantidade_games_csv} | "
            f"Banco: {total_games}"
        )

    if total_awards != quantidade_awards_csv:
        raise RuntimeError(
            "A quantidade importada em awards não "
            "corresponde ao CSV. "
            f"CSV: {quantidade_awards_csv} | "
            f"Banco: {total_awards}"
        )


# ==========================================================
# FUNÇÃO PRINCIPAL
# ==========================================================

def main():
    """
    Executa o processo completo de importação.

    Ordem:

    1. Carregar e validar os CSVs.
    2. Conectar ao PostgreSQL usando database.py e .env.
    3. Limpar as tabelas.
    4. Importar games.
    5. Importar awards.
    6. Conferir as quantidades.
    7. Confirmar ou desfazer a transação.
    8. Encerrar a conexão.
    """

    print(
        "=========================================================="
    )
    print(
        "The AAA Archive — Importação CSV para PostgreSQL"
    )
    print(
        "=========================================================="
    )
    print()

    conexao = None

    try:
        # ------------------------------------------------------
        # 1. Carregar e validar os CSVs
        # ------------------------------------------------------

        print(
            "1. Carregando e validando arquivos CSV..."
        )
        print()

        df_games = carregar_csv_games()
        df_awards = carregar_csv_awards()

        print()
        print(
            f"games.csv carregado com "
            f"{len(df_games)} registros."
        )
        print(
            f"awards.csv carregado com "
            f"{len(df_awards)} registros."
        )
        print()

        # ------------------------------------------------------
        # 2. Conectar ao PostgreSQL
        # ------------------------------------------------------

        print(
            "2. Conectando ao PostgreSQL "
            "usando o arquivo .env..."
        )
        print()

        conexao = conectar_postgres()

        print(
            "Conexão realizada com sucesso."
        )
        print()

        # ------------------------------------------------------
        # 3. Executar a importação em uma transação
        # ------------------------------------------------------

        with conexao:
            with conexao.cursor() as cursor:
                print(
                    "3. Limpando tabelas antigas..."
                )

                limpar_tabelas(
                    cursor
                )

                print(
                    "Tabelas limpas com sucesso."
                )
                print()

                print(
                    "4. Importando games.csv "
                    "para a tabela games..."
                )

                importar_games(
                    cursor,
                    df_games,
                )

                print(
                    "Importação de games concluída."
                )
                print()

                print(
                    "5. Importando awards.csv "
                    "para a tabela awards..."
                )

                importar_awards(
                    cursor,
                    df_awards,
                )

                print(
                    "Importação de awards concluída."
                )
                print()

                print(
                    "6. Conferindo quantidades importadas..."
                )

                total_games = contar_registros(
                    cursor,
                    "games",
                )

                total_awards = contar_registros(
                    cursor,
                    "awards",
                )

                validar_quantidades_importadas(
                    total_games=total_games,
                    total_awards=total_awards,
                    quantidade_games_csv=len(df_games),
                    quantidade_awards_csv=len(df_awards),
                )

                print()
                print(
                    f"Registros na tabela games: "
                    f"{total_games}"
                )
                print(
                    f"Registros na tabela awards: "
                    f"{total_awards}"
                )

        print()
        print(
            "=========================================================="
        )
        print(
            "Importação concluída com sucesso!"
        )
        print(
            "=========================================================="
        )

    except Exception as erro:
        print()
        print(
            "=========================================================="
        )
        print(
            "Erro durante a importação."
        )
        print(
            "=========================================================="
        )
        print()
        print(
            "Mensagem do erro:"
        )
        print(
            erro
        )
        print()
        print(
            "Possíveis causas:"
        )
        print(
            "- PostgreSQL não está em execução;"
        )
        print(
            "- arquivo .env ausente ou incompleto;"
        )
        print(
            "- credenciais do PostgreSQL incorretas;"
        )
        print(
            "- banco aaa_archive não existe;"
        )
        print(
            "- tabelas games e awards não existem;"
        )
        print(
            "- colunas do banco diferentes das esperadas;"
        )
        print(
            "- CSV ausente, inválido ou com valor inesperado."
        )
        print()

        # Encerra o processo com código de erro.
        #
        # Isso permite que terminal, testes ou automações
        # percebam que a importação não foi concluída.
        raise SystemExit(1) from erro

    finally:
        if conexao is not None:
            conexao.close()

            print()
            print(
                "Conexão com PostgreSQL encerrada."
            )


# ==========================================================
# EXECUÇÃO DO SCRIPT
# ==========================================================

if __name__ == "__main__":
    main()