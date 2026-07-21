/*
===========================================================
The AAA Archive
Arquivo: sortGames.ts

Objetivo:
Centralizar a ordenação dos jogos exibidos no front-end.

A ordenação acontece somente no React.

Nenhuma requisição adicional é enviada para:
- FastAPI;
- PostgreSQL.

A função sempre cria uma nova lista antes de ordenar,
evitando modificar diretamente o estado original.
===========================================================
*/

import type { Game } from '../types/Game'


// ==========================================================
// OPÇÕES DE ORDENAÇÃO
// ==========================================================

/*
SortOption define todas as formas de ordenação atualmente
permitidas pela interface.

archive-order:
ordem original dos registros, utilizando o ID.

title-asc:
nome do jogo em ordem alfabética.

year-asc:
jogos mais antigos primeiro.

year-desc:
jogos mais recentes primeiro.

metacritic-desc:
maiores notas do Metacritic primeiro.
*/

export type SortOption =
  | 'archive-order'
  | 'title-asc'
  | 'year-asc'
  | 'year-desc'
  | 'metacritic-desc'


// ==========================================================
// VALORES AUXILIARES
// ==========================================================

/*
Alguns jogos podem possuir ano ou Metacritic com valor null.

Esses valores precisam ser tratados para não prejudicar a
ordenação.
*/

const UNKNOWN_YEAR = Number.MAX_SAFE_INTEGER

const UNKNOWN_SCORE = -1


// ==========================================================
// FUNÇÃO PRINCIPAL
// ==========================================================

/**
 * Recebe uma lista de jogos e uma opção de ordenação.
 *
 * Retorna uma nova lista ordenada sem modificar a lista
 * recebida originalmente.
 */

export function sortGames(
  games: Game[],
  sortOption: SortOption,
): Game[] {
  /*
  O operador spread cria uma cópia da lista.

  Sem essa cópia, Array.sort() modificaria diretamente o
  array original armazenado pelo React.
  */

  const sortedGames = [...games]


  // ========================================================
  // ORDEM ORIGINAL DO ARQUIVO
  // ========================================================

  if (sortOption === 'archive-order') {
    return sortedGames.sort(
      (firstGame, secondGame) =>
        firstGame.id - secondGame.id,
    )
  }


  // ========================================================
  // ORDEM ALFABÉTICA
  // ========================================================

  if (sortOption === 'title-asc') {
    return sortedGames.sort(
      (firstGame, secondGame) =>
        firstGame.nome.localeCompare(
          secondGame.nome,
          'en',
          {
            sensitivity: 'base',
          },
        ),
    )
  }


  // ========================================================
  // JOGOS MAIS ANTIGOS PRIMEIRO
  // ========================================================

  if (sortOption === 'year-asc') {
    return sortedGames.sort(
      (firstGame, secondGame) => {
        const firstYear =
          firstGame.ano_lancamento
          ?? UNKNOWN_YEAR

        const secondYear =
          secondGame.ano_lancamento
          ?? UNKNOWN_YEAR

        /*
        Caso os dois jogos tenham o mesmo ano, utilizamos o
        ID para manter uma ordem previsível.
        */

        if (firstYear === secondYear) {
          return firstGame.id - secondGame.id
        }

        return firstYear - secondYear
      },
    )
  }


  // ========================================================
  // JOGOS MAIS RECENTES PRIMEIRO
  // ========================================================

  if (sortOption === 'year-desc') {
    return sortedGames.sort(
      (firstGame, secondGame) => {
        /*
        Para a ordem decrescente, registros sem ano devem
        continuar no final da lista.
        */

        if (
          firstGame.ano_lancamento === null
          && secondGame.ano_lancamento === null
        ) {
          return firstGame.id - secondGame.id
        }

        if (firstGame.ano_lancamento === null) {
          return 1
        }

        if (secondGame.ano_lancamento === null) {
          return -1
        }

        if (
          firstGame.ano_lancamento
          === secondGame.ano_lancamento
        ) {
          return firstGame.id - secondGame.id
        }

        return (
          secondGame.ano_lancamento
          - firstGame.ano_lancamento
        )
      },
    )
  }


  // ========================================================
  // MAIORES NOTAS DO METACRITIC PRIMEIRO
  // ========================================================

  return sortedGames.sort(
    (firstGame, secondGame) => {
      const firstScore =
        firstGame.metacritic
        ?? UNKNOWN_SCORE

      const secondScore =
        secondGame.metacritic
        ?? UNKNOWN_SCORE

      /*
      A subtração é invertida porque desejamos uma ordem
      decrescente:

      95
      92
      88
      ...
      */

      if (firstScore === secondScore) {
        return firstGame.id - secondGame.id
      }

      return secondScore - firstScore
    },
  )
}