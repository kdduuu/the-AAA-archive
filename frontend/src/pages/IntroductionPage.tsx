/*
===========================================================
The AAA Archive
Arquivo: IntroductionPage.tsx

Objetivo:
Representar a porta de entrada do arquivo.

A página apresenta:
- identificação do sistema;
- sequência progressiva de inicialização;
- confirmação de acesso;
- opção para pular a sequência;
- botão para desbloquear o arquivo.

A Introdução não depende da API.
===========================================================
*/

import {
  useEffect,
  useState,
} from 'react'
import { useNavigate } from 'react-router'

import './IntroductionPage.css'

const ACCESS_STORAGE_KEY =
  'the-aaa-archive-access-granted'

const systemMessages = [
  'signal detected',
  'restoring archive node',
  'database integrity verified',
  'foundation records: 66',
  'awards logs: 127',
  'access level: visitor',
]

function IntroductionPage() {
  const navigate = useNavigate()

  const [
    visibleMessageCount,
    setVisibleMessageCount,
  ] = useState(0)

  const sequenceCompleted =
    visibleMessageCount >= systemMessages.length

  useEffect(() => {
    const accessAlreadyGranted =
      window.sessionStorage.getItem(
        ACCESS_STORAGE_KEY,
      )

    if (accessAlreadyGranted === 'true') {
      navigate('/home', {
        replace: true,
      })

      return
    }

    const sequenceInterval =
      window.setInterval(() => {
        setVisibleMessageCount(
          (currentMessageCount) => {
            const nextMessageCount =
              currentMessageCount + 1

            if (
              nextMessageCount >=
              systemMessages.length
            ) {
              window.clearInterval(
                sequenceInterval,
              )
            }

            return Math.min(
              nextMessageCount,
              systemMessages.length,
            )
          },
        )
      }, 430)

    return () => {
      window.clearInterval(sequenceInterval)
    }
  }, [navigate])

  function handleSkipSequence() {
    setVisibleMessageCount(
      systemMessages.length,
    )
  }

  function handleUnlockArchive() {
    window.sessionStorage.setItem(
      ACCESS_STORAGE_KEY,
      'true',
    )

    navigate('/home')
  }

  return (
    <main className="introduction-page">
      <button
        type="button"
        className="introduction-skip"
        onClick={handleSkipSequence}
        disabled={sequenceCompleted}
      >
        {sequenceCompleted
          ? 'SEQUENCE COMPLETE'
          : 'SKIP SEQUENCE'}
      </button>

      <section
        className="introduction-panel"
        aria-labelledby="archive-introduction-title"
      >
        <header className="introduction-header">
          <p className="introduction-node">
            ARCHIVE NODE 01
          </p>

          <h1 id="archive-introduction-title">
            THE AAA ARCHIVE
          </h1>

          <p className="introduction-subtitle">
            digital preservation system
          </p>
        </header>

        <div
          className="introduction-terminal"
          aria-live="polite"
        >
          {systemMessages.map(
            (message, index) => {
              const messageIsVisible =
                index < visibleMessageCount

              return (
                <div
                  key={message}
                  className={
                    messageIsVisible
                      ? 'introduction-terminal__line introduction-terminal__line--visible'
                      : 'introduction-terminal__line'
                  }
                  aria-hidden={
                    !messageIsVisible
                  }
                >
                  <span className="introduction-terminal__message">
                    <span aria-hidden="true">
                      &gt;
                    </span>

                    {message}
                  </span>

                  <span className="introduction-terminal__status">
                    [OK]
                  </span>
                </div>
              )
            },
          )}
        </div>

        <div
          className={
            sequenceCompleted
              ? 'introduction-access introduction-access--visible'
              : 'introduction-access'
          }
          aria-hidden={!sequenceCompleted}
        >
          <p className="introduction-access__label">
            ACCESS GRANTED
          </p>

          <button
            type="button"
            className="introduction-unlock"
            onClick={handleUnlockArchive}
            tabIndex={
              sequenceCompleted
                ? 0
                : -1
            }
          >
            <svg
              className="introduction-unlock__icon"
              viewBox="0 0 24 24"
              aria-hidden="true"
            >
              <path
                d="M7 10V7a5 5 0 0 1 10 0v3"
                fill="none"
                stroke="currentColor"
                strokeWidth="1.4"
              />

              <rect
                x="5"
                y="10"
                width="14"
                height="11"
                rx="1"
                fill="none"
                stroke="currentColor"
                strokeWidth="1.4"
              />

              <path
                d="M12 14v3"
                fill="none"
                stroke="currentColor"
                strokeWidth="1.4"
              />
            </svg>

            <span>
              UNLOCK ARCHIVE
            </span>

            <svg
              className="introduction-unlock__arrow"
              viewBox="0 0 24 24"
              aria-hidden="true"
            >
              <path
                d="M5 12h13M14 7l5 5-5 5"
                fill="none"
                stroke="currentColor"
                strokeWidth="1.4"
              />
            </svg>
          </button>
        </div>

        <footer className="introduction-footer">
          <span>
            the past is not gone. it is archived.
          </span>

          <span className="introduction-footer__status">
            node stable
          </span>
        </footer>
      </section>
    </main>
  )
}

export default IntroductionPage