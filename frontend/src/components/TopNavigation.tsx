/*
===========================================================
The AAA Archive
Arquivo: TopNavigation.tsx

Objetivo:
Representar a navegação superior da aplicação e exibir
informações globais sobre o estado do arquivo.

Nesta fase, os itens da navegação ainda são somente
elementos visuais. As rotas serão ativadas durante a
implementação das páginas reais.
===========================================================
*/

import SystemClock from './SystemClock'

const navigationItems = [
  {
    label: 'HOME',
    active: true,
  },
  {
    label: 'FOUNDATION',
    active: false,
  },
  {
    label: 'AWARDS',
    active: false,
  },
  {
    label: 'DATA ROOM',
    active: false,
  },
]

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
        {navigationItems.map((item) => (
          <span
            key={item.label}
            className={
              item.active
                ? 'top-navigation__item top-navigation__item--active'
                : 'top-navigation__item'
            }
            aria-current={
              item.active
                ? 'page'
                : undefined
            }
          >
            {item.label}
          </span>
        ))}
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