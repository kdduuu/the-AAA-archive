/*
===========================================================
The AAA Archive
Arquivo: Game.ts

Objetivo:
Representar no front-end o formato de um jogo retornado
pela FastAPI por meio do endpoint GET /games.

Este tipo foi criado com base na resposta JSON real da API.

Os campos que podem vir vazios do PostgreSQL utilizam:
tipo | null

Exemplo:
string | null
number | null
boolean | null
===========================================================
*/

export type Game = {
  // Identificador único do jogo dentro da Foundation Collection.
  id: number;

  // Nome obrigatório do jogo.
  nome: string;

  // Informações gerais que podem estar vazias no banco.
  ano_lancamento: number | null;
  genero: string | null;
  developer: string | null;
  franchise: string | null;

  // Texto editorial do jogo.
  descricao: string | null;

  // Notas disponíveis no projeto.
  metacritic: number | null;
  nota_kadu: number | null;
  nota_pavam: number | null;

  // Marcações editoriais históricas.
  historico_importante: boolean | null;
  historico_influente: boolean | null;
};