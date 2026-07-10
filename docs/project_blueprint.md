# Project Blueprint — The AAA Archive

> **Este documento representa a visão oficial de produto do The AAA Archive.**
>
> Antes de implementar novas funcionalidades, alterar a arquitetura ou iniciar uma nova fase, este documento deve ser utilizado como uma das principais referências.
>
> O blueprint define o que o projeto pretende ser, como suas áreas se relacionam e quais princípios devem orientar sua evolução.

---

# O que é o The AAA Archive?

O **The AAA Archive** é um projeto pessoal de desenvolvimento de software criado por **Kadu Almeida**.

Seu objetivo é construir um arquivo digital curado dedicado à preservação, organização e exploração da história dos videogames, com foco em jogos **AAA single-player historicamente relevantes**.

O projeto nasceu como uma forma de estudar Python, Pandas e análise de dados utilizando um dataset próprio, mas evoluiu para uma aplicação composta por diferentes camadas:

* datasets editoriais em CSV;
* banco de dados PostgreSQL;
* backend modular em Python;
* camada centralizada de acesso aos dados;
* testes;
* API com FastAPI;
* dashboard com Streamlit;
* documentação técnica;
* futura aplicação web própria.

A arquitetura atual pode ser resumida da seguinte forma:

```text
Datasets editoriais
↓
PostgreSQL
↓
Backend Python
↓
API FastAPI
↓
Dashboard Streamlit
↓
Futura aplicação web
```

A **Foundation Collection** representa o núcleo principal do projeto.

Ela reúne uma seleção cuidadosamente curada de jogos considerados relevantes para a história da indústria.

Além dela, o projeto possui uma base independente chamada **Awards History**, responsável por armazenar vencedores e indicados a premiações de **Game of the Year**.

O objetivo do The AAA Archive não é catalogar todos os jogos existentes.

A proposta é construir uma coleção:

* consistente;
* organizada;
* editorialmente clara;
* historicamente relevante;
* tecnicamente estruturada;
* preparada para crescer sem perder identidade.

---

# Natureza do Projeto

O The AAA Archive possui quatro dimensões principais.

## Projeto Editorial

O projeto seleciona e organiza jogos segundo critérios próprios de importância histórica.

Ele não funciona como um banco de dados genérico ou uma enciclopédia completa.

---

## Projeto de Software

O Archive é construído como uma aplicação real, com:

* dados;
* banco;
* backend;
* API;
* dashboard;
* testes;
* documentação;
* futura interface web.

---

## Projeto Educacional

Cada fase é utilizada para aprender uma nova tecnologia ou conceito.

A aprendizagem acontece por meio da evolução do próprio sistema.

---

## Projeto de Portfólio

O projeto demonstra conhecimentos e evolução prática em:

* Python;
* Pandas;
* PostgreSQL;
* SQL;
* FastAPI;
* Streamlit;
* análise de dados;
* organização de software;
* testes;
* documentação;
* Git e GitHub;
* futuramente, desenvolvimento front-end.

---

# Objetivos do Projeto

O desenvolvimento do The AAA Archive possui objetivos técnicos, educacionais e editoriais.

Os principais objetivos são:

* construir uma Foundation Collection organizada;
* manter uma documentação editorial consistente;
* preservar um histórico de premiações de Game of the Year;
* organizar os dados em CSV e PostgreSQL;
* desenvolver um backend reutilizável;
* disponibilizar os dados através de uma API;
* criar visualizações e análises com Streamlit;
* praticar testes e validação;
* aplicar boas práticas de organização;
* manter a documentação alinhada ao código;
* construir uma aplicação web própria;
* criar uma base sólida para portfólio.

Todo código desenvolvido deve possuir uma finalidade prática dentro do produto.

Novas tecnologias não devem ser adicionadas apenas por popularidade ou complexidade.

---

# Princípios Editoriais

A Foundation Collection é uma curadoria.

Um jogo pode ser incluído por critérios como:

* importância histórica;
* influência sobre outros jogos;
* contribuição para a indústria;
* impacto cultural;
* reconhecimento crítico;
* relevância para uma franquia;
* inovação técnica;
* inovação narrativa;
* inovação mecânica;
* importância para determinado gênero;
* força editorial dentro da proposta do Archive.

A presença em premiações não garante automaticamente a entrada na Foundation Collection.

Da mesma forma, um jogo não precisa ter vencido grandes prêmios para ser considerado historicamente relevante.

---

# Bases Principais

O projeto trabalha com duas bases editoriais:

