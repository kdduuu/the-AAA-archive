# Project Context — The AAA Archive

## Sobre o Projeto

O **The AAA Archive** é um projeto pessoal desenvolvido por **Kadu Almeida** para estudar e aplicar conceitos de:

* análise de dados;
* engenharia de software;
* Python;
* Pandas;
* banco de dados;
* backend;
* APIs;
* dashboards;
* testes;
* documentação;
* futuramente, desenvolvimento front-end.

A proposta é construir um arquivo digital curado sobre jogos **AAA single-player historicamente relevantes**, utilizando um tema de interesse pessoal como base para aprender tecnologias reais de desenvolvimento.

O projeto começou como uma forma de praticar Python e Pandas com um dataset próprio, mas evoluiu para uma aplicação composta por diferentes camadas:

```text
Datasets em CSV
↓
PostgreSQL
↓
Camada Python de dados
↓
API FastAPI
↓
Dashboard Streamlit
↓
Futura aplicação web
```

Atualmente, o projeto possui:

* dataset principal da Foundation Collection;
* dataset da Awards History;
* banco de dados PostgreSQL;
* script de criação das tabelas;
* script de importação dos CSVs;
* camada centralizada de acesso ao banco;
* módulos de filtros, busca, estatísticas e premiações;
* API com FastAPI;
* dashboard com Streamlit;
* testes dos módulos principais;
* testes do banco;
* testes da API;
* documentação técnica organizada por fases.

O desenvolvimento acontece de forma incremental.

Cada etapa possui o objetivo de ensinar uma parte nova do processo sem pular fundamentos e sem transformar o projeto em algo complexo demais antes da hora.

---

## Objetivos

O projeto possui objetivos técnicos, educacionais, editoriais e de portfólio.

Durante seu desenvolvimento, busca-se:

* aprender Python aplicado a um projeto real;
* praticar Pandas com datasets próprios;
* organizar e validar dados em arquivos CSV;
* compreender o papel de um banco de dados relacional;
* importar dados para PostgreSQL;
* criar uma camada centralizada de acesso ao banco;
* desenvolver módulos reutilizáveis;
* disponibilizar dados por meio de uma API;
* apresentar informações em um dashboard;
* aplicar testes simples;
* praticar Git e GitHub;
* manter documentação atualizada;
* compreender a separação de responsabilidades;
* preparar o projeto para uma aplicação web final;
* construir um projeto consistente para portfólio.

O objetivo não é apenas acumular tecnologias.

Cada ferramenta deve possuir uma responsabilidade clara dentro do sistema.

---

## Filosofia Editorial

O **The AAA Archive** não pretende catalogar todos os jogos já produzidos.

A proposta é criar uma coleção curada de jogos considerados importantes para a história dos videogames, principalmente dentro do recorte de jogos **AAA single-player**.

Essa coleção principal recebe o nome de:

```text
Foundation Collection
```

A Foundation Collection representa o núcleo editorial permanente do projeto.

Ela reúne jogos selecionados por critérios como:

* importância histórica;
* influência na indústria;
* impacto cultural;
* reconhecimento crítico;
* relevância dentro de uma franquia;
* contribuição para gêneros;
* contribuição para mecânicas;
* contribuição para narrativas;
* força editorial dentro da proposta do Archive.

O projeto também possui uma base separada chamada:

```text
Awards History
```

A Awards History registra vencedores e indicados a premiações de **Game of the Year**.

É importante diferenciar as duas bases:

* a Foundation Collection é uma curadoria editorial;
* a Awards History é um histórico de premiações;
* um jogo pode estar presente nas duas bases;
* um jogo pode aparecer na Awards History e não fazer parte da Foundation Collection;
* estar indicado ou vencer um prêmio não garante entrada automática na Foundation Collection;
* o objetivo não é transformar o projeto em um catálogo infinito.

No futuro, novas coleções editoriais poderão ser criadas, como possíveis **Expansion Collections**, desde que preservem a identidade e os critérios do Archive.

---

## Filosofia de Desenvolvimento

O projeto segue alguns princípios:

