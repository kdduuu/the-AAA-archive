# Project Conventions — The AAA Archive

# Objetivo

Este documento define os padrões adotados durante o desenvolvimento do **The AAA Archive**.

Seu objetivo é garantir consistência, organização e clareza ao longo da evolução do projeto, servindo como referência para futuras implementações, manutenções e revisões.

O The AAA Archive é um projeto pessoal e educacional, mas deve ser desenvolvido com uma mentalidade próxima de um projeto profissional.

Isso significa que cada arquivo, função, módulo e documento deve existir por um motivo claro dentro do sistema.

---

# Filosofia do Projeto

O **The AAA Archive** é um projeto pessoal desenvolvido por **Kadu Almeida** para estudar:

* Python;
* Pandas;
* Análise de Dados;
* Engenharia de Software;
* Backend;
* API;
* Dashboard;
* Git e GitHub;
* futuramente PostgreSQL;
* futuramente desenvolvimento web mais completo.

Embora o projeto tenha finalidade educacional, todas as decisões devem buscar organização, clareza e evolução incremental.

O projeto não deve crescer de forma bagunçada.

Antes de adicionar uma nova funcionalidade, deve-se pensar:

> Isso realmente ajuda o produto ou só aumenta a complexidade?

Toda funcionalidade implementada deve possuir uma aplicação real dentro do sistema.

O projeto deve priorizar:

* clareza antes de complexidade;
* organização antes de velocidade;
* aprendizado antes de atalhos;
* evolução gradual antes de grandes refatorações;
* código simples antes de estruturas exageradas.

---

# Stack Tecnológica

## Stack Atual

Atualmente, o projeto utiliza:

* Python;
* Pandas;
* CSV;
* FastAPI;
* Streamlit;
* Git;
* GitHub;
* VS Code.

## Dados

Atualmente, os dados são armazenados em arquivos CSV:

* `data/games.csv`;
* `data/awards.csv`.

## API

A API atual utiliza:

* FastAPI;
* Pandas;
* JSON;
* leitura de CSV.

A API ainda não utiliza banco de dados.

## Dashboard

O dashboard atual utiliza:

* Streamlit;
* Pandas;
* `st.tabs()`;
* `st.sidebar`;
* `st.metric`;
* `st.bar_chart`;
* `st.dataframe`;
* cache com `@st.cache_data`.

## Stack Futura

Futuramente, o projeto poderá utilizar:

* PostgreSQL;
* SQL;
* possível frontend separado;
* possível website próprio;
* organização mais avançada da API com routers;
* organização mais avançada do dashboard com componentes.

Essas tecnologias futuras não devem ser adicionadas antes de uma etapa clara de planejamento.

---

# Estrutura Atual do Projeto

A estrutura atual do projeto é:

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

O projeto já possui:

* datasets principais;
* módulos de backend;
* API inicial;
* dashboard inicial;
* testes simples;
* documentação técnica.

A estrutura poderá evoluir conforme o crescimento do projeto, mas sempre preservando a separação de responsabilidades.

---

# Convenções de Nomenclatura

## Arquivos

Utilizar sempre **snake_case** para arquivos Python e documentos internos.

Exemplos:

```text
games.csv
awards.csv
load_data.py
filters.py
search.py
site_statistics.py
awards.py
api_plan.md
api_checkpoint.md
dashboard_plan.md
dashboard_checkpoint.md
project_context.md
project_blueprint.md
project_conventions.md
```

Evitar nomes genéricos ou inconsistentes.

Exemplos ruins:

```text
coisas.py
teste2.py
dadosnovos.csv
arquivo_final_final.py
```

---

## Pastas

Pastas devem ter nomes simples, objetivos e em letras minúsculas.

Exemplos:

```text
api/
data/
docs/
dashboard/
scripts/
assets/
notebooks/
```

Evitar nomes longos ou confusos.

---

## Variáveis

Utilizar sempre **snake_case**.

Exemplos:

```python
nome_jogo
ano_lancamento
developer_name
jogos_filtrados
dados_awards
```

