"""
===========================================================
The AAA Archive
Arquivo: awards.py

Objetivo:
Centralizar as consultas relacionadas ao histórico de
premiações de Game of the Year.

Este módulo trabalha com a base independente awards.csv.

Ele será utilizado futuramente pela seção Awards do site,
pela API e pelo Dashboard.

Autor: Kadu Almeida
===========================================================
"""

# ==========================================================
# IMPORTAÇÃO DOS MÓDULOS
# ==========================================================

from load_data import carregar_awards


# ==========================================================
# FUNÇÕES GERAIS
# ==========================================================

def listar_premiacoes(df):
    """
    Retorna todas as premiações presentes na base.

    Exemplo:
        Spike Video Game Awards
        VGX
        The Game Awards

    Args:
        df: DataFrame contendo os dados de premiações.

    Returns:
        list: lista com os nomes das premiações.
    """

    premiacoes = (
        df["premiacao"]
        .dropna()
        .astype(str)
        .str.strip()
        .unique()
    )

    return sorted(premiacoes)


def listar_anos_disponiveis(df):
    """
    Retorna todos os anos disponíveis na base de premiações.

    Args:
        df: DataFrame contendo os dados de premiações.

    Returns:
        list: lista de anos ordenada.
    """

    anos = df["ano"].dropna().unique()

    # Convertemos cada ano para int comum do Python.
    # Isso evita aparecer np.int64(2003) no terminal.
    return [int(ano) for ano in sorted(anos)]


# ==========================================================
# CONSULTAS POR ANO
# ==========================================================

def listar_jogos_por_ano(df, ano):
    """
    Retorna todos os jogos registrados em uma edição específica.

    Isso inclui:
    - o vencedor;
    - os indicados.

    Uso futuro no sistema:
        Awards -> exibir a edição completa de um ano.

    Args:
        df: DataFrame contendo os dados de premiações.
        ano: ano da premiação.

    Returns:
        DataFrame: jogos daquele ano.
    """

    filtro = df["ano"] == ano

    return df[filtro].copy()


def buscar_vencedor_por_ano(df, ano):
    """
    Retorna o vencedor de Game of the Year de um ano específico.

    Args:
        df: DataFrame contendo os dados de premiações.
        ano: ano da premiação.

    Returns:
        DataFrame: vencedor daquele ano.
    """

    filtro = (
        (df["ano"] == ano) &
        (df["status"].astype(str).str.strip() == "Vencedor")
    )

    return df[filtro].copy()


def listar_indicados_por_ano(df, ano):
    """
    Retorna apenas os indicados de um ano específico.

    O vencedor não aparece neste resultado.

    Args:
        df: DataFrame contendo os dados de premiações.
        ano: ano da premiação.

    Returns:
        DataFrame: indicados daquele ano.
    """

    filtro = (
        (df["ano"] == ano) &
        (df["status"].astype(str).str.strip() == "Indicado")
    )

    return df[filtro].copy()


# ==========================================================
# CONSULTAS GERAIS
# ==========================================================

def listar_vencedores(df):
    """
    Retorna todos os vencedores registrados na base.

    Uso futuro no sistema:
        Awards -> linha histórica dos vencedores.

    Args:
        df: DataFrame contendo os dados de premiações.

    Returns:
        DataFrame: todos os vencedores.
    """

    filtro = df["status"].astype(str).str.strip() == "Vencedor"

    return df[filtro].copy()


def listar_jogos_por_premiacao(df, premiacao):
    """
    Retorna todos os registros de uma premiação específica.

    Exemplo:
        Spike Video Game Awards
        VGX
        The Game Awards

    Args:
        df: DataFrame contendo os dados de premiações.
        premiacao: nome da premiação.

    Returns:
        DataFrame: registros da premiação informada.
    """

    filtro = (
        df["premiacao"].astype(str).str.strip() == str(premiacao).strip()
    )

    return df[filtro].copy()


# ==========================================================
# ÁREA DE TESTE MANUAL
# ==========================================================

if __name__ == "__main__":
    """
    Esta parte só será executada quando rodarmos este arquivo diretamente.

    Exemplo:
        python scripts/awards.py

    Quando outro arquivo importar este módulo, nada será impresso
    automaticamente.
    """

    df = carregar_awards()

    print("=" * 60)
    print("THE AAA ARCHIVE")
    print("AWARDS")
    print("=" * 60)

    print("\nPremiações cadastradas:")
    print(listar_premiacoes(df))

    print("\nAnos disponíveis:")
    print(listar_anos_disponiveis(df))

    print("\nEdição de 2018:")
    print(listar_jogos_por_ano(df, 2018))

    print("\nVencedor de 2018:")
    print(buscar_vencedor_por_ano(df, 2018))

    print("\nIndicados de 2018:")
    print(listar_indicados_por_ano(df, 2018))

    print("\nTodos os vencedores:")
    print(listar_vencedores(df)[["ano", "premiacao", "jogo", "status"]])