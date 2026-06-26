"""
===========================================================
The AAA Archive
Arquivo: test_awards.py

Objetivo:
Testar as funções do módulo awards.py.

Esses testes garantem que o histórico de premiações usado
futuramente pela seção Awards, API e Dashboard está funcionando
corretamente.
===========================================================
"""

# ==========================================================
# IMPORTAÇÃO DOS MÓDULOS
# ==========================================================

import pandas as pd

from load_data import carregar_awards, carregar_dataset

from awards import (
    listar_premiacoes,
    listar_anos_disponiveis,
    listar_jogos_por_ano,
    buscar_vencedor_por_ano,
    listar_indicados_por_ano,
    listar_vencedores,
    listar_jogos_por_premiacao,
    listar_vencedores_na_foundation,
    listar_indicados_na_foundation,
    listar_jogos_awards_fora_da_foundation,
)


# ==========================================================
# CARREGAMENTO DOS DATASETS
# ==========================================================

df_awards = carregar_awards()
df_games = carregar_dataset()


# ==========================================================
# TESTE - PREMIAÇÕES CADASTRADAS
# ==========================================================

def testar_premiacoes():
    """
    Verifica se as três premiações principais estão cadastradas.
    """

    resultado = listar_premiacoes(df_awards)

    assert isinstance(resultado, list)

    assert "Spike Video Game Awards" in resultado
    assert "VGX" in resultado
    assert "The Game Awards" in resultado


# ==========================================================
# TESTE - ANOS DISPONÍVEIS
# ==========================================================

def testar_anos_disponiveis():
    """
    Verifica se os anos da base vão de 2003 até 2025.
    """

    resultado = listar_anos_disponiveis(df_awards)

    assert isinstance(resultado, list)

    assert 2003 in resultado
    assert 2013 in resultado
    assert 2014 in resultado
    assert 2025 in resultado

    assert min(resultado) == 2003
    assert max(resultado) == 2025


# ==========================================================
# TESTE - EDIÇÃO COMPLETA POR ANO
# ==========================================================

def testar_jogos_por_ano():
    """
    Verifica se a edição de 2018 retorna o vencedor
    e os indicados daquele ano.
    """

    resultado = listar_jogos_por_ano(df_awards, 2018)

    assert isinstance(resultado, pd.DataFrame)
    assert not resultado.empty

    assert "God of War" in resultado["jogo"].values
    assert "Red Dead Redemption 2" in resultado["jogo"].values
    assert "Marvel's Spider-Man" in resultado["jogo"].values

    assert len(resultado) == 6


# ==========================================================
# TESTE - VENCEDOR POR ANO
# ==========================================================

def testar_vencedor_2018():
    """
    Verifica se o vencedor de 2018 é God of War.
    """

    resultado = buscar_vencedor_por_ano(df_awards, 2018)

    assert isinstance(resultado, pd.DataFrame)
    assert not resultado.empty

    assert len(resultado) == 1
    assert resultado.iloc[0]["jogo"] == "God of War"
    assert resultado.iloc[0]["status"] == "Vencedor"


def testar_vencedor_2013():
    """
    Verifica se o vencedor da edição VGX de 2013
    é Grand Theft Auto V.
    """

    resultado = buscar_vencedor_por_ano(df_awards, 2013)

    assert isinstance(resultado, pd.DataFrame)
    assert not resultado.empty

    assert len(resultado) == 1
    assert resultado.iloc[0]["jogo"] == "Grand Theft Auto V"
    assert resultado.iloc[0]["premiacao"] == "VGX"
    assert resultado.iloc[0]["status"] == "Vencedor"


def testar_vencedor_2014():
    """
    Verifica se o vencedor de 2014 é Dragon Age: Inquisition.

    Esse teste é importante porque 2014 marca o início
    do The Game Awards.
    """

    resultado = buscar_vencedor_por_ano(df_awards, 2014)

    assert isinstance(resultado, pd.DataFrame)
    assert not resultado.empty

    assert len(resultado) == 1
    assert resultado.iloc[0]["jogo"] == "Dragon Age: Inquisition"
    assert resultado.iloc[0]["premiacao"] == "The Game Awards"
    assert resultado.iloc[0]["status"] == "Vencedor"


# ==========================================================
# TESTE - INDICADOS POR ANO
# ==========================================================

def testar_indicados_por_ano():
    """
    Verifica se a função retorna apenas indicados,
    sem incluir o vencedor.
    """

    resultado = listar_indicados_por_ano(df_awards, 2018)

    assert isinstance(resultado, pd.DataFrame)
    assert not resultado.empty

    assert "Red Dead Redemption 2" in resultado["jogo"].values
    assert "Marvel's Spider-Man" in resultado["jogo"].values
    assert "God of War" not in resultado["jogo"].values

    assert (resultado["status"] == "Indicado").all()


# ==========================================================
# TESTE - TODOS OS VENCEDORES
# ==========================================================

