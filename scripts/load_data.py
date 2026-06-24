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

from pathlib import Path

import pandas as pd


# ==========================================================
# CAMINHO DO DATASET
# ==========================================================

# Path(__file__) representa o caminho deste arquivo.
# .resolve() transforma esse caminho em um caminho absoluto.
# .parent sobe para a pasta scripts/
# .parent.parent sobe para a raiz do projeto.
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Caminho oficial do dataset da Foundation Collection.
DATASET_PATH = PROJECT_ROOT / "data" / "games.csv"


# ==========================================================
# FUNÇÃO DE CARREGAMENTO
# ==========================================================

def carregar_dataset():
    """
    Carrega o dataset oficial do The AAA Archive.

    Returns:
        pd.DataFrame: DataFrame contendo todos os jogos da coleção.
    """

    return pd.read_csv(DATASET_PATH)