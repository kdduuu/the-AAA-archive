# PostgreSQL Checkpoint — The AAA Archive

## Objetivo deste Documento

Este documento registra o estado final da primeira integração do projeto **The AAA Archive** com PostgreSQL.

O checkpoint documenta:

* banco de dados criado;
* schema utilizado;
* tabelas implementadas;
* estrutura SQL;
* importação dos CSVs;
* conexão entre Python e PostgreSQL;
* uso de variáveis de ambiente;
* camada centralizada de acesso ao banco;
* testes de integração;
* migração da API;
* migração do dashboard;
* fluxo atual dos dados;
* decisões técnicas;
* limitações conhecidas;
* próximos passos recomendados.

Este checkpoint segue a metodologia adotada no projeto:

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
encerrar a fase
```

---

# Status da Fase

Status atual:

```text
Fase PostgreSQL concluída
```

Resultado:

```text
Banco criado
Dados importados
Python conectado
API migrada
Dashboard migrado
Testes passando
```

Fonte operacional atual:

```text
PostgreSQL
```

Fontes editoriais:

```text
data/games.csv
data/awards.csv
```

---

# Arquitetura Alcançada

A arquitetura atual do projeto é:

```text
CSV editorial
↓
scripts/import_to_postgres.py
↓
PostgreSQL
↓
scripts/database.py
↓
Módulos Python
↓
FastAPI e Streamlit
```

Responsabilidades:

```text
CSV
→ edição e preservação editorial

import_to_postgres.py
→ importação e sincronização

PostgreSQL
→ armazenamento operacional

database.py
→ conexão e leitura

módulos Python
→ filtros, pesquisa, estatísticas e comparações

FastAPI
→ disponibilização dos dados em JSON

