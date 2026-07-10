# The AAA Archive

Um arquivo digital dedicado a preservar, catalogar e explorar a história de jogos AAA single-player historicamente relevantes.

O projeto foi criado como uma forma prática de estudar e aplicar conceitos de:

* Python;
* Pandas;
* análise de dados;
* PostgreSQL;
* backend;
* APIs;
* dashboards;
* testes;
* documentação;
* engenharia de software;
* futuramente, desenvolvimento front-end.

O **The AAA Archive** não busca catalogar todos os jogos já lançados. Sua proposta é construir uma coleção curada, com foco em relevância histórica, influência na indústria, impacto cultural, reconhecimento crítico e importância dentro de franquias ou períodos específicos.

---

## Status do Projeto

**Em desenvolvimento**

Fase atual:

```text
Datasets em CSV
↓
Importação para PostgreSQL
↓
Camada Python de acesso aos dados
↓
API FastAPI
↓
Dashboard Streamlit
↓
Planejamento da aplicação web final
```

A fase de integração com PostgreSQL foi concluída.

Atualmente, o projeto já possui:

* dataset da Foundation Collection;
* dataset do histórico de premiações;
* banco de dados PostgreSQL;
* script de criação das tabelas;
* script de importação dos CSVs;
* camada centralizada de conexão com o banco;
* módulos Python de filtros, pesquisa, estatísticas e premiações;
* testes dos módulos principais;
* testes de conexão e leitura do banco;
* API desenvolvida com FastAPI;
* endpoints de consulta da Foundation Collection;
* endpoints editoriais;
* endpoints da Awards History;
* testes da API;
* dashboard desenvolvido com Streamlit;
* integração do dashboard com PostgreSQL;
* documentação das principais fases do projeto.

---

## Objetivo do Projeto

O objetivo do **The AAA Archive** é construir uma aplicação completa para organização e exploração de jogos AAA single-player historicamente relevantes.

A aplicação é desenvolvida de forma incremental, conectando diferentes camadas:

```text
Dados
↓
Banco de dados
↓
Backend
↓
API
↓
Visualização
↓
Aplicação web
```

O projeto permite estudar tecnologias dentro de um sistema real, em vez de utilizá-las apenas em exercícios isolados.

Entre os objetivos estão:

* organizar uma coleção editorial de jogos;
* preservar informações históricas;
* explorar os dados com filtros e pesquisas;
* gerar estatísticas;
* comparar a Foundation Collection com premiações de Game of the Year;
* disponibilizar os dados por meio de uma API;
* apresentar os dados em um dashboard;
* futuramente, criar uma aplicação web própria.

---

## Filosofia do Projeto

O projeto segue uma abordagem simples, gradual e documentada:

1. Clareza antes de complexidade.
2. Documentação antes da implementação.
3. Backend antes do frontend.
4. Uma responsabilidade principal por arquivo.
5. Uma responsabilidade principal por função.
6. Código reutilizável.
7. Estrutura simples antes de arquitetura complexa.
8. Testar antes de avançar.
9. Registrar checkpoints ao concluir uma fase.
10. Toda função deve possuir uma utilidade real dentro do projeto.

O objetivo não é utilizar tecnologias apenas porque são populares, mas entender qual papel cada uma exerce dentro da aplicação.

---

## Arquitetura Atual

A arquitetura atual do projeto pode ser representada da seguinte forma:

```text
data/games.csv
data/awards.csv
        ↓
scripts/import_to_postgres.py
        ↓
PostgreSQL
        ↓
scripts/database.py
        ↓
API FastAPI
Dashboard Streamlit
```

Os arquivos CSV continuam sendo a fonte editorial original dos dados.

O PostgreSQL é a fonte principal utilizada atualmente pela API e pelo dashboard.

---

## Fontes de Dados

O projeto possui duas bases principais:

```text
Foundation Collection
Awards History
```

