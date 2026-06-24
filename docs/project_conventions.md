# Project Conventions — The AAA Archive

# Objetivo

Este documento define os padrões adotados durante o desenvolvimento do **The AAA Archive**.

Seu objetivo é garantir consistência, organização e qualidade ao longo de toda a evolução do projeto, servindo como referência para futuras implementações e manutenções.

---

# Filosofia do Projeto

O The AAA Archive é um projeto pessoal desenvolvido para estudar:

* Análise de Dados;
* Engenharia de Software;
* Banco de Dados;
* Desenvolvimento Backend;
* Desenvolvimento Web;
* Desenvolvimento Full Stack.

Embora possua finalidade educacional, todas as decisões devem seguir padrões profissionais de desenvolvimento.

Cada funcionalidade implementada deve possuir uma aplicação real dentro do sistema.

---

# Stack Tecnológica

## Backend

* Python
* Pandas
* PostgreSQL
* FastAPI

## Frontend

* HTML
* CSS
* JavaScript

## Visualização de Dados

* Streamlit

## Ferramentas

* Git
* GitHub
* VS Code

---

# Estrutura do Projeto

```text
The-AAA-Archive/

assets/
data/
docs/
notebooks/
scripts/

README.md
requirements.txt
.gitignore
```

A estrutura poderá evoluir conforme o crescimento do projeto, preservando sempre a organização e a separação de responsabilidades.

---

# Convenções de Nomenclatura

## Arquivos

Utilizar sempre **snake_case**.

Exemplos:

* games.csv
* load_data.py
* filters.py
* search.py
* site_statistics.py

Evitar nomes genéricos ou inconsistentes.

---

## Variáveis

Utilizar sempre **snake_case**.

Exemplos:

```python
game_name
release_year
developer_name
```

---

## Classes

Utilizar **PascalCase**.

Exemplos:

```python
Game
Developer
GameAwards
```

---

## Constantes

Utilizar **UPPER_CASE**.

Exemplos:

```python
DEFAULT_PATH
MAX_SCORE
PROJECT_VERSION
```

---

# Organização do Código

Cada arquivo deve possuir apenas uma responsabilidade.

Exemplos:

* `load_data.py` → carregamento dos dados.
* `filters.py` → filtros da coleção.
* `search.py` → pesquisas.
* `site_statistics.py` → estatísticas do website.
* `goty.py` → informações do Game Awards.

Evitar misturar diferentes responsabilidades no mesmo módulo.

---

# Organização das Funções

Cada função deve resolver apenas um problema.

Sempre que possível:

* receber dados;
* executar uma única tarefa;
* retornar um resultado.

Funções pequenas são mais fáceis de testar, reutilizar e manter.

---

# Comentários

Os comentários possuem finalidade didática.

Devem:

* explicar conceitos importantes;
* contextualizar decisões;
* facilitar o aprendizado durante o desenvolvimento.

Evitar comentários que apenas repitam o que o código já informa.

---

# Filosofia de Desenvolvimento

O desenvolvimento do The AAA Archive segue uma abordagem incremental.

Antes de implementar qualquer funcionalidade, deve-se responder:

> **Qual parte do sistema utilizará este código?**

Toda funcionalidade deverá possuir uma aplicação prática no produto final.

Exemplo:

* Home → `site_statistics.py`
* Archive → `filters.py` e `search.py`
* Game Awards → `goty.py`
* Dashboard → estatísticas do backend

Essa abordagem evita código desnecessário e mantém o projeto orientado ao produto.

---

# Organização dos Dados

Durante a Fase 1, o projeto utiliza um único dataset:

```text
data/games.csv
```

A estrutura oficial desse arquivo encontra-se documentada em **`data_dictionary.md`**.

No futuro, os dados serão normalizados em PostgreSQL.

---

# Fontes dos Dados

Sempre que possível, utilizar fontes oficiais.

## Dados técnicos

* IGDB
* Metacritic

## Conteúdo editorial

Produzido exclusivamente para o The AAA Archive:

* descrição;
* nota Kadu;
* nota Pavam;
* histórico importante;
* histórico influente.

---

# Padrão dos Commits

Utilizar mensagens curtas, objetivas e descritivas.

Exemplos:

```text
docs: update project blueprint

feat: create search module

feat: add site statistics

refactor: improve filters

fix: correct metacritic values

data: update foundation collection
```

---

# Princípios do Projeto

Durante todo o desenvolvimento serão seguidos os seguintes princípios:

* Clareza acima da complexidade.
* Organização acima da velocidade.
* Qualidade acima da quantidade.
* Documentação antes da implementação.
* Evolução incremental.
* Código limpo.
* Código reutilizável.
* Responsabilidade única por módulo.
* Backend antes do frontend.
* Projeto orientado a portfólio.

---

# Objetivo Final

Construir um sistema completo para preservar, organizar e disponibilizar informações sobre videogames através de um backend modular, uma API, um website e um dashboard analítico.

Todo o desenvolvimento deverá priorizar simplicidade, organização e escalabilidade, permitindo que o projeto evolua continuamente sem perder sua consistência arquitetural.