1. Clareza antes de complexidade.
2. Documentação antes de grandes mudanças.
3. Backend antes do frontend.
4. Evolução incremental.
5. Uma responsabilidade principal por arquivo.
6. Uma responsabilidade principal por função.
7. Código reutilizável.
8. Estrutura simples antes de arquitetura complexa.
9. Testar antes de avançar.
10. Registrar checkpoints após concluir fases importantes.
11. Não adicionar tecnologias sem uma necessidade real.
12. Não alterar muitas partes do projeto ao mesmo tempo.

O desenvolvimento segue, sempre que possível, este fluxo:

```text
planejar
↓
implementar
↓
testar
↓
documentar
↓
criar checkpoint
↓
avançar
```

---

## Arquitetura Atual

A arquitetura atual pode ser representada da seguinte forma:

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

Os arquivos CSV continuam sendo a fonte editorial original.

O PostgreSQL é a fonte operacional utilizada pela API e pelo dashboard.

Isso significa que os dados são editados nos CSVs e depois importados novamente para o banco.

Fluxo atual de atualização:

```text
Editar CSV
↓
Executar import_to_postgres.py
↓
Atualizar PostgreSQL
↓
API e dashboard passam a utilizar os dados atualizados
```

---

## Stack Tecnológica Atual

### Desenvolvimento

* Python;
* Pandas;
* FastAPI;
* Streamlit;
* Git;
* GitHub;
* VS Code.

### Dados

* CSV;
* PostgreSQL;
* SQL;
* DataFrames Pandas.

### Banco de Dados

* PostgreSQL;
* pgAdmin;
* psycopg;
* python-dotenv.

### API

* FastAPI;
* JSON;
* PostgreSQL como fonte de dados;
* camada de banco centralizada em `scripts/database.py`.

### Dashboard

* Streamlit;
* Pandas;
* PostgreSQL como fonte de dados;
* cache com `st.cache_data`;
* gráficos;
* filtros interativos;
* busca textual;
* métricas;
* tabelas dinâmicas.

### Futuro

* aplicação web própria;
* HTML;
* CSS;
* JavaScript;
* possível biblioteca ou framework front-end;
* consumo público da API;
* deploy;
* possíveis melhorias na arquitetura da API.

A stack da aplicação web final ainda não foi definida.

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
├── .gitignore
├── README.md
└── requirements.txt
```

O arquivo `.env` existe somente no ambiente local e não deve ser enviado para o GitHub.

---

## Fontes de Dados

O projeto possui duas fontes editoriais principais:

```text
data/games.csv
data/awards.csv
```

Esses arquivos continuam armazenados no projeto mesmo após a migração para PostgreSQL.

Eles servem como:

* fonte original dos dados;
* base de edição manual;
* referência histórica;
* entrada para o script de importação;
* forma simples de conferir os registros.

---

## `data/games.csv`

Dataset principal da:

```text
Foundation Collection
```

Quantidade atual:

```text
66 jogos
```

Cada linha representa um jogo.

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

Esse dataset representa o núcleo editorial do projeto.

Alguns campos editoriais ainda estão em processo de preenchimento, especialmente:

```text
descricao
metacritic
nota_kadu
nota_pavam
historico_importante
historico_influente
```

A ausência atual desses valores não impede o funcionamento estrutural do projeto, mas limita algumas funcionalidades editoriais.

---

## `data/awards.csv`

Dataset responsável pelo histórico de premiações de Game of the Year.

Quantidade atual:

```text
127 registros
```

Colunas:

```text
ano
premiacao
jogo
status
```

Premiações catalogadas:

* Spike Video Game Awards;
* VGX;
* The Game Awards.

O arquivo registra vencedores e indicados.

No PostgreSQL, cada registro também recebe um campo `id` automático.

---

## PostgreSQL

O projeto utiliza PostgreSQL como banco de dados relacional.

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

A estrutura do banco está registrada em:

```text
database/schema.sql
```

Esse arquivo serve como referência para recriar as tabelas.

---

## Tabela `games`

Estrutura:

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

Quantidade esperada:

```text
66 registros
```

---

## Tabela `awards`

Estrutura:

```sql
CREATE TABLE IF NOT EXISTS awards (
    id SERIAL PRIMARY KEY,
    ano INTEGER,
    premiacao VARCHAR(150),
    jogo VARCHAR(200),
    status VARCHAR(50)
);
```

A coluna `id` é gerada automaticamente porque o arquivo `awards.csv` não possui uma identificação própria.

Quantidade esperada:

```text
127 registros
```

---

## Variáveis de Ambiente

As configurações do PostgreSQL são armazenadas em:

```text
.env
```

Estrutura:

```env
POSTGRES_DB=aaa_archive
POSTGRES_USER=postgres
POSTGRES_PASSWORD=sua_senha
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

