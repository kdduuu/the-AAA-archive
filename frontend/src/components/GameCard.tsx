/*
===========================================================
The AAA Archive
Arquivo: GameCard.tsx

Objetivo:
Representar visualmente um jogo dentro da Foundation
Collection e permitir o acesso ao registro individual.

O componente recebe um objeto do tipo Game por meio de props.

Nesta versão, o card apresenta:
- representação visual temporária;
- ID do registro;
- ano de lançamento;
- nome do jogo;
- desenvolvedora;
- navegação para /games/{game.id}.

Ainda não são implementados:
- imagem definitiva;
- plataforma;
- estados de seleção;
- favoritos ou outras ações.
===========================================================
*/

import { Link } from 'react-router'

import type { Game } from '../types/Game'

import './GameCard.css'


// ==========================================================
// PROPRIEDADES DO COMPONENTE
// ==========================================================

/*
GameCardProps define quais informações o componente espera
receber.

Neste caso, ele recebe um único objeto chamado game, que deve
seguir o tipo Game criado anteriormente.
*/

type GameCardProps = {
  game: Game
}


// ==========================================================
// COMPONENTE PRINCIPAL
// ==========================================================

function GameCard({
  game,
}: GameCardProps) {
  /*
  Alguns campos podem chegar como null pela API.

  Por isso, criamos textos alternativos para evitar que a
  interface mostre valores vazios ao visitante.
  */

  const releaseYear =
    game.ano_lancamento ?? 'YEAR UNKNOWN'

  const developer =
    game.developer ?? 'DEVELOPER UNKNOWN'

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
      <div className="game-card__visual">
        <span className="game-card__record-id">
          REC-{recordId}
        </span>

        <span className="game-card__year">
          [{releaseYear}]
        </span>

        <div
          className="game-card__placeholder"
          aria-hidden="true"
        >
          <span>IMAGE NOT ARCHIVED</span>

          <small>
            FOUNDATION RECORD
          </small>
        </div>
      </div>

      <div className="game-card__content">
        <h2>{game.nome}</h2>

        <p>{developer}</p>
      </div>
    </Link>
  )
}

export default GameCard