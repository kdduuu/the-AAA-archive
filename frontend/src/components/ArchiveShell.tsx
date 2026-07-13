/*
===========================================================
The AAA Archive
Arquivo: ArchiveShell.tsx

Objetivo:
Definir a estrutura global utilizada pelas páginas internas
do arquivo.

A estrutura contém:
- identificação do projeto;
- navegação superior;
- navegação contextual configurável;
- área principal de conteúdo.
===========================================================
*/

import type { ReactNode } from 'react'

import ContextSidebar from './ContextSidebar'
import type { ContextSidebarItem } from './ContextSidebar'
import TopNavigation from './TopNavigation'

interface ArchiveShellProps {
  children: ReactNode
  sidebarTitle: string
  sidebarItems: ContextSidebarItem[]
  activeSidebarItem?: string
}

function ArchiveShell({
  children,
  sidebarTitle,
  sidebarItems,
  activeSidebarItem,
}: ArchiveShellProps) {
  return (
    <div className="archive-shell">
      <aside className="archive-shell__sidebar">
        <div className="archive-brand">
          THE AAA ARCHIVE
        </div>

        <ContextSidebar
          title={sidebarTitle}
          items={sidebarItems}
          activeItem={activeSidebarItem}
        />
      </aside>

      <div className="archive-shell__workspace">
        <TopNavigation />

        <main className="archive-content">
          {children}
        </main>
      </div>
    </div>
  )
}

export default ArchiveShell