O `.env` contém informações sensíveis e deve permanecer apenas localmente.

O `.gitignore` deve impedir que ele seja enviado para o GitHub.

Também está prevista a criação de:

```text
.env.example
```

Esse arquivo deverá demonstrar quais variáveis são necessárias, mas sem conter senhas reais.

---

## Importação para o PostgreSQL

O script responsável pela importação é:

```text
scripts/import_to_postgres.py
```

Fluxo:

```text
data/games.csv
data/awards.csv
        ↓
Python + Pandas
        ↓
PostgreSQL
        ↓
games
awards
```

Comando:

```bash
python scripts/import_to_postgres.py
```

Resultado esperado:

```text
Registros na tabela games: 66
Registros na tabela awards: 127
Importação concluída com sucesso!
```

O script permite recriar ou atualizar o conteúdo das tabelas a partir das fontes editoriais em CSV.

---

## Camada de Acesso ao Banco

O arquivo responsável por centralizar a conexão e a leitura do PostgreSQL é:

```text
scripts/database.py
```

Funções principais:

* `obter_configuracao_banco()`;
* `conectar_postgres()`;
* `executar_select()`;
* `carregar_games_do_banco()`;
* `carregar_awards_do_banco()`;
* `contar_games_do_banco()`;
* `contar_awards_do_banco()`.

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

Essa centralização evita que API e dashboard repitam código de conexão.

---

## Módulos Implementados

## `load_data.py`

Responsável por carregar diretamente os datasets em CSV.

Funções principais:

* `carregar_dataset()`;
* `carregar_awards()`.

O módulo continua sendo utilizado por testes e operações baseadas nos arquivos originais.

---

## `filters.py`

Responsável pelos filtros da Foundation Collection.

Funções principais:

* `listar_jogos_por_developer()`;
* `listar_jogos_por_genero()`;
* `listar_jogos_por_franquia()`;
* `listar_jogos_por_ano()`;
* `listar_jogos_por_decada()`.

---

## `search.py`

Responsável pela pesquisa textual de jogos.

Funções principais:

* `pesquisar_jogos()`;
* `pesquisar_jogos_por_nome()`.

A pesquisa pode considerar campos como:

* nome;
* gênero;
* desenvolvedora;
* franquia;
* descrição.

---

## `site_statistics.py`

Responsável pelas estatísticas da Foundation Collection.

Funções principais:

* `contar_total_jogos()`;
* `contar_total_developers()`;
* `contar_total_franquias()`;
* `contar_total_generos()`;
* `listar_quantidade_por_genero()`;
* `listar_quantidade_por_developer()`;
* `listar_quantidade_por_franquia()`;
* `listar_quantidade_por_decada()`;
* `listar_jogos_historicos()`;
* `listar_jogos_influentes()`;
* `gerar_estatisticas_home()`.

---

## `awards.py`

Responsável pelas consultas relacionadas à Awards History.

Funções principais:

* `listar_premiacoes()`;
* `listar_anos_disponiveis()`;
* `listar_jogos_por_ano()`;
* `buscar_vencedor_por_ano()`;
* `listar_indicados_por_ano()`;
* `listar_vencedores()`;
* `listar_jogos_por_premiacao()`;
* `listar_vencedores_na_foundation()`;
* `listar_indicados_na_foundation()`;
* `listar_jogos_awards_fora_da_foundation()`.

---

## API

A API está localizada em:

```text
api/main.py
```

Ela foi desenvolvida com FastAPI.

A versão atual utiliza PostgreSQL como fonte de dados por meio de:

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

A API atualmente realiza operações de leitura.

Ela ainda não possui:

* cadastro de jogos;
* edição;
* exclusão;
* autenticação;
* painel administrativo;
* routers separados;
* paginação;
* filtros combinados;
* ordenação avançada.

A ausência dessas funcionalidades é intencional.

A versão atual foi construída para consolidar a leitura, consulta e exposição dos dados antes de uma expansão arquitetural.

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

A versão atual da API é identificada como:

