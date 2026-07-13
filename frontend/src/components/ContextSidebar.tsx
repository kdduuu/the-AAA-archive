/*
===========================================================
The AAA Archive
Arquivo: ContextSidebar.tsx

Objetivo:
Representar a navegação contextual da página atual.

O conteúdo da lateral não é fixo. Cada página poderá
informar:
- o título da seção;
- seus próprios itens;
- qual item está ativo.

Isso permite reutilizar a mesma estrutura na Home,
Foundation, Awards, Data Room e página individual.
===========================================================
*/

export interface ContextSidebarItem {
  label: string
  target: string
}

interface ContextSidebarProps {
  title: string
  items: ContextSidebarItem[]
  activeItem?: string
}

function ContextSidebar({
  title,
  items,
  activeItem,
}: ContextSidebarProps) {
  const currentActiveItem =
    activeItem ?? items[0]?.label

  return (
    <div className="context-sidebar">
      <div className="context-sidebar__content">
        <p className="context-sidebar__title">
          {title}
        </p>

        <nav
          className="context-sidebar__navigation"
          aria-label="Navegação contextual"
        >
          {items.map((item) => {
            const isActive =
              item.label === currentActiveItem

            return (
              <a
                key={item.label}
                className={
                  isActive
                    ? 'context-sidebar__item context-sidebar__item--active'
                    : 'context-sidebar__item'
                }
                href={item.target}
                aria-current={
                  isActive
                    ? 'location'
                    : undefined
                }
              >
                <span
                  className="context-sidebar__marker"
                  aria-hidden="true"
                />

                <span className="context-sidebar__label">
                  {item.label}
                </span>

                <span
                  className="context-sidebar__arrow"
                  aria-hidden="true"
                >
                  ›
                </span>
              </a>
            )
          })}
        </nav>
      </div>

      <footer className="context-sidebar__footer">
        <p>THE AAA ARCHIVE v1.0</p>
        <p>build: development</p>
        <p>node: aaa-archive-01</p>
      </footer>
    </div>
  )
}

export default ContextSidebar