Os dados originais são armazenados em arquivos CSV e importados para o PostgreSQL.

---

## Foundation Collection

Arquivo original:

```text
data/games.csv
```

Tabela no PostgreSQL:

```text
games
```

A Foundation Collection contém a lista curada de jogos que formam o núcleo do **The AAA Archive**.

Cada linha representa um jogo.

Quantidade atual:

```text
66 jogos
```

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

A coleção reúne jogos selecionados por critérios como:

* importância histórica;
* influência na indústria;
* relevância cultural;
* reconhecimento crítico;
* importância dentro de uma franquia;
* força editorial dentro da proposta do projeto.

Algumas colunas editoriais ainda estão em processo de preenchimento.

---

## Awards History

Arquivo original:

```text
data/awards.csv
```

Tabela no PostgreSQL:

```text
awards
```

A Awards History armazena vencedores e indicados a **Game of the Year**.

Quantidade atual:

```text
127 registros
```

Premiações catalogadas:

```text
Spike Video Game Awards
VGX
The Game Awards
```

Colunas no CSV:

```text
ano
premiacao
jogo
status
```

No PostgreSQL, a tabela também possui uma coluna automática:

```text
id
```

A Awards History é independente da Foundation Collection, mas as duas bases podem ser comparadas pelo nome dos jogos.

Essa comparação permite identificar:

* vencedores presentes na Foundation Collection;
* indicados presentes na Foundation Collection;
* jogos premiados que ainda estão fora da coleção.

---

## PostgreSQL

O projeto utiliza PostgreSQL como banco de dados relacional.

Banco local:

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

A estrutura das tabelas está registrada em:

```text
database/schema.sql
```

Esse arquivo pode ser usado como referência para recriar o banco.

---

## Estrutura da Tabela `games`

```sql
CREATE TABLE IF NOT EXISTS games (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(200) NOT NULL,
    ano_lancamento INTEGER,
    genero VARCHAR(100),
    developer VARCHAR(150),
    franchise VARCHAR(150),
    descricao TEXT,
    metacritic INTEGER,
    nota_kadu NUMERIC(3, 1),
    nota_pavam NUMERIC(3, 1),
    historico_importante BOOLEAN,
    historico_influente BOOLEAN
);
```

---

## Estrutura da Tabela `awards`

```sql
CREATE TABLE IF NOT EXISTS awards (
    id SERIAL PRIMARY KEY,
    ano INTEGER,
    premiacao VARCHAR(150),
    jogo VARCHAR(200),
    status VARCHAR(50)
);
```

O campo `id` é gerado automaticamente pelo PostgreSQL porque o arquivo `awards.csv` não possui uma coluna de identificação.

---

## Estrutura Atual do Projeto

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
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

O arquivo `.env` existe apenas localmente e não deve ser enviado para o GitHub.

---

## Configuração de Ambiente

As configurações do PostgreSQL são armazenadas em um arquivo:

```text
.env
```

Estrutura esperada:

```env
POSTGRES_DB=aaa_archive
POSTGRES_USER=postgres
POSTGRES_PASSWORD=sua_senha
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

O arquivo `.env` deve permanecer fora do repositório.

Para demonstrar as variáveis necessárias sem expor informações sensíveis, o projeto também deve possuir:

```text
.env.example
```

Exemplo:

```env
POSTGRES_DB=aaa_archive
POSTGRES_USER=postgres
POSTGRES_PASSWORD=sua_senha_aqui
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

O `.gitignore` deve conter:

```gitignore
.env
```

---

## Importação dos Dados

O script responsável por importar os arquivos CSV para o PostgreSQL é:

```text
scripts/import_to_postgres.py
```

Fluxo:

```text
data/games.csv
data/awards.csv
        ↓
Pandas
        ↓
PostgreSQL
        ↓
games
awards
```

Para executar a importação:

```bash
python scripts/import_to_postgres.py
```

Resultado esperado:

```text
Registros na tabela games: 66
Registros na tabela awards: 127
Importação concluída com sucesso!
```

Atualmente, o fluxo de atualização dos dados funciona assim:

```text
Editar os CSVs
↓
Executar import_to_postgres.py
↓
Atualizar o PostgreSQL
↓
API e dashboard passam a utilizar os novos dados
```

---

## Camada de Acesso ao Banco

O arquivo responsável por centralizar a conexão e a leitura do PostgreSQL é:

```text
scripts/database.py
```

Funções principais:

```python
obter_configuracao_banco()
conectar_postgres()
executar_select()
carregar_games_do_banco()
carregar_awards_do_banco()
contar_games_do_banco()
contar_awards_do_banco()
```

Fluxo:

```text
.env
↓
scripts/database.py
↓
PostgreSQL
↓
DataFrame Pandas
```

A centralização da conexão evita que a API e o dashboard repitam configurações do banco.

---

## Módulos Python

Os módulos reutilizáveis ficam principalmente em:

```text
scripts/
```

Eles concentram a lógica de carregamento, filtros, busca, estatísticas, premiações, importação e conexão com o banco.

---

## `load_data.py`

Responsável por carregar os datasets originais em CSV.

Funções principais:

```python
carregar_dataset()
carregar_awards()
```

Arquivos utilizados:

```text
data/games.csv
data/awards.csv
```

Esse módulo continua sendo útil para testes e operações diretamente relacionadas aos arquivos originais.

---

## `filters.py`

Contém os filtros da Foundation Collection.

Funções principais:

```python
listar_jogos_por_developer()
listar_jogos_por_genero()
listar_jogos_por_franquia()
listar_jogos_por_ano()
listar_jogos_por_decada()
```

Permite filtrar jogos por:

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

A busca pode considerar colunas como:

* nome;
* gênero;
* desenvolvedora;
* franquia;
* descrição.

---

## `site_statistics.py`

Gera estatísticas utilizadas pela API e pelo dashboard.

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

Estatísticas disponíveis:

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

Responsável por consultar e comparar a Awards History.

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
* listar anos catalogados;
* consultar vencedores;
* consultar indicados;
* filtrar registros por premiação;
* comparar a Awards History com a Foundation Collection;
* identificar jogos premiados que ainda estão fora da coleção.

---

## API FastAPI

A API está localizada em:

```text
api/main.py
```

Ela utiliza a camada de banco definida em:

```text
scripts/database.py
```

Fluxo:

```text
FastAPI
↓
scripts/database.py
↓
PostgreSQL
```

Para iniciar a API:

```bash
fastapi dev api/main.py
```

A documentação automática fica disponível em:

```text
http://127.0.0.1:8000/docs
```

---

## Endpoint Inicial

```text
GET /
```

Retorna informações básicas sobre o estado da API.

Exemplo:

```json
{
  "mensagem": "The AAA Archive API está funcionando",
  "status": "online",
  "versao": "0.2.0",
  "fonte_dados": "PostgreSQL"
}
```

---

## Endpoints de Games

### Listar todos os jogos

```text
GET /games
```

Retorna todos os jogos da Foundation Collection.

---

### Pesquisa textual

```text
GET /games/search?term=zelda
```

Pesquisa jogos por termo.

A busca considera campos como:

```text
nome
genero
developer
franchise
descricao
```

---

### Filtrar por desenvolvedora

```text
GET /games/developer/{developer}
```

Exemplo:

```text
GET /games/developer/Capcom
```

---

### Filtrar por gênero

```text
GET /games/genre/{genre}
```

Exemplo:

```text
GET /games/genre/Survival Horror
```

---

### Filtrar por franquia

```text
GET /games/franchise/{franchise}
```

Exemplo:

```text
GET /games/franchise/Resident Evil
```

---

### Filtrar por ano

```text
GET /games/year/{year}
```

Exemplo:

```text
GET /games/year/2018
```