```text
0.2.0
```

O endpoint inicial informa que a fonte de dados é PostgreSQL.

A API está considerada concluída para esta fase.

Não há necessidade de adicionar novos endpoints antes do planejamento da aplicação web.

---

## Dashboard

O dashboard está localizado em:

```text
dashboard/app.py
```

As funções auxiliares ficam em:

```text
dashboard/dashboard_helpers.py
```

Ele foi desenvolvido com Streamlit e representa a primeira camada visual do projeto.

O dashboard utiliza PostgreSQL como fonte de dados.

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

O dashboard possui:

* organização com `st.tabs()`;
* aba Foundation Collection;
* aba Awards History;
* cache com `@st.cache_data`;
* filtros interativos;
* busca textual;
* métricas;
* gráficos;
* tabelas dinâmicas;
* seção de recorte editorial;
* consulta de premiações por ano;
* histórico de vencedores;
* comparação entre Awards History e Foundation Collection.

O dashboard atual está concluído para esta fase.

Não há necessidade de expandi-lo antes da definição da aplicação web final.

---

## Testes

O projeto possui testes simples em Python para validar seus módulos e integrações.

Comandos:

```bash
python scripts/test_filters.py
python scripts/test_search.py
python scripts/test_site_statistics.py
python scripts/test_awards.py
python scripts/test_database.py
python api/test_main.py
```

Esses testes verificam:

* filtros;
* pesquisa;
* estatísticas;
* consultas da Awards History;
* configuração do `.env`;
* conexão com PostgreSQL;
* leitura das tabelas;
* retorno dos dados como DataFrames;
* endpoints principais da API.