```text
data/games.csv
data/awards.csv
```

Esses arquivos são importados para PostgreSQL.

Fluxo atual:

```text
CSV
↓
scripts/import_to_postgres.py
↓
PostgreSQL
↓
API e Dashboard
```

Os CSVs continuam sendo a fonte editorial original.

O PostgreSQL funciona como fonte operacional da aplicação.

---

# Foundation Collection

Arquivo editorial:

```text
data/games.csv
```

Tabela no PostgreSQL:

```text
games
```

A Foundation Collection representa o núcleo principal do The AAA Archive.

Cada linha representa um jogo da coleção.

Quantidade atual:

```text
66 jogos
```

A base é utilizada por:

* filtros;
* pesquisa textual;
* estatísticas;
* API;
* dashboard;
* futura aplicação web;
* futuras análises históricas;
* futuras páginas individuais de jogos.

Colunas:

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

A Foundation Collection não deve crescer de forma automática ou ilimitada.

A entrada de novos jogos deve ser discutida e justificada editorialmente.

---

# Awards History

Arquivo editorial:

```text
data/awards.csv
```

Tabela no PostgreSQL:

```text
awards
```

A Awards History representa o histórico de vencedores e indicados a prêmios de **Game of the Year**.

Quantidade atual:

```text
127 registros
```

Colunas no CSV:

```text
ano
premiacao
jogo
status
```

A tabela PostgreSQL também possui:

```text
id
```

A Awards History é independente da Foundation Collection.

Isso significa que um jogo pode aparecer no histórico de premiações sem fazer parte da coleção principal.

As duas bases são comparadas pelos campos:

```text
awards.jogo
games.nome
```

Essa comparação permite identificar:

* vencedores presentes na Foundation Collection;
* indicados presentes na Foundation Collection;
* jogos premiados fora da Foundation Collection;
* diferenças entre reconhecimento institucional e curadoria editorial.

Essa separação preserva a identidade do Archive.

---

# Arquitetura Geral

O projeto utiliza uma arquitetura simples e incremental.

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
import_to_postgres.py
│
▼
PostgreSQL
│
├── tabela games
│
└── tabela awards
│
▼
database.py
│
▼
Camada de lógica
│
├── filters.py
├── search.py
├── site_statistics.py
├── awards.py
└── outros módulos
│
├───────────────┐
▼               ▼
API FastAPI     Dashboard Streamlit
│               │
└───────┬───────┘
        ▼
Futura aplicação web
```

Cada camada possui uma função clara:

* os CSVs preservam e recebem a edição editorial;
* o importador envia os dados ao banco;
* PostgreSQL armazena os dados operacionais;
* `database.py` centraliza a conexão e as consultas;
* os módulos executam a lógica;
* a API disponibiliza os dados;
* o dashboard apresenta análises;
* a aplicação web apresentará a experiência final do Archive.

---

# Estrutura Atual do Projeto

```text
The-AAA-Archive/
│
├── api/
│   ├── main.py
│   └── test_main.py
│
├── dashboard/
│   ├── app.py
│   └── dashboard_helpers.py
│
├── data/
│   ├── games.csv
│   └── awards.csv
│
├── database/
│   └── schema.sql
│
├── docs/
│   ├── api_checkpoint.md
│   ├── api_plan.md
│   ├── awards_dictionary.md
│   ├── dashboard_checkpoint.md
│   ├── dashboard_plan.md
│   ├── data_dictionary.md
│   ├── foundation_collection.md
│   ├── postgresql_checkpoint.md
│   ├── postgresql_plan.md
│   ├── project_blueprint.md
│   ├── project_context.md
│   └── project_conventions.md
│
├── scripts/
│   ├── awards.py
│   ├── database.py
│   ├── filters.py
│   ├── import_to_postgres.py
│   ├── load_data.py
│   ├── search.py
│   ├── site_statistics.py
│   ├── test_awards.py
│   ├── test_database.py
│   ├── test_filters.py
│   ├── test_search.py
│   └── test_site_statistics.py
│
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

O arquivo `.env` deve permanecer apenas localmente.

---

# Estrutura dos Módulos

Cada módulo possui uma responsabilidade principal.

---

## `load_data.py`

Responsável por carregar diretamente os datasets editoriais em CSV.

Funções principais:

```text
carregar_dataset()
carregar_awards()
```

Esse módulo continua sendo utilizado por testes e operações baseadas nos arquivos originais.

Ele não é mais a fonte direta da API e do dashboard.

---

## `import_to_postgres.py`

