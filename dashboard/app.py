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
# - carregamento do dataset awards.csv;
# - filtros interativos na sidebar;
# - busca textual;
# - métricas principais da Foundation Collection;
# - gráficos simples de estatísticas;
# - tabela com os jogos cadastrados;
# - seção de Awards History;
# - organização visual por abas.
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
from load_data import carregar_dataset, carregar_awards
from site_statistics import gerar_estatisticas_home
from awards import (
    listar_anos_disponiveis,
    listar_jogos_por_ano as listar_awards_por_ano,
    buscar_vencedor_por_ano,
    listar_vencedores,
    listar_vencedores_na_foundation,
    listar_indicados_na_foundation,
    listar_jogos_awards_fora_da_foundation,
)


# ==========================================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================================

st.set_page_config(
    page_title="The AAA Archive",
    page_icon="🎮",
    layout="wide"
)


# ==========================================================
# FUNÇÃO AUXILIAR DE BUSCA
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
# CARREGAMENTO DOS DADOS
# ==========================================================

# Aqui carregamos os dois datasets principais do projeto.
#
# games.csv:
#     base da Foundation Collection.
#
# awards.csv:
#     base independente do histórico de premiações.

df_games = carregar_dataset()
df_awards = carregar_awards()


# ==========================================================
# FILTROS INTERATIVOS
# ==========================================================

# A sidebar é uma barra lateral do Streamlit.
# Ela é muito usada em dashboards para colocar filtros,
# menus e controles sem poluir a tela principal.
#
# Neste dashboard, os filtros da sidebar afetam apenas a
# Foundation Collection.

st.sidebar.title("Filtros")

st.sidebar.write(
    """
    Use os filtros abaixo para explorar a Foundation Collection.
    """
)


# ----------------------------------------------------------
# CAMPO DE BUSCA TEXTUAL
# ----------------------------------------------------------

termo_busca = st.sidebar.text_input(
    "Buscar jogo, gênero, desenvolvedora ou franquia",
    placeholder="Ex: zelda, rockstar, rpg..."
)

