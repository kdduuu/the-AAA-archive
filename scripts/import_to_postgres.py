# ==========================================================
# The AAA Archive
# Arquivo: import_to_postgres.py
#
# Objetivo:
# Importar os dados dos arquivos CSV do projeto para o PostgreSQL.
#
# Em outras palavras:
#
# data/games.csv
# data/awards.csv
#        ↓
# Python + Pandas
#        ↓
# PostgreSQL
#        ↓
# tabelas games e awards
#
# Este script NÃO altera a API.
# Este script NÃO altera o dashboard.
# Este script apenas pega os dados dos CSVs e coloca no banco.
#
# Autor: Kadu Almeida
# ==========================================================


# ==========================================================
# IMPORTAÇÃO DOS MÓDULOS
# ==========================================================

# pathlib ajuda a trabalhar com caminhos de arquivos e pastas
# de um jeito mais seguro do que escrever caminhos manualmente.
from pathlib import Path

# getpass permite pedir uma senha no terminal sem mostrar ela na tela.
#
# Quando você digitar a senha do PostgreSQL, ela não vai aparecer.
# Isso é normal.
#
# Usamos isso para NÃO deixar a senha escrita dentro do código.
from getpass import getpass

# Pandas será usado para ler os arquivos CSV.
#
# Ele transforma o CSV em DataFrame.
# DataFrame é como se fosse uma tabela dentro do Python.
import pandas as pd

# psycopg é a biblioteca que permite o Python conversar com o PostgreSQL.
#
# Sem ela, o Python não consegue conectar no banco.
import psycopg


# ==========================================================
# CONFIGURAÇÃO DOS CAMINHOS DO PROJETO
# ==========================================================

# Este arquivo import_to_postgres.py está dentro da pasta scripts/.
#
# Estrutura:
#
# The-AAA-Archive/
# │
# ├── data/
# │   ├── games.csv
# │   └── awards.csv
# │
# └── scripts/
#     └── import_to_postgres.py
#
# Como este arquivo está dentro de scripts/,
# a raiz do projeto é a pasta anterior.

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Caminho completo até o games.csv.
GAMES_CSV_PATH = PROJECT_ROOT / "data" / "games.csv"

# Caminho completo até o awards.csv.
AWARDS_CSV_PATH = PROJECT_ROOT / "data" / "awards.csv"


# ==========================================================
# CONFIGURAÇÃO DO BANCO DE DADOS
# ==========================================================

# Aqui ficam as informações necessárias para conectar no PostgreSQL.
#
# IMPORTANTE:
# A senha NÃO fica aqui.
# A senha será pedida no terminal usando getpass().
#
# Isso evita deixar senha salva no código e no GitHub.

# Nome do banco que criamos no pgAdmin.
DB_NAME = "aaa_archive"

# Usuário padrão que você configurou na instalação do PostgreSQL.
DB_USER = "postgres"

# localhost significa:
# "o banco está rodando no meu próprio computador".
DB_HOST = "localhost"

# 5432 é a porta padrão do PostgreSQL.
DB_PORT = 5432


# ==========================================================
# FUNÇÕES AUXILIARES DE TRATAMENTO DE DADOS
# ==========================================================

# Por que essas funções existem?
#
# Porque os dados vêm do CSV.
#
# No CSV, alguns campos podem vir vazios.
# Quando o Pandas lê um campo vazio, ele pode transformar isso em NaN.
#
# Só que o PostgreSQL não usa NaN do Pandas.
# O PostgreSQL usa NULL.
#
# Em Python, para mandar NULL para o PostgreSQL, usamos None.
#
# Então essas funções ajudam a converter os valores antes da inserção.


def tratar_valor(valor):
    """
    Trata valores vazios antes de inserir no PostgreSQL.

    Se o valor estiver vazio no Pandas, retornamos None.

    No PostgreSQL:
    None do Python vira NULL no banco.
    """

    if pd.isna(valor):
        return None

    return valor


def converter_int(valor):
    """
    Converte um valor para inteiro.

    Exemplo:
    "2005" → 2005

    Se o valor estiver vazio, retorna None.
    """

    valor = tratar_valor(valor)

    if valor is None:
        return None

    return int(valor)


def converter_float(valor):
    """
    Converte um valor para número decimal.

    Exemplo:
    "9.5" → 9.5

    Se o valor estiver vazio, retorna None.
    """

    valor = tratar_valor(valor)

    if valor is None:
        return None

    return float(valor)


def converter_texto(valor):
    """
    Converte um valor para texto.

    Exemplo:
    Resident Evil 4 → "Resident Evil 4"

    Se o valor estiver vazio, retorna None.
    """

    valor = tratar_valor(valor)

    if valor is None:
        return None

    return str(valor)


