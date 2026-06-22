"""
===========================================================
The AAA Archive
Arquivo: load_data.py

Objetivo:
Centralizar o carregamento do dataset oficial do projeto.

Este módulo possui apenas uma responsabilidade:
ler o arquivo CSV e retornar um DataFrame para que outros
módulos possam reutilizar os dados.

Autor: Kadu Almeida
===========================================================
"""

# ==========================================================
# IMPORTAÇÃO DAS BIBLIOTECAS
# ==========================================================

# O Pandas é a principal biblioteca de análise de dados do Python.
# Durante todo o projeto utilizaremos DataFrames para manipular
# os dados da coleção.
import pandas as pd


# ==========================================================
# CAMINHO DO DATASET
# ==========================================================

# Caminho do arquivo CSV oficial do projeto.
# Caso o dataset seja movido de pasta futuramente,
# basta alterar esta variável.
file_path = "data/games.csv"


# ==========================================================
# FUNÇÃO DE CARREGAMENTO
# ==========================================================

def carregar_dataset():
    """
    Carrega o dataset oficial do The AAA Archive.

    Returns:
        pd.DataFrame: DataFrame contendo todos os jogos da coleção.
    """

    return pd.read_csv(file_path)