Responsável por importar os datasets para PostgreSQL.

Fluxo:

```text
games.csv
awards.csv
↓
Pandas
↓
PostgreSQL
```

Esse script mantém o banco sincronizado com as fontes editoriais.

---

## `database.py`

Centraliza a conexão e as consultas ao PostgreSQL.

Funções principais:

```text
obter_configuracao_banco()
conectar_postgres()
executar_select()
carregar_games_do_banco()
carregar_awards_do_banco()
contar_games_do_banco()
contar_awards_do_banco()
```

Esse módulo é a porta de entrada operacional dos dados para a API e o dashboard.

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

Esse módulo pode ser reutilizado pela:

* API;
* dashboard;
* futura aplicação web;
* testes.

---

## `search.py`

Responsável pela pesquisa textual.

Funções principais:

```text
pesquisar_jogos()
pesquisar_jogos_por_nome()
```

A pesquisa pode considerar:

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

Informações estatísticas não devem ser escritas manualmente quando puderem ser calculadas a partir dos dados.

---

## `awards.py`

Responsável pelas consultas relacionadas à Awards History.

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

Esse módulo também realiza comparações entre Foundation Collection e Awards History.

---

# PostgreSQL

O PostgreSQL é a fonte operacional atual do projeto.

Banco:

```text
aaa_archive
```

Schema:

```text
public
```

Tabelas:

```text
games
awards
```

Estrutura:

```text
database/schema.sql
```

A integração com PostgreSQL já está concluída.

O banco é utilizado por:

* API;
* dashboard;
* testes de integração;
* futuras camadas da aplicação.

---

# API

A API está localizada em:

```text
api/main.py
```

Ela foi criada com FastAPI.

A versão atual utiliza:

* PostgreSQL;
* Pandas;
* `scripts/database.py`;
* módulos da pasta `scripts/`;
* respostas em JSON.

Fluxo:

```text
FastAPI
↓
database.py
↓
PostgreSQL
```

A API atual possui operações de leitura.

Ela ainda não oferece:

* cadastro;
* edição;
* exclusão;
* autenticação;
* painel administrativo;
* routers separados;
* paginação;
* ordenação avançada;
* filtros combinados.

Essa decisão é intencional.

A API atual foi criada para disponibilizar os dados necessários à exploração da coleção.

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

A versão atual da API está concluída para esta fase.

Novos endpoints devem ser criados somente quando uma necessidade real da aplicação web for identificada.

---

# Dashboard

O dashboard está localizado em:

```text
dashboard/app.py
```

As funções auxiliares estão em:

```text
dashboard/dashboard_helpers.py
```

Ele foi desenvolvido com Streamlit e representa a primeira interface visual do projeto.

Fluxo:

```text
Streamlit
↓
dashboard_helpers.py
↓
database.py
↓
PostgreSQL
```

O dashboard possui:

* abas com `st.tabs()`;
* aba Foundation Collection;
* aba Awards History;
* cache com `@st.cache_data`;
* filtros interativos;
* pesquisa textual;
* métricas;
* gráficos;
* tabelas dinâmicas;
* seção de recorte editorial;
* consulta por ano;
* histórico de vencedores;
* comparação entre as duas bases.

O dashboard está concluído para esta fase.

Ele funciona como ferramenta analítica e protótipo visual, mas não substitui a futura aplicação web.

---

# Visão da Aplicação Web

A aplicação web será a experiência principal do The AAA Archive.

Seu objetivo será transformar os dados, a API e a curadoria editorial em uma experiência visual navegável.

A aplicação não deverá parecer apenas:

* uma tabela;
* um dashboard;
* uma planilha;
* uma documentação técnica;
* um catálogo genérico.

Ela deverá transmitir a identidade de um arquivo histórico e editorial sobre videogames.

A definição detalhada da experiência, stack e identidade visual será feita em uma fase própria de planejamento.

---

# Estrutura Visual Inicial

A visão atual considera quatro áreas principais:

```text
Home
Archive
Awards
Dashboard
```

Essa estrutura ainda poderá ser ajustada durante o planejamento do front-end.

---

# Home

A Home será a porta de entrada do The AAA Archive.

Sua função será apresentar:

* o conceito do projeto;
* a identidade do Archive;
* a Foundation Collection;
* destaques editoriais;
* dados gerais;
* caminhos para exploração.

A Home poderá exibir:

* total de jogos;
* total de desenvolvedoras;
* total de franquias;
* total de gêneros;
* linha do tempo;
* jogos historicamente importantes;
* jogos influentes;
* jogos em destaque;
* acesso à coleção;
* acesso à Awards History.