As variáveis devem indicar claramente o que armazenam.

---

## Funções

Utilizar sempre **snake_case**.

Exemplos:

```python
carregar_dataset()
carregar_awards()
listar_jogos_por_genero()
buscar_vencedor_por_ano()
gerar_estatisticas_home()
```

Os nomes das funções devem deixar claro o que elas fazem.

Evitar nomes vagos como:

```python
fazer()
pegar()
coisa()
processar_dados()
```

Quando possível, o nome da função deve indicar ação + alvo.

Exemplos:

```python
listar_jogos_por_developer()
pesquisar_jogos_por_nome()
listar_vencedores_na_foundation()
```

---

## Classes

Caso o projeto passe a utilizar classes no futuro, utilizar **PascalCase**.

Exemplos:

```python
Game
Developer
GameAward
DatabaseConnection
```

Atualmente, o projeto ainda trabalha principalmente com funções e módulos simples.

---

## Constantes

Utilizar **UPPER_CASE**.

Exemplos:

```python
DEFAULT_PATH
DATA_PATH
GAMES_CSV_PATH
AWARDS_CSV_PATH
PROJECT_VERSION
```

Constantes devem ser usadas para valores fixos e reutilizados.

---

# Organização do Código

Cada arquivo deve possuir uma responsabilidade principal.

Exemplos:

```text
load_data.py
```

Responsável pelo carregamento dos dados.

```text
filters.py
```

Responsável pelos filtros da Foundation Collection.

```text
search.py
```

Responsável pela pesquisa textual da Foundation Collection.

```text
site_statistics.py
```

Responsável pelas estatísticas da Foundation Collection.

```text
awards.py
```

Responsável pelas consultas da base Awards History.

```text
api/main.py
```

Responsável por expor os dados através da API FastAPI.

```text
dashboard/app.py
```

Responsável pela interface visual do dashboard Streamlit.

Evitar misturar responsabilidades diferentes no mesmo módulo.

Por exemplo:

* filtros não devem carregar arquivos diretamente se isso já é função do `load_data.py`;
* funções de awards não devem ficar dentro de `site_statistics.py`;
* lógica da API não deve ser duplicada dentro do dashboard;
* regras de curadoria não devem ficar espalhadas sem documentação.

---

# Organização das Funções

Cada função deve resolver apenas um problema.

Sempre que possível, uma função deve:

* receber dados;
* executar uma tarefa clara;
* retornar um resultado.

Funções pequenas são mais fáceis de testar, reutilizar e manter.

Toda função criada deve possuir uma utilidade real no projeto.

Antes de criar uma nova função, deve-se responder:

> Qual parte do sistema utilizará este código?

Exemplos de boas funções:

```python
listar_jogos_por_genero()
listar_jogos_por_decada()
buscar_vencedor_por_ano()
contar_total_jogos()
```

Essas funções são boas porque possuem nomes claros e responsabilidades específicas.

---

# Comentários

Os comentários possuem finalidade didática.

Eles devem ajudar no aprendizado e na manutenção do projeto.

Comentários devem:

* explicar conceitos importantes;
* contextualizar decisões;
* facilitar o entendimento de trechos menos óbvios;
* explicar o motivo de uma escolha técnica;
* ajudar quem está estudando o código.

Evitar comentários que apenas repetem o que o código já informa.

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

Como o projeto também serve para estudo, comentários didáticos são bem-vindos, desde que não deixem o código poluído.

---

# Filosofia de Desenvolvimento

O desenvolvimento do The AAA Archive segue uma abordagem incremental.

Antes de implementar qualquer funcionalidade, deve-se responder:

> Qual parte do sistema utilizará este código?

Toda funcionalidade deverá possuir uma aplicação prática no produto.

Exemplos:

```text
Home / estatísticas gerais
→ site_statistics.py
```

```text
Archive / filtros
→ filters.py
```

```text
Archive / busca textual
→ search.py
```

```text
Awards / vencedores e indicados
→ awards.py
```