Streamlit
→ análise e visualização
```

---

# Banco de Dados

O banco principal do projeto se chama:

```text
aaa_archive
```

Ele foi criado localmente utilizando PostgreSQL.

Ferramenta visual utilizada durante a configuração:

```text
pgAdmin
```

Schema:

```text
public
```

Tabelas principais:

```text
games
awards
```

---

# Tabela `games`

A tabela `games` representa a:

```text
Foundation Collection
```

Fonte editorial:

```text
data/games.csv
```

Cada registro representa um jogo da coleção.

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

Quantidade atual esperada:

```text
66 jogos
```

---

# Colunas da Tabela `games`

| Coluna                 | Tipo PostgreSQL | Finalidade                          |
| ---------------------- | --------------- | ----------------------------------- |
| `id`                   | `INTEGER`       | Identificador único                 |
| `nome`                 | `VARCHAR(200)`  | Nome oficial do jogo                |
| `ano_lancamento`       | `INTEGER`       | Ano de lançamento original          |
| `genero`               | `VARCHAR(100)`  | Gênero principal                    |
| `developer`            | `VARCHAR(150)`  | Desenvolvedora principal            |
| `franchise`            | `VARCHAR(150)`  | Franquia ou propriedade intelectual |
| `descricao`            | `TEXT`          | Descrição editorial                 |
| `metacritic`           | `INTEGER`       | Nota do Metacritic                  |
| `nota_kadu`            | `NUMERIC(3,1)`  | Avaliação de Kadu                   |
| `nota_pavam`           | `NUMERIC(3,1)`  | Avaliação de Pavam                  |
| `historico_importante` | `BOOLEAN`       | Marcação de importância histórica   |
| `historico_influente`  | `BOOLEAN`       | Marcação de influência histórica    |

As regras de preenchimento estão documentadas em:

```text
docs/data_dictionary.md
```

---

# Tabela `awards`

A tabela `awards` representa a:

```text
Awards History
```

Fonte editorial:

```text
data/awards.csv
```

Cada registro representa um jogo vencedor ou indicado em uma edição de Game of the Year.

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

Quantidade atual esperada:

```text
127 registros
```

---

# Campo `id` da Tabela `awards`

O arquivo:

```text
data/awards.csv
```

não possui uma coluna `id`.

Por isso, o PostgreSQL utiliza:

```sql
id SERIAL PRIMARY KEY
```

O identificador é gerado automaticamente durante a inserção.

Ele possui finalidade técnica e não representa uma informação editorial da premiação.

---

# Colunas da Tabela `awards`

| Coluna      | Tipo PostgreSQL | Finalidade                |
| ----------- | --------------- | ------------------------- |
| `id`        | `SERIAL`        | Identificador automático  |
| `ano`       | `INTEGER`       | Ano da edição             |
| `premiacao` | `VARCHAR(150)`  | Nome da premiação         |
| `jogo`      | `VARCHAR(200)`  | Jogo vencedor ou indicado |
| `status`    | `VARCHAR(50)`   | `Vencedor` ou `Indicado`  |

As regras estão documentadas em:

```text
docs/awards_dictionary.md
```

---

# Arquivo de Schema

Foi criado:

```text
database/schema.sql
```

O arquivo registra a estrutura oficial inicial do banco.

Ele pode conter:

* contexto do banco;
* criação da tabela `games`;
* criação da tabela `awards`;
* comentários sobre as colunas;
* consultas para conferência;
* explicação do fluxo de dados.

O `schema.sql` deve ser atualizado sempre que houver mudança estrutural no banco.

Não se deve alterar uma tabela apenas pelo pgAdmin e esquecer de registrar a mudança no arquivo.

---

# Consultas de Conferência

Exemplos:

```sql
SELECT * FROM games;
```

```sql
SELECT * FROM awards;
```

Contagem:

```sql
SELECT COUNT(*) FROM games;
```

```sql
SELECT COUNT(*) FROM awards;
```

Resultados atuais esperados:

```text
games  → 66
awards → 127
```

---

# Script de Importação

Foi criado:

```text
scripts/import_to_postgres.py
```

Fluxo:

```text
data/games.csv
data/awards.csv
↓
Python e Pandas
↓
PostgreSQL
↓
games e awards
```

Responsabilidades:

* localizar os CSVs;
* carregar os arquivos;
* preparar os dados;
* tratar campos vazios;
* converter valores nulos;
* conectar ao PostgreSQL;
* limpar registros antigos quando previsto;
* inserir os dados atualizados;
* conferir as quantidades finais;
* informar o resultado da operação.

---

# Comando de Importação

Na raiz do projeto:

```bash
python scripts/import_to_postgres.py
```

Resultado esperado:

```text
Registros na tabela games: 66
Registros na tabela awards: 127
Importação concluída com sucesso!
```

---

# Regra de Atualização dos Dados

Enquanto os CSVs forem as fontes editoriais, o fluxo oficial será:

```text
Editar CSV
↓
Validar dados
↓
Executar import_to_postgres.py
↓
Verificar quantidades
↓
Executar testes
↓
Abrir API ou dashboard
```

Não se deve editar apenas o PostgreSQL e esquecer de atualizar os CSVs.

Isso criaria divergência entre:

```text
fonte editorial
fonte operacional
```

---

# Camada de Acesso ao Banco

Foi criado:

```text
scripts/database.py
```

Esse arquivo centraliza:

* leitura das configurações;
* abertura da conexão;
* execução de consultas;
* fechamento da conexão;
* carregamento de registros;
* conversão para DataFrames;
* contagem de registros.

Fluxo:

```text
API / Dashboard
↓
scripts/database.py
↓
PostgreSQL
```

---

# Funções do `database.py`

Funções atuais:

```python
obter_configuracao_banco()
conectar_postgres()
executar_select()
carregar_games_do_banco()
carregar_awards_do_banco()
contar_games_do_banco()
contar_awards_do_banco()
```

---

# `obter_configuracao_banco()`

Responsável por carregar as variáveis necessárias para a conexão.

Configurações esperadas:

```text
POSTGRES_DB
POSTGRES_USER
POSTGRES_PASSWORD
POSTGRES_HOST
POSTGRES_PORT
```

A função deve apresentar erro compreensível quando uma variável obrigatória estiver ausente.

---

# `conectar_postgres()`

Responsável por criar a conexão com o banco.

Ela utiliza as configurações carregadas do ambiente.

A senha não deve ser escrita diretamente na função.

---

# `executar_select()`

Responsável por:

* receber uma consulta de leitura;
* executá-la;
* recuperar colunas e registros;
* retornar o resultado como DataFrame.

Na fase atual, essa função deve ser utilizada apenas com consultas internas controladas pelo projeto.

Consultas dinâmicas envolvendo nomes de tabelas ou colunas devem ser tratadas com cuidado, pois parâmetros comuns de SQL não substituem identificadores.

---

# `carregar_games_do_banco()`

Executa a leitura da tabela:

```text
games
```

e retorna os registros como DataFrame Pandas.

---

# `carregar_awards_do_banco()`

Executa a leitura da tabela:

```text
awards
```

e retorna os registros como DataFrame Pandas.

---

# Funções de Contagem

As funções:

```python
contar_games_do_banco()
contar_awards_do_banco()
```

retornam as quantidades de registros das tabelas.

Elas são utilizadas principalmente para:

* validações;
* testes;
* conferência da importação.

---

# Por que Centralizar o Banco?

Sem `database.py`, cada arquivo precisaria repetir:

* leitura do `.env`;
* host;
* porta;
* usuário;
* senha;
* conexão;
* execução;
* fechamento.

A centralização melhora:

* organização;
* manutenção;
* segurança;
* reutilização;
* legibilidade;
* testes.

---

# Uso de DataFrames

Mesmo com PostgreSQL, o projeto continua utilizando Pandas.

Fluxo:

```text
PostgreSQL
↓
consulta SQL
↓
DataFrame
↓
módulos atuais
```

Essa decisão permitiu manter:

* `filters.py`;
* `search.py`;
* `site_statistics.py`;
* `awards.py`;
* conversão da API;
* lógica do dashboard.

A primeira migração não teve como objetivo substituir toda a lógica por SQL.

---

# Variáveis de Ambiente

Foi criado localmente:

```text
.env
```

Ele fica na raiz do projeto.

Estrutura:

```env
POSTGRES_DB=aaa_archive
POSTGRES_USER=postgres
POSTGRES_PASSWORD=sua_senha
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

