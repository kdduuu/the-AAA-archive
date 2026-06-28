"""
===========================================================
The AAA Archive
Arquivo: main.py

Objetivo:
Criar a primeira versão da API do The AAA Archive.

Nesta fase, a API já possui:
- endpoint inicial de teste;
- endpoint para listar os jogos da Foundation Collection.

Autor: Kadu Almeida
===========================================================
"""

# ==========================================================
# IMPORTAÇÃO DOS MÓDULOS
# ==========================================================

from pathlib import Path
import sys

import pandas as pd
from fastapi import FastAPI


# ==========================================================
# CONFIGURAÇÃO DOS CAMINHOS DO PROJETO
# ==========================================================

"""
O arquivo main.py está dentro da pasta api/.

Já os módulos do backend estão dentro da pasta scripts/.

Por isso, precisamos ensinar o Python onde encontrar esses módulos.

Estrutura:

The-AAA-Archive/
│
├── api/
│   └── main.py
│
└── scripts/
    └── load_data.py

A variável PROJECT_ROOT representa a raiz do projeto.
A variável SCRIPTS_PATH representa a pasta scripts/.
"""

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_PATH = PROJECT_ROOT / "scripts"

sys.path.append(str(SCRIPTS_PATH))


# Agora o Python consegue importar os módulos da pasta scripts.
from load_data import carregar_dataset


# ==========================================================
# CRIAÇÃO DA APLICAÇÃO
# ==========================================================

app = FastAPI(
    title="The AAA Archive API",
    description="API para consultar dados do projeto The AAA Archive.",
    version="0.1.0"
)


# ==========================================================
# FUNÇÃO AUXILIAR
# ==========================================================

def dataframe_para_json(df):
    """
    Converte um DataFrame do Pandas em uma lista de dicionários.

    Por que fazemos isso?

    O Pandas trabalha com DataFrames.
    Mas uma API normalmente devolve dados em JSON.

    Então precisamos transformar algo assim:

        DataFrame

    em algo assim:

        [
            {"nome": "Resident Evil 4", "ano_lancamento": 2005},
            {"nome": "God of War", "ano_lancamento": 2018}
        ]

    Também tratamos valores vazios.

    O Pandas pode representar valores vazios como NaN.
    Mas JSON não trabalha bem com NaN.

    Por isso:
    - transformamos o DataFrame em object;
    - trocamos valores vazios por None;
    - no JSON, None vira null.

    Args:
        df: DataFrame que será convertido.

    Returns:
        list: lista de dicionários pronta para ser retornada pela API.
    """

    df = df.astype(object).where(pd.notnull(df), None)

    return df.to_dict(orient="records")


# ==========================================================
# ENDPOINT INICIAL
# ==========================================================

@app.get("/")
def read_root():
    """
    Endpoint inicial da API.

    Endpoint:
        GET /

    Objetivo:
        Verificar se a API está funcionando corretamente.

    Returns:
        dict: mensagem simples confirmando que a API está ativa.
    """

    return {
        "mensagem": "The AAA Archive API está funcionando",
        "status": "online",
        "versao": "0.1.0"
    }


# ==========================================================
# ENDPOINTS DE JOGOS
# ==========================================================

@app.get("/games")
def listar_games():
    """
    Retorna todos os jogos da Foundation Collection.

    Endpoint:
        GET /games

    Fluxo:
        1. Carrega o games.csv usando carregar_dataset().
        2. Converte o DataFrame em lista de dicionários.
        3. Retorna os dados em formato JSON.

    Returns:
        list: lista com todos os jogos cadastrados.
    """

    df_games = carregar_dataset()

    games = dataframe_para_json(df_games)

    return games