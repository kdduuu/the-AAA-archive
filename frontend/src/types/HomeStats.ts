/*
===========================================================
The AAA Archive
Arquivo: HomeStats.ts

Objetivo:
Representar no React o formato retornado pelo endpoint
GET /stats/home.

O tipo mantém o contrato atual da FastAPI e poderá ser
reutilizado futuramente pela Home e pela Data Room.
===========================================================
*/

import type { Game } from './Game'


export interface GenreCount {
  genero: string
  total: number
}

export interface DeveloperCount {
  developer: string
  total: number
}

export interface FranchiseCount {
  franchise: string
  total: number
}

export interface DecadeCount {
  decada: number
  total: number
}

export interface HomeStats {
  total_jogos: number
  total_developers: number
  total_franquias: number
  total_generos: number
  quantidade_por_genero: GenreCount[]
  quantidade_por_developer: DeveloperCount[]
  quantidade_por_franquia: FranchiseCount[]
  quantidade_por_decada: DecadeCount[]
  jogos_historicos: Game[]
  jogos_influentes: Game[]
}