O arquivo contém configurações específicas do ambiente local.

---

# Motivo do `.env`

O `.env` impede que informações sensíveis sejam escritas diretamente nos arquivos Python.

Fluxo:

```text
.env
↓
python-dotenv
↓
database.py
↓
PostgreSQL
```

Isso torna o projeto:

* mais seguro;
* mais configurável;
* mais fácil de compartilhar;
* mais próximo de aplicações reais.

---

# Proteção do `.env`

O arquivo deve estar listado em:

```text
.gitignore
```

Regra esperada:

```gitignore
.env
```

O `.env` não deve ser:

* enviado ao GitHub;
* incluído em ZIP público;
* publicado em documentação;
* mostrado em screenshots;
* colado em conversas;
* enviado junto com o projeto;
* usado como arquivo de exemplo.

---

# Verificação no Git

É recomendado executar:

```bash
git status
```

O `.env` não deve aparecer como arquivo novo ou modificado a ser enviado.

Caso ele tenha sido adicionado ao Git anteriormente, apenas incluí-lo no `.gitignore` não será suficiente.

Nesse caso, deverá ser removido do rastreamento sem apagar o arquivo local:

```bash
git rm --cached .env
```

Depois:

```bash
git commit -m "chore: stop tracking environment file"
```

Caso uma senha real tenha sido publicada, ela deverá ser alterada.

---

# Arquivo `.env.example`

O projeto deve possuir:

```text
.env.example
```

Esse arquivo documenta as variáveis necessárias sem expor valores sensíveis.

Conteúdo recomendado:

```env
POSTGRES_DB=aaa_archive
POSTGRES_USER=postgres
POSTGRES_PASSWORD=sua_senha_aqui
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

O `.env.example` pode ser enviado ao GitHub.

O `.env` real não pode.

---

# Dependências da Fase PostgreSQL

Dependências principais:

```text
psycopg[binary]
python-dotenv
```

Funções:

```text
psycopg[binary]
→ conexão com PostgreSQL

