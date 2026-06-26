# The AAA Archive

Um arquivo digital focado em preservar, catalogar e explorar a história dos jogos AAA single-player.

O projeto foi criado como uma forma prática de estudar Python, Pandas, análise de dados e engenharia de software através do desenvolvimento de um sistema real.

---

## Status do Projeto

**Em desenvolvimento**

Fase atual: **Backend e estruturação dos dados**

O projeto já possui:

* dataset da Foundation Collection;
* dataset do histórico de premiações;
* módulo de carregamento de dados;
* módulo de filtros;
* módulo de pesquisa textual;
* módulo de estatísticas do site;
* módulo de premiações;
* scripts de teste para os módulos atuais do backend.

---

## Objetivo do Projeto

O objetivo do The AAA Archive não é catalogar todos os jogos já lançados.

A proposta é construir um arquivo curado de jogos AAA single-player historicamente relevantes, permitindo futura exploração através de:

* módulos de backend;
* API;
* website;
* dashboard;
* análises históricas e editoriais.

O projeto está sendo desenvolvido de forma incremental, com documentação e backend sendo construídos antes do frontend.

---

## Bases de Dados Atuais

### Foundation Collection

Arquivo principal:

```text
data/games.csv
```

Este dataset contém a lista curada de jogos que formam o núcleo do The AAA Archive.

Cada linha representa um jogo.

Os principais campos atuais incluem:

* id;
* nome;
* ano de lançamento;
* gênero;
* desenvolvedora;
* franquia;
* descrição;
* nota Metacritic;
* notas pessoais;
* importância histórica;
* influência histórica.

### Awards History

Arquivo principal:

```text
data/awards.csv
```

Este dataset armazena vencedores e indicados a Game of the Year das seguintes premiações:

* Spike Video Game Awards;
* VGX;
* The Game Awards.

A base Awards History é independente da Foundation Collection, mas ambas podem ser comparadas pelo nome do jogo.

---

## Estrutura Atual do Projeto

```text
The-AAA-Archive/

assets/
data/
  games.csv
  awards.csv

docs/
  awards_dictionary.md
  data_dictionary.md
  foundation_collection.md
  project_blueprint.md
  project_context.md
  project_conventions.md

notebooks/

scripts/
  load_data.py
  filters.py
  search.py
  site_statistics.py
  awards.py
  test_filters.py
  test_search.py
  test_site_statistics.py
  test_awards.py

README.md
requirements.txt
.gitignore
```

---

## Módulos do Backend

### `load_data.py`

Responsável por carregar os datasets oficiais do projeto.

Atualmente carrega:

* `games.csv`;
* `awards.csv`.

---

### `filters.py`

Contém os filtros utilizados futuramente pela página Archive.

Filtros atuais:

* jogos por desenvolvedora;
* jogos por gênero;
* jogos por franquia;
* jogos por ano de lançamento;
* jogos por década.

---

### `search.py`

Contém a lógica de pesquisa textual da futura página Archive.

Permite pesquisar jogos por termos encontrados em colunas como:

* nome;
* gênero;
* desenvolvedora;
* franquia;
* descrição.

---

### `site_statistics.py`

Gera estatísticas que serão usadas futuramente pela Home, API e dashboard.

Estatísticas atuais:

* total de jogos;
* total de desenvolvedoras;
* total de franquias;
* total de gêneros;
* jogos por gênero;
* jogos por desenvolvedora;
* jogos por franquia;
* jogos por década;
* jogos historicamente importantes;
* jogos historicamente influentes.

---

### `awards.py`

Responsável pela base Awards History.

Funcionalidades atuais:

* listar premiações disponíveis;
* listar anos disponíveis;
* listar jogos por ano da premiação;
* buscar o vencedor de Game of the Year por ano;
* listar indicados por ano;
* listar todos os vencedores;
* filtrar registros por premiação;
* comparar Awards History com a Foundation Collection;
* listar jogos premiados que ainda não estão na Foundation Collection.

---

## Testes

O projeto utiliza scripts simples de teste em Python com `assert`.

Testes disponíveis:

```text
scripts/test_filters.py
scripts/test_search.py
scripts/test_site_statistics.py
scripts/test_awards.py
```

Para rodar todos os testes:

```bash
python scripts/test_filters.py
python scripts/test_site_statistics.py
python scripts/test_search.py
python scripts/test_awards.py
```

Se todos os testes passarem, os módulos atuais do backend estão funcionando corretamente.

---

## Tecnologias

Tecnologias atuais:

* Python;
* Pandas;
* CSV;
* Git;
* GitHub.

Tecnologias planejadas:

* PostgreSQL;
* FastAPI;
* HTML;
* CSS;
* JavaScript;
* Streamlit.

---

## Filosofia de Desenvolvimento

O projeto segue uma abordagem incremental simples:

1. Documentação antes da implementação.
2. Backend antes do frontend.
3. Uma responsabilidade por arquivo.
4. Uma responsabilidade por função.
5. Código reutilizável.
6. Estrutura simples antes de arquitetura complexa.
7. Toda função deve ter uma utilidade real no produto final.

O objetivo não é apenas aprender tecnologias, mas construir um software real utilizando essas tecnologias como ferramentas.

---

## Roadmap

Fase atual:

```text
Datasets em CSV
↓
Módulos de backend com Pandas
```

Próximas etapas planejadas:

```text
Revisão do backend
↓
FastAPI
↓
Website
↓
Dashboard
↓
Migração para PostgreSQL
```

---

## Autor

Desenvolvido por **Kadu Almeida** como um projeto pessoal de software, análise de dados e portfólio.
