/*
===========================================================
The AAA Archive
Arquivo: App.tsx

Objetivo:
Definir a estrutura inicial de rotas da aplicação.

Nesta fase, existe apenas uma tela temporária para confirmar
que React, TypeScript e React Router estão funcionando.
===========================================================
*/

import { Route, Routes } from 'react-router'

import './App.css'

function PreparationStatus() {
  return (
    <main className="preparation-page">
      <section className="preparation-panel">
        <p className="preparation-label">THE AAA ARCHIVE</p>

        <h1>Frontend initialized</h1>

        <p className="preparation-description">
          React, Vite, TypeScript and React Router are working.
        </p>

        <p className="preparation-status">
          &gt; preparation status: complete
        </p>
      </section>
    </main>
  )
}

function App() {
  return (
    <Routes>
      <Route path="/" element={<PreparationStatus />} />
    </Routes>
  )
}

export default App