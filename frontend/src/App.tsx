/*
===========================================================
The AAA Archive
Arquivo: App.tsx

Objetivo:
Definir as rotas atualmente disponíveis na aplicação.

Rotas atuais:
- /             → Introdução oficial;
- /home         → Home oficial;
- /foundation   → Foundation Collection;
- /games/:id    → página individual de um jogo;
- /awards       → estrutura inicial da Awards History.
===========================================================
*/

import {
  Route,
  Routes,
} from 'react-router'

import AwardsPage from './pages/AwardsPage'
import FoundationPage from './pages/FoundationPage'
import GamePage from './pages/GamePage'
import HomePage from './pages/HomePage'
import IntroductionPage from './pages/IntroductionPage'

import './App.css'


// ==========================================================
// COMPONENTE PRINCIPAL
// ==========================================================

function App() {
  return (
    <Routes>
      <Route
        path="/"
        element={<IntroductionPage />}
      />

      <Route
        path="/home"
        element={<HomePage />}
      />

      <Route
        path="/foundation"
        element={<FoundationPage />}
      />

      <Route
        path="/games/:id"
        element={<GamePage />}
      />

      <Route
        path="/awards"
        element={<AwardsPage />}
      />
    </Routes>
  )
}

export default App