Os testes de banco e API dependem do PostgreSQL local estar ativo e configurado.

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
docs/postgresql_plan.md
docs/postgresql_checkpoint.md
```

Cada documento possui uma responsabilidade específica.

---

## Responsabilidade dos Principais Documentos

### `README.md`

Apresenta o projeto, sua arquitetura, recursos, tecnologias e instruções de execução.

É o principal documento para quem acessa o repositório.

---

### `project_context.md`

Explica:

* contexto geral;
* objetivos;
* filosofia editorial;
* arquitetura;
* stack;
* estrutura;
* estado atual;
* decisões;
* próximos passos.

É a principal referência interna para compreender o projeto como um todo.

---

### `project_blueprint.md`

Define a visão de produto do The AAA Archive.

Registra:

* áreas principais;
* experiência desejada;
* possíveis páginas;
* evolução futura da aplicação.

Esse documento deverá ser revisado antes do planejamento do front-end.

---

### `project_conventions.md`

Define convenções de:

* organização;
* nomenclatura;
* código;
* testes;
* documentação;
* segurança;
* evolução do projeto.

---

### `foundation_collection.md`

Documenta:

* conceito da coleção;
* critérios de inclusão;
* regras editoriais;
* jogos pertencentes à coleção.

---

### `data_dictionary.md`

Explica as colunas e as regras dos dados da Foundation Collection.

Deve considerar tanto o CSV quanto a tabela `games`.

---

### `awards_dictionary.md`

Explica as colunas e as regras da Awards History.

Deve considerar tanto o CSV quanto a tabela `awards`.

---

### `api_plan.md`

Registra o planejamento inicial da API.

É um documento histórico de planejamento.

---

### `api_checkpoint.md`

Registra o estado da API após sua implementação e posterior migração para PostgreSQL.

---

### `dashboard_plan.md`

Registra o planejamento inicial do dashboard.

É um documento histórico de planejamento.

---

### `dashboard_checkpoint.md`

Registra o estado do dashboard após sua implementação e migração para PostgreSQL.

---

### `postgresql_plan.md`

Registra o planejamento da migração dos CSVs para PostgreSQL.

---

### `postgresql_checkpoint.md`

Registra o resultado da fase PostgreSQL, incluindo:

* banco;
* tabelas;
* importação;
* camada Python;
* API;
* dashboard;
* testes.

---

## Estado Atual

O projeto concluiu a fase de integração com PostgreSQL.

### Concluído

* planejamento inicial;
* estrutura do repositório;
* Foundation Collection;
* dataset `games.csv`;
* Awards History;
* dataset `awards.csv`;
* leitura dos CSVs com Pandas;
* módulo de filtros;
* módulo de busca;
* módulo de estatísticas;
* módulo de premiações;
* testes dos módulos;
* API com FastAPI;
* testes da API;
* dashboard com Streamlit;
* organização do dashboard com arquivo auxiliar;
* instalação e configuração do PostgreSQL;
* criação do banco `aaa_archive`;
* criação das tabelas;
* criação do `schema.sql`;
* criação do script de importação;
* importação dos CSVs;
* criação da camada Python de banco;
* teste da conexão;
* migração da API para PostgreSQL;
* migração do dashboard para PostgreSQL;
* documentação da fase PostgreSQL.

---

## Fase Atual

A fase atual é o encerramento documental da integração com PostgreSQL.

O foco imediato é:

* sincronizar os documentos gerais com o estado real;
* revisar documentos antigos;
* indicar quais planos já foram concluídos;
* criar um `.env.example`;
* revisar o `.gitignore`;
* garantir que o `.env` permaneça privado;
* registrar um commit de checkpoint;
* somente depois começar o planejamento do front-end.

Nenhum código do front-end deve ser iniciado antes dessa organização.

---

## Próximas Etapas Imediatas

A ordem recomendada é:

```text
1. Atualizar README.md.
2. Atualizar project_context.md.
3. Atualizar project_blueprint.md.
4. Atualizar project_conventions.md.
5. Revisar os dicionários de dados.
6. Marcar documentos de planejamento como concluídos.
7. Criar .env.example.
8. Revisar .gitignore.
9. Executar os testes finais.
10. Criar commit de checkpoint da fase PostgreSQL.
11. Iniciar o planejamento da aplicação web.
```

---

## Melhorias Futuras Possíveis

Depois do fechamento da fase atual, poderão ser avaliadas melhorias como:

* preenchimento das descrições dos jogos;
* preenchimento das notas;
* preenchimento do Metacritic;
* definição dos jogos históricos;
* definição dos jogos influentes;
* documentação mais detalhada no Swagger;
* filtros combinados;
* paginação;
* ordenação;
* routers no FastAPI;
* normalização de entidades no banco;
* imagens e capas;
* aplicação web própria;
* painel administrativo;
* autenticação;
* deploy.

Essas melhorias não devem ser implementadas ao mesmo tempo.

Cada uma será avaliada conforme a necessidade real do produto.

---

## Diretrizes Atuais

Durante o encerramento desta fase:

* não iniciar o front-end ainda;
* não adicionar novos endpoints sem necessidade;
* não expandir o dashboard;
* não alterar a arquitetura do banco;
* não normalizar tabelas neste momento;
* não remover os CSVs;
* não expor o `.env`;
* não alterar várias camadas ao mesmo tempo;
* priorizar coerência documental;
* preservar o funcionamento atual.

---

## Decisões Técnicas Atuais

As decisões técnicas vigentes são:

* os CSVs continuam como fonte editorial;
* o PostgreSQL é a fonte operacional;
* a API lê dados do PostgreSQL;
* o dashboard lê dados do PostgreSQL;
* a conexão é centralizada em `database.py`;
* a API permanece somente de leitura nesta fase;
* o dashboard atual está concluído;
* a API atual está concluída;
* os módulos de CSV continuam úteis;
* a stack do front-end ainda não foi escolhida;
* a documentação deve ser fechada antes da próxima fase.

---

## Objetivo Final

O objetivo final do **The AAA Archive** é construir um sistema completo capaz de preservar, organizar, analisar e disponibilizar informações sobre jogos historicamente relevantes.

Mais do que um catálogo, o projeto busca se tornar um arquivo digital consistente, com identidade editorial própria e preparado para evoluir tecnicamente.

No longo prazo, o projeto poderá contar com:

* banco PostgreSQL mais estruturado;
* API mais robusta;
* aplicação web própria;
* dashboard analítico;
* imagens e capas;
* novas coleções editoriais;
* ferramentas de gerenciamento;
* deploy público;
* documentação mais profunda;
* visualização histórica da indústria dos games.

O **The AAA Archive** é, ao mesmo tempo:

* um projeto de estudo;
* um projeto de portfólio;
* um arquivo editorial;
* uma aplicação em desenvolvimento;
* uma forma de transformar interesse por videogames em experiência prática com tecnologia.
