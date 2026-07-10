# ==========================================================
# The AAA Archive
# Arquivo: dashboard_helpers.py
#
# Objetivo:
# Guardar funções auxiliares usadas pelo dashboard Streamlit.
#
# Este arquivo ajuda a deixar o app.py mais limpo.
#
# O app.py fica responsável pela interface visual.
# O dashboard_helpers.py fica responsável por pequenas lógicas auxiliares,
# como carregamento dos dados, busca, filtros e dados derivados.
#
# Mudança importante desta versão:
# Antes, o dashboard carregava os dados diretamente dos CSVs.
#
# Fluxo antigo:
#   dashboard_helpers.py
#       ↓
#   load_data.py
#       ↓
#   data/games.csv / data/awards.csv
#
# Agora, o dashboard carrega os dados do PostgreSQL.
#
# Fluxo novo:
#   dashboard_helpers.py
#       ↓
#   database.py
#       ↓
#   PostgreSQL
#       ↓
#   DataFrame Pandas
#
# Autor: Kadu Almeida
# ==========================================================


# ==========================================================
# IMPORTAÇÃO DOS MÓDULOS
# ==========================================================

from pathlib import Path
import sys

import streamlit as st


# ==========================================================
# CONFIGURAÇÃO DOS CAMINHOS DO PROJETO
# ==========================================================

# O arquivo dashboard_helpers.py está dentro da pasta dashboard/.
# Já os módulos principais do projeto estão dentro da pasta scripts/.
#
# Por isso, também precisamos ensinar o Python onde encontrar
# os módulos do backend.

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_PATH = PROJECT_ROOT / "scripts"

if str(SCRIPTS_PATH) not in sys.path:
    sys.path.append(str(SCRIPTS_PATH))


# ==========================================================
# IMPORTAÇÃO DOS MÓDULOS DO PROJETO
# ==========================================================

# Antes, este arquivo importava:
#
#   from load_data import carregar_dataset, carregar_awards
#
# Essas funções liam os arquivos CSV.
#
# Agora usamos as funções do database.py, que leem os dados
# diretamente do PostgreSQL.

from database import (
    carregar_games_do_banco,
    carregar_awards_do_banco,
)

from awards import (
    listar_anos_disponiveis,
    listar_vencedores,
    listar_vencedores_na_foundation,
    listar_indicados_na_foundation,
    listar_jogos_awards_fora_da_foundation,
)


# ==========================================================
# CARREGAMENTO DOS DADOS COM CACHE
# ==========================================================

@st.cache_data
def carregar_games_com_cache():
    """
    Carrega os dados da tabela games usando cache do Streamlit.

    Antes:
        games.csv
            ↓
        load_data.py
            ↓
        dashboard

    Agora:
        PostgreSQL
            ↓
        database.py
            ↓
        dashboard

    O cache evita que o dashboard consulte o banco do zero toda vez que
    o usuário interage com filtros, abas ou campos de busca.

    Observação:
        Se os dados forem reimportados no PostgreSQL e o Streamlit ainda
        mostrar dados antigos, basta reiniciar o app ou limpar o cache.
    """

    df_games = carregar_games_do_banco()

    return df_games


@st.cache_data
def carregar_awards_com_cache():
    """
    Carrega os dados da tabela awards usando cache do Streamlit.

    Antes:
        awards.csv
            ↓
        load_data.py
            ↓
        dashboard

    Agora:
        PostgreSQL
            ↓
        database.py
            ↓
        dashboard

    Observação importante:
        No PostgreSQL, a tabela awards possui uma coluna id automática.

        O awards.csv original não tinha essa coluna.

        Para manter o dashboard visualmente parecido com a versão antiga,
        removemos a coluna id aqui.
    """

    df_awards = carregar_awards_do_banco()

    if "id" in df_awards.columns:
        df_awards = df_awards.drop(columns=["id"])

    return df_awards


# ==========================================================
# BUSCA TEXTUAL
# ==========================================================

