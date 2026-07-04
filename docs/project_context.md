# Project Context — The AAA Archive

## Sobre o Projeto

O **The AAA Archive** é um projeto pessoal desenvolvido por **Kadu Almeida** para estudar Análise de Dados, Engenharia de Software, Backend, API, Dashboard e futuramente Banco de Dados e Website.

A proposta do projeto é construir um arquivo digital curado sobre jogos **AAA single-player historicamente relevantes**, usando um tema de interesse pessoal como base para aprender tecnologias reais de desenvolvimento.

O projeto começou como uma forma de praticar **Python** e **Pandas** com um dataset próprio, mas evoluiu para uma aplicação mais completa, composta por:

* dataset principal em CSV;
* módulos de leitura, filtros, busca e estatísticas;
* histórico de premiações de Game of the Year;
* API com FastAPI;
* dashboard com Streamlit;
* documentação técnica;
* testes simples para validar os módulos principais.

O desenvolvimento acontece de forma incremental. Cada etapa tem o objetivo de ensinar uma parte nova do processo, sem pular fundamentos e sem transformar o projeto em algo complexo demais antes da hora.

---

## Objetivos

O projeto possui objetivos técnicos, educacionais e de portfólio.

Durante seu desenvolvimento, busca-se:

* Aprender Python aplicado a um projeto real.
* Praticar Pandas com datasets próprios.
* Organizar dados em arquivos CSV antes de migrar para banco de dados.
* Criar módulos reutilizáveis para leitura, filtros, busca, estatísticas e premiações.
* Desenvolver uma API com FastAPI para disponibilizar os dados em JSON.
* Criar um dashboard com Streamlit para análise e visualização dos dados.
* Praticar Git e GitHub durante a evolução do projeto.
* Aplicar boas práticas de organização de pastas, documentação e testes.
* Preparar o projeto para uma futura migração para PostgreSQL.
* Construir um projeto sólido para portfólio.

---

## Filosofia Editorial

O **The AAA Archive** não pretende catalogar todos os jogos já produzidos.

A proposta do projeto é criar uma coleção curada de jogos considerados importantes para a história dos videogames, principalmente dentro do recorte de jogos **AAA single-player**.

Essa coleção principal recebe o nome de **Foundation Collection**.

A **Foundation Collection** representa o núcleo permanente do projeto. Ela reúne jogos selecionados por critérios como:

* importância histórica;
* influência na indústria;
* impacto cultural;
* reconhecimento crítico;
* relevância dentro de uma franquia;
* contribuição para gêneros, mecânicas ou narrativas.

O projeto também possui uma base separada chamada **Awards History**, responsável por registrar vencedores e indicados a prêmios de **Game of the Year**.

É importante deixar claro que:

* a Foundation Collection é uma curadoria editorial;
* o Awards History é um histórico de premiações;
* um jogo pode estar nas duas bases;
* um jogo pode aparecer no Awards History e não fazer parte da Foundation Collection;
* o objetivo não é transformar o projeto em um catálogo infinito.

No futuro, novas coleções poderão ser criadas, como **Expansion Collections**, mas sempre mantendo a identidade editorial do Archive.

---

## Stack Tecnológica Atual

## Desenvolvimento

* Python
* Pandas
* CSV
* FastAPI
* Streamlit
* Git
* GitHub
* VS Code

## Dados

* `games.csv`
* `awards.csv`

## API

* FastAPI
* JSON
* CSV + Pandas como fonte de dados atual

## Dashboard

* Streamlit
* Pandas
* Gráficos simples com `st.bar_chart`
* Filtros interativos
* Busca textual
* Métricas principais
* Tabelas dinâmicas

## Futuro

* PostgreSQL
* Website
* Possível frontend separado
* Melhor organização interna da API
* Possível uso de routers no FastAPI
* Possível expansão do dashboard

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

Essa estrutura representa a fase atual do projeto.

O projeto já possui uma API inicial, um dashboard inicial e módulos de apoio funcionando com CSV e Pandas.

---

## Datasets

## `data/games.csv`

Dataset principal da **Foundation Collection**.

Atualmente, contém cerca de 66 jogos curados.

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

Esse dataset representa o núcleo editorial do projeto.

---

## `data/awards.csv`

Dataset responsável pelo histórico de premiações de Game of the Year.

Atualmente, contém cerca de 127 registros.

Colunas principais:

```text
ano
premiacao
jogo
status
```

Esse dataset registra vencedores e indicados de premiações como:

