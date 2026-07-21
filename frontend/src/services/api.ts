/*
===========================================================
The AAA Archive
Arquivo: api.ts

Objetivo:
Centralizar as requisições realizadas pelo front-end para
a FastAPI do The AAA Archive.

Nesta etapa, o serviço consegue:
- carregar a Foundation Collection completa;
- pesquisar jogos;
- filtrar jogos por década;
- filtrar jogos por ano;
- filtrar jogos por gênero;
- filtrar jogos por desenvolvedora;
- filtrar jogos por franquia;
- carregar um único jogo pelo ID;
- carregar todos os registros da Awards History;
- carregar vencedor e indicados de um ano específico;
- carregar vencedores presentes na Foundation Collection.

Arquitetura:

React
↓
services/api.ts
↓
Fetch API
↓
FastAPI
↓
PostgreSQL

O React nunca acessa diretamente:
- arquivos CSV;
- PostgreSQL;
- módulos Python.
===========================================================
*/

import type { Award } from '../types/Award'
import type { Game } from '../types/Game'


// ==========================================================
// ENDEREÇO PRINCIPAL DA API
// ==========================================================

/*
Durante o desenvolvimento local:

React:
http://localhost:5173

FastAPI:
http://127.0.0.1:8000
*/

const API_BASE_URL = 'http://127.0.0.1:8000'


// ==========================================================
// VALIDAÇÃO DAS RESPOSTAS
// ==========================================================

/*
Esta função verifica se a resposta HTTP foi concluída
corretamente.

Exemplos considerados corretos:

200
201

Exemplos considerados erros:

400
404
500

O endpoint de jogo individual trata o status 404 antes de
utilizar esta função, pois um registro inexistente será
representado por null no React.
*/

function validateResponse(response: Response) {
  if (!response.ok) {
    throw new Error(
      `API request failed with status ${response.status}.`,
    )
  }
}


// ==========================================================
// REQUISIÇÕES QUE RETORNAM LISTAS DE JOGOS
// ==========================================================

/*
Os endpoints da Foundation retornam listas de jogos.

Exemplos:

GET /games
→ Game[]

GET /games/developer/Capcom
→ Game[]

GET /games/search?term=zelda
→ Game[]

Esta função evita repetir fetch, validação e conversão para
JSON em todas as funções de lista.
*/

async function requestGames(
  endpoint: string,
): Promise<Game[]> {
  const response = await fetch(
    `${API_BASE_URL}${endpoint}`,
  )

  validateResponse(response)

  const games: Game[] = await response.json()

  return games
}


// ==========================================================
// REQUISIÇÕES QUE RETORNAM REGISTROS DE AWARDS
// ==========================================================

/*
Os endpoints da Awards History retornam listas de registros.

Exemplo:

GET /awards
→ Award[]

Esta função mantém o mesmo fluxo utilizado pelos jogos:
fetch, validação, conversão para JSON e retorno tipado.
*/

async function requestAwards(
  endpoint: string,
): Promise<Award[]> {
  const response = await fetch(
    `${API_BASE_URL}${endpoint}`,
  )

  validateResponse(response)

  const awards: Award[] = await response.json()

  return awards
}


// ==========================================================
// COLEÇÃO COMPLETA
// ==========================================================

/**
 * Carrega todos os jogos da Foundation Collection.
 *
 * Endpoint:
 * GET /games
 */

export async function getGames(): Promise<Game[]> {
  return requestGames('/games')
}


// ==========================================================
// JOGO INDIVIDUAL
// ==========================================================

/**
 * Carrega um único jogo utilizando seu ID.
 *
 * Endpoint:
 * GET /games/{id}
 *
 * Retornos:
 *
 * jogo encontrado
 * → Game
 *
 * jogo inexistente
 * → null
 *
 * falha de comunicação
 * → lança um erro
 */

