/*
===========================================================
The AAA Archive
Arquivo: HomePage.tsx

Objetivo:
Representar o hall principal do museu digital.

A Home apresenta:
- introdução ao arquivo;
- estado geral do sistema;
- resumo da evolução dos videogames;
- registros em destaque;
- métricas reais do acervo;
- acessos às áreas principais.

Nesta etapa, o painel Archive Status consulta a FastAPI
para apresentar os valores atuais da Foundation Collection
e da Awards History.
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
  getGames,
  getHomeStats,
} from '../services/api'

import './HomePage.css'


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
}

type ArchiveMetricItem = {
  label: string
  value: string
  stable?: boolean
}


// ==========================================================
// NAVEGAÇÃO CONTEXTUAL
// ==========================================================

const homeSidebarItems: ContextSidebarItem[] = [
  {
    label: 'ARCHIVE OVERVIEW',
    target: '#archive-overview',
  },
  {
    label: 'SYSTEM EVOLUTION',
    target: '#system-evolution',
  },
  {
    label: 'FEATURED RECORDS',
    target: '#featured-records',
  },
  {
    label: 'COLLECTION ACCESS',
    target: '#collection-access',
  },
]


// ==========================================================
// CONTEÚDO EDITORIAL DA HOME
// ==========================================================

const evolutionPeriods = [
  {
    index: 'ERA 01',
    period: '1972—1982',
    title: 'EARLY SYSTEMS / ARCADES',
    summary:
      'O videogame se estabelece primeiro como uma experiência pública e competitiva. Pouco depois, os cartuchos levam essa linguagem para dentro de casa.',
    systems: [
      'Arcades',
      'Atari 2600',
      'Intellivision',
    ],
    technicalShift:
      'Gabinetes dedicados, gráficos formados por poucos elementos, placares persistentes e cartuchos intercambiáveis.',
    experienceShift:
      'Partidas curtas, busca por pontuação e controles fáceis de entender criam uma cultura de repetição e domínio.',
    landmarks: [
      'Pong',
      'Space Invaders',
      'Pac-Man',
      'Donkey Kong',
      'Adventure',
    ],
  },
  {
    index: 'ERA 02',
    period: '1983—1992',
    title: '8 & 16-BIT ERA',
    summary:
      'Depois da crise norte-americana de 1983, consoles japoneses reorganizam o mercado e transformam personagens em símbolos reconhecidos por gerações.',
    systems: [
      'NES',
      'Master System',
      'Mega Drive',
      'Super Nintendo',
    ],
    technicalShift:
      'Sprites mais detalhados, rolagem de tela, trilhas maiores, controles mais precisos e sistemas de salvamento.',
    experienceShift:
      'Campanhas mais longas, mundos conectados e gêneros bem definidos fortalecem séries que continuam ativas décadas depois.',
    landmarks: [
      'Super Mario Bros.',
      'The Legend of Zelda',
      'Metroid',
      'Sonic the Hedgehog',
      'Street Fighter II',
      'Donkey Kong Country',
    ],
  },
  {
    index: 'ERA 03',
    period: '1993—1998',
    title: '3D TRANSITION',
    summary:
      'Polígonos, CDs e controles analógicos alteram a maneira de construir espaços. A câmera se torna parte da linguagem e do desafio.',
    systems: [
      'PlayStation',
      'Nintendo 64',
      'Sega Saturn',
    ],
    technicalShift:
      'Ambientes tridimensionais, mídia em CD, cenas pré-renderizadas, vozes gravadas e novas soluções de câmera.',
    experienceShift:
      'Exploração em 3D, narrativa cinematográfica, terror de sobrevivência e mundos mais abertos redefinem expectativas.',
    landmarks: [
      'Super Mario 64',
      'Final Fantasy VII',
      'Metal Gear Solid',
      'Resident Evil',
      'Crash Bandicoot',
      'Ocarina of Time',
    ],
  },
  {
    index: 'ERA 04',
    period: '1999—2006',
    title: 'SIXTH GENERATION',
    summary:
      'O aumento de memória e processamento aproxima os jogos do cinema sem abandonar a experimentação. Cidades, conflitos e personagens ganham nova escala.',
    systems: [
      'Dreamcast',
      'PlayStation 2',
      'GameCube',
      'Xbox',
    ],
    technicalShift:
      'Modelos mais detalhados, mídia em DVD, iluminação mais complexa, mundos contínuos e infraestrutura online inicial.',
    experienceShift:
      'Sandboxes, ação cinematográfica e narrativas mais maduras consolidam o jogo como grande produção cultural.',
    landmarks: [
      'Grand Theft Auto III',
      'Halo',
      'Silent Hill 2',
      'Resident Evil 4',
      'Shadow of the Colossus',
      'Metal Gear Solid 3',
    ],
  },
  {
    index: 'ERA 05',
    period: '2007—2013',
    title: 'HD ERA',
    summary:
      'A alta definição amplia detalhes, atuação e escala. Ao mesmo tempo, serviços digitais passam a conectar jogos, jogadores e atualizações constantes.',
    systems: [
      'Xbox 360',
      'PlayStation 3',
      'Nintendo Wii',
    ],
    technicalShift:
      'Resolução HD, física avançada, captura de movimento, controles por movimento e distribuição digital.',
    experienceShift:
      'Escolhas narrativas, grandes mundos abertos e experiências cinematográficas passam a ocupar o centro das produções AAA.',
    landmarks: [
      'BioShock',
      'Mass Effect 2',
      'The Elder Scrolls V: Skyrim',
      'Dark Souls',
      'Red Dead Redemption',
      'The Last of Us',
    ],
  },
  {
    index: 'ERA 06',
    period: '2014—PRESENT',
    title: 'MODERN SYSTEMS',
    summary:
      'A geração atual combina alta fidelidade, mundos sistêmicos e diferentes formas de acesso. Tecnologia e direção artística passam a dividir o mesmo protagonismo.',
    systems: [
      'PlayStation 4 / 5',
      'Xbox One / Series',
      'Nintendo Switch',
    ],
    technicalShift:
      'SSDs, iluminação em tempo real, captura facial, áudio espacial, maior densidade de cenários e tempos de carregamento menores.',
    experienceShift:
      'Mundos mais reativos, experiências híbridas e maior atenção à acessibilidade ampliam como e onde os jogos podem ser vividos.',
    landmarks: [
      'The Witcher 3',
      'Bloodborne',
      'Breath of the Wild',
      'Red Dead Redemption 2',
      'Elden Ring',
      'Baldur’s Gate 3',
    ],
  },
]

/*
Os Featured Records são uma curadoria fixa da Home.

Cada item corresponde a um registro que já existe na
Foundation Collection. O ID abre a página individual do
jogo pela rota /games/:id.
*/