* Spike Video Game Awards;
* VGX;
* The Game Awards.

---

## Módulos Implementados

## `load_data.py`

Responsável por carregar os datasets do projeto.

Funções principais:

* `carregar_dataset()`
* `carregar_awards()`

---

## `filters.py`

Responsável por filtros simples na Foundation Collection.

Funções principais:

* `listar_jogos_por_developer()`
* `listar_jogos_por_genero()`
* `listar_jogos_por_franquia()`
* `listar_jogos_por_ano()`
* `listar_jogos_por_decada()`

---

## `search.py`

Responsável pela pesquisa textual de jogos.

Funções principais:

* `pesquisar_jogos()`
* `pesquisar_jogos_por_nome()`

---

## `site_statistics.py`

Responsável por estatísticas da Foundation Collection.

Funções principais:

* `contar_total_jogos()`
* `contar_total_developers()`
* `contar_total_franquias()`
* `contar_total_generos()`
* `listar_quantidade_por_genero()`
* `listar_quantidade_por_developer()`
* `listar_quantidade_por_franquia()`
* `listar_quantidade_por_decada()`
* `listar_jogos_historicos()`
* `listar_jogos_influentes()`
* `gerar_estatisticas_home()`

---

## `awards.py`

Responsável pelas consultas relacionadas ao Awards History.

Funções principais:

* `listar_premiacoes()`
* `listar_anos_disponiveis()`
* `listar_jogos_por_ano()`
* `buscar_vencedor_por_ano()`
* `listar_indicados_por_ano()`
* `listar_vencedores()`
* `listar_jogos_por_premiacao()`
* `listar_vencedores_na_foundation()`
* `listar_indicados_na_foundation()`
* `listar_jogos_awards_fora_da_foundation()`

---

## API

A API está localizada em:

```text
api/main.py
```

A API inicial foi concluída e está funcionando com **FastAPI**.

Ela ainda usa **CSV + Pandas** como fonte de dados.

A API atualmente apenas lê dados e retorna respostas em JSON.

Ela ainda não possui:

* cadastro de dados;
* edição;
* exclusão;
* autenticação;
* banco de dados;
* routers separados.

Essa decisão é intencional, pois a primeira versão da API foi criada para consolidar a leitura e exposição dos dados antes da migração para PostgreSQL.

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

A API inicial está fechada por enquanto.

Não há intenção de adicionar novos endpoints nesta fase.

---

## Dashboard

O dashboard está localizado em:

```text
dashboard/app.py
```

Ele foi desenvolvido com **Streamlit** e representa a primeira versão visual do projeto.

O dashboard já possui:

* `st.tabs()`;
* aba Foundation Collection;
* aba Awards History;
* cache com `@st.cache_data`;
* filtros interativos na sidebar;
* busca textual;
* métricas principais;
* gráficos simples;
* tabelas dinâmicas;
* seção de Recorte Editorial;
* jogos historicamente importantes;
* jogos historicamente influentes;
* consulta de Awards por ano;
* histórico de vencedores;
* comparação entre Awards History e Foundation Collection.

O dashboard inicial está concluído.

A próxima etapa não é adicionar novas funcionalidades, mas organizar melhor o arquivo `dashboard/app.py`, pois ele cresceu bastante.

---

## Testes

O projeto possui testes simples para validar os módulos principais.

Comandos utilizados:

```bash
python scripts/test_filters.py
python scripts/test_search.py
python scripts/test_site_statistics.py
python scripts/test_awards.py
python api/test_main.py
```

Esses testes ajudam a garantir que os filtros, buscas, estatísticas, consultas de premiações e endpoints principais da API continuam funcionando após alterações.

---

## Documentação

A documentação oficial do projeto é composta por:

```text
README.md
docs/project_context.md
docs/project_blueprint.md
docs/project_conventions.md
docs/foundation_collection.md
docs/data_dictionary.md
docs/awards_dictionary.md
docs/api_plan.md
docs/api_checkpoint.md
docs/dashboard_plan.md
docs/dashboard_checkpoint.md
```

Cada documento possui uma responsabilidade específica.

## Responsabilidade dos principais documentos

```text
project_context.md
```

Explica o contexto geral do projeto, seus objetivos, filosofia editorial, stack, estrutura atual e fase de desenvolvimento.

```text
project_blueprint.md
```

Define a visão de produto do The AAA Archive, incluindo suas áreas principais e possíveis evoluções futuras.

```text
project_conventions.md
```

Define convenções de organização, nomenclatura, testes, documentação e boas práticas do projeto.

