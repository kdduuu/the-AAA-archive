/*
===========================================================
The AAA Archive
Arquivo: GameCard.tsx

Objetivo:
Representar visualmente um jogo dentro da Foundation
Collection e permitir o acesso ao registro individual.

O componente recebe um objeto do tipo Game por meio de props.

Nesta versão, o card apresenta:
- imagem cover.webp quando ela estiver disponível;
- fallback visual automático quando a imagem não existir;
- identificação do registro;
- ano de lançamento;
- nome do jogo;
- desenvolvedora;
- gênero;
- navegação para /games/{game.id}.

Caminho esperado para cada imagem:
frontend/public/assets/games/{id}/cover.webp
===========================================================
*/

import {
  useState,
} from 'react'
import { Link } from 'react-router'

import type { Game } from '../types/Game'

import './GameCard.css'


// ==========================================================
// PROPRIEDADES DO COMPONENTE
// ==========================================================

type GameCardProps = {
  game: Game
}


type CoverStatus =
  | 'loading'
  | 'loaded'
  | 'error'


// ==========================================================
// COMPONENTE PRINCIPAL
// ==========================================================

function GameCard({
  game,
}: GameCardProps) {
  /*
  Enquanto a imagem está sendo carregada, o placeholder
  continua visível.

  Quando cover.webp é encontrada, a imagem aparece.

  Se o arquivo não existir ou não puder ser carregado, o
  placeholder permanece no card sem exibir imagem quebrada.
  */

  const [coverStatus, setCoverStatus] =
    useState<CoverStatus>('loading')

  /*
  Alguns campos podem chegar como null pela API.

  Os textos alternativos evitam espaços vazios na interface
  enquanto mantêm o estilo técnico do arquivo.
  */

  const releaseYear =
    game.ano_lancamento ?? 'YEAR UNKNOWN'

  const developer =
    game.developer ?? 'DEVELOPER UNKNOWN'

  const genre =
    game.genero ?? 'GENRE UNCLASSIFIED'

  const coverPath =
    `/assets/games/${game.id}/cover.webp`

  const hasCover =
    coverStatus === 'loaded'

  /*
  padStart adiciona zeros antes do ID.

  Exemplo:

  1
  → 001

  24
  → 024
  */

  const recordId =
    String(game.id).padStart(3, '0')


  // ========================================================
  // INTERFACE
  // ========================================================

  return (
    <Link
      to={`/games/${game.id}`}
      className="game-card"
      aria-label={`Abrir registro de ${game.nome}`}
    >
      <div
        className={
          `game-card__visual${
            hasCover
              ? ' game-card__visual--has-cover'
              : ''
          }`
        }
      >
        {coverStatus !== 'error' && (
          <img
            src={coverPath}
            alt=""
            className="game-card__cover"
            loading="lazy"
            decoding="async"
            onLoad={() => setCoverStatus('loaded')}
            onError={() => setCoverStatus('error')}
          />
        )}

        <div className="game-card__visual-header">
          <span>REC-{recordId}</span>

          <span className="game-card__status">
            <span aria-hidden="true" />
            FOUNDATION
          </span>
        </div>

        <div
          className="game-card__placeholder"
          aria-hidden="true"
        >
          <strong>{recordId}</strong>

          <span>VISUAL RECORD PENDING</span>

          <small>
            COVER IMAGE NOT ARCHIVED
          </small>
        </div>

        <span
          className="game-card__visual-year"
          aria-hidden="true"
        >
          {releaseYear}
        </span>
      </div>

      <div className="game-card__content">
        <div className="game-card__metadata">
          <span>[{releaseYear}]</span>
          <span>ARCHIVE ENTRY</span>
        </div>

        <div className="game-card__identity">
          <h2>{game.nome}</h2>
          <p>{developer}</p>
        </div>

        <div className="game-card__footer">
          <span>{genre}</span>

          <span className="game-card__action">
            OPEN RECORD
            <span aria-hidden="true">→</span>
          </span>
        </div>
      </div>
    </Link>
  )
}

export default GameCard