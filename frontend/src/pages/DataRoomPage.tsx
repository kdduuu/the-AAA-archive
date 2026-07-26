/*
===========================================================
The AAA Archive
Arquivo: DataRoomPage.tsx

Objetivo:
Apresentar a área analítica do projeto e carregar as
métricas gerais reais do arquivo.

Nesta etapa, a página:
- utiliza ArchiveShell;
- possui navegação contextual;
- consulta GET /stats/home;
- consulta GET /games;
- consulta GET /awards;
- representa loading, success, empty e error;
- calcula a distribuição da Foundation por década;
- calcula a distribuição da Foundation por gênero;
- calcula as desenvolvedoras com mais registros;
- apresenta os gráficos da Foundation;
- apresenta a presença dos vencedores na Foundation;
- abre o dashboard Streamlit em outra aba.
===========================================================
*/

import {
  useEffect,
  useState,
} from 'react'

import ArchivePanel from '../components/ArchivePanel'
import ArchiveShell from '../components/ArchiveShell'
import type { ContextSidebarItem } from '../components/ContextSidebar'
import {
  getAwards,
  getFoundationAwardWinners,
  getGames,
  getHomeStats,
} from '../services/api'
import type { Game } from '../types/Game'

import './DataRoomPage.css'


// ==========================================================
// TIPOS INTERNOS DA PÁGINA
// ==========================================================

type MetricsRequestState =
  | 'loading'
  | 'success'
  | 'empty'
  | 'error'

type ArchiveMetrics = {
  foundationRecords: number
  awardsLogs: number
  archivePeriod: string
  awardsPeriod: string
  developers: number
  genres: number
  awardEditions: number
  winners: number
}

type FoundationDistributionItem = {
  decade: number
  count: number
}

type GenreDistributionItem = {
  genre: string
  count: number
}

type DeveloperDistributionItem = {
  developer: string
  count: number
}

type AwardsDistribution = {
  totalWinners: number
  confirmedWinners: number
  outsideFoundation: number
  confirmedPercentage: number
}


// ==========================================================
// NAVEGAÇÃO CONTEXTUAL
// ==========================================================

const dataRoomSidebarItems: ContextSidebarItem[] = [
  {
    label: 'ARCHIVE METRICS',
    target: '#data-room-metrics',
  },
  {
    label: 'FOUNDATION DATA',
    target: '#data-room-foundation',
  },
  {
    label: 'AWARDS DATA',
    target: '#data-room-awards',
  },
  {
    label: 'OPEN DASHBOARD',
    target: '#data-room-dashboard',
  },
  {
    label: 'SYSTEM INFORMATION',
    target: '#data-room-system',
  },
]


// ==========================================================
// ENDEREÇO LOCAL DO DASHBOARD
// ==========================================================

/*
O Streamlit funciona como uma aplicação separada do React.

Durante o desenvolvimento local, seu endereço padrão é:
http://localhost:8501
*/

const STREAMLIT_DASHBOARD_URL = (
  import.meta.env.VITE_STREAMLIT_URL?.trim()
  || 'http://localhost:8501'
).replace(/\/+$/, '')

