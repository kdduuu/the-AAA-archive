/*
===========================================================
The AAA Archive
Arquivo: AwardsPage.tsx

Objetivo:
Permitir a exploração da Awards History por ano.

Nesta etapa, a página:
- carrega todos os registros para montar o índice de anos;
- seleciona 2003 como primeiro registro disponível;
- consulta GET /awards/{year};
- apresenta vencedor e indicados;
- representa loading, success, empty e error;
- verifica se o vencedor está na Foundation Collection;
- abre o registro individual quando o jogo está preservado;
- apresenta o contexto da premiação selecionada.
===========================================================
*/

import {
  useEffect,
  useState,
} from 'react'

import { Link } from 'react-router'

import ArchivePanel from '../components/ArchivePanel'
import ArchiveShell from '../components/ArchiveShell'
import type { ContextSidebarItem } from '../components/ContextSidebar'
import {
  getAwards,
  getAwardsByYear,
  getFoundationAwardWinners,
  getGames,
} from '../services/api'
import type { Award } from '../types/Award'
import type { Game } from '../types/Game'

import './AwardsPage.css'


type AwardsRequestState =
  | 'loading'
  | 'success'
  | 'empty'
  | 'error'


type SelectedYearRequestState =
  | 'idle'
  | 'loading'
  | 'success'
  | 'empty'
  | 'error'


type FoundationRequestState =
  | 'loading'
  | 'success'
  | 'error'


function normalizeTitle(title: string) {
  return title
    .trim()
    .toLocaleLowerCase()
}


// ==========================================================
// CONTEXTO EDITORIAL DAS PREMIAÇÕES
// ==========================================================

/*
O banco informa o nome da cerimônia de cada registro.

A partir desse nome, o React seleciona um texto curto e
estático para contextualizar a fase correspondente da
premiação, sem criar uma nova requisição à API.
*/

function getCeremonyContext(
  ceremonyName: string | undefined,
) {
  if (ceremonyName === 'Spike Video Game Awards') {
    return {
      code: 'SPIKE VGA',
      title: 'SPIKE VIDEO GAME AWARDS',
      description:
        'A primeira fase do arquivo acompanha a premiação televisionada pela Spike TV, quando o reconhecimento anual dos jogos ainda carregava a linguagem e a energia da televisão dos anos 2000.',
    }
  }

  if (ceremonyName === 'VGX') {
    return {
      code: 'VGX',
      title: 'VGX',
      description:
        'O VGX representou uma transição breve no formato da cerimônia. A identidade mudou, mas o registro anual de vencedores e indicados continuou preservado dentro da mesma linha histórica.',
    }
  }

  if (ceremonyName === 'The Game Awards') {
    return {
      code: 'TGA',
      title: 'THE GAME AWARDS',
      description:
        'The Game Awards consolidou uma nova fase da premiação, combinando reconhecimento da indústria, apresentações e anúncios em uma cerimônia anual de alcance internacional.',
    }
  }

  return {
    code: 'AWAITING DATA',
    title: 'CEREMONY CONTEXT UNAVAILABLE',
    description:
      'Selecione um ano válido para recuperar o contexto da premiação correspondente.',
  }
}


const awardsSidebarItems: ContextSidebarItem[] = [
  {
    label: 'AWARDS OVERVIEW',
    target: '#awards-overview',
  },
  {
    label: 'YEAR INDEX',
    target: '#awards-year-index',
  },
  {
    label: 'SELECTED YEAR',
    target: '#awards-selected-year',
  },
  {
    label: 'FOUNDATION STATUS',
    target: '#awards-foundation-status',
  },
  {
    label: 'ABOUT THE AWARD',
    target: '#awards-about-award',
  },
]