export async function getGameById(
  id: number,
): Promise<Game | null> {
  const response = await fetch(
    `${API_BASE_URL}/games/${id}`,
  )

  /*
  O status 404 não significa que toda a API falhou.

  Ele significa apenas que o registro solicitado não existe.

  Por isso retornamos null, permitindo que a futura GamePage
  apresente um estado específico:

  RECORD NOT FOUND
  */

  if (response.status === 404) {
    return null
  }

  validateResponse(response)

  const game: Game = await response.json()

  return game
}


// ==========================================================
// PESQUISA
// ==========================================================

/**
 * Pesquisa jogos utilizando um termo textual.
 *
 * O encodeURIComponent protege valores que possuem:
 * - espaços;
 * - acentos;
 * - caracteres especiais.
 *
 * Exemplo:
 *
 * Resident Evil
 * ↓
 * Resident%20Evil
 */

export async function searchGames(
  term: string,
): Promise<Game[]> {
  const encodedTerm = encodeURIComponent(term)

  return requestGames(
    `/games/search?term=${encodedTerm}`,
  )
}


// ==========================================================
// FILTRO POR DÉCADA
// ==========================================================

/**
 * Carrega jogos pertencentes a uma década.
 *
 * Exemplo:
 *
 * 2000
 * ↓
 * jogos lançados entre 2000 e 2009
 */

export async function getGamesByDecade(
  decade: number,
): Promise<Game[]> {
  return requestGames(
    `/games/decade/${decade}`,
  )
}


// ==========================================================
// FILTRO POR ANO
// ==========================================================

/**
 * Carrega jogos lançados em um ano específico.
 */

export async function getGamesByYear(
  year: number,
): Promise<Game[]> {
  return requestGames(
    `/games/year/${year}`,
  )
}


// ==========================================================
// FILTRO POR GÊNERO
// ==========================================================

/**
 * Carrega jogos pertencentes a um gênero.
 *
 * Exemplo:
 *
 * Survival Horror
 * ↓
 * Survival%20Horror
 */

export async function getGamesByGenre(
  genre: string,
): Promise<Game[]> {
  const encodedGenre =
    encodeURIComponent(genre)

  return requestGames(
    `/games/genre/${encodedGenre}`,
  )
}


// ==========================================================
// FILTRO POR DESENVOLVEDORA
// ==========================================================

/**
 * Carrega jogos pertencentes a uma desenvolvedora.
 */

export async function getGamesByDeveloper(
  developer: string,
): Promise<Game[]> {
  const encodedDeveloper =
    encodeURIComponent(developer)

  return requestGames(
    `/games/developer/${encodedDeveloper}`,
  )
}


// ==========================================================
// FILTRO POR FRANQUIA
// ==========================================================

/**
 * Carrega jogos pertencentes a uma franquia.
 */

export async function getGamesByFranchise(
  franchise: string,
): Promise<Game[]> {
  const encodedFranchise =
    encodeURIComponent(franchise)

  return requestGames(
    `/games/franchise/${encodedFranchise}`,
  )
}

// ==========================================================
// AWARDS HISTORY COMPLETA
// ==========================================================

/**
 * Carrega todos os registros da Awards History.
 *
 * Endpoint:
 * GET /awards
 */

export async function getAwards(): Promise<Award[]> {
  return requestAwards('/awards')
}

// ==========================================================
// AWARDS HISTORY POR ANO
// ==========================================================

/**
 * Carrega o vencedor e os indicados de um ano específico.
 *
 * Endpoint:
 * GET /awards/{year}
 */

export async function getAwardsByYear(
  year: number,
): Promise<Award[]> {
  return requestAwards(`/awards/${year}`)
}

// ==========================================================
// VENCEDORES PRESENTES NA FOUNDATION
// ==========================================================

/**
 * Carrega os vencedores de Game of the Year que também estão
 * presentes na Foundation Collection.
 *
 * Endpoint:
 * GET /awards/foundation/winners
 */

export async function getFoundationAwardWinners(
): Promise<Award[]> {
  return requestAwards(
    '/awards/foundation/winners',
  )
}