python-dotenv
→ leitura do arquivo .env
```

O projeto também utiliza:

```text
pandas
fastapi[standard]
streamlit
```

---

# `requirements.txt`

Conteúdo principal esperado:

```text
pandas
streamlit
fastapi[standard]
psycopg[binary]
python-dotenv
```

As versões podem ser fixadas futuramente quando houver necessidade de reproduzir exatamente o ambiente.

Comandos como:

```text
pip freeze > requirements.txt
```

não devem aparecer dentro do arquivo de dependências.

---

# Teste do Banco

Foi criado:

```text
scripts/test_database.py
```

O teste verifica:

* leitura das configurações;
* conexão com PostgreSQL;
* acesso à tabela `games`;
* acesso à tabela `awards`;
* contagem dos registros;
* carregamento em DataFrames;
* presença de colunas esperadas.

Comando:

```bash
python scripts/test_database.py
```

Resultado esperado:

```text
TODOS OS TESTES DO BANCO PASSARAM!
```

---

# Quantidades Verificadas

O teste atual espera:

```text
games  → 66
awards → 127
```

Esses valores representam o estado atual dos datasets.

Quando os dados crescerem, os testes com números fixos deverão ser atualizados ou substituídos por validações menos frágeis.

---

# API Migrada para PostgreSQL

A API foi migrada para utilizar PostgreSQL como fonte operacional.

Antes:

```text
FastAPI
↓
load_data.py
↓
CSV
```

Agora:

```text
FastAPI
↓
database.py
↓
PostgreSQL
```

Arquivos alterados:

```text
api/main.py
api/test_main.py
```

---

# Mudanças no `api/main.py`

A API passou a utilizar:

```python
carregar_games_do_banco()
carregar_awards_do_banco()
```

Essas funções vêm de:

```text
scripts/database.py
```

O endpoint inicial informa:

```json
{
  "mensagem": "The AAA Archive API está funcionando",
  "status": "online",
  "versao": "0.2.0",
  "fonte_dados": "PostgreSQL"
}
```

---

# Endpoints Preservados

A migração não alterou o contrato principal das rotas.

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

A alteração foi interna:

```text
antes → CSV
agora → PostgreSQL
```

---

# Teste da API

Arquivo:

```text
api/test_main.py
```

Comando:

```bash
python api/test_main.py
```

O teste considera:

* versão `0.2.0`;
* fonte `PostgreSQL`;
* rota inicial;
* quantidade de jogos;
* quantidade de registros da Awards History;
* filtros;
* pesquisa;
* estatísticas;
* consultas por ano;
* comparações entre as bases.

Resultado esperado:

```text
TODOS OS TESTES DA API PASSARAM!
```

---

# Dashboard Migrado para PostgreSQL

O dashboard também utiliza PostgreSQL como fonte operacional.

Antes:

```text
Streamlit
↓
dashboard_helpers.py
↓
load_data.py
↓
CSV
```

Agora:

```text
Streamlit
↓
dashboard_helpers.py
↓
database.py
↓
PostgreSQL
```

Arquivos relacionados:

```text
dashboard/app.py
dashboard/dashboard_helpers.py
```

---

# Mudanças no `dashboard_helpers.py`

O arquivo passou a utilizar:

```python
carregar_games_do_banco()
carregar_awards_do_banco()
```

As funções com cache continuam existindo:

```python
carregar_games_com_cache()
carregar_awards_com_cache()
```

A diferença é que agora elas recebem os registros do PostgreSQL.

---

# `dashboard/app.py`

O `app.py` permanece focado na interface.

Foram preservados:

* título;
* sidebar;
* filtros;
* busca;
* métricas;
* gráficos;
* tabelas;
* aba Foundation Collection;
* aba Awards History;
* recorte editorial;
* comparação entre as bases.

A migração não teve como objetivo alterar o visual.

---

# Comando do Dashboard

```bash
streamlit run dashboard/app.py
```

Resultado esperado:

```text
O dashboard abre no navegador.
Os dados são carregados do PostgreSQL.
```

---

# Cache do Streamlit

Como o dashboard utiliza:

```python
@st.cache_data
```

alterações importadas para o banco podem não aparecer imediatamente em uma sessão já aberta.

Quando necessário:

```text
Menu do Streamlit
→ Clear cache
```

ou:

```bash
CTRL + C
streamlit run dashboard/app.py
```

---

# Sequência Completa de Validação

## 1. Importar os dados

```bash
python scripts/import_to_postgres.py
```

## 2. Testar o banco

```bash
python scripts/test_database.py
```

## 3. Testar módulos baseados nos dados

```bash
python scripts/test_filters.py
python scripts/test_search.py
python scripts/test_site_statistics.py
python scripts/test_awards.py
```

## 4. Testar a API

```bash
python api/test_main.py
```

## 5. Validar o dashboard

```bash
streamlit run dashboard/app.py
```

---

# Estado Atual dos Testes

Testes disponíveis:

```text
scripts/test_filters.py
scripts/test_search.py
scripts/test_site_statistics.py
scripts/test_awards.py
scripts/test_database.py
api/test_main.py
```

Status registrado:

```text
Testes passando
```

Os testes do banco e da API dependem do PostgreSQL local estar ativo e configurado.

---

# Arquivos Criados na Fase

```text
database/schema.sql
scripts/import_to_postgres.py
scripts/database.py
scripts/test_database.py
docs/postgresql_plan.md
docs/postgresql_checkpoint.md
.env
```

O `.env` é um arquivo local e não deve ser versionado.

---

# Arquivos Alterados na Fase

```text
.gitignore
requirements.txt
api/main.py
api/test_main.py
dashboard/app.py
dashboard/dashboard_helpers.py
```

Outros documentos também foram posteriormente atualizados para refletir a nova arquitetura.

---

# Estrutura Atual Relacionada

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
├── scripts/
│   ├── database.py
│   ├── import_to_postgres.py
│   └── test_database.py
│
├── .env
├── .env.example
├── .gitignore
└── requirements.txt
```