def testar_listar_vencedores():
    """
    Verifica se a função retorna apenas vencedores
    e se existe exatamente um vencedor por ano.
    """

    resultado = listar_vencedores(df_awards)

    assert isinstance(resultado, pd.DataFrame)
    assert not resultado.empty

    assert (resultado["status"] == "Vencedor").all()

    # Cada ano deve possuir apenas um vencedor.
    assert resultado["ano"].nunique() == len(resultado)

    # Como a base atual vai de 2003 até 2025,
    # esperamos 23 vencedores.
    assert len(resultado) == 23

    assert "Grand Theft Auto V" in resultado["jogo"].values
    assert "Dragon Age: Inquisition" in resultado["jogo"].values
    assert "Clair Obscur: Expedition 33" in resultado["jogo"].values


# ==========================================================
# TESTE - FILTRO POR PREMIAÇÃO
# ==========================================================

def testar_jogos_por_premiacao_vgx():
    """
    Verifica se o filtro por premiação retorna apenas registros da VGX.
    """

    resultado = listar_jogos_por_premiacao(df_awards, "VGX")

    assert isinstance(resultado, pd.DataFrame)
    assert not resultado.empty

    assert (resultado["premiacao"] == "VGX").all()
    assert "Grand Theft Auto V" in resultado["jogo"].values
    assert resultado["ano"].nunique() == 1
    assert resultado.iloc[0]["ano"] == 2013


def testar_jogos_por_premiacao_the_game_awards():
    """
    Verifica se o filtro por The Game Awards retorna registros
    a partir de 2014.
    """

    resultado = listar_jogos_por_premiacao(df_awards, "The Game Awards")

    assert isinstance(resultado, pd.DataFrame)
    assert not resultado.empty

    assert (resultado["premiacao"] == "The Game Awards").all()
    assert resultado["ano"].min() == 2014
    assert resultado["ano"].max() == 2025


def testar_jogos_por_premiacao_spike():
    """
    Verifica se o filtro por Spike Video Game Awards retorna registros
    de 2003 até 2012.
    """

    resultado = listar_jogos_por_premiacao(df_awards, "Spike Video Game Awards")

    assert isinstance(resultado, pd.DataFrame)
    assert not resultado.empty

    assert (resultado["premiacao"] == "Spike Video Game Awards").all()
    assert resultado["ano"].min() == 2003
    assert resultado["ano"].max() == 2012


# ==========================================================
# TESTE - RELAÇÃO COM A FOUNDATION COLLECTION
# ==========================================================

def testar_vencedores_na_foundation():
    """
    Verifica se a função retorna vencedores do Awards
    que também estão na Foundation Collection.
    """

    resultado = listar_vencedores_na_foundation(df_awards, df_games)

    assert isinstance(resultado, pd.DataFrame)
    assert not resultado.empty

    assert "God of War" in resultado["jogo"].values
    assert "Elden Ring" in resultado["jogo"].values
    assert "Baldur's Gate 3" in resultado["jogo"].values

    assert (resultado["status"] == "Vencedor").all()


def testar_indicados_na_foundation():
    """
    Verifica se a função retorna indicados do Awards
    que também estão na Foundation Collection.
    """

    resultado = listar_indicados_na_foundation(df_awards, df_games)

    assert isinstance(resultado, pd.DataFrame)
    assert not resultado.empty

    assert "Red Dead Redemption 2" in resultado["jogo"].values
    assert "Marvel's Spider-Man" in resultado["jogo"].values
    assert "The Last of Us" in resultado["jogo"].values

    assert (resultado["status"] == "Indicado").all()


def testar_jogos_awards_fora_da_foundation():
    """
    Verifica se a função retorna jogos presentes no Awards,
    mas ausentes da Foundation Collection.
    """

    resultado = listar_jogos_awards_fora_da_foundation(df_awards, df_games)

    assert isinstance(resultado, pd.DataFrame)
    assert not resultado.empty

    assert "Madden NFL 2004" in resultado["jogo"].values
    assert "Hades II" in resultado["jogo"].values
    assert "Hollow Knight: Silksong" in resultado["jogo"].values

    assert "God of War" not in resultado["jogo"].values
    assert "Elden Ring" not in resultado["jogo"].values


# ==========================================================
# TESTE - BUSCA SEM RESULTADO
# ==========================================================

def testar_vencedor_ano_inexistente():
    """
    Verifica se buscar um ano inexistente retorna
    um DataFrame vazio, sem gerar erro.
    """

    resultado = buscar_vencedor_por_ano(df_awards, 1999)

    assert isinstance(resultado, pd.DataFrame)
    assert resultado.empty


# ==========================================================
# EXECUÇÃO DOS TESTES
# ==========================================================

if __name__ == "__main__":
    """
    Executa todos os testes manualmente.

    Se nenhum erro aparecer no terminal,
    significa que todos os testes passaram.
    """

    testar_premiacoes()
    testar_anos_disponiveis()

    testar_jogos_por_ano()

    testar_vencedor_2018()
    testar_vencedor_2013()
    testar_vencedor_2014()

    testar_indicados_por_ano()

    testar_listar_vencedores()

    testar_jogos_por_premiacao_vgx()
    testar_jogos_por_premiacao_the_game_awards()
    testar_jogos_por_premiacao_spike()

    testar_vencedores_na_foundation()
    testar_indicados_na_foundation()
    testar_jogos_awards_fora_da_foundation()

    testar_vencedor_ano_inexistente()

    print("=" * 60)
    print("TODOS OS TESTES DE awards.py PASSARAM!")
    print("=" * 60)