```text
foundation_collection.md
```

Documenta a curadoria principal de jogos do projeto.

```text
data_dictionary.md
```

Explica as colunas e regras do dataset `games.csv`.

```text
awards_dictionary.md
```

Explica as colunas e regras do dataset `awards.csv`.

```text
api_plan.md
```

Registra o planejamento inicial da API.

```text
api_checkpoint.md
```

Registra o estado atual da API inicial após sua conclusão.

```text
dashboard_plan.md
```

Registra o planejamento inicial do dashboard.

```text
dashboard_checkpoint.md
```

Registra o estado atual do dashboard após sua primeira versão funcional.

---

## Estado Atual

O projeto está em uma fase de organização antes da migração para PostgreSQL.

## Concluído

* Planejamento inicial do projeto.
* Estrutura inicial do repositório.
* Foundation Collection definida.
* Dataset `games.csv` estruturado.
* Dataset `awards.csv` estruturado.
* Leitura de dados com Pandas.
* Módulo de filtros.
* Módulo de busca.
* Módulo de estatísticas.
* Módulo de awards.
* Testes dos módulos principais.
* API inicial com FastAPI.
* Teste da API.
* Dashboard inicial com Streamlit.
* Documentação inicial da API.
* Documentação inicial do dashboard.
* README atualizado com endpoints e comandos principais.

## Fase Atual

A fase atual é uma organização curta antes do PostgreSQL.

O foco agora é:

* confirmar o estado do Git;
* organizar melhor o arquivo `dashboard/app.py`;
* não alterar o visual do dashboard;
* não adicionar grandes funcionalidades;
* não adicionar novos endpoints na API;
* revisar `requirements.txt`;
* criar `docs/postgresql_plan.md`;
* só depois iniciar a migração para PostgreSQL.

---

## Próximas Etapas

A ordem recomendada para a continuidade do projeto é:

```text
1. Confirmar git status e fazer commit/push se necessário.
2. Organizar dashboard/app.py com uma refatoração leve.
3. Manter o visual e as funcionalidades atuais do dashboard.
4. Revisar requirements.txt.
5. Criar docs/postgresql_plan.md.
6. Planejar a migração dos CSVs para PostgreSQL.
7. Iniciar a integração do projeto com banco de dados.
8. Futuramente, melhorar a organização interna da API.
9. Futuramente, construir um website próprio para o The AAA Archive.
```

---

## Diretrizes do Projeto

Durante todo o desenvolvimento, serão seguidos os seguintes princípios:

* Organização antes da implementação.
* Documentação antes de grandes mudanças.
* Evolução incremental.
* Código simples antes de código complexo.
* Clareza acima de abstração exagerada.
* Cada módulo deve possuir uma responsabilidade clara.
* Toda funcionalidade deve ter uma aplicação real dentro do produto.
* A API não deve receber novas funcionalidades nesta fase.
* O dashboard deve ser organizado sem mudar sua proposta visual atual.
* A migração para PostgreSQL deve ser planejada antes de ser implementada.

---

## Decisões Técnicas Atuais

Algumas decisões importantes da fase atual:

* O projeto continuará usando CSV + Pandas até a fase de PostgreSQL.
* A API inicial está fechada.
* O dashboard inicial está concluído.
* O foco imediato é organização, não expansão.
* O arquivo `dashboard/app.py` deve ser dividido com calma.
* A primeira organização do dashboard deve evitar uma estrutura exagerada.
* A opção preferida para o momento é criar um arquivo auxiliar, como `dashboard_helpers.py`, antes de separar tudo em múltiplos componentes.
* A revisão do `requirements.txt` deve acontecer depois da organização documental e antes do PostgreSQL.

---

## Objetivo Final

O objetivo final do **The AAA Archive** é construir um sistema completo capaz de preservar, organizar, analisar e disponibilizar informações sobre jogos historicamente relevantes.

Mais do que um catálogo de jogos, o projeto busca se tornar um arquivo digital consistente, com identidade editorial própria e preparado para evoluir tecnicamente.

No longo prazo, o projeto poderá contar com:

* banco de dados PostgreSQL;
* API mais robusta;
* dashboard analítico mais completo;
* website próprio;
* novas coleções editoriais;
* documentação mais profunda;
* visualização histórica da indústria dos games.

O The AAA Archive é, ao mesmo tempo, um projeto de estudo, um projeto de portfólio e uma tentativa de transformar gosto pessoal por videogames em uma aplicação real de tecnologia.
