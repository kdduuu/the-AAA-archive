# The AAA Archive

Um arquivo digital focado em preservar, catalogar e explorar a história dos jogos AAA single-player historicamente relevantes.

O projeto foi criado como uma forma prática de estudar **Python**, **Pandas**, **análise de dados**, **backend**, **API**, **dashboards** e **engenharia de software** através do desenvolvimento de um sistema real.

---

## Status do Projeto

**Em desenvolvimento**

Fase atual:

```text
CSV + Pandas
↓
Módulos Python
↓
Testes
↓
FastAPI
↓
Streamlit Dashboard
```

O projeto já possui:

* dataset da Foundation Collection;
* dataset do histórico de premiações;
* módulo de carregamento de dados;
* módulo de filtros;
* módulo de pesquisa textual;
* módulo de estatísticas;
* módulo de premiações;
* testes dos módulos principais;
* primeira versão da API com FastAPI;
* endpoints editoriais na API;
* testes da API;
* primeira versão do dashboard com Streamlit;
* documentação principal do projeto.

---

## Objetivo do Projeto

O objetivo do **The AAA Archive** não é catalogar todos os jogos já lançados.

A proposta é construir um arquivo curado de jogos AAA single-player historicamente relevantes, permitindo exploração através de:

* módulos de backend;
* API;
* dashboard;
* análises históricas;
* análises editoriais;
* futuramente, website e banco de dados.

O projeto está sendo desenvolvido de forma incremental, com documentação e backend sendo construídos antes de etapas mais complexas.

---

## Filosofia do Projeto

O projeto segue uma abordagem simples e incremental:

1. Clareza antes de complexidade.
2. Documentação antes da implementação.
3. Backend antes do frontend.
4. Uma responsabilidade por arquivo.
5. Uma responsabilidade por função.
6. Código reutilizável.
7. Estrutura simples antes de arquitetura complexa.
8. Toda função deve ter uma utilidade real no produto final.

O objetivo não é apenas aprender tecnologias isoladas, mas construir um software real utilizando essas tecnologias como ferramentas.

---

## Bases de Dados Atuais

O projeto possui duas bases principais em CSV.

---

## Foundation Collection

Arquivo:

```text
data/games.csv
```

Este dataset contém a lista curada de jogos que formam o núcleo do **The AAA Archive**.

Cada linha representa um jogo.

Colunas principais:

```text
id
nome
ano_lancamento
genero
developer
franchise
descricao
metacritic
nota_kadu
nota_pavam
historico_importante
historico_influente
```

A Foundation Collection reúne jogos AAA single-player selecionados por relevância histórica, impacto cultural, influência, reconhecimento crítico ou importância dentro da indústria.

---

## Awards History

Arquivo:

```text
data/awards.csv
```

Este dataset armazena vencedores e indicados a **Game of the Year** das seguintes premiações:

```text
Spike Video Game Awards
VGX
The Game Awards
```

Colunas principais:

```text
ano
premiacao
jogo
status
```

A base Awards History é independente da Foundation Collection, mas ambas podem ser comparadas pelo nome do jogo.

---

## Estrutura Atual do Projeto

