"""
===========================================================
The AAA Archive
Arquivo: filters.py

Objetivo:
Centralizar todos os filtros utilizados pelo Archive.

Este módulo será utilizado futuramente pela página Archive,
pela API e por outras partes do sistema que precisem consultar
subconjuntos da Foundation Collection.

Todas as funções recebem um DataFrame e retornam um novo
DataFrame filtrado, sem modificar os dados originais.

Autor: Kadu Almeida
===========================================================
"""


# ==========================================================
# FUNÇÃO AUXILIAR
# ==========================================================

def _filtrar_por_valor_exato(df, coluna, valor):
    """
    Filtra o DataFrame usando uma coluna e um valor exato.

    Esta função é interna do módulo. Por isso, o nome começa
    com underline (_). Ela existe para evitar repetição de código
    entre os filtros públicos.

    Exemplo:
        coluna = "developer"
        valor = "Capcom"

    Args:
        df: DataFrame contendo os jogos.
        coluna: nome da coluna que será filtrada.
        valor: valor que será procurado na coluna.

    Returns:
        DataFrame: jogos que correspondem ao filtro informado.
    """

    filtro = df[coluna] == valor

    # copy() evita que alterações futuras no resultado afetem
    # acidentalmente o DataFrame original.
    return df[filtro].copy()


# ==========================================================
# FILTROS POR DESENVOLVEDORA
# ==========================================================

def listar_jogos_por_developer(df, developer):
    """
    Retorna todos os jogos da desenvolvedora informada.

    Uso futuro no sistema:
        Archive -> filtro por desenvolvedora.
        API     -> endpoint de jogos por desenvolvedora.

    Args:
        df: DataFrame contendo os jogos.
        developer: nome da desenvolvedora.

    Returns:
        DataFrame: jogos da desenvolvedora informada.
    """

    return _filtrar_por_valor_exato(df, "developer", developer)


# ==========================================================
# FILTROS POR GÊNERO
# ==========================================================

def listar_jogos_por_genero(df, genero):
    """
    Retorna todos os jogos do gênero informado.

    Uso futuro no sistema:
        Archive -> filtro por gênero.
        API     -> endpoint de jogos por gênero.

    Args:
        df: DataFrame contendo os jogos.
        genero: nome do gênero.

    Returns:
        DataFrame: jogos do gênero informado.
    """

    return _filtrar_por_valor_exato(df, "genero", genero)


# ==========================================================
# FILTROS POR FRANQUIA
# ==========================================================

def listar_jogos_por_franquia(df, franquia):
    """
    Retorna todos os jogos da franquia informada.

    Uso futuro no sistema:
        Archive -> filtro por franquia.
        API     -> endpoint de jogos por franquia.

    Args:
        df: DataFrame contendo os jogos.
        franquia: nome da franquia.

    Returns:
        DataFrame: jogos da franquia informada.
    """

    return _filtrar_por_valor_exato(df, "franchise", franquia)


# ==========================================================
# FILTROS POR ANO
# ==========================================================

def listar_jogos_por_ano(df, ano):
    """
    Retorna todos os jogos lançados no ano informado.

    Uso futuro no sistema:
        Archive -> filtro por ano de lançamento.
        API     -> endpoint de jogos por ano.

    Args:
        df: DataFrame contendo os jogos.
        ano: ano de lançamento.

    Returns:
        DataFrame: jogos lançados no ano informado.
    """

    return _filtrar_por_valor_exato(df, "ano_lancamento", ano)


# ==========================================================
# FILTROS POR DÉCADA
# ==========================================================

def listar_jogos_por_decada(df, decada):
    """
    Retorna todos os jogos pertencentes à década informada.

    Exemplo:
        1990 -> jogos de 1990 até 1999
        2000 -> jogos de 2000 até 2009
        2010 -> jogos de 2010 até 2019

    Uso futuro no sistema:
        Archive   -> filtro por década.
        Dashboard -> gráficos históricos por década.
        API       -> endpoint de jogos por década.

    Args:
        df: DataFrame contendo os jogos.
        decada: década desejada.

    Returns:
        DataFrame: jogos pertencentes à década informada.
    """

    inicio_decada = decada
    fim_decada = decada + 9

    filtro = (
        (df["ano_lancamento"] >= inicio_decada) &
        (df["ano_lancamento"] <= fim_decada)
    )

    return df[filtro].copy()


# ==========================================================
# ÁREA DE TESTE MANUAL
# ==========================================================

if __name__ == "__main__":
    """
    Esta parte só será executada quando rodarmos este arquivo diretamente.

    Exemplo:
        python scripts/filters.py

    Quando outro arquivo importar este módulo, nada será executado
    automaticamente. Isso torna o código reutilizável.
    """

    from load_data import carregar_dataset

    df = carregar_dataset()

    print("=" * 60)
    print("THE AAA ARCHIVE")
    print("FILTERS")
    print("=" * 60)

    print("\nJogos da Nintendo:")
    print(listar_jogos_por_developer(df, "Nintendo")[["id", "nome", "developer"]])

    print("\nJogos de Action-Adventure:")
    print(listar_jogos_por_genero(df, "Action-Adventure")[["id", "nome", "genero"]])

    print("\nJogos da franquia Resident Evil:")
    print(listar_jogos_por_franquia(df, "Resident Evil")[["id", "nome", "franchise"]])

    print("\nJogos lançados em 2018:")
    print(listar_jogos_por_ano(df, 2018)[["id", "nome", "ano_lancamento"]])

    print("\nJogos da década de 1990:")
    print(listar_jogos_por_decada(df, 1990)[["id", "nome", "ano_lancamento"]])