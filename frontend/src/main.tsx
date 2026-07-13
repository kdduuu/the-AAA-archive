/*
===========================================================
The AAA Archive
Arquivo: main.tsx

Objetivo:
Inicializar a aplicação React e disponibilizar o sistema
de rotas por meio do BrowserRouter.
===========================================================
*/

import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter } from 'react-router'

import App from './App'
import './index.css'

const rootElement = document.getElementById('root')

if (!rootElement) {
  throw new Error('Elemento root não encontrado.')
}

createRoot(rootElement).render(
  <StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </StrictMode>,
)