# ==========================================================
# The AAA Archive
# Arquivo: test_database.py
#
# Objetivo:
# Testar se o Python consegue ler os dados do PostgreSQL.
#
# Agora este teste não pede mais a senha no terminal.
# Ele usa as configurações do arquivo .env.
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
    Testa se as informações do .env foram carregadas corretamente.

    Este teste não mostra a senha no terminal.
    Ele apenas confirma que as configurações existem.
    """

    config = obter_configuracao_banco()

    assert config["dbname"] == "aaa_archive", "O banco deveria ser aaa_archive."
    assert config["user"] == "postgres", "O usuário deveria ser postgres."
    assert config["host"] == "localhost", "O host deveria ser localhost."
    assert config["port"] == 5432, "A porta deveria ser 5432."
    assert config["password"] is not None, "A senha não foi carregada."

    print("Configurações do .env carregadas com sucesso.")


def testar_contagem_games():
    """
    Testa se a tabela games possui a quantidade esperada de registros.
    """

    total_games = contar_games_do_banco()

    print(f"Registros encontrados na tabela games: {total_games}")

    assert total_games == 66, "A tabela games deveria ter 66 registros."


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

    assert len(df_games) == 66, "O DataFrame de games deveria ter 66 registros."

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
        "historico_influente"
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
        "status"
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