O `.env.example` deverá ser adicionado caso ainda não exista.

---

# Decisões Técnicas

## 1. Duas Tabelas Iniciais

Foram criadas apenas:

```text
games
awards
```

Motivo:

* refletir os CSVs;
* reduzir complexidade;
* facilitar aprendizado;
* preservar os módulos existentes.

---

## 2. CSV como Fonte Editorial

Os CSVs foram preservados.

Motivo:

* facilidade de edição;
* histórico;
* versionamento;
* importação;
* revisão manual.

---

## 3. PostgreSQL como Fonte Operacional

API e dashboard usam o banco.

Motivo:

* centralização;
* persistência;
* preparação para front-end;
* arquitetura mais realista.

---

## 4. Preservação de DataFrames

As consultas retornam DataFrames.

Motivo:

* reaproveitar filtros;
* reaproveitar pesquisa;
* reaproveitar estatísticas;
* migrar de forma incremental.

---

## 5. Ausência de Normalização Completa

Desenvolvedoras, gêneros e franquias continuam armazenados diretamente em `games`.

Motivo:

* evitar complexidade prematura;
* manter compatibilidade;
* adiar relacionamentos até existir necessidade.

---

## 6. Sem Operações de Escrita na API

A API permanece somente de leitura.

Motivo:

* evitar dois caminhos editoriais;
* preservar CSV como fonte de edição;
* manter segurança;
* reduzir inconsistências.

---

## 7. Dashboard sem Consumo da API

O dashboard utiliza diretamente `database.py`.

Motivo:

* mesmo projeto;
* mesma linguagem;
* menor complexidade;
* reutilização direta da camada Python.

---

# Limitações Conhecidas

A primeira integração possui limitações:

* banco somente local;
* ausência de ambiente de produção;
* ausência de banco separado para testes;
* ausência de migrations automatizadas;
* ausência de ORM;
* tabelas não normalizadas;
* ausência de chaves estrangeiras;
* filtros ainda executados principalmente com Pandas;
* testes com quantidades fixas;
* ausência de operações administrativas;
* ausência de deploy;
* dependência de configuração local.

Essas limitações são aceitáveis para o objetivo desta fase.

---

# Possíveis Melhorias Futuras

Poderão ser avaliados futuramente:

* banco separado para testes;
* migrations;
* normalização;
* chaves estrangeiras;
* índices;
* consultas parametrizadas mais avançadas;
* filtros executados em SQL;
* busca textual no PostgreSQL;
* relacionamento por `game_id`;
* paginação;
* operações administrativas;
* autenticação;
* banco em nuvem;
* backup automatizado;
* deploy.

Essas melhorias não devem ser implementadas sem necessidade concreta.

---

# Cuidados de Segurança

Regras obrigatórias:

* não versionar `.env`;
* não compartilhar senha;
* não inserir senha no código;
* não imprimir credenciais;
* não incluir `.env` em ZIPs;
* utilizar `.env.example`;
* revisar `git status`;
* trocar senha exposta;
* restringir consultas dinâmicas;
* manter dependências atualizadas quando necessário.

---

# Arquivos que Não Devem Ser Compartilhados

```text
.env
.git/
.venv/
venv/
__pycache__/
```

Arquivos temporários e caches também devem ser ignorados.

---