Fontes responsáveis:

```text
GET /stats/home
site_statistics.py
```

A Home não deverá mostrar todos os dados disponíveis.

Ela deverá funcionar como introdução e convite à exploração.

---

# Archive

O **Archive** será o coração da aplicação web.

Ele apresentará todos os jogos da Foundation Collection.

O usuário poderá:

* pesquisar;
* aplicar filtros;
* explorar por gênero;
* explorar por desenvolvedora;
* explorar por franquia;
* explorar por ano;
* explorar por década;
* ordenar resultados;
* abrir informações individuais.

Cada jogo poderá apresentar:

* nome;
* capa;
* descrição;
* ano;
* gênero;
* desenvolvedora;
* franquia;
* Metacritic;
* nota de Kadu;
* nota de Pavam;
* importância histórica;
* influência histórica;
* jogos relacionados;
* presença em premiações.

Fontes responsáveis:

```text
GET /games
GET /games/search
GET /games/developer
GET /games/genre
GET /games/franchise
GET /games/year
GET /games/decade
```

Módulos relacionados:

```text
filters.py
search.py
site_statistics.py
```

---

# Página Individual do Jogo

Cada jogo poderá possuir uma página própria.

A página deverá apresentar informações de forma editorial, não apenas como campos técnicos.

Possíveis seções:

```text
Identidade do jogo
Contexto histórico
Descrição
Desenvolvimento
Franquia
Importância
Influência
Recepção
Notas
Premiações
Jogos relacionados
```

Nem todas essas informações estão preenchidas atualmente.

A criação dessa página dependerá do enriquecimento da Foundation Collection.

---

# Awards

A seção **Awards** apresentará o histórico de vencedores e indicados a Game of the Year.

Cada edição poderá exibir:

* ano;
* nome da premiação;
* vencedor;
* indicados;
* relação com a Foundation Collection.

Também poderão existir visões como:

* histórico de vencedores;
* vencedores presentes na coleção;
* indicados presentes na coleção;
* jogos fora da Foundation Collection;
* linha do tempo das premiações.

Fontes responsáveis:

```text
GET /awards
GET /awards/winners
GET /awards/{year}
GET /awards/foundation/winners
GET /awards/foundation/nominees
GET /awards/foundation/outside
```

Módulo relacionado:

```text
awards.py
```

---

# Dashboard

O dashboard representa a área analítica do projeto.

Sua função é apresentar padrões e estatísticas.

Exemplos:

* distribuição por gênero;
* jogos por desenvolvedora;
* jogos por franquia;
* evolução por ano;
* distribuição por década;
* jogos históricos;
* jogos influentes;
* relação entre Foundation Collection e Awards History.

A primeira versão já existe em Streamlit.

No futuro, deverá ser decidido se:

* o Streamlit continuará como ferramenta separada;
* algumas análises serão incorporadas à aplicação web;
* o dashboard será publicado;
* ele permanecerá apenas como ferramenta interna.

---

# Navegação Planejada

Uma navegação inicial poderá seguir esta estrutura:

```text
Home
│
├── Archive
│   ├── Todos os jogos
│   ├── Filtros
│   └── Página do jogo
│
├── Awards
│   ├── Histórico
│   ├── Edição por ano
│   └── Comparações
│
├── Dashboard
│
└── Sobre
```

A área **Sobre** poderá explicar:

* conceito do projeto;
* critérios da Foundation Collection;
* metodologia editorial;
* tecnologias utilizadas;
* autoria;
* evolução do projeto.

---

# Relação entre as Camadas

A aplicação web não deve acessar diretamente os CSVs.

Fluxo planejado:

```text
Usuário
↓
Aplicação web
↓
API FastAPI
↓
PostgreSQL
```

O dashboard atual pode continuar utilizando diretamente a camada Python de banco enquanto for uma ferramenta interna.

A aplicação web final deverá preferencialmente consumir a API.

---

# Conteúdo Editorial Pendente

Alguns recursos visuais dependem do preenchimento de campos ainda vazios.

Campos prioritários:

```text
descricao
metacritic
nota_kadu
nota_pavam
historico_importante
historico_influente
```

Também poderão ser adicionados futuramente:

* capa;
* imagem de fundo;
* diretor;
* publisher;
* data completa de lançamento;
* plataformas;
* texto histórico;
* justificativa de inclusão;
* referências.

Esses campos não devem ser adicionados ao banco sem planejamento.