```text
The-AAA-Archive/

assets/

api/
  main.py
  test_main.py

data/
  games.csv
  awards.csv

docs/
  api_checkpoint.md
  api_plan.md
  awards_dictionary.md
  dashboard_checkpoint.md
  dashboard_plan.md
  data_dictionary.md
  foundation_collection.md
  project_blueprint.md
  project_context.md
  project_conventions.md

dashboard/
  app.py

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

## Módulos Python

Os módulos principais do projeto ficam na pasta:

```text
scripts/
```

Eles concentram a lógica de leitura, filtros, busca, estatísticas e premiações.

---

## `load_data.py`

Responsável por carregar os datasets oficiais do projeto.

Funções principais:

```python
carregar_dataset()
carregar_awards()
```

Atualmente carrega:

* `data/games.csv`;
* `data/awards.csv`.

---

## `filters.py`

Contém filtros para a Foundation Collection.

Funções principais:

```python
listar_jogos_por_developer()
listar_jogos_por_genero()
listar_jogos_por_franquia()
listar_jogos_por_ano()
listar_jogos_por_decada()
```

Permite filtrar os jogos por:

* desenvolvedora;
* gênero;
* franquia;
* ano de lançamento;
* década.

---

## `search.py`

Contém a lógica de pesquisa textual da Foundation Collection.

Funções principais:

```python
pesquisar_jogos()
pesquisar_jogos_por_nome()
```

A busca considera colunas como:

* nome;
* gênero;
* desenvolvedora;
* franquia;
* descrição.

---

## `site_statistics.py`

Gera estatísticas usadas pela API e pelo dashboard.

Funções principais:

```python
contar_total_jogos()
contar_total_developers()
contar_total_franquias()
contar_total_generos()
listar_quantidade_por_genero()
listar_quantidade_por_developer()
listar_quantidade_por_franquia()
listar_quantidade_por_decada()
listar_jogos_historicos()
listar_jogos_influentes()
gerar_estatisticas_home()
```

Estatísticas geradas:

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

## `awards.py`

Responsável por consultar e comparar a base Awards History.

Funções principais:

```python
listar_premiacoes()
listar_anos_disponiveis()
listar_jogos_por_ano()
buscar_vencedor_por_ano()
listar_indicados_por_ano()
listar_vencedores()
listar_jogos_por_premiacao()
listar_vencedores_na_foundation()
listar_indicados_na_foundation()
listar_jogos_awards_fora_da_foundation()
```

Permite:

* listar premiações disponíveis;
* listar anos disponíveis;
* consultar vencedor por ano;
* consultar indicados por ano;
* listar vencedores;
* filtrar por premiação;
* comparar Awards History com a Foundation Collection;
* identificar jogos premiados que ainda estão fora da Foundation Collection.

---

## API FastAPI

A API foi criada em:

```text
api/main.py
```

Ela reaproveita os módulos Python do backend e expõe os dados por meio de endpoints HTTP.

Para rodar a API:

```bash
fastapi dev api/main.py
```

A documentação automática da API fica disponível em:

```text
http://127.0.0.1:8000/docs
```

---

## Endpoints Atuais da API

### Inicial

```text
GET /
```

Verifica se a API está online.

---

### Games

```text
GET /games
```

Retorna todos os jogos da Foundation Collection.

```text
GET /games/search?term=zelda
```

Pesquisa jogos por termo.

A busca considera:

```text
nome
genero
developer
franchise
descricao
```

```text
GET /games/developer/{developer}
```

Filtra jogos por desenvolvedora.

```text
GET /games/genre/{genre}
```

Filtra jogos por gênero.

```text
GET /games/year/{year}
```

Filtra jogos por ano.

```text
GET /games/historical
```

Retorna jogos marcados como historicamente importantes na Foundation Collection.

Esse endpoint utiliza a coluna:

```text
historico_importante
```

```text
GET /games/influential
```

Retorna jogos marcados como historicamente influentes na Foundation Collection.

Esse endpoint utiliza a coluna:

```text
historico_influente
```

---

### Estatísticas

```text
GET /stats/home
```

Retorna estatísticas gerais da Foundation Collection.

Exemplos de dados retornados:

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

### Awards

```text
GET /awards
```

Retorna todos os registros da Awards History.

```text
GET /awards/winners
```

Retorna vencedores de Game of the Year.

```text
GET /awards/{year}
```

Retorna vencedor e indicados de um ano específico.

```text
GET /awards/foundation/winners
```

Retorna vencedores que também estão na Foundation Collection.

```text
GET /awards/foundation/nominees
```

Retorna indicados que também estão na Foundation Collection.

```text
GET /awards/foundation/outside
```

Retorna jogos da Awards History que ainda não estão na Foundation Collection.

---

## Resumo dos Endpoints da API

```text
GET /
GET /games
GET /games/search?term={term}
GET /games/developer/{developer}
GET /games/genre/{genre}
GET /games/year/{year}
GET /games/historical
GET /games/influential
GET /stats/home
GET /awards
GET /awards/winners
GET /awards/{year}
GET /awards/foundation/winners
GET /awards/foundation/nominees
GET /awards/foundation/outside
```

---

## Dashboard Streamlit

O dashboard foi criado em:

```text
dashboard/app.py
```

Ele é a primeira camada visual do projeto.

O dashboard utiliza **Streamlit** para exibir dados da Foundation Collection e da Awards History de forma visual e interativa.

Para rodar o dashboard:

```bash
streamlit run dashboard/app.py
```

O Streamlit normalmente abre automaticamente no navegador.

O endereço local costuma ser:

```text
http://localhost:8501
```

---

## Funcionalidades do Dashboard

A versão atual do dashboard possui:

* organização visual por abas;
* carregamento de dados com cache;
* exploração da Foundation Collection;
* exploração da Awards History;
* filtros interativos;
* busca textual;
* métricas principais;
* gráficos simples;
* tabelas dinâmicas;
* recorte editorial com jogos históricos e influentes.

---

### Organização por Abas

O dashboard utiliza abas com `st.tabs()` para separar melhor as áreas principais.

Abas atuais:

```text
Foundation Collection
Awards History
```

Essa organização deixa a experiência mais limpa, evitando que todas as informações fiquem em uma única página longa.

---

### Cache no Carregamento dos Dados

O dashboard utiliza `@st.cache_data` no carregamento dos datasets.

Datasets carregados com cache:

```text
data/games.csv
data/awards.csv
```

Isso evita que os CSVs sejam recarregados do zero a cada interação do usuário com filtros, busca ou seleção de abas.

---

### Foundation Collection

A aba **Foundation Collection** possui:

* métricas principais;
* gráficos simples;
* filtros interativos;
* busca textual;
* recorte editorial;
* tabela dinâmica de jogos.

Métricas exibidas:

```text
Jogos
Desenvolvedoras
Franquias
Gêneros
```

Filtros disponíveis:

```text
Gênero
Desenvolvedora
Ano de lançamento
Franquia
```

Busca textual aplicada nas colunas:

```text
nome
genero
developer
franchise
descricao
```

Gráficos atuais:

```text
Jogos por Década
Jogos por Gênero
Desenvolvedoras com Mais Jogos
```

---

### Recorte Editorial

A aba **Foundation Collection** também possui uma seção chamada:

```text
Recorte Editorial
```

Essa seção destaca jogos marcados no dataset como:

```text
historicamente importantes
historicamente influentes
```

Ela utiliza as colunas:

```text
historico_importante
historico_influente
```

A seção possui:

* métrica de jogos historicamente importantes;
* métrica de jogos historicamente influentes;
* tabela expansível de jogos historicamente importantes;
* tabela expansível de jogos historicamente influentes.

Esses resultados também reagem aos filtros e à busca textual.

---

### Awards History

A aba **Awards History** possui:

* métricas da base de premiações;
* consulta por ano;
* vencedor do ano selecionado;
* tabela da edição selecionada;
* histórico de vencedores;
* comparação entre Awards History e Foundation Collection.

Métricas exibidas:

```text
Registros no Awards
Anos catalogados
Vencedores
Fora da Foundation
```

Comparações exibidas:

```text
Vencedores presentes na Foundation Collection
Indicados presentes na Foundation Collection
Jogos do Awards fora da Foundation Collection
```

---

## Testes

O projeto utiliza scripts simples de teste em Python com `assert`.

Testes disponíveis:

```text
scripts/test_filters.py
scripts/test_search.py
scripts/test_site_statistics.py
scripts/test_awards.py
api/test_main.py
```

Para rodar todos os testes:

```bash
python scripts/test_filters.py
python scripts/test_search.py
python scripts/test_site_statistics.py
python scripts/test_awards.py
python api/test_main.py
```

Se todos os testes passarem, os módulos atuais do backend e a API estão funcionando corretamente.

---

## Testes da API

O arquivo:

```text
api/test_main.py
```

testa os principais endpoints da API.

Endpoints testados:

```text
GET /
GET /games
GET /games/search?term=zelda
GET /games/developer/Capcom
GET /games/genre/Survival Horror
GET /games/year/2018
GET /games/historical
GET /games/influential
GET /stats/home
GET /awards
GET /awards/winners
GET /awards/2018
GET /awards/foundation/winners
GET /awards/foundation/nominees
GET /awards/foundation/outside
```

Para rodar apenas os testes da API:

```bash
python api/test_main.py
```

---

## Tecnologias

Tecnologias usadas atualmente:

* Python;
* Pandas;
* CSV;
* FastAPI;
* Streamlit;
* Git;
* GitHub.

Tecnologias planejadas para fases futuras:

* PostgreSQL;
* HTML;
* CSS;
* JavaScript;
* website próprio;
* possível deploy.

---

## Instalação das Dependências

As dependências do projeto ficam no arquivo:

```text
requirements.txt
```

Para instalar as dependências:

```bash
pip install -r requirements.txt
```

Dependências principais atuais:

```text
pandas
fastapi
streamlit
```

---

## Como Rodar o Projeto

### 1. Rodar os testes dos módulos

```bash
python scripts/test_filters.py
python scripts/test_search.py
python scripts/test_site_statistics.py
python scripts/test_awards.py
```

---

### 2. Rodar os testes da API

```bash
python api/test_main.py
```

---

### 3. Rodar a API

```bash
fastapi dev api/main.py
```

Documentação automática:

```text
http://127.0.0.1:8000/docs
```

---

### 4. Rodar o Dashboard

```bash
streamlit run dashboard/app.py
```

Endereço local esperado:

```text
http://localhost:8501
```

---

## Documentação

A documentação principal do projeto fica na pasta:

```text
docs/
```

Documentos atuais:

```text
api_checkpoint.md
api_plan.md
awards_dictionary.md
dashboard_checkpoint.md
dashboard_plan.md
data_dictionary.md
foundation_collection.md
project_blueprint.md
project_context.md
project_conventions.md
```

Esses documentos registram a visão do projeto, os datasets, as convenções, o planejamento da API, o checkpoint da API, o planejamento do dashboard e o checkpoint do dashboard.

---

## Roadmap

Fases já iniciadas ou concluídas:

```text
Datasets em CSV
↓
Módulos Python com Pandas
↓
Testes dos módulos
↓
API com FastAPI
↓
Endpoints editoriais na API
↓
Dashboard com Streamlit
↓
Documentação do dashboard
↓
Documentação atualizada da API
```

Próximas etapas possíveis:

```text
adicionar endpoint por década
↓
adicionar endpoint por franquia
↓
adicionar filtros combinados com query params
↓
melhorar organização interna do dashboard/app.py
↓
refatorar a API com routers
↓
planejar migração para PostgreSQL
↓
futuramente criar website próprio
```

---

## O que Ainda Não Está Sendo Feito

Nesta fase, o projeto ainda não utiliza:

* PostgreSQL;
* frontend próprio com HTML/CSS/JavaScript;
* autenticação;
* deploy;
* consumo da API dentro do Streamlit;
* API refatorada em routers;
* paginação;
* filtros combinados por query params.

Essas etapas podem ser feitas no futuro, mas ainda não são prioridade.

---

## Autor

Desenvolvido por **Kadu Almeida** como um projeto pessoal de software, análise de dados e portfólio.
