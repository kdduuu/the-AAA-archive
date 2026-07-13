/*
===========================================================
The AAA Archive
Arquivo: App.tsx

Objetivo:
Definir a rota atual e apresentar uma prévia da estrutura
visual global da aplicação.

Esta tela ainda não representa a Home definitiva.
Ela será substituída quando a Fase 3 começar.
===========================================================
*/

import {
  Route,
  Routes,
} from 'react-router'

import ArchivePanel from './components/ArchivePanel'
import ArchiveShell from './components/ArchiveShell'
import type { ContextSidebarItem } from './components/ContextSidebar'

import './App.css'

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

function BaseVisualPreview() {
  return (
    <ArchiveShell
      sidebarTitle="MAIN TERMINAL"
      sidebarItems={homeSidebarItems}
      activeSidebarItem="ARCHIVE OVERVIEW"
    >
      <section
        id="archive-overview"
        className="archive-panel preview-hero"
      >
        <div className="preview-hero__content">
          <p className="archive-eyebrow">
            // BASE VISUAL
          </p>

          <h1>THE AAA ARCHIVE</h1>

          <p className="preview-hero__description">
            A estrutura principal do sistema de
            preservação foi inicializada. As páginas
            e os registros serão adicionados
            progressivamente.
          </p>

          <p className="archive-system-message">
            &gt; visual foundation:
            <span>stable</span>
          </p>
        </div>

        <div
          className="preview-hero__signal"
          aria-hidden="true"
        >
          <span>ARCHIVE NODE</span>
          <strong>01</strong>
          <small>CONNECTED</small>
        </div>
      </section>

      <div className="preview-grid">
        <ArchivePanel
          id="system-evolution"
          title="SYSTEM EVOLUTION"
          code="01"
          className="preview-card"
        >
          <div className="preview-card__content">
            <p>
              Uma introdução à evolução dos
              videogames, consoles e formas de jogar.
            </p>

            <span className="preview-card__status">
              MODULE RESERVED
            </span>
          </div>
        </ArchivePanel>

        <ArchivePanel
          id="featured-records"
          title="FEATURED RECORDS"
          code="02"
          className="preview-card"
        >
          <div className="preview-card__content">
            <p>
              Registros selecionados de diferentes
              períodos da história dos videogames.
            </p>

            <span className="preview-card__status">
              MODULE RESERVED
            </span>
          </div>
        </ArchivePanel>

        <ArchivePanel
          id="collection-access"
          title="COLLECTION ACCESS"
          code="03"
          className="preview-card"
        >
          <div className="preview-card__content">
            <p>
              Acesso futuro à Foundation Collection,
              Awards History e Data Room.
            </p>

            <span className="preview-card__status">
              MODULE RESERVED
            </span>
          </div>
        </ArchivePanel>
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

function App() {
  return (
    <Routes>
      <Route
        path="/"
        element={<BaseVisualPreview />}
      />
    </Routes>
  )
}

export default App