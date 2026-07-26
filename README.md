The AAA Archive

The AAA Archive é um museu digital dedicado à memória, à história e à evolução dos videogames.

O projeto apresenta uma coleção curada de jogos considerados relevantes por importância histórica, influência, inovação, reconhecimento crítico, valor artístico e relação pessoal com o criador. Apesar do nome, o acervo também preserva clássicos, jogos independentes e experiências experimentais importantes para a história do meio.

Acesse o projeto

Site: https://the-aaa-archive.vercel.app

API: https://the-aaa-archive-api.onrender.com

Documentação da API: https://the-aaa-archive-api.onrender.com/docs

Dashboard: https://the-aaa-archive-dashboard.streamlit.app

A API utiliza o plano gratuito do Render e pode levar alguns segundos para responder após um período sem acessos.

Estado final

projeto publicado e funcional;

Foundation Collection com 105 jogos;

Awards History com 127 registros, de 2003 a 2025;

páginas individuais para todos os jogos;

busca, filtros e ordenação;

integração completa entre frontend, API e PostgreSQL;

dashboard analítico em Streamlit;

navegação adaptada para desktop e mobile;

testes de backend, banco e frontend concluídos.

Experiência

A identidade visual combina:

museu digital
+
arquivo tecnológico antigo
+
site perdido da internet
+
fliperama depois que todos foram embora

A interface utiliza preto, grafite, branco envelhecido, tipografia monoespaçada, bordas técnicas, scanlines discretas e pouco uso de cor.

Áreas do site

Rota

Área

/

Introduction

/home

Home

/foundation

Foundation Collection

/games/:id

Registro individual

/awards

Awards History

/data-room

Data Room

Destaques

Foundation Collection

A Foundation possui IDs contínuos de 1 a 105, com uma imagem cover.webp para cada jogo.

O acervo inclui grandes produções, clássicos históricos, jogos independentes, terror experimental e experiências narrativas.

O ranking pessoal exibido na Foundation é:

Silent Hill 2

The Last of Us

Life is Strange

Silent Hill 2 e Silent Hill 2 Remake são registros separados.

Awards History

A Awards History reúne vencedores e indicados a Game of the Year de:

Spike Video Game Awards;

VGX;

The Game Awards.

Os registros são comparados com a Foundation para identificar quais jogos premiados estão preservados no acervo.

Data Room

A Data Room apresenta uma síntese analítica integrada ao site e oferece acesso ao dashboard completo em Streamlit.

Arquitetura

CSV
↓
PostgreSQL
↓
FastAPI
↓
JSON
↓
React

Dashboard:

Streamlit
↓
PostgreSQL

Os CSVs são a fonte editorial original. O PostgreSQL é a fonte operacional utilizada pela API e pelo dashboard.

Tecnologias

Frontend

React

Vite

TypeScript

React Router

CSS personalizado

Fetch API

Backend e dados

Python

FastAPI

Pandas

PostgreSQL

psycopg

pytest

Dashboard e infraestrutura

Streamlit

Neon

Render

Vercel

Streamlit Community Cloud

Estrutura principal

The-AAA-Archive/
├── api/
├── dashboard/
├── data/
├── database/
├── docs/
├── frontend/
├── scripts/
├── .env.example
├── README.md
└── requirements.txt

Executar localmente

1. Dependências Python

python -m venv .venv
pip install -r requirements.txt

2. Banco de dados

Crie um arquivo .env na raiz:

POSTGRES_DB=aaa_archive
POSTGRES_USER=postgres
POSTGRES_PASSWORD=sua_senha
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
CORS_ALLOWED_ORIGINS=http://localhost:5173,http://127.0.0.1:5173

Crie as tabelas usando:

database/schema.sql

Depois importe os dados:

python scripts/import_to_postgres.py

3. API

fastapi dev api/main.py

A documentação ficará em:

http://127.0.0.1:8000/docs

4. Frontend

cd frontend
npm install
npm run dev

O site ficará em:

http://localhost:5173

5. Dashboard

Na raiz do projeto:

python -m streamlit run dashboard/app.py

O dashboard ficará em:

http://localhost:8501

Testes

Backend e banco:

python scripts/test_database.py
python -m pytest api/test_main.py -v

Módulos de dados:

python scripts/test_filters.py
python scripts/test_search.py
python scripts/test_site_statistics.py
python scripts/test_awards.py

Frontend:

cd frontend
npm run lint
npm run build

Atualização dos dados

Editar data/games.csv ou data/awards.csv
↓
Executar scripts/import_to_postgres.py
↓
Rodar os testes
↓
Validar API, site e dashboard

Novas imagens devem seguir:

frontend/public/assets/games/{id}/cover.webp

Documentação

A documentação final está em docs/:

Visão geral

Arquitetura

Dados e coleção

Frontend

Backend e dashboard

Deploy e manutenção

Segurança

o arquivo .env não deve ser enviado ao GitHub;

senhas e connection strings nunca devem ser documentadas;

.env.example deve conter apenas valores de exemplo;

credenciais expostas devem ser redefinidas imediatamente.

Autor

Desenvolvido por Kadu Almeida como projeto pessoal de software, dados, história dos videogames e portfólio.