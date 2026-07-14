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
- métricas do acervo;
- acessos às áreas principais.

Nesta etapa, os dados são estáticos e correspondem aos
números reais já registrados no projeto.
===========================================================
*/

import ArchivePanel from '../components/ArchivePanel'
import ArchiveShell from '../components/ArchiveShell'
import type { ContextSidebarItem } from '../components/ContextSidebar'

import './HomePage.css'

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

const evolutionPeriods = [
  {
    period: '1972—1982',
    title: 'EARLY ARCADES / ATARI',
    description:
      'Os arcades surgem como espaços coletivos e o Atari 2600 leva os videogames para dentro de casa.',
  },
  {
    period: '1983—1992',
    title: '8 & 16-BIT ERA',
    description:
      'NES, Master System, Mega Drive e Super Nintendo consolidam gêneros, personagens e franquias.',
  },
  {
    period: '1993—1998',
    title: '3D TRANSITION',
    description:
      'PlayStation, Nintendo 64 e Sega Saturn transformam mundos, câmeras e narrativas.',
  },
  {
    period: '1999—2006',
    title: 'SIXTH GENERATION',
    description:
      'Dreamcast, PlayStation 2, GameCube e Xbox ampliam o potencial técnico e cinematográfico.',
  },
  {
    period: '2007—2013',
    title: 'HD ERA',
    description:
      'Alta definição, serviços online e novas formas de interação alteram a escala das experiências.',
  },
  {
    period: '2014—PRESENT',
    title: 'MODERN SYSTEMS',
    description:
      'Mundos mais densos, carregamentos rápidos e maior fidelidade aproximam tecnologia e expressão.',
  },
]

const featuredRecords = [
  {
    year: '1996',
    title: 'SUPER MARIO 64',
    developer: 'Nintendo EAD',
    platform: 'Nintendo 64',
    description:
      'Um novo vocabulário para movimento e espaço em 3D.',
    code: 'REC-01',
  },
  {
    year: '1998',
    title: 'METAL GEAR SOLID',
    developer: 'Konami Computer Entertainment Japan',
    platform: 'PlayStation',
    description:
      'Infiltração, linguagem cinematográfica e tensão.',
    code: 'REC-02',
  },
  {
    year: '2001',
    title: 'SILENT HILL 2',
    developer: 'Team Silent',
    platform: 'PlayStation 2',
    description:
      'O terror que deixou de olhar apenas para fora.',
    code: 'REC-03',
  },
  {
    year: '2013',
    title: 'THE LAST OF US',
    developer: 'Naughty Dog',
    platform: 'PlayStation 3',
    description:
      'Humanidade preservada dentro de um mundo em ruínas.',
    code: 'REC-04',
  },
]

const archiveMetrics = [
  {
    label: 'Foundation Records',
    value: '66',
  },
  {
    label: 'Awards Logs',
    value: '127',
  },
  {
    label: 'Archive Period',
    value: '1993—2025',
  },
  {
    label: 'Node Status',
    value: 'Stable',
    stable: true,
  },
]

const directAccessItems = [
  {
    title: 'ENTER FOUNDATION',
    description: 'Explore os registros fundamentais.',
    status: 'MODULE LOCKED',
  },
  {
    title: 'OPEN AWARDS LOG',
    description: 'Veja os vencedores e indicados.',
    status: 'MODULE LOCKED',
  },
  {
    title: 'ENTER DATA ROOM',
    description: 'Acesse as bases de pesquisa.',
    status: 'MODULE LOCKED',
  },
]

function HomePage() {
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
          aria-label="Representação do hall do arquivo"
        >
          <div
            className="home-hero__visual-grid"
            aria-hidden="true"
          />

          <div className="home-hero__visual-content">
            <span>ARCHIVE HALL FEED</span>

            <strong>NODE 01</strong>

            <small>
              atmospheric image awaiting local asset
            </small>
          </div>
        </div>
      </section>

      <ArchivePanel
        id="system-evolution"
        title="SYSTEM EVOLUTION"
        code="ARCHIVE TIMELINE"
        className="home-evolution"
      >
        <div className="home-timeline">
          {evolutionPeriods.map((period) => (
            <article
              key={period.period}
              className="home-timeline__item"
            >
              <div className="home-timeline__marker">
                <span aria-hidden="true" />
              </div>

              <p className="home-timeline__period">
                {period.period}
              </p>

              <div className="home-timeline__content">
                <h3>{period.title}</h3>

                <p>{period.description}</p>
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
              <article
                key={record.code}
                className="home-featured__record"
              >
                <div
                  className="home-featured__image"
                  aria-hidden="true"
                >
                  <span>{record.code}</span>
                </div>

                <div className="home-featured__content">
                  <div className="home-featured__heading">
                    <h3>{record.title}</h3>

                    <span>[{record.year}]</span>
                  </div>

                  <p className="home-featured__metadata">
                    {record.developer}
                    <span>{record.platform}</span>
                  </p>

                  <p className="home-featured__description">
                    {record.description}
                  </p>
                </div>
              </article>
            ))}
          </div>
        </ArchivePanel>

        <div className="home-side-panels">
          <ArchivePanel
            title="ARCHIVE STATUS"
            code="LIVE"
            className="home-status"
          >
            <dl className="home-status__list">
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
                <button
                  key={item.title}
                  type="button"
                  className="home-access__item"
                  disabled
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
                </button>
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