# ==========================================================
# The AAA Archive
# Arquivo: app.py
#
# Objetivo:
# Criar o Dashboard do The AAA Archive utilizando Streamlit.
#
# Nesta fase, o dashboard possui:
# - título inicial;
# - descrição do projeto;
# - carregamento do dataset games.csv;
# - filtros interativos na sidebar;
# - métricas principais da Foundation Collection;
# - gráficos simples de estatísticas;
# - tabela com os jogos cadastrados.
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

# O arquivo app.py está dentro da pasta dashboard/.
# Já os módulos principais do projeto estão dentro da pasta scripts/.
#
# Por isso, assim como fizemos na API, precisamos ensinar o Python
# onde encontrar os módulos do backend.

# Caminho absoluto da raiz do projeto.
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Caminho absoluto da pasta scripts/.
SCRIPTS_PATH = PROJECT_ROOT / "scripts"

# Adiciona a pasta scripts/ ao caminho de importação do Python.
if str(SCRIPTS_PATH) not in sys.path:
    sys.path.append(str(SCRIPTS_PATH))


# Agora conseguimos importar os módulos do backend.
from load_data import carregar_dataset
from site_statistics import gerar_estatisticas_home


# ==========================================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================================

st.set_page_config(
    page_title="The AAA Archive",
    page_icon="🎮",
    layout="wide"
)


# ==========================================================
# CARREGAMENTO DOS DADOS
# ==========================================================

# Aqui carregamos o dataset principal do projeto.
# A função carregar_dataset() já existe no backend.
# Isso evita repetir lógica dentro do dashboard.

df_games = carregar_dataset()


# ==========================================================
# FILTROS INTERATIVOS
# ==========================================================

# A sidebar é uma barra lateral do Streamlit.
# Ela é muito usada em dashboards para colocar filtros,
# menus e controles sem poluir a tela principal.

st.sidebar.title("Filtros")

st.sidebar.write(
    """
    Use os filtros abaixo para explorar a Foundation Collection.
    """
)


# ----------------------------------------------------------
# OPÇÕES DOS FILTROS
# ----------------------------------------------------------

# Criamos listas com as opções disponíveis no dataset.
# O valor "Todos" permite visualizar a coleção inteira.

opcoes_genero = ["Todos"] + sorted(df_games["genero"].dropna().unique().tolist())

opcoes_developer = ["Todos"] + sorted(df_games["developer"].dropna().unique().tolist())

opcoes_ano = ["Todos"] + sorted(df_games["ano_lancamento"].dropna().unique().tolist())

opcoes_franquia = ["Todos"] + sorted(df_games["franchise"].dropna().unique().tolist())


# ----------------------------------------------------------
# CAMPOS VISUAIS DA SIDEBAR
# ----------------------------------------------------------

genero_selecionado = st.sidebar.selectbox(
    "Gênero",
    opcoes_genero
)

developer_selecionada = st.sidebar.selectbox(
    "Desenvolvedora",
    opcoes_developer
)

ano_selecionado = st.sidebar.selectbox(
    "Ano de lançamento",
    opcoes_ano
)

franquia_selecionada = st.sidebar.selectbox(
    "Franquia",
    opcoes_franquia
)


# ----------------------------------------------------------
# APLICAÇÃO DOS FILTROS
# ----------------------------------------------------------

# Começamos com uma cópia do dataset completo.
# Depois, vamos reduzindo esse DataFrame conforme os filtros escolhidos.

df_filtrado = df_games.copy()

if genero_selecionado != "Todos":
    df_filtrado = df_filtrado[df_filtrado["genero"] == genero_selecionado]

if developer_selecionada != "Todos":
    df_filtrado = df_filtrado[df_filtrado["developer"] == developer_selecionada]

if ano_selecionado != "Todos":
    df_filtrado = df_filtrado[df_filtrado["ano_lancamento"] == ano_selecionado]

