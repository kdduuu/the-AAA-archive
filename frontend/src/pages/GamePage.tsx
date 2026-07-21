/*
===========================================================
The AAA Archive
Arquivo: GamePage.tsx

Objetivo:
Representar a página individual de um jogo preservado na
Foundation Collection.

A página:
- recebe o ID presente na URL;
- valida o formato do ID;
- utiliza getGameById();
- representa loading, success, not found e error;
- apresenta o resumo do registro;
- apresenta a descrição editorial disponível;
- apresenta marcações históricas;
- apresenta os dados arquivados do jogo.

Ainda não são implementados:
- imagens definitivas;
- contexto detalhado da era;
- relação com premiações;
- registros relacionados.
===========================================================
*/

import {
  useEffect,
  useState,
} from 'react'

import {
  Link,
  useParams,
} from 'react-router'

import ArchivePanel from '../components/ArchivePanel'
import ArchiveShell from '../components/ArchiveShell'
import type { ContextSidebarItem } from '../components/ContextSidebar'
import { getGameById } from '../services/api'
import type { Game } from '../types/Game'

import './GamePage.css'


// ==========================================================
// ESTADOS DA REQUISIÇÃO
// ==========================================================

type GameRequestState =
  | 'loading'
  | 'success'
  | 'not-found'
  | 'error'


// ==========================================================
// COMPONENTE PRINCIPAL
// ==========================================================