---

### Filtrar por década

```text
GET /games/decade/{decade}
```

Exemplo:

```text
GET /games/decade/2000
```

Retorna jogos lançados entre 2000 e 2009.

---

### Jogos historicamente importantes

```text
GET /games/historical
```

Retorna jogos marcados na coluna:

```text
historico_importante
```

---

### Jogos historicamente influentes

```text
GET /games/influential
```

Retorna jogos marcados na coluna:

```text
historico_influente
```

---

## Endpoint de Estatísticas

```text
GET /stats/home
```

Retorna estatísticas gerais da Foundation Collection.

Entre os dados disponíveis estão:

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

## Endpoints da Awards History

### Listar todos os registros

```text
GET /awards
```

---

### Listar vencedores

```text
GET /awards/winners
```

---

### Consultar uma edição por ano

```text
GET /awards/{year}
```

Exemplo:

```text
GET /awards/2018
```

Retorna o vencedor e os indicados do ano informado.

---

### Vencedores presentes na Foundation Collection

```text
GET /awards/foundation/winners
```

---

### Indicados presentes na Foundation Collection

```text
GET /awards/foundation/nominees
```

---

### Jogos fora da Foundation Collection

```text
GET /awards/foundation/outside
```

Retorna jogos da Awards History que ainda não estão presentes na Foundation Collection.

---

## Resumo dos Endpoints

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

## Dashboard Streamlit

O dashboard está localizado em:

```text
dashboard/app.py
```

As funções auxiliares ficam em:

```text
dashboard/dashboard_helpers.py
```

O dashboard utiliza PostgreSQL como fonte principal de dados.

Fluxo:

```text
Streamlit
↓
dashboard_helpers.py
↓
scripts/database.py
↓
PostgreSQL
```

Para iniciar o dashboard:

```bash
streamlit run dashboard/app.py
```

O endereço local normalmente é:

```text
http://localhost:8501
```

---

## Funcionalidades do Dashboard

A versão atual possui:

* organização visual por abas;
* carregamento de dados com cache;
* exploração da Foundation Collection;
* exploração da Awards History;
* filtros interativos;
* pesquisa textual;
* métricas principais;
* gráficos;
* tabelas dinâmicas;
* recorte editorial;
* comparação entre as duas bases.

---

## Organização por Abas

O dashboard utiliza:

```python
st.tabs()
```

Abas atuais:

```text
Foundation Collection
Awards History
```

Essa separação evita que todas as informações sejam exibidas em uma única página extensa.

---

## Cache dos Dados

O carregamento utiliza:

```python
@st.cache_data
```

Os dados são obtidos do PostgreSQL por meio das funções auxiliares do dashboard.

O cache reduz recarregamentos desnecessários durante interações com:

* filtros;
* pesquisa;
* seleção de abas;
* atualização de componentes.

---

## Aba Foundation Collection

A aba Foundation Collection possui:

* métricas principais;
* gráficos;
* filtros;
* pesquisa textual;
* recorte editorial;
* tabela dinâmica.

Métricas:

```text
Jogos
Desenvolvedoras
Franquias
Gêneros
```

Filtros:

```text
Gênero
Desenvolvedora
Ano de lançamento
Franquia
```

Gráficos:

```text
Jogos por Década
Jogos por Gênero
Desenvolvedoras com Mais Jogos
```

---

## Recorte Editorial

A Foundation Collection possui uma seção editorial dedicada aos jogos marcados como:

```text
historicamente importantes
historicamente influentes
```

Campos utilizados:

```text
historico_importante
historico_influente
```

A seção pode apresentar:

* quantidade de jogos historicamente importantes;
* quantidade de jogos historicamente influentes;
* tabela de jogos importantes;
* tabela de jogos influentes.

Esses resultados também respondem aos filtros e à busca textual.

---

## Aba Awards History

A aba Awards History possui:

