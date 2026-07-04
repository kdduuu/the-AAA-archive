# Project Blueprint — The AAA Archive

> **Este documento representa a visão oficial do The AAA Archive.**
>
> Antes de implementar novas funcionalidades, alterar a arquitetura ou iniciar uma nova conversa sobre o projeto, este documento deve ser utilizado como uma das principais referências.

---

# O que é o The AAA Archive?

O **The AAA Archive** é um projeto pessoal de desenvolvimento de software criado por **Kadu Almeida**.

Seu objetivo é construir um arquivo digital curado dedicado à preservação, organização e exploração da história dos videogames, com foco em jogos **AAA single-player historicamente relevantes**.

O projeto nasceu como uma forma de estudar **Python**, **Pandas** e análise de dados usando um dataset próprio, mas evoluiu para uma aplicação mais completa, envolvendo:

* backend modular;
* datasets em CSV;
* testes simples;
* API com FastAPI;
* dashboard com Streamlit;
* documentação técnica;
* futura migração para PostgreSQL;
* possível website próprio no futuro.

A **Foundation Collection** representa o núcleo principal do projeto. Ela reúne uma seleção cuidadosamente curada de jogos considerados importantes para a história da indústria.

Além dela, o projeto também possui uma base independente chamada **Awards History**, responsável por armazenar vencedores e indicados a prêmios de **Game of the Year**.

O objetivo do The AAA Archive não é catalogar todos os jogos existentes, mas construir uma coleção consistente, organizada, editorialmente clara e preparada para crescer ao longo do tempo.

---

# Objetivos do Projeto

O desenvolvimento do The AAA Archive possui objetivos técnicos, educacionais e editoriais.

Os principais objetivos são:

* construir uma Foundation Collection organizada e bem documentada;
* manter um histórico de premiações de Game of the Year;
* desenvolver um backend reutilizável utilizando Python e Pandas;
* disponibilizar os dados através de uma API com FastAPI;
* criar um dashboard analítico com Streamlit;
* praticar organização de projeto, documentação, testes e Git/GitHub;
* preparar o projeto para uma futura migração para PostgreSQL;
* construir uma base sólida para portfólio.

Todo código desenvolvido deve possuir uma finalidade prática dentro do produto.

Nesta fase, o objetivo não é adicionar novas funcionalidades grandes, mas organizar melhor o que já foi construído antes de avançar para PostgreSQL.

---

# Bases Principais do Projeto

O projeto trabalha atualmente com duas bases em CSV:

```text
data/games.csv
data/awards.csv
```

Essas bases são lidas com Python e Pandas e alimentam os módulos, a API e o dashboard.

---

## Foundation Collection

Arquivo:

```text
data/games.csv
```

A **Foundation Collection** representa o núcleo principal do The AAA Archive.

Cada linha do arquivo representa um jogo da coleção principal.

Essa base é usada por:

* filtros;
* busca textual;
* estatísticas;
* API;
* dashboard;
* futuras páginas do website;
* futuras análises históricas.

O dataset possui colunas como:

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

A Foundation Collection não é uma lista infinita de jogos.

Ela é uma curadoria editorial.

Um jogo entra nessa base porque possui relevância histórica, influência cultural, reconhecimento crítico ou importância dentro da evolução dos videogames.

---

## Awards History

Arquivo:

```text
data/awards.csv
```

O **Awards History** representa o histórico de vencedores e indicados a prêmios de **Game of the Year**.

Essa base é independente da Foundation Collection.

Isso significa que um jogo pode aparecer no histórico de premiações mesmo sem fazer parte da coleção principal.

O dataset possui colunas como:

```text
ano
premiacao
jogo
status
```

As duas bases podem ser comparadas pelo nome do jogo:

```text
awards.csv → jogo
games.csv  → nome
```

Essa comparação permite identificar:

* vencedores que já estão na Foundation Collection;
* indicados que já estão na Foundation Collection;
* jogos premiados ou indicados que ainda estão fora da Foundation Collection.

Essa separação é importante porque mantém a curadoria editorial da Foundation Collection sem apagar a importância histórica dos prêmios.

---

# Arquitetura Geral

O projeto é desenvolvido em camadas simples.

```text
Datasets CSV
│
├── games.csv
│   └── Foundation Collection
│
├── awards.csv
│   └── Awards History
│
▼
load_data.py
│
▼
Módulos do Projeto
│
├── filters.py
├── search.py
├── site_statistics.py
├── awards.py
└── ...
│
▼
API FastAPI
│
▼
Dashboard Streamlit
│
▼
Futuro Website
```

Atualmente, os arquivos CSV são a fonte principal de dados.

No futuro, eles poderão ser migrados para um banco de dados PostgreSQL.

A ideia é que a fonte dos dados mude, mas as responsabilidades principais continuem claras:

