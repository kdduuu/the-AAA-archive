"""
===========================================================
The AAA Archive
Arquivo: search.py

Objetivo:
Centralizar a pesquisa textual utilizada pelo Archive.

Este módulo será usado futuramente pela página Archive,
pela API e por outras partes do sistema que precisem buscar
jogos por texto.

Diferente dos filtros, a pesquisa não exige valor exato.
Ela permite encontrar jogos por partes do texto.

Exemplos:
    "zelda"   -> encontra jogos da franquia Zelda
    "capcom"  -> encontra jogos desenvolvidos pela Capcom
    "horror"  -> encontra jogos relacionados a Survival Horror

Autor: Kadu Almeida
===========================================================
"""


# ==========================================================
# IMPORTAÇÃO DOS MÓDULOS
# ==========================================================

import pandas as pd


# ==========================================================
# FUNÇÕES AUXILIARES
# ==========================================================

def _normalizar_termo(termo):
    """
    Normaliza o termo pesquisado pelo usuário.

    Isso significa:
    - transformar o valor em texto;
    - remover espaços extras no começo e no fim;
    - transformar tudo em letras minúsculas.

    Assim, buscas como:
        "Zelda"
        "zelda"
        " ZELDA "

    serão tratadas da mesma forma.

    Args:
        termo: texto digitado pelo usuário.

    Returns:
        str: termo normalizado.
    """

    return str(termo).strip().lower()


def _criar_mascara_busca(df, coluna, termo):
    """
    Cria uma máscara booleana para buscar um termo em uma coluna.

    Máscara booleana é uma sequência de True e False usada pelo Pandas
    para decidir quais linhas devem permanecer no resultado.

    Exemplo:
        termo = "zelda"

        Linha com Zelda      -> True
        Linha sem Zelda      -> False

    Args:
        df: DataFrame contendo os jogos.
        coluna: coluna onde a busca será feita.
        termo: termo já normalizado.

    Returns:
        Series booleana indicando as linhas encontradas.
    """

    return (
        df[coluna]
        .fillna("")
        .astype(str)
        .str.lower()
        .str.contains(termo, regex=False)
    )


# ==========================================================
# PESQUISA PRINCIPAL DO ARCHIVE
# ==========================================================

def pesquisar_jogos(df, termo):
    """
    Pesquisa jogos em várias colunas importantes do dataset.

    Esta será a principal função de busca do Archive.

    A busca será feita nas colunas:
    - nome;
    - gênero;
    - desenvolvedora;
    - franquia;
    - descrição.

    Uso futuro no sistema:
        Archive -> barra de pesquisa principal.
        API     -> endpoint de pesquisa textual.

    Args:
        df: DataFrame contendo os jogos.
        termo: texto digitado pelo usuário.

    Returns:
        DataFrame: jogos encontrados pela pesquisa.
    """

    termo_normalizado = _normalizar_termo(termo)

    # Quando o usuário não digitar nada na busca,
    # o Archive deverá continuar exibindo todos os jogos.
    if termo_normalizado == "":
        return df.copy()

    colunas_pesquisaveis = [
        "nome",
        "genero",
        "developer",
        "franchise",
        "descricao",
    ]

    # Começamos com uma máscara totalmente falsa.
    # Depois, cada coluna pesquisada poderá marcar linhas como True.
    mascara_final = pd.Series(False, index=df.index)

    for coluna in colunas_pesquisaveis:
        mascara_coluna = _criar_mascara_busca(df, coluna, termo_normalizado)

        # O operador | funciona como "OU".
        # Se o termo aparecer em qualquer coluna, o jogo entra no resultado.
        mascara_final = mascara_final | mascara_coluna

    return df[mascara_final].copy()


# ==========================================================
# PESQUISA ESPECÍFICA POR NOME
# ==========================================================

def pesquisar_jogos_por_nome(df, termo):
    """
    Pesquisa jogos apenas pelo nome.

    Esta função poderá ser útil futuramente para:
    - localizar rapidamente um jogo específico;
    - ajudar na criação da página individual do jogo;
    - criar sugestões de busca no Archive.

    Args:
        df: DataFrame contendo os jogos.
        termo: nome ou parte do nome do jogo.

    Returns:
        DataFrame: jogos encontrados pelo nome.
    """

    termo_normalizado = _normalizar_termo(termo)

    if termo_normalizado == "":
        return df.copy()

    mascara = _criar_mascara_busca(df, "nome", termo_normalizado)

    return df[mascara].copy()


# ==========================================================
# ÁREA DE TESTE MANUAL
# ==========================================================

if __name__ == "__main__":
    """
    Esta parte só será executada quando rodarmos este arquivo diretamente.

    Exemplo:
        python scripts/search.py

    Quando outro arquivo importar este módulo, nada será executado
    automaticamente. Isso torna o código reutilizável.
    """

    from load_data import carregar_dataset

    df = carregar_dataset()

    print("=" * 60)
    print("THE AAA ARCHIVE")
    print("SEARCH")
    print("=" * 60)

    print("\nPesquisa geral por 'zelda':")
    print(pesquisar_jogos(df, "zelda")[["id", "nome", "franchise"]])

    print("\nPesquisa geral por 'capcom':")
    print(pesquisar_jogos(df, "capcom")[["id", "nome", "developer"]])

    print("\nPesquisa geral por 'horror':")
    print(pesquisar_jogos(df, "horror")[["id", "nome", "genero"]])

    print("\nPesquisa por nome 'god of war':")
    print(pesquisar_jogos_por_nome(df, "god of war")[["id", "nome", "ano_lancamento"]])