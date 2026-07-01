"""
===========================================================
The AAA Archive
Arquivo: app.py

Objetivo:
Criar a primeira versão do Dashboard do The AAA Archive
utilizando Streamlit.

Nesta fase, o dashboard já possui:
- título inicial;
- descrição do projeto;
- carregamento do dataset games.csv;
- métricas principais da Foundation Collection;
- tabela inicial com os jogos cadastrados.

Autor: Kadu Almeida
===========================================================
"""

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

estatisticas = gerar_estatisticas_home(df_games)


# ==========================================================
# CABEÇALHO DO DASHBOARD
# ==========================================================

st.title("The AAA Archive")

st.write(
    """
    Um arquivo digital sobre jogos AAA single-player historicamente relevantes.

    Este dashboard apresenta uma primeira visualização da Foundation Collection,
    utilizando os dados já organizados no projeto.
    """
)

st.divider()


# ==========================================================
# MÉTRICAS PRINCIPAIS
# ==========================================================

st.header("Visão Geral da Foundation Collection")

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
# TABELA PRINCIPAL DE JOGOS
# ==========================================================

st.header("Jogos Cadastrados")

st.write(
    """
    A tabela abaixo mostra os jogos presentes no dataset principal
    da Foundation Collection.
    """
)

# Para a primeira versão, vamos mostrar apenas algumas colunas principais.
# A coluna descricao existe no dataset, mas pode deixar a tabela muito larga.

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
    df_games[colunas_tabela],
    use_container_width=True
)


# ==========================================================
# RODAPÉ SIMPLES
# ==========================================================

st.divider()

st.caption(
    "Primeira versão do dashboard — CSV + Pandas + Streamlit"
)