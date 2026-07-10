# ==========================================================
# The AAA Archive
# Arquivo: database.py
#
# Objetivo:
# Centralizar funções de conexão e leitura do PostgreSQL.
#
# Agora este arquivo lê as configurações do banco a partir
# do arquivo .env localizado na raiz do projeto.
#
# Fluxo:
#
# .env
#   ↓
# database.py
#   ↓
# PostgreSQL
#   ↓
# DataFrame Pandas
#
# Autor: Kadu Almeida
# ==========================================================


# ==========================================================
# IMPORTAÇÃO DOS MÓDULOS
# ==========================================================

from pathlib import Path
import os

import pandas as pd
import psycopg

from dotenv import load_dotenv


# ==========================================================
# LOCALIZAÇÃO DO PROJETO E DO .env
# ==========================================================

# Este arquivo está dentro da pasta scripts/.
#
# Estrutura:
#
# The-AAA-Archive/
# │
# ├── .env
# │
# └── scripts/
#     └── database.py
#
# Por isso usamos parent.parent:
#
# database.py -> scripts -> The-AAA-Archive

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Caminho completo até o arquivo .env.
ENV_PATH = PROJECT_ROOT / ".env"

# Carrega as variáveis do arquivo .env.
load_dotenv(ENV_PATH)


# ==========================================================
# FUNÇÃO PARA LER CONFIGURAÇÕES DO BANCO
# ==========================================================

def obter_configuracao_banco():
    """
    Lê as configurações do PostgreSQL a partir do arquivo .env.

    O arquivo .env deve conter:

        POSTGRES_DB=aaa_archive
        POSTGRES_USER=postgres
        POSTGRES_PASSWORD=sua_senha
        POSTGRES_HOST=localhost
        POSTGRES_PORT=5432

    Retorno:
        Um dicionário com as informações necessárias para conectar
        no PostgreSQL.

    Por que isso existe?
        Para não deixar senha escrita diretamente no código.
        Assim, o código pode ir para o GitHub, mas o .env fica apenas
        no seu computador.
    """

    config = {
        "dbname": os.getenv("POSTGRES_DB"),
        "user": os.getenv("POSTGRES_USER"),
        "password": os.getenv("POSTGRES_PASSWORD"),
        "host": os.getenv("POSTGRES_HOST"),
        "port": os.getenv("POSTGRES_PORT"),
    }

    # Verifica se alguma informação está faltando no .env.
    variaveis_faltando = []

    for chave, valor in config.items():
        if valor is None or valor == "":
            variaveis_faltando.append(chave)

    if variaveis_faltando:
        raise ValueError(
            "Existem configurações faltando no arquivo .env: "
            + ", ".join(variaveis_faltando)
        )

    # A porta vem do .env como texto.
    # Exemplo: "5432"
    #
    # O psycopg aceita isso, mas converter para inteiro deixa mais correto.
    config["port"] = int(config["port"])

    return config


# ==========================================================
# FUNÇÃO DE CONEXÃO
# ==========================================================

def conectar_postgres():
    """
    Cria uma conexão com o banco PostgreSQL usando as configurações do .env.

    Antes:
        conectar_postgres(senha)

    Agora:
        conectar_postgres()

    A senha e as outras informações são lidas automaticamente do .env.
    """

    config = obter_configuracao_banco()

    conexao = psycopg.connect(
        dbname=config["dbname"],
        user=config["user"],
        password=config["password"],
        host=config["host"],
        port=config["port"]
    )

    return conexao


# ==========================================================
# FUNÇÃO GENÉRICA PARA CONSULTAR DADOS
# ==========================================================

def executar_select(sql):
    """
    Executa um comando SELECT no PostgreSQL e retorna um DataFrame.

    Parâmetro:
        sql:
            Comando SQL que será executado.

    Retorno:
        DataFrame com o resultado da consulta.

    Exemplo:
        SELECT * FROM games;
    """

    conexao = conectar_postgres()

    try:
        with conexao.cursor() as cursor:
            cursor.execute(sql)

            colunas = [coluna.name for coluna in cursor.description]
            linhas = cursor.fetchall()

            df = pd.DataFrame(
                linhas,
                columns=colunas
            )

            return df

    finally:
        conexao.close()


# ==========================================================
# FUNÇÕES ESPECÍFICAS DO PROJETO
# ==========================================================

def carregar_games_do_banco():
    """
    Carrega todos os jogos da tabela games.

    Retorno:
        DataFrame com os jogos da Foundation Collection.
    """

    sql = """
        SELECT
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
        FROM games
        ORDER BY id;
    """

    df_games = executar_select(sql)

    # Como nota_kadu e nota_pavam são NUMERIC no PostgreSQL,
    # elas podem voltar como Decimal no Python.
    #
    # Convertendo para float, o comportamento fica mais parecido
    # com o que já acontecia quando líamos o CSV com Pandas.
    if "nota_kadu" in df_games.columns:
        df_games["nota_kadu"] = df_games["nota_kadu"].astype(float)

    if "nota_pavam" in df_games.columns:
        df_games["nota_pavam"] = df_games["nota_pavam"].astype(float)

    return df_games


def carregar_awards_do_banco():
    """
    Carrega todos os registros da tabela awards.

    Retorno:
        DataFrame com os registros da Awards History.
    """

    sql = """
        SELECT
            id,
            ano,
            premiacao,
            jogo,
            status
        FROM awards
        ORDER BY ano, id;
    """

    df_awards = executar_select(sql)

    return df_awards


# ==========================================================
# FUNÇÕES DE CONFERÊNCIA
# ==========================================================

def contar_games_do_banco():
    """
    Conta quantos registros existem na tabela games.

    Retorno esperado atualmente:
        66
    """

    sql = """
        SELECT COUNT(*) AS total
        FROM games;
    """

    df_resultado = executar_select(sql)

    total = df_resultado.loc[0, "total"]

    return total


def contar_awards_do_banco():
    """
    Conta quantos registros existem na tabela awards.

    Retorno esperado atualmente:
        127
    """

    sql = """
        SELECT COUNT(*) AS total
        FROM awards;
    """

    df_resultado = executar_select(sql)

    total = df_resultado.loc[0, "total"]

    return total