```text
API
→ reutiliza os módulos existentes
```

```text
Dashboard
→ reutiliza os módulos existentes e exibe os dados visualmente
```

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

Cada linha representa um jogo da Foundation Collection.

A estrutura oficial desse dataset encontra-se documentada em:

```text
docs/data_dictionary.md
```

Colunas atuais:

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

---

## Awards History

Arquivo:

```text
data/awards.csv
```

Esse arquivo representa o histórico de vencedores e indicados a prêmios de Game of the Year.

A estrutura oficial desse dataset encontra-se documentada em:

```text
docs/awards_dictionary.md
```

Colunas atuais:

```text
ano
premiacao
jogo
status
```

A base Awards History é independente da Foundation Collection.

No entanto, as duas bases podem ser comparadas pelo nome do jogo:

```text
awards.csv → jogo
games.csv  → nome
```

Essa comparação permite identificar:

* jogos vencedores que já fazem parte da Foundation Collection;
* jogos indicados que já fazem parte da Foundation Collection;
* jogos premiados ou indicados que ainda estão fora da Foundation Collection.

No futuro, os dados poderão ser migrados para PostgreSQL.

Essa migração deverá ser planejada antes de ser implementada.

---

# Fontes dos Dados

Sempre que possível, utilizar fontes oficiais ou verificáveis.

## Dados técnicos dos jogos

Possíveis fontes:

* IGDB;
* Metacritic;
* páginas oficiais;
* documentações públicas confiáveis;
* sites reconhecidos da indústria.

## Dados de premiações

Possíveis fontes:

* registros oficiais das premiações;
* páginas oficiais;
* bases públicas confiáveis;
* fontes jornalísticas reconhecidas, quando necessário.

## Conteúdo editorial

O conteúdo editorial é produzido para o The AAA Archive.

Exemplos:

* descrição;
* nota Kadu;
* nota Pavam;
* marcação de histórico importante;
* marcação de histórico influente;
* critérios de curadoria;
* textos explicativos.

Essas informações fazem parte da identidade editorial do projeto.

---

# API

A API está localizada em:

```text
api/main.py
```

Ela foi criada com FastAPI.

A API inicial está concluída e fechada por enquanto.

Ela atualmente:

* lê dados de CSV;
* utiliza Pandas;
* reutiliza os módulos da pasta `scripts/`;
* retorna respostas em JSON;
* não altera os dados.

A API ainda não possui:

* cadastro;
* edição;
* exclusão;
* autenticação;
* banco de dados;
* routers separados.

Nesta fase, não devem ser adicionados novos endpoints.

A API só deverá voltar a evoluir depois da organização do dashboard e do planejamento da migração para PostgreSQL.

---

## Endpoints Atuais

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

---

# Dashboard

O dashboard está localizado em:

```text
dashboard/app.py
```

Ele foi criado com Streamlit.

O dashboard inicial está funcionando e possui:

* abas com `st.tabs()`;
* aba Foundation Collection;
* aba Awards History;
* cache com `@st.cache_data`;
* filtros interativos na sidebar;
* busca textual;
* métricas principais;
* gráficos simples;
* tabelas dinâmicas;
* seção Recorte Editorial;
* jogos historicamente importantes;
* jogos historicamente influentes;
* consulta de Awards por ano;
* histórico de vencedores;
* comparação entre Awards History e Foundation Collection.

A próxima etapa relacionada ao dashboard é organizar melhor o arquivo `dashboard/app.py`.

Essa organização deve seguir uma refatoração leve.

A opção preferida para a fase atual é:

```text
dashboard/
  app.py
  dashboard_helpers.py
```

O objetivo é separar funções auxiliares sem quebrar o entendimento do arquivo principal.

Nesta fase, não se deve alterar:

* visual;
* fluxo principal;
* filtros existentes;
* abas existentes;
* funcionalidades principais.

Também não é recomendado, por enquanto, criar uma estrutura maior como:

```text
dashboard/
  components/
    sidebar.py
    foundation_tab.py
    awards_tab.py
```

