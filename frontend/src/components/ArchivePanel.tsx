/*
===========================================================
The AAA Archive
Arquivo: ArchivePanel.tsx

Objetivo:
Representar um painel visual reutilizável da aplicação.

O componente centraliza a estrutura comum dos painéis:
- borda externa;
- cabeçalho;
- título;
- código opcional;
- conteúdo interno.

Ele será utilizado apenas quando o mesmo formato aparecer
em diferentes áreas ou páginas.
===========================================================
*/

import type { ReactNode } from 'react'

interface ArchivePanelProps {
  id?: string
  title: string
  code?: string
  className?: string
  children: ReactNode
}

function ArchivePanel({
  id,
  title,
  code,
  className = '',
  children,
}: ArchivePanelProps) {
  const panelClassName = [
    'archive-panel',
    className,
  ]
    .filter(Boolean)
    .join(' ')

  return (
    <section
      id={id}
      className={panelClassName}
    >
      <header className="archive-panel__header">
        <h2>{title}</h2>

        {code ? <span>{code}</span> : null}
      </header>

      {children}
    </section>
  )
}

export default ArchivePanel