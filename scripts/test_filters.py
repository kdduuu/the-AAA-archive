"""
===========================================================
The AAA Archive
Arquivo: test_filters.py

Objetivo:
Testar as funções do módulo filters.py.

Esses testes garantem que os filtros usados futuramente
pelo Archive, API e Dashboard estão funcionando corretamente.
===========================================================
"""

# ==========================================================
# IMPORTAÇÃO DOS MÓDULOS
# ==========================================================

import pandas as pd

from load_data import carregar_dataset

from filters import (
    listar_jogos_por_developer,
    listar_jogos_por_genero,
    listar_jogos_por_franquia,
    listar_jogos_por_ano,
    listar_jogos_por_decada,
)


# ==========================================================
# CARREGAMENTO DO DATASET
# ==========================================================

df = carregar_dataset()


# ==========================================================
# TESTE - DESENVOLVEDORA
# ==========================================================

def testar_filtro_por_developer():
    """
    Verifica se o filtro por desenvolvedora retorna apenas
    jogos da desenvolvedora informada.
    """

    resultado = listar_jogos_por_developer(df, "Nintendo")

    assert isinstance(resultado, pd.DataFrame)
    assert not resultado.empty
    assert (resultado["developer"] == "Nintendo").all()
    assert "The Legend of Zelda: Ocarina of Time" in resultado["nome"].values
    assert "The Legend of Zelda: Breath of the Wild" in resultado["nome"].values


# ==========================================================
# TESTE - GÊNERO
# ==========================================================

def testar_filtro_por_genero():
    """
    Verifica se o filtro por gênero retorna apenas jogos
    do gênero informado.
    """

    resultado = listar_jogos_por_genero(df, "Action-Adventure")

    assert isinstance(resultado, pd.DataFrame)
    assert not resultado.empty
    assert (resultado["genero"] == "Action-Adventure").all()


# ==========================================================
# TESTE - FRANQUIA
# ==========================================================

def testar_filtro_por_franquia():
    """
    Verifica se o filtro por franquia retorna apenas jogos
    da franquia informada.
    """

    resultado = listar_jogos_por_franquia(df, "Resident Evil")

    assert isinstance(resultado, pd.DataFrame)
    assert not resultado.empty
    assert (resultado["franchise"] == "Resident Evil").all()
    assert "Resident Evil 2" in resultado["nome"].values
    assert "Resident Evil 4" in resultado["nome"].values


# ==========================================================
# TESTE - ANO
# ==========================================================

def testar_filtro_por_ano():
    """
    Verifica se o filtro por ano retorna apenas jogos
    lançados no ano informado.
    """

    resultado = listar_jogos_por_ano(df, 2018)

    assert isinstance(resultado, pd.DataFrame)
    assert not resultado.empty
    assert (resultado["ano_lancamento"] == 2018).all()
    assert "God of War" in resultado["nome"].values
    assert "Marvel's Spider-Man" in resultado["nome"].values
    assert "Red Dead Redemption 2" in resultado["nome"].values


# ==========================================================
# TESTE - DÉCADA
# ==========================================================

def testar_filtro_por_decada():
    """
    Verifica se o filtro por década retorna apenas jogos
    dentro do intervalo esperado.

    Exemplo:
        1990 -> 1990 até 1999
    """

    resultado = listar_jogos_por_decada(df, 1990)

    assert isinstance(resultado, pd.DataFrame)
    assert not resultado.empty
    assert (resultado["ano_lancamento"] >= 1990).all()
    assert (resultado["ano_lancamento"] <= 1999).all()
    assert "Final Fantasy VII" in resultado["nome"].values
    assert "Silent Hill" in resultado["nome"].values


# ==========================================================
# TESTE - FILTRO SEM RESULTADO
# ==========================================================

def testar_filtro_sem_resultado():
    """
    Verifica se um filtro sem correspondência retorna
    um DataFrame vazio, sem gerar erro.
    """

    resultado = listar_jogos_por_developer(df, "Desenvolvedora Inexistente")

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

    testar_filtro_por_developer()
    testar_filtro_por_genero()
    testar_filtro_por_franquia()
    testar_filtro_por_ano()
    testar_filtro_por_decada()
    testar_filtro_sem_resultado()

    print("=" * 60)
    print("TODOS OS TESTES DE filters.py PASSARAM!")
    print("=" * 60)