const featuredRecords = [
  {
    id: 1,
    year: '1997',
    title: 'FINAL FANTASY VII',
    developer: 'Square Enix',
    genre: 'RPG',
    description:
      'Escala cinematográfica e identidade visual levaram o RPG japonês a um público ainda maior.',
    code: 'REC-001',
    image: '/assets/games/1/featured.webp',
  },
  {
    id: 3,
    year: '1998',
    title: 'METAL GEAR SOLID',
    developer: 'Konami',
    genre: 'Stealth',
    description:
      'Infiltração, direção cinematográfica e tensão política transformadas em linguagem interativa.',
    code: 'REC-003',
    image: '/assets/games/3/featured.webp',
  },
  {
    id: 14,
    year: '2005',
    title: 'RESIDENT EVIL 4',
    developer: 'Capcom',
    genre: 'Survival Horror',
    description:
      'Uma nova câmera e um novo ritmo que redefiniram a ação em terceira pessoa.',
    code: 'REC-014',
    image: '/assets/games/14/featured.webp',
  },
  {
    id: 41,
    year: '2013',
    title: 'THE LAST OF US',
    developer: 'Naughty Dog',
    genre: 'Action-Adventure',
    description:
      'Intimidade, violência e sobrevivência tratadas com maturidade dentro de uma grande produção.',
    code: 'REC-041',
    image: '/assets/games/41/featured.webp',
  },
]

