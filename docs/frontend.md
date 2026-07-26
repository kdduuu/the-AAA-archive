# Frontend

## Objetivo

O frontend é a experiência principal do The AAA Archive. Ele apresenta os dados da API dentro da linguagem visual de museu digital e arquivo tecnológico.

## Estrutura

```text
frontend/src/
├── components/     componentes compartilhados
├── pages/          páginas das rotas
├── services/       comunicação com a API
├── types/          tipos TypeScript
├── App.tsx         rotas
├── App.css         shell e navegação globais
└── index.css       tokens e base visual
```

## Rotas

| Rota | Página |
| --- | --- |
| `/` | `IntroductionPage` |
| `/home` | `HomePage` |
| `/foundation` | `FoundationPage` |
| `/games/:id` | `GamePage` |
| `/awards` | `AwardsPage` |
| `/data-room` | `DataRoomPage` |

O `frontend/vercel.json` reescreve rotas para `index.html`, permitindo recarregar URLs internas sem erro 404 na Vercel.

## Componentes globais

- `ArchiveShell`: estrutura geral da interface;
- `TopNavigation`: navegação entre Home, Foundation, Awards e Data Room;
- `ContextSidebar`: navegação interna de cada página;
- `ArchivePanel`: painéis reutilizáveis;
- `GameCard`: card dos registros da Foundation;
- `SystemClock`: relógio do sistema.

A navegação principal permanece visível no desktop e foi adaptada para o celular.

## Páginas

### Introduction

Entrada narrativa do arquivo. Apresenta o sistema e encaminha o visitante para a Home.

### Home

Contém:

- hero principal;
- métricas reais da API;
- System Evolution;
- Featured Records;
- Direct Access;
- links para as páginas individuais.

Featured Records:

- Final Fantasy VII — `/games/1`;
- Metal Gear Solid — `/games/3`;
- Resident Evil 4 — `/games/14`;
- The Last of Us — `/games/41`.

### Foundation Collection

Carrega os 105 jogos por `GET /games` e oferece:

- busca textual;
- filtros por década, ano, gênero, desenvolvedora e franquia;
- ordenação;
- navegação para `/games/:id`;
- ranking pessoal;
- estados `loading`, `success`, `empty` e `error`.

### GamePage

Consulta `GET /games/{id}` e apresenta:

- título, ano, gênero, desenvolvedora e franquia;
- descrição editorial;
- Metacritic e notas pessoais quando disponíveis;
- flags históricas;
- `cover.webp`;
- fallback de imagem;
- estados `loading`, `not found` e `error`.

IDs inválidos ou inexistentes exibem `RECORD NOT FOUND` sem quebrar a aplicação.

### Awards History

Apresenta:

- índice de anos;
- vencedor e indicados de cada edição;
- premiação correspondente;
- confirmação de presença do vencedor na Foundation;
- contexto sobre a base de Awards.

### Data Room

Combina dados de:

- `/stats/home`;
- `/games`;
- `/awards`;
- `/awards/foundation/winners`.

Exibe métricas, distribuição por década e gênero, principais desenvolvedoras e presença dos vencedores na Foundation. O botão `OPEN DASHBOARD` abre a aplicação Streamlit.

## Comunicação com a API

Todas as requisições estão centralizadas em:

```text
frontend/src/services/api.ts
```

Variável de ambiente:

```env
VITE_API_URL=http://127.0.0.1:8000
```

## Dashboard externo

Variável de ambiente:

```env
VITE_STREAMLIT_URL=http://localhost:8501
```

Em produção, a Vercel usa os endereços públicos.

## Comandos

Dentro de `frontend/`:

```powershell
npm install
npm run dev
npm run lint
npm run build
npm run preview
```

Antes de enviar alterações, `npm run lint` e `npm run build` devem passar.