* métricas gerais;
* consulta por ano;
* vencedor do ano selecionado;
* tabela da edição selecionada;
* histórico de vencedores;
* comparação com a Foundation Collection.

Métricas:

```text
Registros no Awards
Anos catalogados
Vencedores
Fora da Foundation
```

Comparações:

```text
Vencedores presentes na Foundation Collection
Indicados presentes na Foundation Collection
Jogos da Awards History fora da Foundation Collection
```

---

## Testes

O projeto utiliza scripts de teste em Python com `assert`.

Testes disponíveis:

```text
scripts/test_filters.py
scripts/test_search.py
scripts/test_site_statistics.py
scripts/test_awards.py
scripts/test_database.py
api/test_main.py
```

---

## Testes dos Módulos

```bash
python scripts/test_filters.py
python scripts/test_search.py
python scripts/test_site_statistics.py
python scripts/test_awards.py
```

Esses testes validam:

* filtros;
* pesquisa;
* estatísticas;
* consultas da Awards History.

---

## Teste do Banco

Arquivo:

```text
scripts/test_database.py
```

Comando:

```bash
python scripts/test_database.py
```

O teste verifica:

* leitura das variáveis do `.env`;
* conexão com PostgreSQL;
* leitura da tabela `games`;
* leitura da tabela `awards`;
* retorno dos dados como DataFrame;
* quantidade esperada de registros.

Resultado esperado:

```text
TODOS OS TESTES DO BANCO PASSARAM!
```

---

## Testes da API

Arquivo:

```text
api/test_main.py
```

Comando:

```bash
python api/test_main.py
```

O teste valida os principais endpoints:

```text
GET /
GET /games
GET /games/search?term=zelda
GET /games/developer/Capcom
GET /games/genre/Survival Horror
GET /games/franchise/Resident Evil
GET /games/year/2018
GET /games/decade/2000
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

Resultado esperado:

```text
TODOS OS TESTES DA API PASSARAM!
```

---

## Tecnologias Utilizadas

Tecnologias utilizadas atualmente:

* Python;
* Pandas;
* PostgreSQL;
* psycopg;
* python-dotenv;
* FastAPI;
* Streamlit;
* CSV;
* Git;
* GitHub.

Tecnologias previstas para fases futuras:

* HTML;
* CSS;
* JavaScript;
* possível biblioteca ou framework front-end;
* deploy da API;
* deploy do banco;
* deploy da aplicação web.

A stack do front-end ainda não foi definida.

---

## Instalação das Dependências

As dependências estão registradas em:

```text
requirements.txt
```

Para instalar:

```bash
pip install -r requirements.txt
```

Dependências principais:

```text
pandas
fastapi
streamlit
psycopg
python-dotenv
```

A lista completa deve ser consultada no próprio `requirements.txt`.

---

## Como Rodar o Projeto

### 1. Instalar as dependências

```bash
pip install -r requirements.txt
```

---

### 2. Configurar o PostgreSQL

Crie o banco:

```text
aaa_archive
```

Depois, execute o conteúdo de:

```text
database/schema.sql
```

Isso criará as tabelas:

```text
games
awards
```

---

### 3. Configurar o `.env`

Crie um arquivo `.env` na raiz do projeto:

```env
POSTGRES_DB=aaa_archive
POSTGRES_USER=postgres
POSTGRES_PASSWORD=sua_senha
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

---

### 4. Importar os dados

```bash
python scripts/import_to_postgres.py
```

---

### 5. Testar o banco

```bash
python scripts/test_database.py
```

---

### 6. Rodar os testes dos módulos

```bash
python scripts/test_filters.py
python scripts/test_search.py
python scripts/test_site_statistics.py
python scripts/test_awards.py
```

---

### 7. Rodar os testes da API

```bash
python api/test_main.py
```

---

### 8. Iniciar a API

```bash
fastapi dev api/main.py
```

Documentação automática:

```text
http://127.0.0.1:8000/docs
```

