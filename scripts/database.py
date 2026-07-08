# ==========================================================
# The AAA Archive
# Arquivo: database.py
#
# Objetivo:
# Centralizar funções de conexão e leitura do PostgreSQL.
#
# Este arquivo faz o caminho:
#
# PostgreSQL
#     ↓
# Python
#     ↓
# DataFrame
#
# Ou seja:
# Ele busca dados que já estão no banco e transforma esses dados
# em DataFrames do Pandas, para que o restante do projeto consiga
# trabalhar com eles de forma parecida com os CSVs.
#
# Autor: Kadu Almeida
# ==========================================================


# ==========================================================
# IMPORTAÇÃO DOS MÓDULOS
# ==========================================================

# Pandas será usado para transformar o resultado do banco em DataFrame.
import pandas as pd

# psycopg é a biblioteca que permite o Python conversar com o PostgreSQL.
import psycopg


# ==========================================================
# CONFIGURAÇÃO DO BANCO DE DADOS
# ==========================================================

# Nome do banco criado no pgAdmin.
DB_NAME = "aaa_archive"

# Usuário padrão criado durante a instalação do PostgreSQL.
DB_USER = "postgres"

# localhost significa que o banco está rodando no seu próprio computador.
DB_HOST = "localhost"

# Porta padrão do PostgreSQL.
DB_PORT = 5432


# ==========================================================
# FUNÇÃO DE CONEXÃO
# ==========================================================

def conectar_postgres(senha):
    """
    Cria uma conexão com o banco PostgreSQL.

    Parâmetro:
        senha:
            Senha do usuário postgres.

    Retorno:
        Uma conexão ativa com o banco aaa_archive.

    Explicação simples:
        Essa função é como "abrir a porta" do banco para o Python.

        Python
          ↓
        psycopg
          ↓
        PostgreSQL
    """

    conexao = psycopg.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=senha,
        host=DB_HOST,
        port=DB_PORT
    )

    return conexao


# ==========================================================
# FUNÇÃO GENÉRICA PARA CONSULTAR DADOS
# ==========================================================

def executar_select(senha, sql):
    """
    Executa um comando SELECT no PostgreSQL e retorna um DataFrame.

    Parâmetros:
        senha:
            Senha do usuário postgres.

        sql:
            Comando SQL que será executado.

    Retorno:
        DataFrame com o resultado da consulta.

    Por que essa função existe?
        Para evitar repetir o mesmo código de conexão, cursor,
        execução de SQL e conversão para DataFrame várias vezes.

    Exemplo de SQL:
        SELECT * FROM games;
    """

    # Abrimos a conexão com o banco.
    conexao = conectar_postgres(senha)

    try:
        # O cursor é o objeto responsável por executar comandos SQL.
        with conexao.cursor() as cursor:

            # Executa o comando SQL recebido.
            cursor.execute(sql)

            # cursor.description guarda informações sobre as colunas retornadas.
            #
            # Exemplo:
            # Se o SELECT retorna id, nome e ano_lancamento,
            # essa parte captura esses nomes.
            colunas = [coluna.name for coluna in cursor.description]

            # fetchall() pega todas as linhas retornadas pelo SELECT.
            linhas = cursor.fetchall()

            # Transformamos o resultado em DataFrame.
            df = pd.DataFrame(
                linhas,
                columns=colunas
            )

            return df

    finally:
        # Fechamos a conexão ao final.
        #
        # Isso é importante para não deixar conexões abertas sem necessidade.
        conexao.close()


# ==========================================================
# FUNÇÕES ESPECÍFICAS DO PROJETO
# ==========================================================

def carregar_games_do_banco(senha):
    """
    Carrega todos os jogos da tabela games.

    Essa função é o equivalente, no PostgreSQL, ao que antes era feito
    com o games.csv.

    Antes:
        carregar_dataset()
        ↓
        lê data/games.csv

    Agora:
        carregar_games_do_banco()
        ↓
        lê tabela games no PostgreSQL

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

    df_games = executar_select(senha, sql)

    # Como as colunas nota_kadu e nota_pavam foram criadas como NUMERIC
    # no PostgreSQL, elas podem voltar como Decimal no Python.
    #
    # Para facilitar o uso com Pandas e manter parecido com o CSV,
    # convertemos essas colunas para float.
    if "nota_kadu" in df_games.columns:
        df_games["nota_kadu"] = df_games["nota_kadu"].astype(float)

    if "nota_pavam" in df_games.columns:
        df_games["nota_pavam"] = df_games["nota_pavam"].astype(float)

    return df_games


def carregar_awards_do_banco(senha):
    """
    Carrega todos os registros da tabela awards.

    Essa função é o equivalente, no PostgreSQL, ao que antes era feito
    com o awards.csv.

    Antes:
        carregar_awards()
        ↓
        lê data/awards.csv

    Agora:
        carregar_awards_do_banco()
        ↓
        lê tabela awards no PostgreSQL

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

    df_awards = executar_select(senha, sql)

    return df_awards


# ==========================================================
# FUNÇÕES DE CONFERÊNCIA
# ==========================================================

def contar_games_do_banco(senha):
    """
    Conta quantos registros existem na tabela games.

    Retorno esperado atualmente:
        66
    """

    sql = """
        SELECT COUNT(*) AS total
        FROM games;
    """

    df_resultado = executar_select(senha, sql)

    total = df_resultado.loc[0, "total"]

    return total


def contar_awards_do_banco(senha):
    """
    Conta quantos registros existem na tabela awards.

    Retorno esperado atualmente:
        127
    """

    sql = """
        SELECT COUNT(*) AS total
        FROM awards;
    """

    df_resultado = executar_select(senha, sql)

    total = df_resultado.loc[0, "total"]

    return total