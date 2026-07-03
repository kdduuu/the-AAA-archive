"""
===========================================================
The AAA Archive
Arquivo: main.py

Objetivo:
Criar a primeira versão da API do The AAA Archive.

Nesta fase, a API já possui:
- endpoint inicial de teste;
- endpoint para listar os jogos da Foundation Collection;
- endpoint para pesquisar jogos da Foundation Collection;
- endpoints para filtrar jogos por desenvolvedora, gênero, franquia, ano e década;
- endpoints para listar jogos historicamente importantes e influentes;
- endpoint para retornar estatísticas da Home;
- endpoints para consultar o histórico de premiações.

Autor: Kadu Almeida
===========================================================
"""

# ==========================================================
# IMPORTAÇÃO DOS MÓDULOS
# ==========================================================

from pathlib import Path
import sys

import pandas as pd
from fastapi import FastAPI, Query


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
    ├── load_data.py
    ├── search.py
    ├── filters.py
    ├── site_statistics.py
    └── awards.py

A variável PROJECT_ROOT representa a raiz do projeto.
A variável SCRIPTS_PATH representa a pasta scripts/.
"""

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_PATH = PROJECT_ROOT / "scripts"

if str(SCRIPTS_PATH) not in sys.path:
    sys.path.append(str(SCRIPTS_PATH))


# Agora o Python consegue importar os módulos da pasta scripts.
from load_data import carregar_dataset, carregar_awards
from search import pesquisar_jogos
from filters import (
    listar_jogos_por_developer,
    listar_jogos_por_genero,
    listar_jogos_por_franquia,
    listar_jogos_por_ano,
    listar_jogos_por_decada,
)
from site_statistics import (
    gerar_estatisticas_home,
    listar_jogos_historicos,
    listar_jogos_influentes,
)
from awards import (
    listar_jogos_por_ano as consultar_awards_por_ano,
    listar_vencedores,
    listar_vencedores_na_foundation,
    listar_indicados_na_foundation,
    listar_jogos_awards_fora_da_foundation,
)


# ==========================================================
# CRIAÇÃO DA APLICAÇÃO
# ==========================================================

app = FastAPI(
    title="The AAA Archive API",
    description="API para consultar dados do projeto The AAA Archive.",
    version="0.1.0"
)


# ==========================================================
# FUNÇÕES AUXILIARES
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


def dados_para_json(dados):
    """
    Converte diferentes tipos de dados para formatos compatíveis com JSON.

    Por que essa função existe?

    Algumas funções do backend retornam apenas um DataFrame.
    Outras retornam um dicionário que contém vários DataFrames dentro.

    Exemplo:

        {
            "total_jogos": 66,
            "jogos_por_genero": DataFrame,
            "jogos_por_decada": DataFrame
        }

    A API não consegue devolver um DataFrame diretamente.

    Então essa função verifica o tipo do dado:

    - se for DataFrame, converte para lista de dicionários;
    - se for dicionário, analisa cada item dentro dele;
    - se for lista, analisa cada item da lista;
    - se for um valor simples, retorna normalmente.

    Args:
        dados: qualquer dado retornado pelos módulos do backend.

    Returns:
        dados em formato compatível com JSON.
    """

    if isinstance(dados, pd.DataFrame):
        return dataframe_para_json(dados)

    if isinstance(dados, dict):
        return {
            chave: dados_para_json(valor)
            for chave, valor in dados.items()
        }

    if isinstance(dados, list):
        return [
            dados_para_json(item)
            for item in dados
        ]

    return dados


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


@app.get("/games/search")
def pesquisar_games(
    term: str = Query(
        "",
        description="Termo usado para pesquisar jogos por nome, gênero, desenvolvedora, franquia ou descrição."
    )
):
    """
    Pesquisa jogos da Foundation Collection a partir de um termo.

    Endpoint:
        GET /games/search

    Exemplo:
        /games/search?term=zelda

    Fluxo:
        1. Recebe o termo pesquisado pela URL.
        2. Carrega o games.csv usando carregar_dataset().
        3. Usa a função pesquisar_jogos() do módulo search.py.
        4. Converte o resultado para JSON.
        5. Retorna os jogos encontrados.

    Args:
        term: termo pesquisado pelo usuário.

    Returns:
        list: lista de jogos encontrados.
    """

    df_games = carregar_dataset()

    resultado = pesquisar_jogos(df_games, term)

    games = dataframe_para_json(resultado)

    return games


@app.get("/games/developer/{developer}")
def listar_games_por_developer(developer: str):
    """
    Retorna jogos de uma desenvolvedora específica.

    Endpoint:
        GET /games/developer/{developer}

    Exemplo:
        /games/developer/Capcom

    Fluxo:
        1. Recebe o nome da desenvolvedora pela URL.
        2. Carrega o games.csv usando carregar_dataset().
        3. Usa a função listar_jogos_por_developer() do módulo filters.py.
        4. Converte o resultado para JSON.
        5. Retorna os jogos encontrados.

    Args:
        developer: nome da desenvolvedora.

    Returns:
        list: lista de jogos da desenvolvedora informada.
    """

    df_games = carregar_dataset()

    resultado = listar_jogos_por_developer(df_games, developer)

    games = dataframe_para_json(resultado)

    return games


@app.get("/games/genre/{genre}")
def listar_games_por_genero(genre: str):
    """
    Retorna jogos de um gênero específico.

    Endpoint:
        GET /games/genre/{genre}

    Exemplo:
        /games/genre/Survival Horror

    Fluxo:
        1. Recebe o gênero pela URL.
        2. Carrega o games.csv usando carregar_dataset().
        3. Usa a função listar_jogos_por_genero() do módulo filters.py.
        4. Converte o resultado para JSON.
        5. Retorna os jogos encontrados.

    Args:
        genre: gênero pesquisado.

    Returns:
        list: lista de jogos do gênero informado.
    """

    df_games = carregar_dataset()

    resultado = listar_jogos_por_genero(df_games, genre)

    games = dataframe_para_json(resultado)

    return games


@app.get("/games/franchise/{franchise}")
def listar_games_por_franquia(franchise: str):
    """
    Retorna jogos de uma franquia específica.

    Endpoint:
        GET /games/franchise/{franchise}

    Exemplo:
        /games/franchise/Resident Evil

    Fluxo:
        1. Recebe o nome da franquia pela URL.
        2. Carrega o games.csv usando carregar_dataset().
        3. Usa a função listar_jogos_por_franquia() do módulo filters.py.
        4. Converte o resultado para JSON.
        5. Retorna os jogos encontrados.

    Args:
        franchise: nome da franquia.

    Returns:
        list: lista de jogos da franquia informada.
    """

    df_games = carregar_dataset()

    resultado = listar_jogos_por_franquia(df_games, franchise)

    games = dataframe_para_json(resultado)

    return games


@app.get("/games/year/{year}")
def listar_games_por_ano(year: int):
    """
    Retorna jogos lançados em um ano específico.

    Endpoint:
        GET /games/year/{year}

    Exemplo:
        /games/year/2018

    Fluxo:
        1. Recebe o ano pela URL.
        2. Carrega o games.csv usando carregar_dataset().
        3. Usa a função listar_jogos_por_ano() do módulo filters.py.
        4. Converte o resultado para JSON.
        5. Retorna os jogos encontrados.

    Args:
        year: ano de lançamento.

    Returns:
        list: lista de jogos lançados no ano informado.
    """

    df_games = carregar_dataset()

    resultado = listar_jogos_por_ano(df_games, year)

    games = dataframe_para_json(resultado)

    return games


@app.get("/games/decade/{decade}")
def listar_games_por_decada(decade: int):
    """
    Retorna jogos lançados em uma década específica.

    Endpoint:
        GET /games/decade/{decade}

    Exemplo:
        /games/decade/2000

    Fluxo:
        1. Recebe a década pela URL.
        2. Carrega o games.csv usando carregar_dataset().
        3. Usa a função listar_jogos_por_decada() do módulo filters.py.
        4. Converte o resultado para JSON.
        5. Retorna os jogos encontrados.

    Args:
        decade: década pesquisada. Exemplo: 1990, 2000, 2010.

    Returns:
        list: lista de jogos lançados na década informada.
    """

    df_games = carregar_dataset()

    resultado = listar_jogos_por_decada(df_games, decade)

    games = dataframe_para_json(resultado)

    return games


@app.get("/games/historical")
def listar_games_historicos():
    """
    Retorna jogos marcados como historicamente importantes.

    Endpoint:
        GET /games/historical

    Fluxo:
        1. Carrega o games.csv usando carregar_dataset().
        2. Usa a função listar_jogos_historicos() do módulo site_statistics.py.
        3. Converte o resultado para JSON.
        4. Retorna os jogos historicamente importantes.

    Returns:
        list: lista de jogos marcados como historicamente importantes.
    """

    df_games = carregar_dataset()

    resultado = listar_jogos_historicos(df_games)

    games = dataframe_para_json(resultado)

    return games


@app.get("/games/influential")
def listar_games_influentes():
    """
    Retorna jogos marcados como historicamente influentes.

    Endpoint:
        GET /games/influential

    Fluxo:
        1. Carrega o games.csv usando carregar_dataset().
        2. Usa a função listar_jogos_influentes() do módulo site_statistics.py.
        3. Converte o resultado para JSON.
        4. Retorna os jogos historicamente influentes.

    Returns:
        list: lista de jogos marcados como historicamente influentes.
    """

    df_games = carregar_dataset()

    resultado = listar_jogos_influentes(df_games)

    games = dataframe_para_json(resultado)

    return games


# ==========================================================
# ENDPOINTS DE ESTATÍSTICAS
# ==========================================================

@app.get("/stats/home")
def obter_estatisticas_home():
    """
    Retorna estatísticas gerais para a futura Home do site.

    Endpoint:
        GET /stats/home

    Fluxo:
        1. Carrega o games.csv usando carregar_dataset().
        2. Usa a função gerar_estatisticas_home() do módulo site_statistics.py.
        3. Converte os dados para um formato compatível com JSON.
        4. Retorna as estatísticas da Home.

    Returns:
        dict: estatísticas gerais da Foundation Collection.
    """

    df_games = carregar_dataset()

    estatisticas = gerar_estatisticas_home(df_games)

    estatisticas_json = dados_para_json(estatisticas)

    return estatisticas_json


# ==========================================================
# ENDPOINTS DE AWARDS
# ==========================================================

@app.get("/awards")
def listar_awards():
    """
    Retorna todos os registros da base Awards History.

    Endpoint:
        GET /awards

    Fluxo:
        1. Carrega o awards.csv usando carregar_awards().
        2. Converte o DataFrame em lista de dicionários.
        3. Retorna todos os registros em JSON.

    Returns:
        list: lista com vencedores e indicados cadastrados.
    """

    df_awards = carregar_awards()

    awards = dataframe_para_json(df_awards)

    return awards


@app.get("/awards/winners")
def listar_awards_vencedores():
    """
    Retorna todos os vencedores de Game of the Year.

    Endpoint:
        GET /awards/winners

    Fluxo:
        1. Carrega o awards.csv.
        2. Usa a função listar_vencedores() do módulo awards.py.
        3. Converte o resultado para JSON.
        4. Retorna os vencedores.

    Returns:
        list: lista com todos os vencedores.
    """

    df_awards = carregar_awards()

    resultado = listar_vencedores(df_awards)

    vencedores = dataframe_para_json(resultado)

    return vencedores


@app.get("/awards/foundation/winners")
def listar_awards_vencedores_na_foundation():
    """
    Retorna vencedores de Game of the Year que também estão
    presentes na Foundation Collection.

    Endpoint:
        GET /awards/foundation/winners

    Fluxo:
        1. Carrega o awards.csv.
        2. Carrega o games.csv.
        3. Usa a função listar_vencedores_na_foundation().
        4. Converte o resultado para JSON.
        5. Retorna os vencedores encontrados nas duas bases.

    Returns:
        list: lista com vencedores presentes na Foundation Collection.
    """

    df_awards = carregar_awards()
    df_games = carregar_dataset()

    resultado = listar_vencedores_na_foundation(df_awards, df_games)

    vencedores = dataframe_para_json(resultado)

    return vencedores


@app.get("/awards/foundation/nominees")
def listar_awards_indicados_na_foundation():
    """
    Retorna indicados a Game of the Year que também estão
    presentes na Foundation Collection.

    Endpoint:
        GET /awards/foundation/nominees

    Fluxo:
        1. Carrega o awards.csv.
        2. Carrega o games.csv.
        3. Usa a função listar_indicados_na_foundation().
        4. Converte o resultado para JSON.
        5. Retorna os indicados encontrados nas duas bases.

    Returns:
        list: lista com indicados presentes na Foundation Collection.
    """

    df_awards = carregar_awards()
    df_games = carregar_dataset()

    resultado = listar_indicados_na_foundation(df_awards, df_games)

    indicados = dataframe_para_json(resultado)

    return indicados


@app.get("/awards/foundation/outside")
def listar_awards_fora_da_foundation():
    """
    Retorna jogos presentes na Awards History, mas que ainda
    não estão na Foundation Collection.

    Endpoint:
        GET /awards/foundation/outside

    Fluxo:
        1. Carrega o awards.csv.
        2. Carrega o games.csv.
        3. Usa a função listar_jogos_awards_fora_da_foundation().
        4. Converte o resultado para JSON.
        5. Retorna os jogos fora da Foundation Collection.

    Returns:
        list: lista com jogos do Awards que não estão na Foundation Collection.
    """

    df_awards = carregar_awards()
    df_games = carregar_dataset()

    resultado = listar_jogos_awards_fora_da_foundation(df_awards, df_games)

    jogos = dataframe_para_json(resultado)

    return jogos


@app.get("/awards/{year}")
def obter_awards_por_ano(year: int):
    """
    Retorna vencedor e indicados de uma edição específica.

    Endpoint:
        GET /awards/{year}

    Exemplo:
        /awards/2018

    Fluxo:
        1. Recebe o ano pela URL.
        2. Carrega o awards.csv.
        3. Usa a função listar_jogos_por_ano() do módulo awards.py.
        4. Converte o resultado para JSON.
        5. Retorna vencedor e indicados daquele ano.

    Args:
        year: ano da premiação.

    Returns:
        list: lista com vencedor e indicados do ano informado.
    """

    df_awards = carregar_awards()

    resultado = consultar_awards_por_ano(df_awards, year)

    awards = dataframe_para_json(resultado)

    return awards