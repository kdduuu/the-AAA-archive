/*
===========================================================
The AAA Archive
Arquivo: Award.ts

Objetivo:
Representar no React o formato de cada registro retornado
pelos endpoints da Awards History.

Contrato atual da FastAPI:
- ano;
- premiacao;
- jogo;
- status.
===========================================================
*/

export type AwardStatus =
  | 'Vencedor'
  | 'Indicado'

export interface Award {
  ano: number
  premiacao: string
  jogo: string
  status: AwardStatus
}