const STREAMLIT_DASHBOARD_ADDRESS =
  STREAMLIT_DASHBOARD_URL
    .replace(/^https?:\/\//, '')

/*
A página apresenta somente as desenvolvedoras com maior
presença para manter a leitura compacta.

A lista completa continua disponível no dashboard Streamlit.
*/

const DEVELOPER_DISPLAY_LIMIT = 8


// ==========================================================
// INFORMAÇÕES TÉCNICAS ESTÁVEIS
// ==========================================================

const systemInformation = [
  {
    label: 'DATA SOURCE',
    value: 'PostgreSQL',
  },
  {
    label: 'PROCESSING',
    value: 'Python / Pandas',
  },
  {
    label: 'API LAYER',
    value: 'FastAPI',
  },
  {
    label: 'FRONTEND',
    value: 'React / TypeScript',
  },
  {
    label: 'DASHBOARD',
    value: 'Streamlit',
  },
  {
    label: 'STATUS',
    value: 'Online',
    stable: true,
  },
]


// ==========================================================
// FUNÇÃO AUXILIAR PARA PERÍODOS
// ==========================================================

function formatPeriod(years: number[]) {
  if (years.length === 0) {
    return 'NO DATA'
  }

  const firstYear = Math.min(...years)
  const lastYear = Math.max(...years)

  if (firstYear === lastYear) {
    return String(firstYear)
  }

  return `${firstYear}—${lastYear}`
}


// ==========================================================
// DISTRIBUIÇÃO DA FOUNDATION POR DÉCADA
// ==========================================================

function createFoundationDistribution(
  games: Game[],
): FoundationDistributionItem[] {
  const decadeCounts = new Map<number, number>()

  games.forEach((game) => {
    if (game.ano_lancamento === null) {
      return
    }

    const decade =
      Math.floor(game.ano_lancamento / 10) * 10

    const currentCount =
      decadeCounts.get(decade) ?? 0

    decadeCounts.set(
      decade,
      currentCount + 1,
    )
  })

  return Array.from(decadeCounts.entries())
    .sort(([firstDecade], [secondDecade]) => (
      firstDecade - secondDecade
    ))
    .map(([decade, count]) => ({
      decade,
      count,
    }))
}


// ==========================================================
// DISTRIBUIÇÃO DA FOUNDATION POR GÊNERO
// ==========================================================

function createGenreDistribution(
  games: Game[],
): GenreDistributionItem[] {
  const genreCounts = new Map<string, number>()

  games.forEach((game) => {
    const genre = game.genero?.trim()

    if (!genre) {
      return
    }

    const currentCount =
      genreCounts.get(genre) ?? 0

    genreCounts.set(
      genre,
      currentCount + 1,
    )
  })

  return Array.from(genreCounts.entries())
    .map(([genre, count]) => ({
      genre,
      count,
    }))
    .sort((firstGenre, secondGenre) => (
      secondGenre.count - firstGenre.count
      || firstGenre.genre.localeCompare(
        secondGenre.genre,
        'pt-BR',
      )
    ))
}


// ==========================================================
// DESENVOLVEDORAS COM MAIS REGISTROS
// ==========================================================

function createDeveloperDistribution(
  games: Game[],
): DeveloperDistributionItem[] {
  const developerCounts = new Map<string, number>()

  games.forEach((game) => {
    const developer = game.developer?.trim()

    if (!developer) {
      return
    }

    const currentCount =
      developerCounts.get(developer) ?? 0

    developerCounts.set(
      developer,
      currentCount + 1,
    )
  })

  return Array.from(developerCounts.entries())
    .map(([developer, count]) => ({
      developer,
      count,
    }))
    .sort((firstDeveloper, secondDeveloper) => (
      secondDeveloper.count - firstDeveloper.count
      || firstDeveloper.developer.localeCompare(
        secondDeveloper.developer,
        'pt-BR',
      )
    ))
    .slice(0, DEVELOPER_DISPLAY_LIMIT)
}


// ==========================================================
// COMPONENTE PRINCIPAL
// ==========================================================

function DataRoomPage() {
  const [metrics, setMetrics] =
    useState<ArchiveMetrics | null>(null)

  const [requestState, setRequestState] =
    useState<MetricsRequestState>('loading')

  const [
    foundationDistribution,
    setFoundationDistribution,
  ] = useState<FoundationDistributionItem[]>([])

  const [
    genreDistribution,
    setGenreDistribution,
  ] = useState<GenreDistributionItem[]>([])

  const [
    developerDistribution,
    setDeveloperDistribution,
  ] = useState<DeveloperDistributionItem[]>([])

  const [
    awardsDistribution,
    setAwardsDistribution,
  ] = useState<AwardsDistribution | null>(null)


  // ========================================================
  // CARREGAMENTO DAS MÉTRICAS
  // ========================================================

  useEffect(() => {
    let pageIsActive = true

    async function loadMetrics() {
      try {
        const [
          statistics,
          games,
          awards,
          foundationWinners,
        ] = await Promise.all([
          getHomeStats(),
          getGames(),
          getAwards(),
          getFoundationAwardWinners(),
        ])

        if (!pageIsActive) {
          return
        }

        if (
          statistics.total_jogos === 0
          && awards.length === 0
        ) {
          setMetrics(null)
          setFoundationDistribution([])
          setGenreDistribution([])
          setDeveloperDistribution([])
          setAwardsDistribution(null)
          setRequestState('empty')
          return
        }

        const gameYears = games
          .map((game) => game.ano_lancamento)
          .filter((year): year is number => (
            year !== null
          ))

        const awardYears = awards.map((award) => (
          award.ano
        ))

        const awardEditions = new Set(
          awardYears,
        ).size

        const winnerYears = new Set(
          awards
            .filter((award) => (
              award.status === 'Vencedor'
            ))
            .map((award) => award.ano),
        )

        const confirmedWinnerYears = new Set(
          foundationWinners.map((award) => award.ano),
        )

        const winners = winnerYears.size
        const confirmedWinners =
          confirmedWinnerYears.size
        const outsideFoundation = Math.max(
          winners - confirmedWinners,
          0,
        )
        const confirmedPercentage = winners > 0
          ? Math.round(
              (confirmedWinners / winners) * 100,
            )
          : 0

        const distribution =
          createFoundationDistribution(games)

        const genres =
          createGenreDistribution(games)

        const developers =
          createDeveloperDistribution(games)

        setMetrics({
          foundationRecords: statistics.total_jogos,
          awardsLogs: awards.length,
          archivePeriod: formatPeriod(gameYears),
          awardsPeriod: formatPeriod(awardYears),
          developers: statistics.total_developers,
          genres: statistics.total_generos,
          awardEditions,
          winners,
        })

        setFoundationDistribution(distribution)
        setGenreDistribution(genres)
        setDeveloperDistribution(developers)
        setAwardsDistribution({
          totalWinners: winners,
          confirmedWinners,
          outsideFoundation,
          confirmedPercentage,
        })
        setRequestState('success')
      } catch {
        if (pageIsActive) {
          setMetrics(null)
          setFoundationDistribution([])
          setGenreDistribution([])
          setDeveloperDistribution([])
          setAwardsDistribution(null)
          setRequestState('error')
        }
      }
    }

    loadMetrics()

    return () => {
      pageIsActive = false
    }
  }, [])


  // ========================================================
  // CONTEÚDO VISUAL DAS MÉTRICAS
  // ========================================================

  let analyticalStatus = 'retrieving'
  let metricsCode = 'RETRIEVING'
  let metricValue = '—'
  let metricDetail = 'waiting for API'

  if (requestState === 'success') {
    analyticalStatus = 'stable'
    metricsCode = 'SYNCHRONIZED'
  }

  if (requestState === 'empty') {
    analyticalStatus = 'empty'
    metricsCode = 'NO DATA'
    metricValue = '0'
    metricDetail = 'no records returned'
  }

  if (requestState === 'error') {
    analyticalStatus = 'unavailable'
    metricsCode = 'NODE OFFLINE'
    metricDetail = 'API connection failed'
  }

  const metricCards = [
    {
      label: 'FOUNDATION RECORDS',
      value: metrics
        ? String(metrics.foundationRecords)
        : metricValue,
      detail: metrics
        ? `${metrics.developers} developers`
        : metricDetail,
    },
    {
      label: 'AWARDS LOGS',
      value: metrics
        ? String(metrics.awardsLogs)
        : metricValue,
      detail: metrics
        ? `${metrics.winners} winners`
        : metricDetail,
    },
    {
      label: 'ARCHIVE PERIOD',
      value: metrics
        ? metrics.archivePeriod
        : metricValue,
      detail: metrics
        ? `${metrics.genres} genres`
        : metricDetail,
    },
    {
      label: 'AWARDS PERIOD',
      value: metrics
        ? metrics.awardsPeriod
        : metricValue,
      detail: metrics
        ? `${metrics.awardEditions} editions`
        : metricDetail,
    },
  ]


  // ========================================================
  // INFORMAÇÕES DO GRÁFICO DA FOUNDATION
  // ========================================================

  const largestDecadeCount = Math.max(
    ...foundationDistribution.map((item) => item.count),
    1,
  )

  const leadingDecade =
    foundationDistribution.reduce<
      FoundationDistributionItem | null
    >((currentLeader, item) => {
      if (
        currentLeader === null
        || item.count > currentLeader.count
      ) {
        return item
      }

      return currentLeader
    }, null)

  const largestGenreCount = Math.max(
    ...genreDistribution.map((item) => item.count),
    1,
  )

  const leadingGenre = genreDistribution[0] ?? null

  const largestDeveloperCount = Math.max(
    ...developerDistribution.map((item) => item.count),
    1,
  )

  const leadingDeveloper =
    developerDistribution[0] ?? null

  let foundationChartCode = 'RETRIEVING'

  if (
    requestState === 'success'
    && (
      foundationDistribution.length > 0
      || genreDistribution.length > 0
      || developerDistribution.length > 0
    )
  ) {
    foundationChartCode =
      `${metrics?.foundationRecords ?? 0} RECORDS`
  }

  if (
    requestState === 'empty'
    || (
      requestState === 'success'
      && foundationDistribution.length === 0
      && genreDistribution.length === 0
      && developerDistribution.length === 0
    )
  ) {
    foundationChartCode = 'NO DATA'
  }

  if (requestState === 'error') {
    foundationChartCode = 'UNAVAILABLE'
  }


  // ========================================================
  // INFORMAÇÕES DO GRÁFICO DE PREMIAÇÕES
  // ========================================================

  let awardsChartCode = 'RETRIEVING'

  if (
    requestState === 'success'
    && awardsDistribution
    && awardsDistribution.totalWinners > 0
  ) {
    awardsChartCode =
      `${awardsDistribution.totalWinners} WINNERS`
  }

  if (
    requestState === 'empty'
    || (
      requestState === 'success'
      && (
        awardsDistribution === null
        || awardsDistribution.totalWinners === 0
      )
    )
  ) {
    awardsChartCode = 'NO DATA'
  }

  if (requestState === 'error') {
    awardsChartCode = 'UNAVAILABLE'
  }


  // ========================================================
  // INTERFACE
  // ========================================================

  return (
    <ArchiveShell
      sidebarTitle="DATA ROOM"
      sidebarItems={dataRoomSidebarItems}
      activeSidebarItem="ARCHIVE METRICS"
    >
      <section className="archive-panel data-room__hero">
        <div className="data-room__hero-content">
          <p className="archive-eyebrow">
            // DATA ROOM / ANALYTICAL NODE
          </p>

          <h1>DATA ROOM</h1>

          <p className="data-room__description">
            Nas outras áreas, os jogos são preservados como
            obras e memórias. Aqui, os mesmos registros são
            observados como dados.
          </p>

          <p
            className={
              requestState === 'error'
                ? 'archive-system-message data-room__status data-room__status--error'
                : 'archive-system-message data-room__status'
            }
          >
            &gt; analytical node status:

            <span> {analyticalStatus}</span>
          </p>
        </div>

        <div
          className="data-room__hero-visual"
          aria-label="Representação temporária da sala analítica"
        >
          <div
            className="data-room__hero-grid"
            aria-hidden="true"
          />

          <div className="data-room__hero-placeholder">
            <span>ANALYTICAL FEED</span>

            <strong>NODE 02</strong>

            <small>
              {requestState === 'success'
                ? 'archive metrics synchronized'
                : 'metrics awaiting API synchronization'}
            </small>
          </div>
        </div>
      </section>

      <ArchivePanel
        id="data-room-metrics"
        title="ARCHIVE METRICS"
        code={metricsCode}
        className="data-room__metrics-panel"
      >
        <div
          className="data-room__metrics-grid"
          aria-live="polite"
        >
          {metricCards.map((metric) => (
            <article
              key={metric.label}
              className={
                requestState === 'error'
                  ? 'data-room__metric data-room__metric--error'
                  : 'data-room__metric'
              }
            >
              <span>{metric.label}</span>
              <strong>{metric.value}</strong>
              <small>{metric.detail}</small>
            </article>
          ))}
        </div>
      </ArchivePanel>

      <div className="data-room__data-grid">
        <ArchivePanel
          id="data-room-foundation"
          title="FOUNDATION DATA"
          code={foundationChartCode}
        >
          <div
            className="data-room__foundation-chart"
            aria-live="polite"
          >
            {requestState === 'loading' && (
              <div className="data-room__chart-state">
                <span>FOUNDATION DISTRIBUTION</span>

                <strong>CALCULATING DECADES...</strong>

                <p>
                  Os registros estão sendo organizados de acordo
                  com seus anos de lançamento.
                </p>
              </div>
            )}

            {requestState === 'error' && (
              <div className="data-room__chart-state data-room__chart-state--error">
                <span>FOUNDATION DISTRIBUTION</span>

                <strong>CHART NODE UNAVAILABLE</strong>

                <p>
                  A distribuição não pôde ser calculada porque
                  os jogos não foram recebidos da FastAPI.
                </p>
              </div>
            )}

            {(
              requestState === 'empty'
              || (
                requestState === 'success'
                && foundationDistribution.length === 0
              )
            ) && (
              <div className="data-room__chart-state">
                <span>FOUNDATION DISTRIBUTION</span>

                <strong>NO RELEASE YEARS FOUND</strong>

                <p>
                  Nenhum ano de lançamento está disponível para
                  construir a distribuição por década.
                </p>
              </div>
            )}

            {(
              requestState === 'success'
              && foundationDistribution.length > 0
            ) && (
              <>
                <header className="data-room__chart-header">
                  <div>
                    <span>FOUNDATION DISTRIBUTION</span>

                    <strong>RECORDS BY DECADE</strong>
                  </div>

                  <small>
                    {metrics?.foundationRecords ?? 0} RECORDS
                  </small>
                </header>

                <div
                  className="data-room__decade-chart"
                  role="list"
                  aria-label="Quantidade de jogos da Foundation por década"
                >
                  {foundationDistribution.map((item) => {
                    const barHeight = Math.max(
                      12,
                      (
                        item.count
                        / largestDecadeCount
                      ) * 100,
                    )

                    return (
                      <article
                        key={item.decade}
                        className="data-room__decade-column"
                        role="listitem"
                        aria-label={`${item.decade}s: ${item.count} jogos`}
                      >
                        <strong>{item.count}</strong>

                        <div
                          className="data-room__decade-track"
                          aria-hidden="true"
                        >
                          <span
                            style={{
                              height: `${barHeight}%`,
                            }}
                          />
                        </div>

                        <small>{item.decade}s</small>
                      </article>
                    )
                  })}
                </div>

                <p className="data-room__chart-summary">
                  {leadingDecade
                    ? `A década de ${leadingDecade.decade} concentra ${leadingDecade.count} registros, a maior presença atual na Foundation.`
                    : 'Nenhuma década pôde ser destacada.'}
                </p>
              </>
            )}

            {requestState === 'success' && (
              <section className="data-room__genre-section">
                <header className="data-room__chart-header">
                  <div>
                    <span>GENRE DISTRIBUTION</span>

                    <strong>RECORDS BY GENRE</strong>
                  </div>

                  <small>
                    {genreDistribution.length} GENRES
                  </small>
                </header>

                {genreDistribution.length > 0 ? (
                  <>
                    <div
                      className="data-room__genre-bars"
                      role="list"
                      aria-label="Quantidade de jogos da Foundation por gênero"
                    >
                      {genreDistribution.map((item) => {
                        const barWidth = Math.max(
                          4,
                          (
                            item.count
                            / largestGenreCount
                          ) * 100,
                        )

                        return (
                          <article
                            key={item.genre}
                            className="data-room__genre-bar"
                            role="listitem"
                            aria-label={`${item.genre}: ${item.count} jogos`}
                          >
                            <div className="data-room__genre-bar-header">
                              <span>{item.genre}</span>

                              <strong>{item.count}</strong>
                            </div>

                            <div
                              className="data-room__genre-track"
                              aria-hidden="true"
                            >
                              <span
                                style={{
                                  width: `${barWidth}%`,
                                }}
                              />
                            </div>
                          </article>
                        )
                      })}
                    </div>

                    <p className="data-room__chart-summary">
                      {leadingGenre
                        ? `${leadingGenre.genre} é o gênero mais recorrente, com ${leadingGenre.count} registros preservados.`
                        : 'Nenhum gênero pôde ser destacado.'}
                    </p>
                  </>
                ) : (
                  <div className="data-room__chart-state">
                    <strong>NO GENRES FOUND</strong>

                    <p>
                      Nenhum gênero está disponível para construir
                      esta distribuição.
                    </p>
                  </div>
                )}
              </section>
            )}

            {requestState === 'success' && (
              <section className="data-room__developer-section">
                <header className="data-room__chart-header">
                  <div>
                    <span>DEVELOPER PRESENCE</span>

                    <strong>TOP DEVELOPERS</strong>
                  </div>

                  <small>
                    TOP {developerDistribution.length}
                  </small>
                </header>

                {developerDistribution.length > 0 ? (
                  <>
                    <div
                      className="data-room__developer-bars"
                      role="list"
                      aria-label="Desenvolvedoras com mais jogos na Foundation"
                    >
                      {developerDistribution.map((item, index) => {
                        const barWidth = Math.max(
                          4,
                          (
                            item.count
                            / largestDeveloperCount
                          ) * 100,
                        )

                        return (
                          <article
                            key={item.developer}
                            className="data-room__developer-bar"
                            role="listitem"
                            aria-label={`${item.developer}: ${item.count} jogos`}
                          >
                            <span className="data-room__developer-position">
                              {String(index + 1).padStart(2, '0')}
                            </span>

                            <div className="data-room__developer-content">
                              <div className="data-room__developer-bar-header">
                                <span>{item.developer}</span>

                                <strong>{item.count}</strong>
                              </div>

                              <div
                                className="data-room__developer-track"
                                aria-hidden="true"
                              >
                                <span
                                  style={{
                                    width: `${barWidth}%`,
                                  }}
                                />
                              </div>
                            </div>
                          </article>
                        )
                      })}
                    </div>

                    <p className="data-room__chart-summary">
                      {leadingDeveloper
                        ? `${leadingDeveloper.developer} possui a maior presença atual, com ${leadingDeveloper.count} registros na Foundation.`
                        : 'Nenhuma desenvolvedora pôde ser destacada.'}
                    </p>
                  </>
                ) : (
                  <div className="data-room__chart-state">
                    <strong>NO DEVELOPERS FOUND</strong>

                    <p>
                      Nenhuma desenvolvedora está disponível para
                      construir este ranking.
                    </p>
                  </div>
                )}
              </section>
            )}
          </div>
        </ArchivePanel>

        <ArchivePanel
          id="data-room-awards"
          title="AWARDS DATA"
          code={awardsChartCode}
        >
          <div
            className="data-room__awards-chart"
            aria-live="polite"
          >
            {requestState === 'loading' && (
              <div className="data-room__chart-state">
                <span>FOUNDATION CROSS-REFERENCE</span>

                <strong>CALCULATING WINNER PRESENCE...</strong>

                <p>
                  Os vencedores estão sendo comparados com os
                  registros preservados na Foundation.
                </p>
              </div>
            )}

            {requestState === 'error' && (
              <div className="data-room__chart-state data-room__chart-state--error">
                <span>FOUNDATION CROSS-REFERENCE</span>

                <strong>CHART NODE UNAVAILABLE</strong>

                <p>
                  A presença dos vencedores não pôde ser
                  calculada porque a API não respondeu.
                </p>
              </div>
            )}

            {(
              requestState === 'empty'
              || (
                requestState === 'success'
                && (
                  awardsDistribution === null
                  || awardsDistribution.totalWinners === 0
                )
              )
            ) && (
              <div className="data-room__chart-state">
                <span>FOUNDATION CROSS-REFERENCE</span>

                <strong>NO WINNERS FOUND</strong>

                <p>
                  Nenhum vencedor está disponível para construir
                  a distribuição da Awards History.
                </p>
              </div>
            )}

            {(
              requestState === 'success'
              && awardsDistribution
              && awardsDistribution.totalWinners > 0
            ) && (
              <>
                <header className="data-room__chart-header">
                  <div>
                    <span>FOUNDATION CROSS-REFERENCE</span>

                    <strong>GOTY WINNER PRESENCE</strong>
                  </div>

                  <small>
                    {awardsDistribution.totalWinners} WINNERS
                  </small>
                </header>

                <div
                  className="data-room__awards-bars"
                  role="list"
                  aria-label="Presença dos vencedores de Game of the Year na Foundation"
                >
                  <article
                    className="data-room__awards-bar"
                    role="listitem"
                    aria-label={`${awardsDistribution.confirmedWinners} vencedores presentes na Foundation`}
                  >
                    <div className="data-room__awards-bar-header">
                      <span>CONFIRMED IN FOUNDATION</span>

                      <strong>
                        {awardsDistribution.confirmedWinners}
                      </strong>
                    </div>

                    <div
                      className="data-room__awards-track"
                      aria-hidden="true"
                    >
                      <span
                        className="data-room__awards-fill data-room__awards-fill--confirmed"
                        style={{
                          width: `${awardsDistribution.confirmedPercentage}%`,
                        }}
                      />
                    </div>
                  </article>

                  <article
                    className="data-room__awards-bar"
                    role="listitem"
                    aria-label={`${awardsDistribution.outsideFoundation} vencedores fora da Foundation`}
                  >
                    <div className="data-room__awards-bar-header">
                      <span>OUTSIDE FOUNDATION</span>

                      <strong>
                        {awardsDistribution.outsideFoundation}
                      </strong>
                    </div>

                    <div
                      className="data-room__awards-track"
                      aria-hidden="true"
                    >
                      <span
                        className="data-room__awards-fill data-room__awards-fill--outside"
                        style={{
                          width: `${100 - awardsDistribution.confirmedPercentage}%`,
                        }}
                      />
                    </div>
                  </article>
                </div>

                <div className="data-room__awards-summary">
                  <strong>
                    {awardsDistribution.confirmedPercentage}%
                  </strong>

                  <p>
                    dos vencedores registrados também possuem
                    um registro preservado na Foundation Collection.
                  </p>
                </div>
              </>
            )}
          </div>
        </ArchivePanel>
      </div>

      <div className="data-room__system-grid">
        <ArchivePanel
          id="data-room-dashboard"
          title="OPEN DASHBOARD"
          code="STREAMLIT"
        >
          <div className="data-room__dashboard-content">
            <span>FULL ANALYTICAL SYSTEM</span>

            <strong>STREAMLIT DASHBOARD</strong>

            <p>
              O front-end apresenta uma prévia analítica.
              O dashboard completo continua separado e oferece
              filtros, tabelas e visualizações mais detalhadas.
            </p>

            <a
              href={STREAMLIT_DASHBOARD_URL}
              target="_blank"
              rel="noreferrer"
              className="data-room__dashboard-button"
            >
              OPEN ANALYTICAL DASHBOARD ↗
            </a>

            <small className="data-room__dashboard-address">
              {STREAMLIT_DASHBOARD_ADDRESS} / separate Streamlit process
            </small>
          </div>
        </ArchivePanel>

        <ArchivePanel
          id="data-room-system"
          title="SYSTEM INFORMATION"
          code="ARCHITECTURE"
        >
          <dl className="data-room__system-information">
            {systemInformation.map((information) => (
              <div key={information.label}>
                <dt>{information.label}</dt>

                <span
                  className="data-room__system-dots"
                  aria-hidden="true"
                />

                <dd
                  className={
                    information.stable
                      ? 'data-room__system-value data-room__system-value--stable'
                      : 'data-room__system-value'
                  }
                >
                  {information.value}
                </dd>
              </div>
            ))}
          </dl>
        </ArchivePanel>
      </div>

      <footer className="archive-quote">
        <span>
          “Memory becomes measurable when the archive stays
          long enough.”
        </span>

        <span>— The Archivist</span>
      </footer>
    </ArchiveShell>
  )
}

export default DataRoomPage