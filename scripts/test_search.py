"""
===========================================================
The AAA Archive
Arquivo: test_search.py

Objetivo:
Testar as funções do módulo search.py.

Esses testes garantem que a pesquisa textual usada futuramente
pelo Archive, API e Dashboard está funcionando corretamente.
===========================================================
"""

# ==========================================================
# IMPORTAÇÃO DOS MÓDULOS
# ==========================================================

import pandas as pd

from load_data import carregar_dataset

from search import (
    pesquisar_jogos,
    pesquisar_jogos_por_nome,
)


# ==========================================================
# CARREGAMENTO DO DATASET
# ==========================================================

df = carregar_dataset()


# ==========================================================
# TESTE - PESQUISA POR NOME / FRANQUIA
# ==========================================================

def testar_pesquisa_zelda():
    """
    Verifica se a pesquisa geral encontra jogos relacionados
    ao termo 'zelda'.
    """

    resultado = pesquisar_jogos(df, "zelda")

    assert isinstance(resultado, pd.DataFrame)
    assert not resultado.empty
    assert "The Legend of Zelda: Ocarina of Time" in resultado["nome"].values
    assert "The Legend of Zelda: Breath of the Wild" in resultado["nome"].values


# ==========================================================
# TESTE - PESQUISA POR DESENVOLVEDORA
# ==========================================================

def testar_pesquisa_capcom():
    """
    Verifica se a pesquisa geral encontra jogos relacionados
    à desenvolvedora Capcom.
    """

    resultado = pesquisar_jogos(df, "capcom")

    assert isinstance(resultado, pd.DataFrame)
    assert not resultado.empty
    assert "Resident Evil 2" in resultado["nome"].values
    assert "Resident Evil 4" in resultado["nome"].values


# ==========================================================
# TESTE - PESQUISA POR GÊNERO
# ==========================================================

def testar_pesquisa_horror():
    """
    Verifica se a pesquisa geral encontra jogos relacionados
    ao gênero Survival Horror.
    """

    resultado = pesquisar_jogos(df, "horror")

    assert isinstance(resultado, pd.DataFrame)
    assert not resultado.empty
    assert (resultado["genero"].str.contains("Horror", case=False)).any()
    assert "Silent Hill" in resultado["nome"].values
    assert "Dead Space" in resultado["nome"].values


# ==========================================================
# TESTE - PESQUISA POR NOME
# ==========================================================

def testar_pesquisa_por_nome_god_of_war():
    """
    Verifica se a pesquisa específica por nome encontra
    os jogos chamados God of War.
    """

    resultado = pesquisar_jogos_por_nome(df, "god of war")

    assert isinstance(resultado, pd.DataFrame)
    assert not resultado.empty
    assert (resultado["nome"].str.lower() == "god of war").all()
    assert len(resultado) == 2


# ==========================================================
# TESTE - PESQUISA COM LETRAS MAIÚSCULAS
# ==========================================================

def testar_pesquisa_com_maiusculas():
    """
    Verifica se a pesquisa funciona independentemente
    de letras maiúsculas ou minúsculas.
    """

    resultado = pesquisar_jogos(df, "ZELDA")

    assert isinstance(resultado, pd.DataFrame)
    assert not resultado.empty
    assert "The Legend of Zelda: Ocarina of Time" in resultado["nome"].values


# ==========================================================
# TESTE - PESQUISA COM ESPAÇOS EXTRAS
# ==========================================================

def testar_pesquisa_com_espacos_extras():
    """
    Verifica se a pesquisa ignora espaços extras
    no começo e no fim do termo digitado.
    """

    resultado = pesquisar_jogos(df, "   capcom   ")

    assert isinstance(resultado, pd.DataFrame)
    assert not resultado.empty
    assert "Resident Evil 2" in resultado["nome"].values


# ==========================================================
# TESTE - PESQUISA VAZIA
# ==========================================================

def testar_pesquisa_vazia():
    """
    Verifica se uma pesquisa vazia retorna todos os jogos.

    Isso é importante para o Archive, porque quando o usuário
    não digitar nada na barra de pesquisa, a página deve continuar
    mostrando a coleção completa.
    """

    resultado = pesquisar_jogos(df, "")

    assert isinstance(resultado, pd.DataFrame)
    assert len(resultado) == len(df)


# ==========================================================
# TESTE - PESQUISA SEM RESULTADO
# ==========================================================

def testar_pesquisa_sem_resultado():
    """
    Verifica se uma pesquisa sem correspondência retorna
    um DataFrame vazio, sem gerar erro.
    """

    resultado = pesquisar_jogos(df, "jogo inexistente qualquer")

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

    testar_pesquisa_zelda()
    testar_pesquisa_capcom()
    testar_pesquisa_horror()
    testar_pesquisa_por_nome_god_of_war()

    testar_pesquisa_com_maiusculas()
    testar_pesquisa_com_espacos_extras()

    testar_pesquisa_vazia()
    testar_pesquisa_sem_resultado()

    print("=" * 60)
    print("TODOS OS TESTES DE search.py PASSARAM!")
    print("=" * 60)