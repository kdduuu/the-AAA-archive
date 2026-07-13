/*
===========================================================
The AAA Archive
Arquivo: SystemClock.tsx

Objetivo:
Exibir o horário atual no painel de status do sistema.

O relógio é atualizado uma vez por segundo e representa
o primeiro comportamento dinâmico simples da interface.
===========================================================
*/

import {
  useEffect,
  useState,
} from 'react'

function formatSystemTime(date: Date) {
  return new Intl.DateTimeFormat(
    'en-US',
    {
      hour: '2-digit',
      minute: '2-digit',
      second: '2-digit',
      hour12: true,
    },
  ).format(date)
}

function SystemClock() {
  const [currentTime, setCurrentTime] = useState(
    new Date(),
  )

  useEffect(() => {
    const clockInterval = window.setInterval(() => {
      setCurrentTime(new Date())
    }, 1000)

    return () => {
      window.clearInterval(clockInterval)
    }
  }, [])

  return (
    <time dateTime={currentTime.toISOString()}>
      {formatSystemTime(currentTime)}
    </time>
  )
}

export default SystemClock