---

# Testes

O projeto possui testes com `assert`.

Comandos:

```bash
python scripts/test_filters.py
python scripts/test_search.py
python scripts/test_site_statistics.py
python scripts/test_awards.py
python scripts/test_database.py
python api/test_main.py
```

Eles validam:

* filtros;
* busca;
* estatísticas;
* premiações;
* conexão com banco;
* leitura das tabelas;
* endpoints da API.

Os testes devem ser executados após mudanças importantes.

---

# Filosofia de Desenvolvimento

O desenvolvimento seguirá princípios fundamentais:

* cada módulo deve possuir uma responsabilidade clara;
* toda função deve possuir uma utilização real;
* antes de criar uma função, deve-se definir onde ela será usada;
* módulos devem ser reutilizáveis;
* duplicação deve ser evitada;
* o código deve permanecer compreensível;
* a estrutura deve crescer gradualmente;
* clareza deve ser priorizada;
* documentação deve acompanhar o código;
* mudanças grandes devem ocorrer após planejamento;
* cada fase deve terminar com testes e checkpoint;
* o projeto não deve adotar complexidade desnecessária.

---

# Fluxo de Desenvolvimento

Novas funcionalidades deverão seguir esta sequência:

```text
Identificar uma necessidade
↓
Definir como ela aparece no produto
↓
Identificar a camada responsável
↓
Planejar dados e comportamento
↓
Implementar
↓
Criar ou atualizar testes
↓
Validar funcionamento
↓
Documentar
↓
Criar checkpoint
```

Esse fluxo evita a criação de código sem finalidade clara.

---

# Estado Atual

A fase PostgreSQL foi concluída.

Concluído:

* datasets CSV;
* Foundation Collection;
* Awards History;
* backend modular;
* filtros;
* pesquisa;
* estatísticas;
* módulo de premiações;
* testes dos módulos;
* API FastAPI;
* testes da API;
* dashboard Streamlit;
* organização do dashboard com arquivo auxiliar;
* banco PostgreSQL;
* tabelas `games` e `awards`;
* `schema.sql`;
* script de importação;
* camada centralizada de banco;
* teste de banco;
* migração da API;
* migração do dashboard;
* documentação da fase PostgreSQL.

---

# Fase Atual de Trabalho

O projeto está encerrando documentalmente a fase PostgreSQL.

Atividades atuais:

* atualização do README;
* atualização do contexto;
* atualização do blueprint;
* atualização das convenções;
* revisão dos dicionários;
* identificação de planos concluídos;
* criação do `.env.example`;
* revisão do `.gitignore`;
* execução final dos testes;
* commit de checkpoint.

O front-end ainda não deve ser iniciado.

---

# Próximos Passos

A ordem recomendada é:

```text
1. Finalizar a atualização da documentação.
2. Criar .env.example.
3. Revisar .gitignore.
4. Confirmar que .env não está rastreado.
5. Executar todos os testes.
6. Criar commit de checkpoint da fase PostgreSQL.
7. Criar frontend_plan.md.
8. Definir a experiência da aplicação.
9. Definir identidade visual.
10. Definir páginas e navegação.
11. Definir como a API será consumida.
12. Escolher a stack de front-end.
13. Criar o primeiro protótipo.
14. Iniciar a implementação.
```

---

# O que Não Deve Ser Decidido Agora

Durante o encerramento documental, ainda não devem ser definidos:

* framework do front-end;
* design final;
* biblioteca de componentes;
* hospedagem;
* autenticação;
* painel administrativo;
* novos endpoints;
* normalização adicional do banco;
* arquitetura definitiva da aplicação web.

Essas decisões pertencem à próxima fase.

---

# Visão de Longo Prazo

Ao final do desenvolvimento, o The AAA Archive poderá possuir:

* Foundation Collection consolidada;
* Awards History organizada;
* banco PostgreSQL;
* backend modular;
* API robusta;
* dashboard analítico;
* aplicação web própria;
* páginas individuais de jogos;
* identidade visual editorial;
* imagens e capas;
* ferramentas de busca;
* filtros avançados;
* novas coleções;
* deploy público;
* documentação técnica consistente.

Mais do que um catálogo, o projeto pretende se tornar um arquivo digital organizado, editorialmente forte e tecnicamente preparado para evoluir.

O The AAA Archive deve continuar sendo:

* simples de compreender;
* consistente;
* documentado;
* testável;
* modular;
* pessoal;
* editorialmente criterioso;
* tecnicamente evolutivo.