const directAccessItems = [
  {
    title: 'ENTER FOUNDATION',
    description: 'Explore os registros fundamentais.',
    status: 'MODULE ONLINE',
    path: '/foundation',
  },
  {
    title: 'OPEN AWARDS LOG',
    description: 'Veja os vencedores e indicados.',
    status: 'MODULE ONLINE',
    path: '/awards',
  },
  {
    title: 'ENTER DATA ROOM',
    description: 'Acesse as bases de pesquisa.',
    status: 'MODULE ONLINE',
    path: '/data-room',
  },
]


// ==========================================================
// FUNÇÃO AUXILIAR PARA O PERÍODO DO ARQUIVO
// ==========================================================

/*
Recebe todos os anos válidos da Foundation Collection e
transforma a lista em um período legível.

Exemplo:

[1993, 1998, 2025]
↓
1993—2025
*/

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
// ESTADO VISUAL DAS MÉTRICAS
// ==========================================================

/*
Esta função converte o estado da requisição nos quatro itens
exibidos pelo painel Archive Status.

Assim, o painel consegue representar:
- carregamento;
- dados carregados;
- base vazia;
- API indisponível.
*/

function createArchiveMetricItems(
  requestState: MetricsRequestState,
  metrics: ArchiveMetrics | null,
): ArchiveMetricItem[] {
  if (requestState === 'loading') {
    return [
      {
        label: 'Foundation Records',
        value: '...',
      },
      {
        label: 'Awards Logs',
        value: '...',
      },
      {
        label: 'Archive Period',
        value: '...',
      },
      {
        label: 'Node Status',
        value: 'Synchronizing',
      },
    ]
  }

  if (requestState === 'empty') {
    return [
      {
        label: 'Foundation Records',
        value: '0',
      },
      {
        label: 'Awards Logs',
        value: '0',
      },
      {
        label: 'Archive Period',
        value: 'NO DATA',
      },
      {
        label: 'Node Status',
        value: 'No Data',
      },
    ]
  }

  if (requestState === 'error' || metrics === null) {
    return [
      {
        label: 'Foundation Records',
        value: 'Unavailable',
      },
      {
        label: 'Awards Logs',
        value: 'Unavailable',
      },
      {
        label: 'Archive Period',
        value: 'Unavailable',
      },
      {
        label: 'Node Status',
        value: 'Offline',
      },
    ]
  }

  return [
    {
      label: 'Foundation Records',
      value: String(metrics.foundationRecords),
    },
    {
      label: 'Awards Logs',
      value: String(metrics.awardsLogs),
    },
    {
      label: 'Archive Period',
      value: metrics.archivePeriod,
    },
    {
      label: 'Node Status',
      value: 'Stable',
      stable: true,
    },
  ]
}


// ==========================================================
// COMPONENTE PRINCIPAL
// ==========================================================