def aplicar_busca_textual(df, termo_busca):
    """
    Aplica uma busca textual simples no DataFrame de jogos.

    A busca procura o termo nas colunas:
    - nome;
    - genero;
    - developer;
    - franchise;
    - descricao.

    Parâmetros:
        df:
            DataFrame com os jogos.

        termo_busca:
            Texto digitado pelo usuário.

    Retorno:
        DataFrame filtrado com os jogos encontrados.
    """

    # Se o usuário não digitou nada, retornamos o DataFrame original.
    if termo_busca == "":
        return df

    # Padronizamos o termo para minúsculo.
    # Isso faz a busca não depender de letras maiúsculas ou minúsculas.
    termo_busca = termo_busca.lower()

    # Colunas onde a busca será aplicada.
    colunas_busca = [
        "nome",
        "genero",
        "developer",
        "franchise",
        "descricao"
    ]

    # Criamos uma condição inicial vazia.
    # Depois vamos somando as buscas de cada coluna.
    condicao_busca = False

    for coluna in colunas_busca:
        condicao_busca = condicao_busca | (
            df[coluna]
            .fillna("")
            .astype(str)
            .str.lower()
            .str.contains(termo_busca, regex=False)
        )

    return df[condicao_busca]


# ==========================================================
# OPÇÕES DOS FILTROS
# ==========================================================

def criar_opcoes_filtro(df_games):
    """
    Cria as opções usadas nos filtros da sidebar.

    O valor "Todos" é colocado no começo de cada lista para permitir
    visualizar a Foundation Collection completa.
    """

    opcoes_genero = ["Todos"] + sorted(
        df_games["genero"].dropna().unique().tolist()
    )

    opcoes_developer = ["Todos"] + sorted(
        df_games["developer"].dropna().unique().tolist()
    )

    opcoes_ano = ["Todos"] + sorted(
        df_games["ano_lancamento"].dropna().unique().tolist()
    )

    opcoes_franquia = ["Todos"] + sorted(
        df_games["franchise"].dropna().unique().tolist()
    )

    return {
        "generos": opcoes_genero,
        "developers": opcoes_developer,
        "anos": opcoes_ano,
        "franquias": opcoes_franquia,
    }


# ==========================================================
# FILTROS DA FOUNDATION COLLECTION
# ==========================================================

def aplicar_filtros_foundation(
    df_games,
    termo_busca,
    genero_selecionado,
    developer_selecionada,
    ano_selecionado,
    franquia_selecionada
):
    """
    Aplica busca textual e filtros da sidebar na Foundation Collection.

    Essa função concentra a lógica de filtragem para deixar o app.py
    mais limpo e mais focado na parte visual do Streamlit.
    """

    # Começamos com uma cópia do dataset completo.
    # Depois vamos reduzindo esse DataFrame conforme os filtros escolhidos.
    df_filtrado = df_games.copy()

    # Primeiro aplicamos a busca textual.
    df_filtrado = aplicar_busca_textual(df_filtrado, termo_busca)

    # Depois aplicamos os filtros específicos.
    if genero_selecionado != "Todos":
        df_filtrado = df_filtrado[df_filtrado["genero"] == genero_selecionado]

    if developer_selecionada != "Todos":
        df_filtrado = df_filtrado[df_filtrado["developer"] == developer_selecionada]

    if ano_selecionado != "Todos":
        df_filtrado = df_filtrado[df_filtrado["ano_lancamento"] == ano_selecionado]

    if franquia_selecionada != "Todos":
        df_filtrado = df_filtrado[df_filtrado["franchise"] == franquia_selecionada]

    return df_filtrado


# ==========================================================
# DADOS AUXILIARES DA AWARDS HISTORY
# ==========================================================

def gerar_dados_awards(df_awards, df_games):
    """
    Gera dados auxiliares usados na aba Awards History.

    Essa função evita que o app.py fique cheio de chamadas repetidas
    para o módulo awards.py.
    """

    df_vencedores = listar_vencedores(df_awards)

    df_vencedores_foundation = listar_vencedores_na_foundation(
        df_awards,
        df_games
    )

    df_indicados_foundation = listar_indicados_na_foundation(
        df_awards,
        df_games
    )

    df_fora_foundation = listar_jogos_awards_fora_da_foundation(
        df_awards,
        df_games
    )

    anos_disponiveis = listar_anos_disponiveis(df_awards)

    return {
        "vencedores": df_vencedores,
        "vencedores_foundation": df_vencedores_foundation,
        "indicados_foundation": df_indicados_foundation,
        "fora_foundation": df_fora_foundation,
        "anos_disponiveis": anos_disponiveis,
    }