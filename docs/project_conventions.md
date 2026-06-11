# Project Conventions - The AAA Archive

## Objetivo

Este documento define os padrões utilizados durante o desenvolvimento do The AAA Archive.

Seu objetivo é garantir consistência na organização do projeto, facilitar futuras manutenções e servir como referência para qualquer desenvolvedor que participe do projeto.

---

# Filosofia do Projeto

O The AAA Archive é um projeto pessoal desenvolvido com foco em:

- Aprendizado de Análise de Dados;
- Engenharia de Software;
- Banco de Dados;
- Visualização de Dados;
- Desenvolvimento Full Stack.

Apesar de possuir finalidade educacional, todas as decisões devem seguir padrões profissionais.

---

# Tecnologias

## Linguagem

Python 3

## Análise de Dados

Pandas

## Banco de Dados

PostgreSQL

## Interface

Streamlit

## Controle de Versão

Git

GitHub

---

# Estrutura do Projeto

The-AAA-Archive/

├── data/
│   ├── raw/
│   ├── processed/
│   └── games.csv
│
├── docs/
│   ├── data_dictionary.md
│   ├── foundation_collection.md
│   └── project_conventions.md
│
├── notebooks/
│
├── scripts/
│
├── dashboard/
│
├── assets/
│
├── README.md
├── requirements.txt
└── .gitignore

---

# Convenções de Nomenclatura

## Arquivos

Sempre utilizar:

snake_case

Exemplos:

games.csv

data_dictionary.md

foundation_collection.md

player_statistics.py

Nunca utilizar:

MeuArquivo.py

Dados Jogos.csv

Projeto Final.py

---

## Variáveis Python

Sempre utilizar:

snake_case

Exemplo:

game_name

release_year

developer_name

---

## Classes

Sempre utilizar:

PascalCase

Exemplo:

Game

Developer

Dashboard

---

## Constantes

Sempre utilizar:

UPPER_CASE

Exemplo:

MAX_SCORE

DEFAULT_PATH

PROJECT_VERSION

---

# Organização dos Dados

Durante a Fase 1, o projeto utilizará apenas um arquivo principal:

games.csv

Durante a evolução para PostgreSQL, os dados serão normalizados em múltiplas tabelas.

---

# Padrão dos Commits

Utilizar mensagens curtas e objetivas.

Exemplos:

docs: create data dictionary

docs: add foundation collection

data: add first games

feat: create pandas loader

feat: first dashboard

refactor: improve project structure

fix: correct metacritic values

---

# Organização do Código

Cada script deve possuir apenas uma responsabilidade.

Exemplo:

load_data.py

Responsável apenas por carregar dados.

Nunca misturar:

- carregamento
- análise
- gráficos
- dashboard

no mesmo arquivo.

---

# Organização dos Dados

Todos os dados deverão possuir uma fonte conhecida.

Fontes oficiais:

- IGDB
- Metacritic

Conteúdo editorial:

- Descrição
- Nota Kadu
- Nota Pavã
- Histórico Importante
- Histórico Influente

---

# Princípios do Projeto

Durante todo o desenvolvimento serão seguidos os seguintes princípios:

- Clareza acima de complexidade.
- Organização acima de velocidade.
- Qualidade acima de quantidade.
- Documentação antes da implementação.
- Evolução incremental.
- Código reutilizável.
- Projeto orientado a portfólio.

---

# Roadmap Oficial

Planejamento

↓

Modelagem dos Dados

↓

Dataset (CSV)

↓

Pandas

↓

Análise Exploratória

↓

PostgreSQL

↓

Streamlit

↓

Deploy

---

# Objetivo Final

Construir um arquivo histórico dos jogos AAA Single Player utilizando práticas profissionais de Engenharia de Software, Ciência de Dados e Desenvolvimento Web.

O projeto deverá servir como portfólio técnico e demonstrar conhecimentos em:

- Python
- Pandas
- PostgreSQL
- Streamlit
- Git
- GitHub
- Modelagem de Dados
- Visualização de Dados