function AwardsPage() {
  const [awards, setAwards] =
    useState<Award[]>([])

  const [requestState, setRequestState] =
    useState<AwardsRequestState>('loading')

  const [selectedYear, setSelectedYear] =
    useState<number | null>(null)

  const [selectedAwards, setSelectedAwards] =
    useState<Award[]>([])

  const [selectedYearRequestState, setSelectedYearRequestState] =
    useState<SelectedYearRequestState>('idle')

  const [foundationWinners, setFoundationWinners] =
    useState<Award[]>([])

  const [foundationGames, setFoundationGames] =
    useState<Game[]>([])

  const [foundationRequestState, setFoundationRequestState] =
    useState<FoundationRequestState>('loading')


  // ========================================================
  // CARREGAMENTO DO ÍNDICE COMPLETO
  // ========================================================

  useEffect(() => {
    let pageIsActive = true

    async function loadAwards() {
      try {
        const receivedAwards = await getAwards()

        if (!pageIsActive) {
          return
        }

        setAwards(receivedAwards)

        if (receivedAwards.length === 0) {
          setRequestState('empty')
          return
        }

        const availableYears = Array.from(
          new Set(
            receivedAwards.map((award) => award.ano),
          ),
        ).sort((firstYear, secondYear) => (
          firstYear - secondYear
        ))

        setRequestState('success')
        setSelectedYear(availableYears[0])
      } catch {
        if (pageIsActive) {
          setAwards([])
          setRequestState('error')
        }
      }
    }

    loadAwards()

    return () => {
      pageIsActive = false
    }
  }, [])


  // ========================================================
  // CARREGAMENTO DA REFERÊNCIA COM A FOUNDATION
  // ========================================================

  useEffect(() => {
    let pageIsActive = true

    async function loadFoundationReference() {
      try {
        const [
          receivedFoundationWinners,
          receivedGames,
        ] = await Promise.all([
          getFoundationAwardWinners(),
          getGames(),
        ])

        if (!pageIsActive) {
          return
        }

        setFoundationWinners(
          receivedFoundationWinners,
        )

        setFoundationGames(receivedGames)
        setFoundationRequestState('success')
      } catch {
        if (pageIsActive) {
          setFoundationWinners([])
          setFoundationGames([])
          setFoundationRequestState('error')
        }
      }
    }

    loadFoundationReference()

    return () => {
      pageIsActive = false
    }
  }, [])


  // ========================================================
  // CARREGAMENTO DO ANO SELECIONADO
  // ========================================================

  useEffect(() => {
    if (selectedYear === null) {
      setSelectedAwards([])
      setSelectedYearRequestState('idle')
      return
    }

    const yearToLoad = selectedYear
    let pageIsActive = true

    setSelectedAwards([])
    setSelectedYearRequestState('loading')

    async function loadSelectedYear() {
      try {
        const receivedAwards = await getAwardsByYear(
          yearToLoad,
        )

        if (!pageIsActive) {
          return
        }

        setSelectedAwards(receivedAwards)

        setSelectedYearRequestState(
          receivedAwards.length > 0
            ? 'success'
            : 'empty',
        )
      } catch {
        if (pageIsActive) {
          setSelectedAwards([])
          setSelectedYearRequestState('error')
        }
      }
    }

    loadSelectedYear()

    return () => {
      pageIsActive = false
    }
  }, [selectedYear])


  // ========================================================
  // INFORMAÇÕES DERIVADAS
  // ========================================================

  const years = Array.from(
    new Set(
      awards.map((award) => award.ano),
    ),
  ).sort((firstYear, secondYear) => (
    firstYear - secondYear
  ))

  const firstYear = years[0]
  const lastYear = years[years.length - 1]

  const winner = selectedAwards.find((award) => (
    award.status === 'Vencedor'
  ))

  const nominees = selectedAwards.filter((award) => (
    award.status === 'Indicado'
  ))

  const ceremonyName = selectedAwards[0]?.premiacao

  const ceremonyContext = getCeremonyContext(
    ceremonyName,
  )

  const winnerInFoundation =
    winner !== undefined
    && foundationWinners.some((foundationWinner) => (
      foundationWinner.ano === winner.ano
      && normalizeTitle(foundationWinner.jogo)
        === normalizeTitle(winner.jogo)
    ))

  const foundationGame =
    winnerInFoundation && winner !== undefined
      ? foundationGames.find((game) => (
          normalizeTitle(game.nome)
            === normalizeTitle(winner.jogo)
        ))
      : undefined


  // ========================================================
  // ESTADO VISUAL
  // ========================================================

  let archiveStatus = 'retrieving'
  let archivePeriod = 'AWAITING DATA'
  let yearIndexCode = 'RETRIEVING'

  if (requestState === 'success') {
    archiveStatus = 'stable'
    archivePeriod = `${firstYear}—${lastYear}`
    yearIndexCode = `${years.length} YEARS`
  }

  if (requestState === 'empty') {
    archiveStatus = 'empty'
    archivePeriod = 'NO RECORDS'
    yearIndexCode = 'EMPTY'
  }

  if (requestState === 'error') {
    archiveStatus = 'unavailable'
    archivePeriod = 'NODE OFFLINE'
    yearIndexCode = 'UNAVAILABLE'
  }

  let selectedYearCode = 'NO RECORD SELECTED'

  if (selectedYear !== null) {
    selectedYearCode = String(selectedYear)
  }

  if (selectedYearRequestState === 'loading') {
    selectedYearCode = 'RETRIEVING'
  }

  if (selectedYearRequestState === 'error') {
    selectedYearCode = 'UNAVAILABLE'
  }

  let foundationStatusCode = 'AWAITING WINNER'

  if (winner !== undefined) {
    foundationStatusCode = 'CHECKING'
  }

  if (
    winner !== undefined
    && foundationRequestState === 'success'
  ) {
    foundationStatusCode = winnerInFoundation
      ? 'CONFIRMED'
      : 'NOT ARCHIVED'
  }

  if (foundationRequestState === 'error') {
    foundationStatusCode = 'UNAVAILABLE'
  }


  // ========================================================
  // INTERFACE
  // ========================================================

  return (
    <ArchiveShell
      sidebarTitle="AWARDS HISTORY"
      sidebarItems={awardsSidebarItems}
      activeSidebarItem="AWARDS OVERVIEW"
    >
      <section
        id="awards-overview"
        className="archive-panel awards-page__hero"
      >
        <div className="awards-page__hero-content">
          <p className="archive-eyebrow">
            // AWARDS / HISTORICAL LOG
          </p>

          <h1>AWARDS HISTORY</h1>

          <p className="awards-page__description">
            Um registro cronológico dos vencedores e indicados
            que permaneceram depois que as cerimônias terminaram.
          </p>

          <p
            className={
              requestState === 'error'
                ? 'archive-system-message awards-page__status awards-page__status--error'
                : 'archive-system-message awards-page__status'
            }
          >
            &gt; awards archive status:

            <span> {archiveStatus}</span>
          </p>
        </div>

        <div
          className="awards-page__hero-visual"
          aria-label="Representação temporária do arquivo de premiações"
        >
          <div
            className="awards-page__hero-grid"
            aria-hidden="true"
          />

          <div className="awards-page__hero-placeholder">
            <span>AWARDS CEREMONY LOG</span>

            <strong>{archivePeriod}</strong>

            <small>
              {requestState === 'success'
                ? `${awards.length} historical records synchronized`
                : 'historical records awaiting synchronization'}
            </small>
          </div>
        </div>
      </section>

      <div className="awards-page__panels">
        <ArchivePanel
          id="awards-year-index"
          title="YEAR INDEX"
          code={yearIndexCode}
        >
          <div
            className="awards-page__year-index-content"
            aria-live="polite"
          >
            {requestState === 'loading' && (
              <div className="awards-page__request-state">
                <span>INDEX NODE</span>

                <strong>RETRIEVING AWARDS...</strong>

                <p>
                  Connecting to the archive node and loading
                  the historical ceremony records.
                </p>
              </div>
            )}

            {requestState === 'error' && (
              <div className="awards-page__request-state awards-page__request-state--error">
                <span>INDEX NODE</span>

                <strong>ARCHIVE NODE UNAVAILABLE</strong>

                <p>
                  Os registros de premiações não puderam ser
                  carregados pela FastAPI.
                </p>
              </div>
            )}

            {requestState === 'empty' && (
              <div className="awards-page__request-state">
                <span>INDEX NODE</span>

                <strong>NO AWARDS RECORDS FOUND</strong>

                <p>
                  A API respondeu corretamente, mas não retornou
                  registros da Awards History.
                </p>
              </div>
            )}

            {requestState === 'success' && (
              <>
                <div className="awards-page__year-index-header">
                  <span>AVAILABLE CEREMONY YEARS</span>

                  <small>
                    select a year to open its preserved record
                  </small>
                </div>

                <div className="awards-page__years">
                  {years.map((year) => (
                    <button
                      key={year}
                      type="button"
                      className={
                        selectedYear === year
                          ? 'awards-page__year awards-page__year--active'
                          : 'awards-page__year'
                      }
                      aria-pressed={selectedYear === year}
                      onClick={() => setSelectedYear(year)}
                    >
                      {year}
                    </button>
                  ))}
                </div>
              </>
            )}
          </div>
        </ArchivePanel>

        <ArchivePanel
          id="awards-selected-year"
          title="SELECTED YEAR"
          code={selectedYearCode}
        >
          <div
            className="awards-page__selected-year-content"
            aria-live="polite"
          >
            {selectedYearRequestState === 'idle' && (
              <div className="awards-page__request-state">
                <span>CEREMONY RECORD</span>

                <strong>AWAITING YEAR</strong>

                <p>
                  Selecione um ano para abrir o registro da cerimônia.
                </p>
              </div>
            )}

            {selectedYearRequestState === 'loading' && (
              <div className="awards-page__request-state">
                <span>CEREMONY RECORD</span>

                <strong>RETRIEVING CEREMONY...</strong>

                <p>
                  Loading the winner and nominees from the
                  selected edition.
                </p>
              </div>
            )}

            {selectedYearRequestState === 'error' && (
              <div className="awards-page__request-state awards-page__request-state--error">
                <span>CEREMONY RECORD</span>

                <strong>CEREMONY RECORD UNAVAILABLE</strong>

                <p>
                  O registro do ano selecionado não pôde ser
                  carregado pela FastAPI.
                </p>
              </div>
            )}

            {selectedYearRequestState === 'empty' && (
              <div className="awards-page__request-state">
                <span>CEREMONY RECORD</span>

                <strong>NO RECORDS FOR THIS YEAR</strong>

                <p>
                  Nenhum vencedor ou indicado foi encontrado
                  para o ano selecionado.
                </p>
              </div>
            )}

            {selectedYearRequestState === 'success' && (
              <div className="awards-page__ceremony-record">
                <header className="awards-page__ceremony-header">
                  <div>
                    <span>SELECTED YEAR</span>

                    <strong>{selectedYear}</strong>
                  </div>

                  <p>{ceremonyName}</p>
                </header>

                <section className="awards-page__winner">
                  <span>GAME OF THE YEAR / WINNER</span>

                  <strong>
                    {winner?.jogo ?? 'WINNER NOT REGISTERED'}
                  </strong>
                </section>

                <section className="awards-page__nominees">
                  <div className="awards-page__nominees-header">
                    <span>NOMINEES</span>

                    <small>{nominees.length} RECORDS</small>
                  </div>

                  {nominees.length > 0 ? (
                    <ol className="awards-page__nominees-list">
                      {nominees.map((nominee, index) => (
                        <li key={`${nominee.jogo}-${index}`}>
                          <span>
                            {String(index + 1).padStart(2, '0')}
                          </span>

                          <strong>{nominee.jogo}</strong>
                        </li>
                      ))}
                    </ol>
                  ) : (
                    <p className="awards-page__no-nominees">
                      NO NOMINEES REGISTERED
                    </p>
                  )}
                </section>
              </div>
            )}
          </div>
        </ArchivePanel>

        <ArchivePanel
          id="awards-foundation-status"
          title="FOUNDATION STATUS"
          code={foundationStatusCode}
          className="awards-page__foundation-panel"
        >
          <div
            className={
              winner !== undefined
              && foundationRequestState === 'success'
                ? winnerInFoundation
                  ? 'awards-page__foundation-content awards-page__foundation-content--confirmed'
                  : 'awards-page__foundation-content awards-page__foundation-content--outside'
                : 'awards-page__foundation-content'
            }
            aria-live="polite"
          >
            <span className="awards-page__foundation-label">
              FOUNDATION CROSS-REFERENCE
            </span>

            {winner === undefined && (
              <>
                <strong>AWAITING WINNER</strong>

                <p>
                  Selecione uma edição válida para verificar
                  o vencedor na Foundation Collection.
                </p>
              </>
            )}

            {
              winner !== undefined
              && foundationRequestState === 'loading'
              && (
                <>
                  <strong>CHECKING FOUNDATION...</strong>

                  <p>
                    Comparing the selected winner with the
                    preserved Foundation records.
                  </p>
                </>
              )
            }

            {
              winner !== undefined
              && foundationRequestState === 'error'
              && (
                <>
                  <strong>FOUNDATION NODE UNAVAILABLE</strong>

                  <p>
                    A presença do vencedor na Foundation não
                    pôde ser verificada pela FastAPI.
                  </p>
                </>
              )
            }

            {
              winner !== undefined
              && foundationRequestState === 'success'
              && winnerInFoundation
              && (
                <>
                  <strong>CONFIRMED</strong>

                  <p>
                    <b>{winner.jogo}</b> está preservado na
                    Foundation Collection.
                  </p>

                  {foundationGame !== undefined && (
                    <Link
                      to={`/games/${foundationGame.id}`}
                      className="awards-page__foundation-link"
                    >
                      VIEW FOUNDATION RECORD
                    </Link>
                  )}
                </>
              )
            }

            {
              winner !== undefined
              && foundationRequestState === 'success'
              && !winnerInFoundation
              && (
                <>
                  <strong>NOT ARCHIVED</strong>

                  <p>
                    <b>{winner.jogo}</b> aparece na Awards
                    History, mas ainda não está preservado na
                    Foundation Collection.
                  </p>
                </>
              )
            }
          </div>
        </ArchivePanel>

        <ArchivePanel
          id="awards-about-award"
          title="ABOUT THE AWARD"
          code={ceremonyContext.code}
          className="awards-page__about-panel"
        >
          <div className="awards-page__about-content">
            <span className="awards-page__about-label">
              CEREMONY CONTEXT
            </span>

            <strong>{ceremonyContext.title}</strong>

            <p>{ceremonyContext.description}</p>

            {ceremonyName !== undefined && (
              <dl className="awards-page__about-metadata">
                <div>
                  <dt>SELECTED EDITION</dt>
                  <dd>{selectedYear}</dd>
                </div>

                <div>
                  <dt>ARCHIVE NAME</dt>
                  <dd>{ceremonyName}</dd>
                </div>
              </dl>
            )}
          </div>
        </ArchivePanel>
      </div>

      <footer className="archive-quote">
        <span>
          “The ceremony ended. The records remained.”
        </span>

        <span>— The Archivist</span>
      </footer>
    </ArchiveShell>
  )
}

export default AwardsPage