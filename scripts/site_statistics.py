"""
===========================================================
The AAA Archive
Arquivo: site_statistics.py

Objetivo:
Gerar estatísticas reutilizáveis sobre a Foundation Collection.

Este módulo será utilizado futuramente pela Home, API e Dashboard.
Por isso, as funções não devem imprimir os resultados diretamente.
Elas devem receber um DataFrame e retornar dados prontos para uso.

Autor: Kadu Almeida
===========================================================
"""

# ==========================================================
# IMPORTAÇÃO DOS MÓDULOS
# ==========================================================

# Importamos a função responsável por carregar o dataset.
# Ela só será usada na área de teste no final do arquivo.
from load_data import carregar_dataset


# ==========================================================
# ESTATÍSTICAS GERAIS
# ==========================================================

def contar_total_jogos(df):
    """
    Conta quantos jogos existem na coleção.

    Cada linha do DataFrame representa um jogo.
    Portanto, len(df) retorna o total de jogos cadastrados.

    Args:
        df: DataFrame contendo os jogos.

    Returns:
        int: total de jogos.
    """

    return len(df)


def contar_total_developers(df):
    """
    Conta quantas desenvolvedoras diferentes existem na coleção.

    nunique() conta apenas valores únicos.
    Exemplo:
        Capcom
        Capcom
        Rockstar

    Resultado:
        2 desenvolvedoras diferentes.

    Args:
        df: DataFrame contendo os jogos.

    Returns:
        int: total de desenvolvedoras únicas.
    """

    return df["developer"].nunique()


def contar_total_franquias(df):
    """
    Conta quantas franquias diferentes existem na coleção.

    Args:
        df: DataFrame contendo os jogos.

    Returns:
        int: total de franquias únicas.
    """

    return df["franchise"].nunique()


def contar_total_generos(df):
    """
    Conta quantos gêneros diferentes existem na coleção.

    Args:
        df: DataFrame contendo os jogos.

    Returns:
        int: total de gêneros únicos.
    """

    return df["genero"].nunique()


# ==========================================================
# CONTAGENS PARA HOME E DASHBOARD
# ==========================================================

def listar_quantidade_por_genero(df):
    """
    Retorna a quantidade de jogos por gênero.

    Esta função poderá ser usada:
    - na Home, para mostrar os gêneros mais presentes;
    - no Dashboard, para gerar gráficos por gênero.

    Args:
        df: DataFrame contendo os jogos.

    Returns:
        DataFrame: tabela com gênero e total de jogos.
    """

    contagem = df["genero"].value_counts().reset_index()

    contagem.columns = ["genero", "total"]

    return contagem


def listar_quantidade_por_developer(df):
    """
    Retorna a quantidade de jogos por desenvolvedora.

    Esta função poderá ser usada:
    - na Home, para destacar desenvolvedoras recorrentes;
    - no Dashboard, para gráficos de distribuição.

    Args:
        df: DataFrame contendo os jogos.

    Returns:
        DataFrame: tabela com desenvolvedora e total de jogos.
    """

    contagem = df["developer"].value_counts().reset_index()

    contagem.columns = ["developer", "total"]

    return contagem


def listar_quantidade_por_franquia(df):
    """
    Retorna a quantidade de jogos por franquia.

    Args:
        df: DataFrame contendo os jogos.

    Returns:
        DataFrame: tabela com franquia e total de jogos.
    """

    contagem = df["franchise"].value_counts().reset_index()

    contagem.columns = ["franchise", "total"]

    return contagem


