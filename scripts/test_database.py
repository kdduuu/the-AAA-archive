# ==========================================================
# The AAA Archive
# Arquivo: test_database.py
#
# Objetivo:
# Testar se o Python consegue ler os dados do PostgreSQL.
#
# Este teste verifica:
# - conexão com o banco aaa_archive;
# - carregamento da tabela games;
# - carregamento da tabela awards;
# - contagem de registros;
# - estrutura básica dos DataFrames retornados.
#
# Autor: Kadu Almeida
# ==========================================================


# ==========================================================
# IMPORTAÇÃO DOS MÓDULOS
# ==========================================================

# pathlib ajuda a trabalhar com caminhos de arquivos/pastas.
from pathlib import Path

# sys permite adicionar caminhos ao sistema de importação do Python.
import sys

# getpass permite pedir senha no terminal sem mostrar ela na tela.
from getpass import getpass


# ==========================================================
# CONFIGURAÇÃO DOS CAMINHOS DO PROJETO
# ==========================================================

# Este arquivo está dentro da pasta scripts/.
#
# Estrutura:
#
# The-AAA-Archive/
# │
# └── scripts/
#     ├── database.py
#     └── test_database.py
#
# Como database.py também está dentro de scripts/,
# precisamos garantir que o Python consiga importar esse módulo.

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
)


# ==========================================================
# FUNÇÕES DE TESTE
# ==========================================================

def testar_contagem_games(senha):
    """
    Testa se a tabela games possui a quantidade esperada de registros.

    Atualmente, o games.csv possui 66 jogos.
    Como importamos esse CSV para o PostgreSQL, esperamos encontrar
    66 registros na tabela games.
    """

    total_games = contar_games_do_banco(senha)

    print(f"Registros encontrados na tabela games: {total_games}")

    assert total_games == 66, "A tabela games deveria ter 66 registros."


def testar_contagem_awards(senha):
    """
    Testa se a tabela awards possui a quantidade esperada de registros.

    Atualmente, o awards.csv possui 127 registros.
    Como importamos esse CSV para o PostgreSQL, esperamos encontrar
    127 registros na tabela awards.
    """

    total_awards = contar_awards_do_banco(senha)

    print(f"Registros encontrados na tabela awards: {total_awards}")

    assert total_awards == 127, "A tabela awards deveria ter 127 registros."


def testar_carregamento_games(senha):
    """
    Testa se os dados da tabela games são carregados como DataFrame.

    Também verifica se algumas colunas importantes existem.
    """

    df_games = carregar_games_do_banco(senha)

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

    assert "nome" in df_games.columns, "A coluna nome deveria existir."
    assert df_games["nome"].notna().any(), "A tabela games deveria possuir nomes de jogos."


def testar_carregamento_awards(senha):
    """
    Testa se os dados da tabela awards são carregados como DataFrame.

    Também verifica se algumas colunas importantes existem.
    """

    df_awards = carregar_awards_do_banco(senha)

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

    assert "jogo" in df_awards.columns, "A coluna jogo deveria existir."
    assert df_awards["jogo"].notna().any(), "A tabela awards deveria possuir nomes de jogos."


# ==========================================================
# FUNÇÃO PRINCIPAL
# ==========================================================

def main():
    """
    Executa todos os testes relacionados ao PostgreSQL.

    A senha é pedida uma vez no início e reutilizada nos testes.
    """

    print("==========================================================")
    print("The AAA Archive — Testes do PostgreSQL")
    print("==========================================================")
    print()

    senha = getpass("Digite a senha do usuário postgres: ")

    print()
    print("Iniciando testes...")
    print()

    testar_contagem_games(senha)
    testar_contagem_awards(senha)
    testar_carregamento_games(senha)
    testar_carregamento_awards(senha)

    print()
    print("==========================================================")
    print("TODOS OS TESTES DO BANCO PASSARAM!")
    print("==========================================================")


# ==========================================================
# EXECUÇÃO DO SCRIPT
# ==========================================================

if __name__ == "__main__":
    main()