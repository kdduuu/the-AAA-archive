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

O projeto deve crescer de forma incremental, priorizando clareza, organização e reutilização de código.

---

# Stack Tecnológica

## Backend

* Python;
* Pandas;
* FastAPI;
* PostgreSQL.

## Frontend

* HTML;
* CSS;
* JavaScript.

## Visualização de Dados

* Streamlit.

## Ferramentas

* Git;
* GitHub;
* VS Code.

---

# Estrutura do Projeto

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

A estrutura poderá evoluir conforme o crescimento do projeto, preservando sempre a organização e a separação de responsabilidades.

---

# Convenções de Nomenclatura

## Arquivos

Utilizar sempre **snake_case**.

Exemplos:

* `games.csv`
* `awards.csv`
* `load_data.py`
* `filters.py`
* `search.py`
* `site_statistics.py`
* `awards.py`

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

## Funções

Utilizar sempre **snake_case**.

Exemplos:

```python
carregar_dataset()
listar_jogos_por_genero()
buscar_vencedor_por_ano()
```

Os nomes das funções devem deixar claro o que elas fazem.

---

## Classes

Utilizar **PascalCase**.

Exemplos:

```python
Game
Developer
GameAward
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

* `load_data.py` → carregamento dos dados;
* `filters.py` → filtros da Foundation Collection;
* `search.py` → pesquisa textual da Foundation Collection;
* `site_statistics.py` → estatísticas da Home, API e dashboard;
* `awards.py` → consultas da base Awards History.

Evitar misturar diferentes responsabilidades no mesmo módulo.

---

# Organização das Funções

Cada função deve resolver apenas um problema.

Sempre que possível, uma função deve:

* receber dados;
* executar uma única tarefa;
* retornar um resultado.

Funções pequenas são mais fáceis de testar, reutilizar e manter.

Toda função criada deve possuir uma utilidade real no projeto.

Antes de criar uma nova função, deve-se responder:

> Qual parte do sistema utilizará este código?

---

# Comentários

Os comentários possuem finalidade didática.

Devem:

* explicar conceitos importantes;
* contextualizar decisões;
* facilitar o aprendizado durante o desenvolvimento.

Evitar comentários que apenas repitam o que o código já informa.

Exemplo ruim:

```python
# Soma 1
x = x + 1
```

Exemplo melhor:

```python
# Criamos uma cópia para evitar alterações acidentais no DataFrame original.
resultado = df[filtro].copy()
```

---

# Filosofia de Desenvolvimento

O desenvolvimento do The AAA Archive segue uma abordagem incremental.

Antes de implementar qualquer funcionalidade, deve-se responder:

> Qual parte do sistema utilizará este código?

Toda funcionalidade deverá possuir uma aplicação prática no produto final.

Exemplos:

* Home → `site_statistics.py`;
* Archive → `filters.py` e `search.py`;
* Awards → `awards.py`;
* Dashboard → módulos de estatísticas e análise;
* API → reutilização dos módulos existentes.

Essa abordagem evita código desnecessário e mantém o projeto orientado ao produto.

---

# Organização dos Dados

Durante a fase atual, o projeto utiliza datasets em CSV.

## Foundation Collection

Arquivo:

```text
data/games.csv
```

Esse arquivo representa a coleção principal do The AAA Archive.

A estrutura oficial desse dataset encontra-se documentada em:

```text
docs/data_dictionary.md
```

## Awards History

Arquivo:

```text
data/awards.csv
```

Esse arquivo representa o histórico de vencedores e indicados a Game of the Year.

A estrutura oficial desse dataset encontra-se documentada em:

```text
docs/awards_dictionary.md
```

A base Awards History é independente da Foundation Collection.

No entanto, as duas bases podem ser comparadas pelo nome do jogo:

```text
awards.csv → jogo
games.csv  → nome
```

Essa comparação permite identificar jogos premiados ou indicados que já fazem parte da Foundation Collection e jogos que ainda estão fora dela.

No futuro, os dados poderão ser normalizados em PostgreSQL.

---

# Fontes dos Dados

Sempre que possível, utilizar fontes oficiais ou verificáveis.

## Dados técnicos

* IGDB;
* Metacritic;
* páginas oficiais;
* documentações públicas confiáveis.

## Dados de premiações

* registros oficiais das premiações;
* páginas oficiais;
* bases públicas confiáveis;
* fontes jornalísticas reconhecidas, quando necessário.

## Conteúdo editorial

Produzido exclusivamente para o The AAA Archive:

* descrição;
* nota Kadu;
* nota Pavam;
* histórico importante;
* histórico influente;
* critérios de curadoria.

---

# Testes

Sempre que uma nova função relevante for criada, deve-se criar ou atualizar um teste correspondente.

Os testes atuais utilizam `assert`.

Arquivos de teste atuais:

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
python scripts/test_site_statistics.py
python scripts/test_awards.py
```

Se todos os testes passarem, significa que os módulos atuais continuam funcionando corretamente.

---

# Padrão dos Commits

Utilizar mensagens curtas, objetivas e descritivas.

Exemplos:

```text
docs: update project blueprint

docs: update project conventions

feat: create search module

feat: add site statistics

feat: add awards history module

feat: add awards foundation integration

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
* Toda função deve possuir finalidade real.
* A estrutura deve permanecer simples enquanto o projeto cresce.

---

# Objetivo Final

Construir um sistema completo para preservar, organizar e disponibilizar informações sobre videogames através de:

* backend modular;
* API;
* banco de dados;
* website;
* dashboard analítico.

Todo o desenvolvimento deverá priorizar simplicidade, organização e escalabilidade, permitindo que o projeto evolua continuamente sem perder sua consistência arquitetural.