function HomePage() {
  const [metrics, setMetrics] =
    useState<ArchiveMetrics | null>(null)

  const [requestState, setRequestState] =
    useState<MetricsRequestState>('loading')


  // ========================================================
  // CARREGAMENTO DAS MÉTRICAS REAIS
  // ========================================================

  useEffect(() => {
    let pageIsActive = true

    async function loadArchiveMetrics() {
      try {
        const [
          statistics,
          games,
          awards,
        ] = await Promise.all([
          getHomeStats(),
          getGames(),
          getAwards(),
        ])

        if (!pageIsActive) {
          return
        }

        if (
          statistics.total_jogos === 0
          && awards.length === 0
        ) {
          setMetrics(null)
          setRequestState('empty')
          return
        }

        const gameYears = games
          .map((game) => game.ano_lancamento)
          .filter((year): year is number => (
            year !== null
          ))

        setMetrics({
          foundationRecords: statistics.total_jogos,
          awardsLogs: awards.length,
          archivePeriod: formatPeriod(gameYears),
        })

        setRequestState('success')
      } catch {
        if (pageIsActive) {
          setMetrics(null)
          setRequestState('error')
        }
      }
    }

    loadArchiveMetrics()

    return () => {
      pageIsActive = false
    }
  }, [])

  const archiveMetrics = createArchiveMetricItems(
    requestState,
    metrics,
  )

  const terminalNodeStatus = (
    requestState === 'success'
      ? 'ACTIVE'
      : requestState === 'loading'
        ? 'SYNCING'
        : requestState === 'empty'
          ? 'NO DATA'
          : 'OFFLINE'
  )

  const terminalRecords = (
    metrics
      ? String(metrics.foundationRecords).padStart(2, '0')
      : '--'
  )

  const terminalPeriod = (
    metrics?.archivePeriod
    ?? '----—----'
  )

  return (
    <ArchiveShell
      sidebarTitle="MAIN TERMINAL"
      sidebarItems={homeSidebarItems}
      activeSidebarItem="ARCHIVE OVERVIEW"
    >
      <section
        id="archive-overview"
        className="archive-panel home-hero"
      >
        <div className="home-hero__content">
          <p className="archive-eyebrow">
            // WELCOME
          </p>

          <h1>THE AAA ARCHIVE</h1>

          <p className="home-hero__description">
            Preservamos o que o tempo esquece.
            <br />
            Fragmentos de código, arte e som —
            <br />
            memórias de mundos antes jogados.
            <br />
            É aqui que eles continuam.
          </p>

          <p className="archive-system-message">
            &gt; archive integrity:
            <span>stable</span>
          </p>
        </div>

        <div
          className="home-hero__visual"
          aria-label="Terminal principal do arquivo em funcionamento"
        >
          <div className="home-hero__terminal">
            <div className="home-hero__terminal-topline">
              <span>THE AAA ARCHIVE // PRESERVATION SYSTEM</span>
              <span>NODE 01</span>
            </div>

            <div className="home-hero__terminal-grid">
              <div className="home-hero__terminal-main">
                <p>VISITOR SESSION ESTABLISHED</p>

                <strong>
                  ARCHIVE ACCESS
                  <br />
                  GRANTED
                </strong>

                <span
                  className="home-hero__terminal-cursor"
                  aria-hidden="true"
                >
                  █
                </span>
              </div>

              <dl className="home-hero__terminal-data">
                <div>
                  <dt>NODE STATUS</dt>
                  <dd>{terminalNodeStatus}</dd>
                </div>

                <div>
                  <dt>RECORDS</dt>
                  <dd>{terminalRecords}</dd>
                </div>

                <div>
                  <dt>PERIOD</dt>
                  <dd>{terminalPeriod}</dd>
                </div>

                <div>
                  <dt>ACCESS</dt>
                  <dd>VISITOR</dd>
                </div>
              </dl>
            </div>

            <div
              className="home-hero__terminal-log"
              aria-hidden="true"
            >
              <span>&gt; signal recovered</span>
              <span>&gt; database mounted</span>
              <span>&gt; historical records indexed</span>
              <span>&gt; waiting for input_</span>
            </div>

            <div className="home-hero__terminal-footer">
              <span>AAA-PRESERVATION-NODE</span>
              <span>[ {terminalNodeStatus} ]</span>
            </div>
          </div>
        </div>
      </section>

      <ArchivePanel
        id="system-evolution"
        title="SYSTEM EVOLUTION"
        code="ARCHIVE TIMELINE"
        className="home-evolution"
      >
        <div className="home-evolution__intro">
          <p>
            Seis eras mostram como tecnologia, design e hábitos
            transformaram a maneira de jogar.
          </p>

          <span>
            Os títulos citados são marcos históricos da era.
            A presença nesta linha do tempo não confirma inclusão
            na Foundation Collection.
          </span>
        </div>

        <div className="home-timeline">
          {evolutionPeriods.map((period) => (
            <article
              key={period.period}
              className="home-timeline__item"
            >
              <p className="home-timeline__period">
                {period.period}
              </p>

              <div className="home-timeline__marker">
                <span aria-hidden="true" />
              </div>

              <div className="home-timeline__content">
                <header className="home-timeline__header">
                  <div>
                    <span className="home-timeline__index">
                      {period.index}
                    </span>

                    <h3>{period.title}</h3>
                  </div>

                  <span className="home-timeline__context-label">
                    HISTORICAL CONTEXT
                  </span>
                </header>

                <p className="home-timeline__summary">
                  {period.summary}
                </p>

                <div className="home-timeline__systems">
                  <span>PRIMARY SYSTEMS</span>

                  <p>{period.systems.join(' / ')}</p>
                </div>

                <div className="home-timeline__shifts">
                  <div className="home-timeline__detail">
                    <span>TECHNICAL SHIFT</span>

                    <p>{period.technicalShift}</p>
                  </div>

                  <div className="home-timeline__detail">
                    <span>PLAYER EXPERIENCE</span>

                    <p>{period.experienceShift}</p>
                  </div>
                </div>

                <div className="home-timeline__landmarks">
                  <span>ERA LANDMARKS</span>

                  <ul>
                    {period.landmarks.map((landmark) => (
                      <li key={landmark}>
                        {landmark}
                      </li>
                    ))}
                  </ul>
                </div>
              </div>
            </article>
          ))}
        </div>
      </ArchivePanel>

      <div className="home-information-grid">
        <ArchivePanel
          id="featured-records"
          title="FEATURED RECORDS"
          code="04 RECORDS"
          className="home-featured"
        >
          <div className="home-featured__list">
            {featuredRecords.map((record) => (
              <Link
                key={record.id}
                to={`/games/${record.id}`}
                className="home-featured__record"
                aria-label={`Open Foundation record: ${record.title}`}
              >
                <div className="home-featured__image">
                  <img
                    src={record.image}
                    alt=""
                    loading="lazy"
                    decoding="async"
                  />

                  <span>{record.code}</span>
                </div>

                <div className="home-featured__content">
                  <div className="home-featured__heading">
                    <h3>{record.title}</h3>

                    <span>[{record.year}]</span>
                  </div>

                  <p className="home-featured__metadata">
                    {record.developer}
                    <span>{record.genre}</span>
                  </p>

                  <p className="home-featured__description">
                    {record.description}
                  </p>
                </div>
              </Link>
            ))}
          </div>
        </ArchivePanel>

        <div className="home-side-panels">
          <ArchivePanel
            title="ARCHIVE STATUS"
            code="LIVE"
            className="home-status"
          >
            <dl
              className="home-status__list"
              aria-live="polite"
            >
              {archiveMetrics.map((metric) => (
                <div
                  key={metric.label}
                  className="home-status__item"
                >
                  <dt>{metric.label}</dt>

                  <span
                    className="home-status__dots"
                    aria-hidden="true"
                  />

                  <dd
                    className={
                      metric.stable
                        ? 'home-status__value home-status__value--stable'
                        : 'home-status__value'
                    }
                  >
                    {metric.value}
                  </dd>
                </div>
              ))}
            </dl>
          </ArchivePanel>

          <ArchivePanel
            id="collection-access"
            title="DIRECT ACCESS"
            code="03 MODULES"
            className="home-access"
          >
            <div className="home-access__list">
              {directAccessItems.map((item) => (
                <Link
                  key={item.title}
                  to={item.path}
                  className="home-access__item"
                >
                  <span className="home-access__symbol">
                    □
                  </span>

                  <span className="home-access__content">
                    <strong>{item.title}</strong>
                    <small>{item.description}</small>
                  </span>

                  <span className="home-access__status">
                    {item.status}
                  </span>
                </Link>
              ))}
            </div>
          </ArchivePanel>
        </div>
      </div>

      <footer className="archive-quote">
        <span>
          “The past is not gone. It is archived.”
        </span>

        <span>— The Archivist</span>
      </footer>
    </ArchiveShell>
  )
}

export default HomePage