* dados ficam em uma fonte organizada;
* módulos tratam a lógica;
* API disponibiliza os dados;
* dashboard apresenta análises;
* futuro website explora a coleção visualmente.

---

# Estrutura Atual do Projeto

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

Essa estrutura representa o estado atual do projeto.

---

# Estrutura dos Módulos

Cada módulo possui uma responsabilidade principal.

---

## `load_data.py`

Responsável por carregar os datasets oficiais do projeto.

Atualmente carrega:

* `games.csv`;
* `awards.csv`.

Funções principais:

```text
carregar_dataset()
carregar_awards()
```

Esse módulo é a porta de entrada dos dados no projeto.

---

## `filters.py`

Centraliza os filtros utilizados na Foundation Collection.

Funções principais:

```text
listar_jogos_por_developer()
listar_jogos_por_genero()
listar_jogos_por_franquia()
listar_jogos_por_ano()
listar_jogos_por_decada()
```

Esse módulo é usado pela API, pelo dashboard e pode ser reutilizado futuramente no website.

---

## `search.py`

Responsável pela pesquisa textual de jogos.

Funções principais:

```text
pesquisar_jogos()
pesquisar_jogos_por_nome()
```

A busca pode considerar campos como:

* nome;
* gênero;
* desenvolvedora;
* franquia;
* descrição.

---

## `site_statistics.py`

Responsável por gerar estatísticas da Foundation Collection.

Funções principais:

```text
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

Nenhuma informação estatística importante deve ser escrita manualmente quando puder ser calculada a partir dos dados.

---

## `awards.py`

Responsável pelas consultas relacionadas ao Awards History.

Funções principais:

```text
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

Esse módulo também é responsável por comparar o `awards.csv` com o `games.csv`.

---

# API

A API do projeto está localizada em:

```text
api/main.py
```

Ela foi criada com **FastAPI** e representa a primeira versão de disponibilização dos dados em JSON.

A API inicial já foi concluída.

Ela usa atualmente:

* CSV;
* Pandas;
* módulos da pasta `scripts/`;
* respostas em JSON.

A API ainda não usa:

* PostgreSQL;
* autenticação;
* cadastro;
* edição;
* exclusão;
* routers separados.

Isso é intencional.

A primeira versão da API tem o objetivo de expor os dados existentes de forma simples antes da migração para banco de dados.

---

## Endpoints Atuais da API

```text
GET /
GET /games
GET /games/search?term={term}
GET /games/developer/{developer}
GET /games/genre/{genre}
GET /games/franchise/{franchise}
GET /games/year/{year}
GET /games/decade/{decade}
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

Nesta fase, a API está fechada.

Não serão adicionados novos endpoints antes da organização do dashboard e do planejamento do PostgreSQL.

---

# Dashboard

O dashboard está localizado em:

```text
dashboard/app.py
```

Ele foi desenvolvido com **Streamlit** e representa a primeira interface visual do projeto.

O dashboard já possui:

* abas com `st.tabs()`;
* aba Foundation Collection;
* aba Awards History;
* cache com `@st.cache_data`;
* filtros interativos na sidebar;
* busca textual;
* métricas principais;
* gráficos simples com `st.bar_chart`;
* tabelas dinâmicas;
* seção Recorte Editorial;
* jogos historicamente importantes;
* jogos historicamente influentes;
* consulta de Awards por ano;
* histórico de vencedores;
* comparação entre Awards History e Foundation Collection.

O dashboard inicial está funcionando.

O foco atual não é mudar o visual nem adicionar grandes funcionalidades.

O foco atual é organizar melhor o arquivo `dashboard/app.py`, pois ele cresceu bastante.

---

# Estrutura Visual Planejada

A longo prazo, o The AAA Archive poderá ter um website próprio.

O website foi planejado para ser simples, intuitivo e de fácil manutenção.

Ao invés de possuir dezenas de páginas independentes, a maior parte das funcionalidades poderá ser concentrada em poucas áreas principais.

---

## Home

A Home será responsável por apresentar uma visão geral do The AAA Archive.

Ela poderá exibir:

* total de jogos da Foundation Collection;
* total de desenvolvedoras;
* total de franquias;
* total de gêneros;
* linha do tempo da coleção;
* jogos históricos;
* jogos influentes;
* destaques da coleção.

Backend responsável:

```text
site_statistics.py
```

---

## Archive

O **Archive** será o coração do website.

Nele estarão todos os jogos da Foundation Collection.

O usuário poderá:

* pesquisar;
* aplicar filtros;
* ordenar resultados;
* abrir informações individuais de qualquer jogo.

Cada jogo poderá apresentar:

* nome;
* descrição;
* ano de lançamento;
* desenvolvedora;
* franquia;
* gênero;
* notas;
* importância histórica;
* influência histórica;
* jogos relacionados.

Backends responsáveis:

```text
filters.py
search.py
site_statistics.py
```

---

## Awards

A seção **Awards** apresentará o histórico de vencedores e indicados a Game of the Year.

Ela utilizará a base independente `awards.csv`.

Cada ano poderá exibir:

* premiação;
* vencedor;
* indicados.

A base Awards History será independente da Foundation Collection.

Quando um jogo existir nas duas bases, o sistema poderá conectá-las por meio do nome do jogo.

Backend responsável:

```text
awards.py
```

---

## Dashboard

Área destinada às análises gráficas do projeto.

Exemplos:

* distribuição dos gêneros;
* quantidade de jogos por desenvolvedora;
* quantidade de jogos por franquia;
* evolução da coleção ao longo dos anos;
* distribuição por década;
* relação entre jogos da Foundation Collection e jogos indicados ou vencedores de Game of the Year.

O dashboard já possui uma primeira versão funcional em Streamlit.

No futuro, ele poderá ser expandido com mais análises, mas a fase atual é apenas de organização do código.

---

# Testes

O projeto possui testes simples com `assert`.

Eles validam os módulos principais e a API.

Comandos atuais:

```bash
python scripts/test_filters.py
python scripts/test_search.py
python scripts/test_site_statistics.py
python scripts/test_awards.py
python api/test_main.py
```

Esses testes devem ser executados após mudanças importantes.

Eles ajudam a garantir que o projeto continue funcionando enquanto novas fases são adicionadas.

---

# Filosofia de Desenvolvimento

O desenvolvimento do The AAA Archive seguirá alguns princípios fundamentais.

* Cada módulo deve possuir apenas uma responsabilidade.
* Toda função criada deve possuir uma utilização real dentro da API, dashboard ou futuro website.
* Antes de criar uma função, deve-se definir qual parte do sistema irá utilizá-la.
* Os módulos devem ser reutilizáveis.
* O código deve permanecer simples, organizado e bem documentado.
* Sempre que possível, evitar duplicação de lógica.
* A estrutura do projeto deve crescer de forma incremental.
* O projeto deve priorizar clareza antes de complexidade.
* A documentação deve acompanhar o estado real do projeto.
* Mudanças grandes devem ser feitas apenas depois de checkpoints claros.

---

# Fluxo de Desenvolvimento

Novas funcionalidades deverão seguir uma sequência simples:

```text
Definir a funcionalidade

