/*
===========================================================
The AAA Archive
Arquivo: TopNavigation.tsx

Objetivo:
Representar a navegação superior da aplicação e exibir
informações globais sobre o estado do arquivo.

Nesta etapa:
- HOME navega para /home;
- FOUNDATION navega para /foundation;
- AWARDS navega para /awards;
- o item correspondente à rota atual é marcado como ativo;
- DATA ROOM permanece bloqueado porque sua página ainda não
  foi implementada.
===========================================================
*/

import { NavLink } from 'react-router'

import SystemClock from './SystemClock'


// ==========================================================
// ITENS DA NAVEGAÇÃO
// ==========================================================

/*
Cada item possui:

label
→ texto exibido na interface;

path
→ endereço da página;

available
→ informa se a rota já pode ser acessada.
*/

const navigationItems = [
  {
    label: 'HOME',
    path: '/home',
    available: true,
  },
  {
    label: 'FOUNDATION',
    path: '/foundation',
    available: true,
  },
  {
    label: 'AWARDS',
    path: '/awards',
    available: true,
  },
  {
    label: 'DATA ROOM',
    path: '/data-room',
    available: false,
  },
]


// ==========================================================
// COMPONENTE PRINCIPAL
// ==========================================================

function TopNavigation() {
  return (
    <header className="top-navigation">
      <span className="top-navigation__mobile-brand">
        THE AAA ARCHIVE
      </span>

      <nav
        className="top-navigation__links"
        aria-label="Navegação principal"
      >
        {navigationItems.map((item) => {
          /*
          Enquanto a página ainda não existe, mostramos
          somente um elemento visual sem navegação.
          */

          if (!item.available) {
            return (
              <span
                key={item.label}
                className="top-navigation__item"
                aria-disabled="true"
                title="Página ainda não implementada"
              >
                {item.label}
              </span>
            )
          }

          /*
          NavLink conhece a rota atual.

          Quando o endereço do item corresponde à página
          aberta, isActive será verdadeiro e a classe
          visual de item ativo será adicionada.
          */

          return (
            <NavLink
              key={item.label}
              to={item.path}
              end
              className={({ isActive }) => (
                isActive
                  ? 'top-navigation__item top-navigation__item--active'
                  : 'top-navigation__item'
              )}
            >
              {item.label}
            </NavLink>
          )
        })}
      </nav>

      <div
        className="system-status"
        aria-label="Estado atual do sistema"
      >
        <span className="system-status__line">
          SYSTEM TIME

          <strong>
            <SystemClock />
          </strong>
        </span>

        <span className="system-status__line">
          ARCHIVE NODE ONLINE

          <span
            className="system-status__indicator"
            aria-hidden="true"
          />
        </span>
      </div>
    </header>
  )
}

export default TopNavigation