def converter_booleano(valor):
    """
    Converte um valor para booleano.

    Booleano é um tipo de dado que só pode ser:

    True  → verdadeiro
    False → falso

    No nosso projeto, as colunas booleanas são:

    - historico_importante
    - historico_influente

    Essa função aceita diferentes formas de representar verdadeiro/falso.

    Exemplos que viram True:
    - True
    - "true"
    - "sim"
    - "1"

    Exemplos que viram False:
    - False
    - "false"
    - "não"
    - "nao"
    - "0"
    """

    valor = tratar_valor(valor)

    if valor is None:
        return None

    # Se o valor já for True ou False, retornamos direto.
    if isinstance(valor, bool):
        return valor

    # Transformamos em texto, removemos espaços e deixamos minúsculo.
    valor_texto = str(valor).strip().lower()

    valores_verdadeiros = [
        "true",
        "1",
        "sim",
        "s",
        "yes",
        "y"
    ]

    valores_falsos = [
        "false",
        "0",
        "não",
        "nao",
        "n",
        "no"
    ]

    if valor_texto in valores_verdadeiros:
        return True

    if valor_texto in valores_falsos:
        return False

    # Se não reconhecermos o valor, retornamos None.
    # Isso evita inserir algo errado no banco.
    return None


# ==========================================================
# FUNÇÕES DE LEITURA DOS CSVs
# ==========================================================

def carregar_csv_games():
    """
    Carrega o arquivo data/games.csv usando Pandas.

    Retorno:
        DataFrame com os jogos da Foundation Collection.
    """

    print(f"Lendo arquivo: {GAMES_CSV_PATH}")

    df_games = pd.read_csv(GAMES_CSV_PATH)

    return df_games


def carregar_csv_awards():
    """
    Carrega o arquivo data/awards.csv usando Pandas.

    Retorno:
        DataFrame com os dados da Awards History.
    """

    print(f"Lendo arquivo: {AWARDS_CSV_PATH}")

    df_awards = pd.read_csv(AWARDS_CSV_PATH)

    return df_awards


# ==========================================================
# FUNÇÃO DE CONEXÃO COM O POSTGRESQL
# ==========================================================

def conectar_postgres():
    """
    Cria uma conexão com o banco PostgreSQL.

    Aqui acontece uma parte importante:

    Python
      ↓
    psycopg
      ↓
    PostgreSQL

    A senha será digitada no terminal quando o script rodar.

    No seu caso, você configurou a senha do usuário postgres durante
    a instalação do PostgreSQL.

    Quando aparecer:

        Digite a senha do usuário postgres:

    você digita sua senha e aperta Enter.

    A senha não aparece na tela. Isso é normal.
    """

    senha = getpass("Digite a senha do usuário postgres: ")

    conexao = psycopg.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=senha,
        host=DB_HOST,
        port=DB_PORT
    )

    return conexao


# ==========================================================
# FUNÇÕES DE LIMPEZA DAS TABELAS
# ==========================================================

def limpar_tabelas(cursor):
    """
    Limpa as tabelas antes de importar os dados novamente.

    Por que limpar?

    Imagine que o script importa 66 jogos.
    Depois você roda o script de novo.
    Se a gente não limpar antes, ele tentaria colocar os mesmos jogos de novo.

    Então a ordem é:

    1. apagar dados antigos das tabelas;
    2. importar tudo novamente a partir dos CSVs.

    TRUNCATE TABLE:
        limpa todos os registros da tabela.

    RESTART IDENTITY:
        reinicia contadores automáticos, como o id SERIAL da tabela awards.
    """

    # Limpamos awards primeiro.
    #
    # No nosso modelo atual, awards não depende de games por chave estrangeira.
    # Mas separar os comandos deixa o processo mais claro.
    cursor.execute("TRUNCATE TABLE awards RESTART IDENTITY;")

    # Limpamos games depois.
    cursor.execute("TRUNCATE TABLE games RESTART IDENTITY;")


# ==========================================================
# FUNÇÃO PARA IMPORTAR GAMES
# ==========================================================

def importar_games(cursor, df_games):
    """
    Importa os dados do games.csv para a tabela games.

    Cada linha do DataFrame vira uma linha na tabela games.

    O DataFrame vem do CSV.
    A tabela games está no PostgreSQL.
    """

    # Este é o comando SQL que será executado várias vezes.
    #
    # INSERT INTO games (...)
    # significa:
    # "insira dados dentro da tabela games".
    #
    # Os %s são espaços reservados.
    # O psycopg troca esses %s pelos valores reais de forma segura.
    #
    # Não colocamos os valores diretamente dentro da string SQL.
    # Isso é uma prática mais segura.

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
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
        );
    """

    # Esta lista vai guardar todos os registros já tratados.
    dados = []

    # iterrows() percorre o DataFrame linha por linha.
    #
    # Cada "linha" representa um jogo do games.csv.
    for _, linha in df_games.iterrows():

        # Aqui montamos uma tupla.
        #
        # Uma tupla é parecida com uma lista, mas geralmente usada
        # para representar um conjunto fixo de valores.
        #
        # A ordem precisa bater com a ordem das colunas do INSERT.
        registro = (
            converter_int(linha["id"]),
            converter_texto(linha["nome"]),
            converter_int(linha["ano_lancamento"]),
            converter_texto(linha["genero"]),
            converter_texto(linha["developer"]),
            converter_texto(linha["franchise"]),
            converter_texto(linha["descricao"]),
            converter_int(linha["metacritic"]),
            converter_float(linha["nota_kadu"]),
            converter_float(linha["nota_pavam"]),
            converter_booleano(linha["historico_importante"]),
            converter_booleano(linha["historico_influente"]),
        )

        dados.append(registro)

    # executemany() executa o mesmo INSERT várias vezes.
    #
    # Em vez de mandar um jogo por vez manualmente,
    # mandamos a lista inteira de registros.
    cursor.executemany(sql, dados)


# ==========================================================
# FUNÇÃO PARA IMPORTAR AWARDS
# ==========================================================

def importar_awards(cursor, df_awards):
    """
    Importa os dados do awards.csv para a tabela awards.

    A tabela awards possui uma coluna id automática no PostgreSQL.

    Como o CSV awards.csv não possui id, nós não inserimos id manualmente.
    O PostgreSQL cria esse id sozinho por causa do SERIAL.
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
            converter_int(linha["ano"]),
            converter_texto(linha["premiacao"]),
            converter_texto(linha["jogo"]),
            converter_texto(linha["status"]),
        )

        dados.append(registro)

    cursor.executemany(sql, dados)


