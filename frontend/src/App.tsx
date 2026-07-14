/*
===========================================================
The AAA Archive
Arquivo: App.tsx

Objetivo:
Definir as rotas atualmente disponíveis na aplicação.

Rotas desta etapa:
- /     → Introdução oficial;
- /home → Home oficial.
===========================================================
*/

import {
  Route,
  Routes,
} from 'react-router'

import HomePage from './pages/HomePage'
import IntroductionPage from './pages/IntroductionPage'

import './App.css'

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
    </Routes>
  )
}

export default App