---

### 9. Iniciar o dashboard

Em outro terminal:

```bash
streamlit run dashboard/app.py
```

Endereço local:

```text
http://localhost:8501
```

---

## Papel Atual dos CSVs

Embora a API e o dashboard utilizem PostgreSQL, os CSVs continuam importantes.

Eles funcionam como:

* fonte editorial original;
* base de edição manual;
* referência histórica do dataset;
* entrada do processo de importação;
* forma simples de visualizar e manter os dados.

O fluxo atual é:

```text
CSV
↓
Importação
↓
PostgreSQL
↓
API e Dashboard
```

---

## Documentação

A documentação do projeto fica em:

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
postgresql_checkpoint.md
postgresql_plan.md
project_blueprint.md
project_context.md
project_conventions.md
```

Os documentos possuem funções diferentes:

* planos registram decisões anteriores à implementação;
* checkpoints registram o resultado de uma fase;
* dicionários explicam os dados;
* documentos gerais registram a visão e as regras do projeto.

---

## Fases Concluídas

```text
Definição editorial do projeto
↓
Criação da Foundation Collection
↓
Criação da Awards History
↓
Leitura dos CSVs com Pandas
↓
Filtros
↓
Pesquisa textual
↓
Estatísticas
↓
Consultas de premiações
↓
Testes dos módulos
↓
API FastAPI
↓
Testes da API
↓
Dashboard Streamlit
↓
Instalação do PostgreSQL
↓
Criação do banco e das tabelas
↓
Importação dos CSVs
↓
Camada Python de acesso ao banco
↓
Migração da API para PostgreSQL
↓
Migração do dashboard para PostgreSQL
↓
Testes e documentação da fase PostgreSQL
```

---

## Próxima Fase

A próxima grande fase do projeto será o planejamento e desenvolvimento de uma aplicação web própria.

Antes da implementação, serão definidos:

* objetivo da aplicação;
* experiência do usuário;
* páginas;
* navegação;
* identidade visual;
* conteúdo editorial;
* relação entre Foundation Collection e Awards History;
* consumo da API;
* stack do front-end;
* estratégia de deploy.

Nenhuma stack de front-end foi escolhida até o momento.

---

## Melhorias Futuras Possíveis

Algumas melhorias que poderão ser avaliadas futuramente:

* preencher os campos editoriais da Foundation Collection;
* adicionar descrições dos jogos;
* adicionar notas;
* adicionar dados do Metacritic;
* melhorar a documentação dos endpoints no Swagger;
* adicionar filtros combinados;
* adicionar ordenação;
* adicionar paginação;
* refatorar a API com routers;
* normalizar algumas entidades do banco;
* adicionar imagens e capas;
* desenvolver o front-end próprio;
* publicar a API;
* publicar o banco;
* publicar a aplicação final.

Essas melhorias não precisam ser implementadas ao mesmo tempo.

Cada uma deve ser avaliada conforme a necessidade real do projeto.

---

## O que Ainda Não Está Sendo Feito

Nesta fase, o projeto ainda não possui:

* frontend próprio;
* autenticação;
* painel administrativo;
* criação ou edição de jogos pela API;
* deploy público;
* API organizada com routers;
* paginação;
* filtros combinados por query parameters;
* ordenação avançada;
* normalização completa do banco;
* atualização automática dos dados.

Essas funcionalidades podem ser desenvolvidas em fases futuras.

---

## Segurança

O arquivo `.env` não deve ser enviado para o GitHub nem incluído em pacotes públicos.

Arquivos e pastas que normalmente devem permanecer fora de compartilhamentos públicos:

```text
.env
.venv/
__pycache__/
.git/
```

O projeto deve compartilhar apenas o `.env.example`, sem credenciais reais.

---

## Autor

Desenvolvido por **Kadu Almeida** como projeto pessoal de software, análise de dados, história dos videogames e portfólio.