# Critérios de Sucesso Atendidos

```text
PostgreSQL instalado ✅
pgAdmin configurado ✅
Banco aaa_archive criado ✅
Schema public utilizado ✅
Tabela games criada ✅
Tabela awards criada ✅
schema.sql criado ✅
CSV games importado ✅
CSV awards importado ✅
66 jogos carregados ✅
127 registros de awards carregados ✅
Conexão Python funcionando ✅
database.py criado ✅
DataFrames carregados ✅
test_database.py criado ✅
Teste do banco passando ✅
API migrada ✅
API 0.2.0 ✅
Teste da API passando ✅
Dashboard migrado ✅
Streamlit validado ✅
CSV preservado ✅
Documentação da fase criada ✅
```

---

# O que Ainda Não Foi Feito

Ainda não foram implementados:

* aplicação web final;
* integração de um front-end externo;
* CORS;
* deploy completo;
* banco de produção;
* autenticação;
* painel administrativo;
* operações de escrita;
* páginas individuais completas;
* armazenamento de imagens;
* normalização avançada.

---

# Encerramento Antes do Front-End

A próxima etapa imediata não deve ser começar diretamente a implementação do front-end.

Antes, é necessário:

```text
Finalizar documentação
↓
Criar .env.example
↓
Revisar .gitignore
↓
Confirmar que .env não está rastreado
↓
Executar testes finais
↓
Validar API e dashboard
↓
Criar commit de checkpoint
```

Somente depois deve ser criado:

```text
docs/frontend_plan.md
```

---

# Planejamento Futuro da Aplicação Web

Durante a próxima fase serão definidos:

* finalidade da aplicação;
* experiência desejada;
* identidade visual;
* páginas;
* navegação;
* conteúdo editorial;
* stack;
* consumo da API;
* CORS;
* responsividade;
* deploy.

CORS não deve ser configurado isoladamente antes de saber:

* qual front-end será utilizado;
* em qual endereço ele rodará;
* quais origens deverão ser permitidas;
* como o ambiente de produção funcionará.

---

# Fluxo Futuro Desejado

```text
Aplicação web
↓
requisição HTTP
↓
FastAPI
↓
database.py
↓
PostgreSQL
```

A aplicação web não deve acessar o banco diretamente.

---

# Comandos Úteis

## Importar os dados

```bash
python scripts/import_to_postgres.py
```

## Testar o banco

```bash
python scripts/test_database.py
```

## Testar a API

```bash
python api/test_main.py
```

## Subir a API

```bash
fastapi dev api/main.py
```

## Rodar o dashboard

```bash
streamlit run dashboard/app.py
```

## Verificar o Git

```bash
git status
```

---

# Commit de Encerramento

Depois de revisar os arquivos e executar os testes:

```bash
git status
git add .
git commit -m "docs: align project after postgresql integration"
git push
```

O comando:

```bash
git add .
```

só deve ser usado após confirmar que:

* `.env` não será adicionado;
* não existem arquivos temporários;
* não existem credenciais;
* as alterações pertencem ao checkpoint.

Também pode ser preferível selecionar os arquivos explicitamente.

---

# Resultado da Fase

Estado anterior:

```text
CSV
↓
Pandas
↓
API e Dashboard
```

Estado atual:

```text
CSV editorial
↓
Importação
↓
PostgreSQL
↓
Camada Python
↓
API e Dashboard
```

O objetivo principal da primeira integração foi atingido.

---

# Status Final do Checkpoint

Status:

```text
Integração PostgreSQL concluída
```

Banco:

```text
aaa_archive
```

Tabelas:

```text
games
awards
```

Fonte operacional:

```text
PostgreSQL
```

Fontes editoriais:

```text
games.csv
awards.csv
```

API:

```text
FastAPI 0.2.0
PostgreSQL
Somente leitura
```

Dashboard:

```text
Streamlit
PostgreSQL
Somente leitura
```

Testes:

```text
Banco passando
API passando
Módulos passando
Dashboard validado manualmente
```

---

# Status do Documento

```text
Checkpoint técnico final da primeira integração PostgreSQL
```

Este documento deve ser atualizado quando houver mudanças relevantes em:

* schema;
* tabelas;
* conexão;
* importação;
* variáveis de ambiente;
* testes;
* API;
* dashboard;
* segurança;
* ambiente de produção.