↓

Identificar onde ela será utilizada no sistema

↓

Definir o módulo responsável

↓

Implementar a função

↓

Criar ou atualizar testes

↓

Documentar

↓

Atualizar README ou checkpoints, se necessário
```

Esse fluxo garante que o projeto cresça de forma organizada e que todo código desenvolvido possua uma finalidade clara.

---

# Estado Atual

A fase atual do projeto é:

```text
API inicial concluída
↓
Dashboard inicial concluído
↓
Organização leve antes do PostgreSQL
```

Concluído:

* datasets CSV;
* backend modular com Pandas;
* filtros;
* busca;
* estatísticas;
* módulo de awards;
* testes dos módulos;
* API inicial com FastAPI;
* teste da API;
* dashboard inicial com Streamlit;
* documentação inicial da API;
* documentação inicial do dashboard;
* README atualizado.

Em andamento:

* alinhamento da documentação;
* preparação para organizar o `dashboard/app.py`.

Próxima etapa prática:

```text
Organizar dashboard/app.py sem alterar visual nem adicionar funcionalidades grandes.
```

---

# Próximos Passos

A ordem recomendada para a continuidade do projeto é:

```text
1. Confirmar git status e fazer commit/push se necessário.
2. Organizar dashboard/app.py com uma refatoração leve.
3. Manter o visual atual do dashboard.
4. Manter as funcionalidades atuais do dashboard.
5. Revisar requirements.txt.
6. Criar docs/postgresql_plan.md.
7. Planejar a migração dos CSVs para PostgreSQL.
8. Iniciar a migração para PostgreSQL.
9. Futuramente, melhorar a organização interna da API.
10. Futuramente, construir um website próprio para o The AAA Archive.
```

Nesta fase, não serão adicionados novos endpoints à API.

---

# Visão de Longo Prazo

Ao final do desenvolvimento, o The AAA Archive poderá possuir:

* Foundation Collection consolidada;
* Awards History organizada;
* backend modular em Python;
* banco de dados PostgreSQL;
* API mais robusta;
* dashboard analítico mais completo;
* website próprio para exploração da coleção;
* documentação técnica consistente;
* possível expansão editorial através de novas coleções.

Mais do que um catálogo de jogos, o projeto pretende se tornar um arquivo digital organizado, escalável e preparado para evoluir continuamente sem perder sua simplicidade.

O The AAA Archive também deve servir como projeto de portfólio, demonstrando evolução prática em:

* Python;
* Pandas;
* análise de dados;
* FastAPI;
* Streamlit;
* organização de software;
* documentação;
* testes;
* Git/GitHub;
* futura integração com PostgreSQL.
