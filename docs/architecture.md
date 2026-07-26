# Arquitetura

## Fluxo principal

```text
data/games.csv + data/awards.csv
                ↓
scripts/import_to_postgres.py
                ↓
          PostgreSQL
          ↙        ↘
      FastAPI     Streamlit
         ↓
        JSON
         ↓
   React + Fetch API
```

Os CSVs funcionam como fonte editorial. O banco é a fonte operacional.

## Stack

### Frontend

- React;
- Vite;
- TypeScript;
- React Router;
- CSS personalizado;
- Fetch API.

### Backend e dados

- Python;
- FastAPI;
- Pandas;
- PostgreSQL;
- psycopg;
- python-dotenv.

### Dashboard

- Streamlit;
- Pandas;
- PostgreSQL.

### Testes e qualidade

- pytest;
- FastAPI TestClient;
- TypeScript build;
- Oxlint.

## Responsabilidades

| Camada | Responsabilidade |
| --- | --- |
| CSV | edição e preservação editorial dos dados |
| Importador | validar e sincronizar os CSVs com o PostgreSQL |
| PostgreSQL | armazenar os dados usados em produção |
| `scripts/database.py` | centralizar conexão e consultas ao banco |
| módulos de `scripts/` | pesquisa, filtros, estatísticas e comparação de Awards |
| FastAPI | expor os dados em JSON |
| React | experiência principal do usuário |
| Streamlit | exploração analítica completa |

O React nunca acessa diretamente os CSVs, o PostgreSQL ou módulos Python.

## Estrutura principal

```text
The-AAA-Archive/
├── api/                 FastAPI e testes da API
├── dashboard/           aplicação Streamlit
├── data/                CSVs editoriais
├── database/            schema SQL
├── docs/                documentação final
├── frontend/            aplicação React/Vite
├── scripts/             lógica, banco, importação e testes
├── .env.example
├── README.md
└── requirements.txt
```

## Comunicação entre serviços

### Frontend → API

O arquivo `frontend/src/services/api.ts` centraliza as requisições HTTP.

A URL é definida por:

```env
VITE_API_URL=https://endereco-da-api
```

Sem a variável, o fallback local é `http://127.0.0.1:8000`.

### Frontend → Streamlit

A Data Room abre o dashboard externo usando:

```env
VITE_STREAMLIT_URL=https://endereco-do-dashboard
```

Sem a variável, o fallback local é `http://localhost:8501`.

### Python → PostgreSQL

A API, o dashboard, os testes e o importador usam as mesmas variáveis:

```env
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=
POSTGRES_PORT=5432
```

## CORS

A FastAPI autoriza o frontend por meio de:

```env
CORS_ALLOWED_ORIGINS=http://localhost:5173,https://dominio-publico
```

Origens múltiplas são separadas por vírgula e não devem terminar com `/`.