# Removemos espaços extras antes e depois do texto.
termo_busca = termo_busca.strip()


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

    Este dashboard apresenta uma visualização inicial da Foundation Collection
    e da Awards History, utilizando os dados já organizados no projeto.
    """
)

st.divider()


# ==========================================================
# ABAS PRINCIPAIS
# ==========================================================

# st.tabs() cria abas dentro da página.
# Isso ajuda a organizar o dashboard sem precisar criar vários arquivos
# ou múltiplas páginas agora.

aba_foundation, aba_awards = st.tabs(
    [
        "Foundation Collection",
        "Awards History"
    ]
)


# ==========================================================
# ABA 1 — FOUNDATION COLLECTION
# ==========================================================

with aba_foundation:

    # ======================================================
    # MÉTRICAS PRINCIPAIS
    # ======================================================

    st.header("Visão Geral da Foundation Collection")

    st.write(
        """
        As métricas abaixo mudam de acordo com a busca e os filtros
        selecionados na barra lateral.
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


    # ======================================================
    # RESUMO DA BUSCA E DOS FILTROS
    # ======================================================

    st.subheader("Resultado da Exploração")

    st.write(
        f"""
        Jogos encontrados: **{len(df_filtrado)}**
        """
    )

    if termo_busca != "":
        st.info(f"Busca aplicada: {termo_busca}")


    # ======================================================
    # VERIFICAÇÃO DE RESULTADOS
    # ======================================================

    # Caso o usuário selecione uma combinação de filtros que não tenha jogos,
    # o dashboard mostra um aviso em vez de tentar gerar gráficos vazios.

    if df_filtrado.empty:
        st.warning("Nenhum jogo encontrado com a busca ou os filtros selecionados.")

    else:

        # ==================================================
        # GRÁFICOS DE ESTATÍSTICAS
        # ==================================================

        st.header("Estatísticas da Foundation Collection")

        st.write(
            """
            Os gráficos abaixo mostram a distribuição dos jogos cadastrados
            de acordo com a busca e os filtros selecionados.
            """
        )


        # --------------------------------------------------
        # GRÁFICO: JOGOS POR DÉCADA
        # --------------------------------------------------

        st.subheader("Jogos por Década")

        df_decadas = estatisticas["quantidade_por_decada"]

        st.bar_chart(
            data=df_decadas,
            x="decada",
            y="total"
        )


        # --------------------------------------------------
        # GRÁFICO: JOGOS POR GÊNERO
        # --------------------------------------------------

        st.subheader("Jogos por Gênero")

        df_generos = estatisticas["quantidade_por_genero"]

        st.bar_chart(
            data=df_generos,
            x="genero",
            y="total"
        )


        # --------------------------------------------------
        # GRÁFICO: JOGOS POR DESENVOLVEDORA
        # --------------------------------------------------

        st.subheader("Desenvolvedoras com Mais Jogos")

        df_developers = estatisticas["quantidade_por_developer"].head(10)

        st.bar_chart(
            data=df_developers,
            x="developer",
            y="total"
        )

        st.divider()


        # ==================================================
        # TABELA PRINCIPAL DE JOGOS
        # ==================================================

        st.header("Jogos Cadastrados")

        st.write(
            """
            A tabela abaixo mostra os jogos encontrados de acordo com
            a busca e os filtros selecionados.
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
# ABA 2 — AWARDS HISTORY
# ==========================================================

with aba_awards:

    st.header("Awards History")

    st.write(
        """
        Esta seção apresenta o histórico de premiações de Game of the Year
        cadastrado no projeto.

        A base de Awards é independente da Foundation Collection, mas também
        pode ser comparada com ela.
        """
    )


    # ======================================================
    # MÉTRICAS DE AWARDS
    # ======================================================

    df_vencedores = listar_vencedores(df_awards)
    df_vencedores_foundation = listar_vencedores_na_foundation(df_awards, df_games)
    df_indicados_foundation = listar_indicados_na_foundation(df_awards, df_games)
    df_fora_foundation = listar_jogos_awards_fora_da_foundation(df_awards, df_games)

    coluna_awards_1, coluna_awards_2, coluna_awards_3, coluna_awards_4 = st.columns(4)

    with coluna_awards_1:
        st.metric(
            label="Registros no Awards",
            value=len(df_awards)
        )

    with coluna_awards_2:
        st.metric(
            label="Anos catalogados",
            value=df_awards["ano"].nunique()
        )

    with coluna_awards_3:
        st.metric(
            label="Vencedores",
            value=len(df_vencedores)
        )

    with coluna_awards_4:
        st.metric(
            label="Fora da Foundation",
            value=len(df_fora_foundation)
        )

    st.divider()


    # ======================================================
    # CONSULTA POR ANO
    # ======================================================

    st.subheader("Consultar edição por ano")

    anos_awards = listar_anos_disponiveis(df_awards)

    ano_awards_selecionado = st.selectbox(
        "Selecione o ano da premiação",
        anos_awards,
        index=len(anos_awards) - 1
    )

    df_awards_ano = listar_awards_por_ano(
        df_awards,
        ano_awards_selecionado
    )

    df_vencedor_ano = buscar_vencedor_por_ano(
        df_awards,
        ano_awards_selecionado
    )

    if df_awards_ano.empty:
        st.warning("Nenhum registro encontrado para o ano selecionado.")

    else:
        if not df_vencedor_ano.empty:
            vencedor = df_vencedor_ano.iloc[0]

            st.success(
                f"Vencedor de {ano_awards_selecionado}: {vencedor['jogo']}"
            )

        st.write(
            """
            A tabela abaixo mostra o vencedor e os indicados da edição selecionada.
            """
        )

        st.dataframe(
            df_awards_ano,
            use_container_width=True
        )


    # ======================================================
    # HISTÓRICO DE VENCEDORES
    # ======================================================

    st.subheader("Histórico de Vencedores")

    st.write(
        """
        A tabela abaixo mostra todos os vencedores de Game of the Year
        cadastrados na base Awards History.
        """
    )

    st.dataframe(
        df_vencedores,
        use_container_width=True
    )


    # ======================================================
    # RELAÇÃO ENTRE AWARDS E FOUNDATION COLLECTION
    # ======================================================

    st.subheader("Relação com a Foundation Collection")

    st.write(
        """
        As tabelas abaixo comparam a Awards History com a Foundation Collection.

        Isso ajuda a identificar quais jogos premiados já estão no arquivo principal
        e quais ainda podem ser analisados futuramente.
        """
    )

    with st.expander("Vencedores presentes na Foundation Collection"):
        st.dataframe(
            df_vencedores_foundation,
            use_container_width=True
        )

    with st.expander("Indicados presentes na Foundation Collection"):
        st.dataframe(
            df_indicados_foundation,
            use_container_width=True
        )

    with st.expander("Jogos do Awards fora da Foundation Collection"):
        st.dataframe(
            df_fora_foundation,
            use_container_width=True
        )


# ==========================================================
# RODAPÉ SIMPLES
# ==========================================================

st.divider()

st.caption(
    "Dashboard inicial — CSV + Pandas + Streamlit"
)