function GamePage() {
  const { id } = useParams<{
    id: string
  }>()

  const [game, setGame] =
    useState<Game | null>(null)

  const [
    requestState,
    setRequestState,
  ] = useState<GameRequestState>('loading')


  // ========================================================
  // CARREGAMENTO DO JOGO
  // ========================================================

  useEffect(() => {
    let pageIsActive = true

    const gameId = Number(id)

    const gameIdIsValid =
      Number.isInteger(gameId)
      && gameId > 0

    if (!gameIdIsValid) {
      setGame(null)
      setRequestState('not-found')

      return () => {
        pageIsActive = false
      }
    }

    setGame(null)
    setRequestState('loading')

    async function loadGame() {
      try {
        const receivedGame =
          await getGameById(gameId)

        if (!pageIsActive) {
          return
        }

        if (receivedGame === null) {
          setRequestState('not-found')

          return
        }

        setGame(receivedGame)
        setRequestState('success')
      } catch {
        if (pageIsActive) {
          setGame(null)
          setRequestState('error')
        }
      }
    }

    loadGame()

    return () => {
      pageIsActive = false
    }
  }, [id])


  // ========================================================
  // IDENTIFICAÇÃO DO REGISTRO
  // ========================================================

  const numericId = Number(id)

  const recordCode =
    Number.isInteger(numericId)
    && numericId > 0
      ? `REC-${String(numericId).padStart(3, '0')}`
      : 'INVALID RECORD'


  // ========================================================
  // STATUS DO REGISTRO
  // ========================================================

  let recordIntegrity = 'retrieving'

  if (requestState === 'success') {
    recordIntegrity = 'stable'
  }

  if (requestState === 'not-found') {
    recordIntegrity = 'not found'
  }

  if (requestState === 'error') {
    recordIntegrity = 'unavailable'
  }

  let statusCode = 'RETRIEVING'
  let statusTitle = 'RETRIEVING RECORD...'
  let statusDescription =
    'Connecting to the archive node and requesting the selected Foundation record.'

  if (requestState === 'not-found') {
    statusCode = '404'
    statusTitle = 'RECORD NOT FOUND'
    statusDescription =
      'The requested identification does not correspond to a preserved Foundation record.'
  }

  if (requestState === 'error') {
    statusCode = 'NODE OFFLINE'
    statusTitle = 'ARCHIVE NODE UNAVAILABLE'
    statusDescription =
      'The individual record could not be retrieved from the data server.'
  }


  // ========================================================
  // NAVEGAÇÃO CONTEXTUAL
  // ========================================================

  const sidebarItems: ContextSidebarItem[] = [
    {
      label: 'RECORD OVERVIEW',
      target: '#game-record-overview',
    },
  ]

  if (requestState === 'success' && game) {
    if (game.descricao !== null) {
      sidebarItems.push({
        label: 'EDITORIAL DESCRIPTION',
        target: '#game-editorial-description',
      })
    }

    if (
      game.historico_importante === true
      || game.historico_influente === true
    ) {
      sidebarItems.push({
        label: 'HISTORICAL NOTES',
        target: '#game-historical-notes',
      })
    }

    sidebarItems.push({
      label: 'ARCHIVE DATA',
      target: '#game-archive-data',
    })
  } else {
    sidebarItems.push({
      label: 'ARCHIVE STATUS',
      target: '#game-archive-status',
    })
  }

  const activeSidebarItem =
    requestState === 'success'
      ? 'RECORD OVERVIEW'
      : 'ARCHIVE STATUS'


  // ========================================================
  // INTERFACE
  // ========================================================

  return (
    <ArchiveShell
      sidebarTitle="FOUNDATION RECORD"
      sidebarItems={sidebarItems}
      activeSidebarItem={activeSidebarItem}
    >
      <section
        id="game-record-overview"
        className="archive-panel game-page__hero"
      >
        <div className="game-page__hero-content">
          <Link
            to="/foundation"
            className="game-page__back-link"
          >
            ← RETURN TO FOUNDATION
          </Link>

          <p className="archive-eyebrow">
            // FOUNDATION / INDIVIDUAL RECORD
          </p>

          <span className="game-page__record-code">
            {recordCode}
          </span>

          {requestState === 'success' && game ? (
            <>
              <h1>{game.nome}</h1>

              <div className="game-page__summary">
                {game.ano_lancamento !== null && (
                  <span>
                    YEAR
                    <strong>
                      {game.ano_lancamento}
                    </strong>
                  </span>
                )}

                {game.developer !== null && (
                  <span>
                    DEVELOPER
                    <strong>
                      {game.developer}
                    </strong>
                  </span>
                )}

                {game.genero !== null && (
                  <span>
                    GENRE
                    <strong>
                      {game.genero}
                    </strong>
                  </span>
                )}

                {game.franchise !== null && (
                  <span>
                    FRANCHISE
                    <strong>
                      {game.franchise}
                    </strong>
                  </span>
                )}
              </div>
            </>
          ) : (
            <>
              <h1>ARCHIVE RECORD</h1>

              <p className="game-page__placeholder-description">
                Individual Foundation record awaiting
                archive synchronization.
              </p>
            </>
          )}

          <p
            className={
              requestState === 'error'
              || requestState === 'not-found'
                ? 'archive-system-message game-page__integrity game-page__integrity--warning'
                : 'archive-system-message game-page__integrity'
            }
          >
            &gt; record integrity:

            <span>{recordIntegrity}</span>
          </p>
        </div>

        <div
          className="game-page__hero-visual"
          aria-label="Área temporária reservada para a imagem do jogo"
        >
          <div
            className="game-page__hero-grid"
            aria-hidden="true"
          />

          <div className="game-page__hero-placeholder">
            <span>FOUNDATION IMAGE FEED</span>

            <strong>
              {requestState === 'success'
                ? recordCode
                : 'AWAITING RECORD'}
            </strong>

            <small>
              individual image awaiting local asset
            </small>
          </div>
        </div>
      </section>

      {requestState !== 'success' && (
        <ArchivePanel
          id="game-archive-status"
          title="RECORD STATUS"
          code={statusCode}
          className="game-page__status-panel"
        >
          <div
            className={
              `game-page__status `
              + `game-page__status--${requestState}`
            }
            aria-live="polite"
          >
            <span className="game-page__status-label">
              ARCHIVE RESPONSE
            </span>

            <strong>{statusTitle}</strong>

            <p>{statusDescription}</p>

            {(
              requestState === 'not-found'
              || requestState === 'error'
            ) && (
              <Link
                to="/foundation"
                className="game-page__return-link"
              >
                RETURN TO FOUNDATION
              </Link>
            )}
          </div>
        </ArchivePanel>
      )}

      {requestState === 'success' && game && (
        <div className="game-page__content-grid">
          {game.descricao !== null && (
            <ArchivePanel
              id="game-editorial-description"
              title="EDITORIAL DESCRIPTION"
              code="ARCHIVED TEXT"
              className="game-page__editorial-panel"
            >
              <div className="game-page__editorial-content">
                <span className="game-page__section-label">
                  PRESERVED DESCRIPTION
                </span>

                <p>{game.descricao}</p>
              </div>
            </ArchivePanel>
          )}

          {(
            game.historico_importante === true
            || game.historico_influente === true
          ) && (
            <ArchivePanel
              id="game-historical-notes"
              title="HISTORICAL NOTES"
              code="FOUNDATION FLAGS"
              className="game-page__historical-panel"
            >
              <div className="game-page__historical-content">
                <span className="game-page__section-label">
                  CURATORIAL CLASSIFICATION
                </span>

                <div className="game-page__historical-flags">
                  {game.historico_importante === true && (
                    <div className="game-page__historical-flag">
                      <span>HISTORICAL IMPORTANCE</span>
                      <strong>CONFIRMED</strong>
                    </div>
                  )}

                  {game.historico_influente === true && (
                    <div className="game-page__historical-flag">
                      <span>INFLUENCE &amp; LEGACY</span>
                      <strong>CONFIRMED</strong>
                    </div>
                  )}
                </div>
              </div>
            </ArchivePanel>
          )}

          <ArchivePanel
            id="game-archive-data"
            title="ARCHIVE DATA"
            code={recordCode}
            className="game-page__data-panel"
          >
            <dl className="game-page__metadata">
              <div>
                <dt>RECORD ID</dt>
                <dd>{recordCode}</dd>
              </div>

              {game.ano_lancamento !== null && (
                <div>
                  <dt>RELEASE YEAR</dt>
                  <dd>{game.ano_lancamento}</dd>
                </div>
              )}

              {game.developer !== null && (
                <div>
                  <dt>DEVELOPER</dt>
                  <dd>{game.developer}</dd>
                </div>
              )}

              {game.genero !== null && (
                <div>
                  <dt>GENRE</dt>
                  <dd>{game.genero}</dd>
                </div>
              )}

              {game.franchise !== null && (
                <div>
                  <dt>FRANCHISE</dt>
                  <dd>{game.franchise}</dd>
                </div>
              )}

              {game.metacritic !== null && (
                <div>
                  <dt>METACRITIC</dt>
                  <dd>{game.metacritic}</dd>
                </div>
              )}

              {game.nota_kadu !== null && (
                <div>
                  <dt>KADU</dt>
                  <dd>{game.nota_kadu}</dd>
                </div>
              )}

              {game.nota_pavam !== null && (
                <div>
                  <dt>PAVAM</dt>
                  <dd>{game.nota_pavam}</dd>
                </div>
              )}
            </dl>
          </ArchivePanel>
        </div>
      )}

      <footer className="archive-quote">
        <span>
          “Every record begins as a signal waiting to be
          recovered.”
        </span>

        <span>— The Archivist</span>
      </footer>
    </ArchiveShell>
  )
}

export default GamePage