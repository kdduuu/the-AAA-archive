# ==========================================================
# The AAA Archive
# Arquivo: test_database.py
#
# Objetivo:
# Testar se o Python consegue ler os dados do PostgreSQL.
#
# O teste funciona tanto com PostgreSQL local quanto com
# PostgreSQL publicado, como o Neon.
#
# Autor: Kadu Almeida
# ==========================================================


# ==========================================================
# IMPORTAÇÃO DOS MÓDULOS
# ==========================================================

from pathlib import Path
import sys


# ==========================================================
# CONFIGURAÇÃO DOS CAMINHOS DO PROJETO
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_PATH = PROJECT_ROOT / "scripts"

if str(SCRIPTS_PATH) not in sys.path:
    sys.path.append(str(SCRIPTS_PATH))


# ==========================================================
# IMPORTAÇÃO DAS FUNÇÕES DO BANCO
# ==========================================================

from database import (
    carregar_games_do_banco,
    carregar_awards_do_banco,
    contar_games_do_banco,
    contar_awards_do_banco,
    obter_configuracao_banco,
)


# ==========================================================
# FUNÇÕES DE TESTE
# ==========================================================

def testar_configuracao_env():
    """
    Testa se as informações essenciais do .env foram carregadas.

    Não exige nomes específicos como aaa_archive, postgres ou
    localhost, pois o projeto pode usar tanto o banco local quanto
    um PostgreSQL publicado, como o Neon.

    A senha nunca é exibida no terminal.
    """

    config = obter_configuracao_banco()

    assert config["dbname"], "POSTGRES_DB não foi carregado."
    assert config["user"], "POSTGRES_USER não foi carregado."
    assert config["password"], "POSTGRES_PASSWORD não foi carregado."
    assert config["host"], "POSTGRES_HOST não foi carregado."
    assert isinstance(config["port"], int), "POSTGRES_PORT deveria ser um número inteiro."
    assert config["port"] > 0, "POSTGRES_PORT deveria ser maior que zero."

    print("Configurações do .env carregadas com sucesso.")


def testar_contagem_games():
    """
    Testa se a tabela games possui a quantidade esperada de registros.
    """

    total_games = contar_games_do_banco()

    print(f"Registros encontrados na tabela games: {total_games}")

    assert total_games == 105, "A tabela games deveria ter 105 registros."


def testar_contagem_awards():
    """
    Testa se a tabela awards possui a quantidade esperada de registros.
    """

    total_awards = contar_awards_do_banco()

    print(f"Registros encontrados na tabela awards: {total_awards}")

    assert total_awards == 127, "A tabela awards deveria ter 127 registros."


def testar_carregamento_games():
    """
    Testa se os dados da tabela games são carregados como DataFrame.
    """

    df_games = carregar_games_do_banco()

    print(f"DataFrame de games carregado com {len(df_games)} registros.")

    assert len(df_games) == 105, "O DataFrame de games deveria ter 105 registros."

    colunas_esperadas = [
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

    for coluna in colunas_esperadas:
        assert coluna in df_games.columns, f"A coluna {coluna} não foi encontrada em games."

    assert df_games["nome"].notna().any(), "A tabela games deveria possuir nomes de jogos."


def testar_carregamento_awards():
    """
    Testa se os dados da tabela awards são carregados como DataFrame.
    """

    df_awards = carregar_awards_do_banco()

    print(f"DataFrame de awards carregado com {len(df_awards)} registros.")

    assert len(df_awards) == 127, "O DataFrame de awards deveria ter 127 registros."

    colunas_esperadas = [
        "id",
        "ano",
        "premiacao",
        "jogo",
        "status",
    ]

    for coluna in colunas_esperadas:
        assert coluna in df_awards.columns, f"A coluna {coluna} não foi encontrada em awards."

    assert df_awards["jogo"].notna().any(), "A tabela awards deveria possuir nomes de jogos."


# ==========================================================
# FUNÇÃO PRINCIPAL
# ==========================================================

def main():
    """
    Executa todos os testes relacionados ao PostgreSQL.
    """

    print("==========================================================")
    print("The AAA Archive — Testes do PostgreSQL")
    print("==========================================================")
    print()

    print("Lendo configurações do arquivo .env...")
    testar_configuracao_env()

    print()
    print("Iniciando testes do banco...")
    print()

    testar_contagem_games()
    testar_contagem_awards()
    testar_carregamento_games()
    testar_carregamento_awards()

    print()
    print("==========================================================")
    print("TODOS OS TESTES DO BANCO PASSARAM!")
    print("==========================================================")


# ==========================================================
# EXECUÇÃO DO SCRIPT
# ==========================================================

if __name__ == "__main__":
    main()