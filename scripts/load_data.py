"""
===========================================================
The AAA Archive
Arquivo: load_data.py

Objetivo:
Centralizar o carregamento dos datasets oficiais do projeto.

Este módulo possui uma responsabilidade simples:
ler os arquivos CSV e retornar DataFrames para que outros
módulos possam reutilizar os dados.

Autor: Kadu Almeida
===========================================================
"""

# ==========================================================
# IMPORTAÇÃO DAS BIBLIOTECAS
# ==========================================================

from pathlib import Path

import pandas as pd


# ==========================================================
# CAMINHOS DOS DATASETS
# ==========================================================

# Caminho absoluto da raiz do projeto.
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Dataset principal da Foundation Collection.
GAMES_PATH = PROJECT_ROOT / "data" / "games.csv"

# Dataset independente do histórico de premiações.
AWARDS_PATH = PROJECT_ROOT / "data" / "awards.csv"


# ==========================================================
# FUNÇÕES DE CARREGAMENTO
# ==========================================================

def carregar_dataset():
    """
    Carrega o dataset oficial da Foundation Collection.

    Returns:
        pd.DataFrame: DataFrame contendo todos os jogos da coleção.
    """

    return pd.read_csv(GAMES_PATH)


def carregar_awards():
    """
    Carrega o dataset oficial do histórico de premiações.

    Returns:
        pd.DataFrame: DataFrame contendo vencedores e indicados.
    """

    return pd.read_csv(AWARDS_PATH)