# ==========================================================
# FUNÇÃO DE CONFERÊNCIA
# ==========================================================

def contar_registros(cursor, nome_tabela):
    """
    Conta quantos registros existem em uma tabela.

    Exemplo de SQL executado:

        SELECT COUNT(*) FROM games;

    Isso ajuda a verificar se a importação deu certo.
    """

    cursor.execute(f"SELECT COUNT(*) FROM {nome_tabela};")

    total = cursor.fetchone()[0]

    return total


# ==========================================================
# FUNÇÃO PRINCIPAL
# ==========================================================

def main():
    """
    Executa o processo completo de importação.

    Ordem do script:

    1. Carregar games.csv
    2. Carregar awards.csv
    3. Conectar no PostgreSQL
    4. Limpar tabelas antigas
    5. Importar games
    6. Importar awards
    7. Conferir quantidade de registros
    8. Encerrar conexão
    """

    print("==========================================================")
    print("The AAA Archive — Importação CSV para PostgreSQL")
    print("==========================================================")
    print()

    # ------------------------------------------------------
    # 1. Carregar CSVs
    # ------------------------------------------------------

    print("1. Carregando arquivos CSV...")
    print()

    df_games = carregar_csv_games()
    df_awards = carregar_csv_awards()

    print()
    print(f"games.csv carregado com {len(df_games)} registros.")
    print(f"awards.csv carregado com {len(df_awards)} registros.")
    print()

    # ------------------------------------------------------
    # 2. Conectar no PostgreSQL
    # ------------------------------------------------------

    print("2. Conectando ao PostgreSQL...")
    print()

    conexao = conectar_postgres()

    print()
    print("Conexão realizada com sucesso.")
    print()

    # ------------------------------------------------------
    # 3. Importar dados
    # ------------------------------------------------------

    try:
        # O "with conexao:" ajuda a controlar transações.
        #
        # Se tudo der certo, ele confirma as alterações.
        # Se der erro, ele desfaz a operação.
        with conexao:

            # O cursor é o objeto que executa comandos SQL.
            #
            # Sempre que quisermos rodar SELECT, INSERT, TRUNCATE etc.,
            # usamos o cursor.
            with conexao.cursor() as cursor:

                print("3. Limpando tabelas antigas...")
                limpar_tabelas(cursor)
                print("Tabelas limpas com sucesso.")
                print()

                print("4. Importando games.csv para a tabela games...")
                importar_games(cursor, df_games)
                print("Importação de games concluída.")
                print()

                print("5. Importando awards.csv para a tabela awards...")
                importar_awards(cursor, df_awards)
                print("Importação de awards concluída.")
                print()

                print("6. Conferindo quantidade de registros no banco...")
                total_games = contar_registros(cursor, "games")
                total_awards = contar_registros(cursor, "awards")

                print()
                print(f"Registros na tabela games: {total_games}")
                print(f"Registros na tabela awards: {total_awards}")

        print()
        print("==========================================================")
        print("Importação concluída com sucesso!")
        print("==========================================================")

    except Exception as erro:
        print()
        print("==========================================================")
        print("Erro durante a importação.")
        print("==========================================================")
        print()
        print("Mensagem do erro:")
        print(erro)
        print()
        print("Possíveis causas:")
        print("- senha do PostgreSQL incorreta;")
        print("- banco aaa_archive não existe;")
        print("- tabelas games e awards não existem;")
        print("- colunas do banco diferentes das colunas esperadas;")
        print("- PostgreSQL não está rodando;")
        print("- CSV com algum valor inesperado.")

    finally:
        # Sempre fechamos a conexão no final.
        #
        # Isso é importante para não deixar conexões abertas sem necessidade.
        conexao.close()

        print()
        print("Conexão com PostgreSQL encerrada.")


# ==========================================================
# EXECUÇÃO DO SCRIPT
# ==========================================================

# Essa parte significa:
#
# "Se este arquivo for executado diretamente pelo terminal,
# rode a função main()."
#
# Exemplo:
#
# python scripts/import_to_postgres.py

if __name__ == "__main__":
    main()