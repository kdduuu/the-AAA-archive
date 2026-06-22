"""
===========================================================
The AAA Archive
Arquivo: test_site_statistics.py

Objetivo:
Testar as funções do módulo site_statistics.py.

Esses testes garantem que as estatísticas usadas futuramente
pela Home, API e Dashboard estão funcionando corretamente.
===========================================================
"""

# ==========================================================
# IMPORTAÇÃO DOS MÓDULOS
# ==========================================================

import pandas as pd

from load_data import carregar_dataset

from site_statistics import (
    contar_total_jogos,
    contar_total_developers,
    contar_total_franquias,
    contar_total_generos,
    listar_quantidade_por_genero,
    listar_quantidade_por_developer,
    listar_quantidade_por_franquia,
    listar_quantidade_por_decada,
    listar_jogos_historicos,
    listar_jogos_influentes,
    gerar_estatisticas_home,
)


# ==========================================================
# CARREGAMENTO DO DATASET
# ==========================================================

df = carregar_dataset()


# ==========================================================
# TESTES DAS ESTATÍSTICAS GERAIS
# ==========================================================

def testar_total_jogos():
    """
    Verifica se o total de jogos retornado pela função
    é igual ao número real de linhas do DataFrame.
    """

    resultado = contar_total_jogos(df)

    assert resultado == len(df)


def testar_total_developers():
    """
    Verifica se o total de desenvolvedoras únicas está correto.
    """

    resultado = contar_total_developers(df)

    assert resultado == df["developer"].nunique()


def testar_total_franquias():
    """
    Verifica se o total de franquias únicas está correto.
    """

    resultado = contar_total_franquias(df)

    assert resultado == df["franchise"].nunique()


def testar_total_generos():
    """
    Verifica se o total de gêneros únicos está correto.
    """

    resultado = contar_total_generos(df)

    assert resultado == df["genero"].nunique()


# ==========================================================
# TESTES DAS CONTAGENS AGRUPADAS
# ==========================================================

def testar_quantidade_por_genero():
    """
    Verifica se a função retorna um DataFrame
    com as colunas esperadas e se a soma dos totais
    bate com o total de jogos.
    """

    resultado = listar_quantidade_por_genero(df)

    assert isinstance(resultado, pd.DataFrame)
    assert list(resultado.columns) == ["genero", "total"]
    assert resultado["total"].sum() == len(df)


def testar_quantidade_por_developer():
    """
    Verifica se a contagem por desenvolvedora está correta.
    """

    resultado = listar_quantidade_por_developer(df)

    assert isinstance(resultado, pd.DataFrame)
    assert list(resultado.columns) == ["developer", "total"]
    assert resultado["total"].sum() == len(df)


def testar_quantidade_por_franquia():
    """
    Verifica se a contagem por franquia está correta.
    """

    resultado = listar_quantidade_por_franquia(df)

    assert isinstance(resultado, pd.DataFrame)
    assert list(resultado.columns) == ["franchise", "total"]
    assert resultado["total"].sum() == len(df)


def testar_quantidade_por_decada():
    """
    Verifica se a contagem por década está correta.

    Cada jogo pertence a uma década.
    Portanto, a soma da coluna total deve bater
    com o total geral de jogos.
    """

    resultado = listar_quantidade_por_decada(df)

    assert isinstance(resultado, pd.DataFrame)
    assert list(resultado.columns) == ["decada", "total"]
    assert resultado["total"].sum() == len(df)


# ==========================================================
# TESTES DOS JOGOS HISTÓRICOS E INFLUENTES
# ==========================================================

def testar_jogos_historicos():
    """
    Verifica se a função de jogos históricos
    retorna um DataFrame.

    Mesmo que ainda existam campos vazios no dataset,
    a função precisa funcionar sem erro.
    """

    resultado = listar_jogos_historicos(df)

    assert isinstance(resultado, pd.DataFrame)


def testar_jogos_influentes():
    """
    Verifica se a função de jogos influentes
    retorna um DataFrame.
    """

    resultado = listar_jogos_influentes(df)

    assert isinstance(resultado, pd.DataFrame)


# ==========================================================
# TESTE DO RESUMO GERAL DA HOME
# ==========================================================

def testar_estatisticas_home():
    """
    Verifica se a função gerar_estatisticas_home()
    retorna um dicionário com todas as chaves esperadas.

    Essa função será importante no futuro porque poderá
    alimentar a Home, a API e o Dashboard.
    """

    resultado = gerar_estatisticas_home(df)

    chaves_esperadas = [
        "total_jogos",
        "total_developers",
        "total_franquias",
        "total_generos",
        "quantidade_por_genero",
        "quantidade_por_developer",
        "quantidade_por_franquia",
        "quantidade_por_decada",
        "jogos_historicos",
        "jogos_influentes",
    ]

    assert isinstance(resultado, dict)

    for chave in chaves_esperadas:
        assert chave in resultado


# ==========================================================
# EXECUÇÃO DOS TESTES
# ==========================================================

if __name__ == "__main__":
    """
    Executa todos os testes manualmente.

    Se nenhum erro aparecer no terminal,
    significa que todos os testes passaram.
    """

    testar_total_jogos()
    testar_total_developers()
    testar_total_franquias()
    testar_total_generos()

    testar_quantidade_por_genero()
    testar_quantidade_por_developer()
    testar_quantidade_por_franquia()
    testar_quantidade_por_decada()

    testar_jogos_historicos()
    testar_jogos_influentes()

    testar_estatisticas_home()

    print("=" * 60)
    print("TODOS OS TESTES DE site_statistics.py PASSARAM!")
    print("=" * 60)