Essa estrutura poderá ser considerada no futuro, quando o dashboard crescer mais.

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

Se todos os testes passarem, significa que os módulos atuais e a API inicial continuam funcionando corretamente.

Após refatorações, principalmente no dashboard ou nos módulos reutilizados, os testes devem ser executados novamente.

---

# Requirements

O arquivo de dependências do projeto é:

```text
requirements.txt
```

Ele deve conter apenas nomes de pacotes e versões necessárias para rodar o projeto.

Exemplo de conteúdo esperado:

```text
pandas
fastapi
uvicorn
streamlit
```

Comandos como o exemplo abaixo não devem ficar dentro do arquivo:

```text
pip freeze > requirements.txt
```

Esse comando serve para gerar o arquivo, não para ser listado como dependência.

A revisão do `requirements.txt` será feita após a organização do dashboard e antes do planejamento do PostgreSQL.

---

# Padrão dos Commits

Utilizar mensagens curtas, objetivas e descritivas.

Exemplos:

```text
docs: update project context
docs: update project blueprint
docs: update project conventions
docs: update dashboard plan
docs: update api checkpoint

feat: create search module
feat: add site statistics
feat: add awards history module
feat: add awards foundation integration
feat: create initial fastapi api
feat: create streamlit dashboard

refactor: organize dashboard helpers
refactor: improve filters

fix: correct metacritic values
fix: adjust awards comparison

data: update foundation collection
data: update awards history

test: add api tests
test: update awards tests
```

O commit deve deixar claro o tipo de alteração feita.

---

# Ordem Recomendada Antes de Grandes Mudanças

Antes de iniciar uma nova fase grande, seguir esta ordem:

```text
1. Verificar o estado atual do projeto.
2. Confirmar se os testes passam.
3. Atualizar documentação, se necessário.
4. Fazer commit das mudanças estáveis.
5. Planejar a próxima fase.
6. Só depois implementar.
```

Essa ordem evita misturar muitas mudanças diferentes no mesmo momento.

---

# Fase Atual do Projeto

A fase atual é uma organização curta antes da migração para PostgreSQL.

Concluído:

* datasets CSV;
* módulos principais;
* testes dos módulos;
* API inicial;
* teste da API;
* dashboard inicial;
* documentação inicial da API;
* documentação inicial do dashboard;
* README atualizado.

Em andamento:

* alinhamento dos documentos principais;
* preparação para organizar o `dashboard/app.py`.

Próximas etapas:

```text
1. Confirmar git status e fazer commit/push se necessário.
2. Organizar dashboard/app.py com uma refatoração leve.
3. Não alterar visual nem funcionalidades principais do dashboard.
4. Revisar requirements.txt.
5. Criar docs/postgresql_plan.md.
6. Só depois iniciar a migração para PostgreSQL.
```

---

# Princípios do Projeto

Durante todo o desenvolvimento serão seguidos os seguintes princípios:

* Clareza acima da complexidade.
* Organização acima da velocidade.
* Qualidade acima da quantidade.
* Documentação antes de grandes mudanças.
* Evolução incremental.
* Código limpo.
* Código reutilizável.
* Responsabilidade única por módulo.
* Testes simples, mas úteis.
* Projeto orientado a portfólio.
* Toda função deve possuir finalidade real.
* A estrutura deve permanecer simples enquanto o projeto cresce.
* A API não deve receber novos endpoints nesta fase.
* O dashboard deve ser organizado sem mudar sua proposta atual.
* A migração para PostgreSQL deve ser planejada antes da implementação.

---

# Objetivo Final

Construir um sistema completo para preservar, organizar, analisar e disponibilizar informações sobre videogames através de:

* backend modular;
* datasets bem estruturados;
* API;
* dashboard analítico;
* banco de dados PostgreSQL;
* futuro website;
* documentação consistente.

Todo o desenvolvimento deverá priorizar simplicidade, organização e escalabilidade.

O The AAA Archive deve evoluir continuamente sem perder sua consistência arquitetural e sem se tornar complexo antes da hora.