if franquia_selecionada != "Todos":
    df_filtrado = df_filtrado[df_filtrado["franchise"] == franquia_selecionada]


# As estatísticas agora são geradas com base no DataFrame filtrado.
# Isso significa que métricas, gráficos e tabela reagem aos filtros.

estatisticas = gerar_estatisticas_home(df_filtrado)


# ==========================================================
# CABEÇALHO DO DASHBOARD
# ==========================================================

st.title("The AAA Archive")

st.write(
    """
    Um arquivo digital sobre jogos AAA single-player historicamente relevantes.

    Este dashboard apresenta uma visualização inicial da Foundation Collection,
    utilizando os dados já organizados no projeto.
    """
)

st.divider()


# ==========================================================
# MÉTRICAS PRINCIPAIS
# ==========================================================

st.header("Visão Geral da Foundation Collection")

st.write(
    """
    As métricas abaixo mudam de acordo com os filtros selecionados.
    """
)

coluna_1, coluna_2, coluna_3, coluna_4 = st.columns(4)

with coluna_1:
    st.metric(
        label="Jogos",
        value=estatisticas["total_jogos"]
    )

with coluna_2:
    st.metric(
        label="Desenvolvedoras",
        value=estatisticas["total_developers"]
    )

with coluna_3:
    st.metric(
        label="Franquias",
        value=estatisticas["total_franquias"]
    )

with coluna_4:
    st.metric(
        label="Gêneros",
        value=estatisticas["total_generos"]
    )

st.divider()


# ==========================================================
# VERIFICAÇÃO DE RESULTADOS
# ==========================================================

# Caso o usuário selecione uma combinação de filtros que não tenha jogos,
# o dashboard mostra um aviso em vez de tentar gerar gráficos vazios.

if df_filtrado.empty:
    st.warning("Nenhum jogo encontrado com os filtros selecionados.")

else:

    # ======================================================
    # GRÁFICOS DE ESTATÍSTICAS
    # ======================================================

    st.header("Estatísticas da Foundation Collection")

    st.write(
        """
        Os gráficos abaixo mostram a distribuição dos jogos cadastrados
        de acordo com os filtros selecionados.
        """
    )


    # ------------------------------------------------------
    # GRÁFICO: JOGOS POR DÉCADA
    # ------------------------------------------------------

    st.subheader("Jogos por Década")

    df_decadas = estatisticas["quantidade_por_decada"]

    st.bar_chart(
        data=df_decadas,
        x="decada",
        y="total"
    )


    # ------------------------------------------------------
    # GRÁFICO: JOGOS POR GÊNERO
    # ------------------------------------------------------

    st.subheader("Jogos por Gênero")

    df_generos = estatisticas["quantidade_por_genero"]

    st.bar_chart(
        data=df_generos,
        x="genero",
        y="total"
    )


    # ------------------------------------------------------
    # GRÁFICO: JOGOS POR DESENVOLVEDORA
    # ------------------------------------------------------

    st.subheader("Desenvolvedoras com Mais Jogos")

    df_developers = estatisticas["quantidade_por_developer"].head(10)

    st.bar_chart(
        data=df_developers,
        x="developer",
        y="total"
    )

    st.divider()


    # ======================================================
    # TABELA PRINCIPAL DE JOGOS
    # ======================================================

    st.header("Jogos Cadastrados")

    st.write(
        """
        A tabela abaixo mostra os jogos encontrados de acordo com
        os filtros selecionados.
        """
    )

    colunas_tabela = [
        "id",
        "nome",
        "ano_lancamento",
        "genero",
        "developer",
        "franchise",
        "metacritic",
        "nota_kadu",
        "nota_pavam"
    ]

    st.dataframe(
        df_filtrado[colunas_tabela],
        use_container_width=True
    )


# ==========================================================
# RODAPÉ SIMPLES
# ==========================================================

st.divider()

st.caption(
    "Dashboard inicial — CSV + Pandas + Streamlit"
)