def listar_quantidade_por_decada(df):
    """
    Retorna a quantidade de jogos por década.

    Exemplo:
        1997 -> 1990
        2004 -> 2000
        2018 -> 2010

    Esta função será útil para criar a linha do tempo da Home
    e gráficos históricos no Dashboard.

    Args:
        df: DataFrame contendo os jogos.

    Returns:
        DataFrame: tabela com década e total de jogos.
    """

    # Criamos uma cópia para não modificar o DataFrame original.
    df_copia = df.copy()

    # Calcula a década com base no ano de lançamento.
    df_copia["decada"] = (df_copia["ano_lancamento"] // 10) * 10

    contagem = df_copia["decada"].value_counts().sort_index().reset_index()

    contagem.columns = ["decada", "total"]

    return contagem


# ==========================================================
# JOGOS HISTÓRICOS E INFLUENTES
# ==========================================================

def listar_jogos_historicos(df):
    """
    Retorna os jogos marcados como historicamente importantes.

    A coluna historico_importante faz parte do contrato oficial
    do dataset, mas pode estar vazia durante a construção inicial.

    Args:
        df: DataFrame contendo os jogos.

    Returns:
        DataFrame: jogos historicamente importantes.
    """

    filtro = (
        (df["historico_importante"] == True) |
        (df["historico_importante"].astype(str).str.upper() == "TRUE")
    )

    # copy() mantém o padrão do projeto:
    # toda função que filtra dados retorna uma cópia independente.
    return df[filtro].copy()


def listar_jogos_influentes(df):
    """
    Retorna os jogos marcados como historicamente influentes.

    Args:
        df: DataFrame contendo os jogos.

    Returns:
        DataFrame: jogos influentes.
    """

    filtro = (
        (df["historico_influente"] == True) |
        (df["historico_influente"].astype(str).str.upper() == "TRUE")
    )

    # copy() evita alterações acidentais no DataFrame original.
    return df[filtro].copy()


# ==========================================================
# ESTATÍSTICAS CONSOLIDADAS DA HOME
# ==========================================================

def gerar_estatisticas_home(df):
    """
    Reúne as principais estatísticas que serão usadas na Home.

    Esta função funciona como um resumo geral do Archive.
    Futuramente, a API poderá chamar esta função para enviar
    esses dados ao website.

    Args:
        df: DataFrame contendo os jogos.

    Returns:
        dict: dicionário com as estatísticas principais.
    """

    estatisticas = {
        "total_jogos": contar_total_jogos(df),
        "total_developers": contar_total_developers(df),
        "total_franquias": contar_total_franquias(df),
        "total_generos": contar_total_generos(df),
        "quantidade_por_genero": listar_quantidade_por_genero(df),
        "quantidade_por_developer": listar_quantidade_por_developer(df),
        "quantidade_por_franquia": listar_quantidade_por_franquia(df),
        "quantidade_por_decada": listar_quantidade_por_decada(df),
        "jogos_historicos": listar_jogos_historicos(df),
        "jogos_influentes": listar_jogos_influentes(df),
    }

    return estatisticas


# ==========================================================
# ÁREA DE TESTE MANUAL
# ==========================================================

if __name__ == "__main__":
    """
    Esta parte só será executada quando rodarmos este arquivo diretamente.

    Exemplo:
        python scripts/site_statistics.py

    Quando outro arquivo importar este módulo, nada será impresso
    automaticamente. Isso torna o código reutilizável.
    """

    df = carregar_dataset()

    estatisticas = gerar_estatisticas_home(df)

    print("=" * 60)
    print("THE AAA ARCHIVE")
    print("SITE STATISTICS")
    print("=" * 60)

    print(f"Jogos cadastrados: {estatisticas['total_jogos']}")
    print(f"Desenvolvedoras: {estatisticas['total_developers']}")
    print(f"Franquias: {estatisticas['total_franquias']}")
    print(f"Gêneros: {estatisticas['total_generos']}")

    print("\nQuantidade por gênero:")
    print(estatisticas["quantidade_por_genero"])

    print("\nQuantidade por desenvolvedora:")
    print(estatisticas["quantidade_por_developer"])

    print("\nQuantidade por década:")
    print(estatisticas["quantidade_por_decada"])