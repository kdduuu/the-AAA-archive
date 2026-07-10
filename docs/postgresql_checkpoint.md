# PostgreSQL Checkpoint — The AAA Archive

## Objetivo deste checkpoint

Este documento registra o estado atual da integração do projeto **The AAA Archive** com PostgreSQL.

Ele serve para documentar:

- o banco criado;
- as tabelas criadas;
- os arquivos relacionados ao PostgreSQL;
- o fluxo de importação dos dados;
- o fluxo de leitura dos dados pelo Python;
- a migração da API para PostgreSQL;
- a migração do dashboard para PostgreSQL;
- o status atual dos testes.

---

# 1. Banco de dados criado

O banco principal do projeto no PostgreSQL se chama:

```text
aaa_archive
```

Ele foi criado localmente usando PostgreSQL e pgAdmin.

---

# 2. Tabelas criadas

Dentro do banco `aaa_archive`, foram criadas duas tabelas principais:

```text
games
awards
```

Essas tabelas estão no schema padrão:

```text
public
```

---

# 3. Tabela `games`

A tabela `games` representa a **Foundation Collection** do The AAA Archive.

Ela foi baseada no arquivo:

```text
data/games.csv
```

Cada linha representa um jogo da coleção principal.

## Estrutura da tabela

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

## Quantidade esperada de registros

```text
66 jogos
```

---

# 4. Tabela `awards`

A tabela `awards` representa o histórico de premiações de Game of the Year.

Ela foi baseada no arquivo:

```text
data/awards.csv
```

Cada linha representa um jogo indicado ou vencedor em uma edição de premiação.

## Estrutura da tabela

```sql
CREATE TABLE IF NOT EXISTS awards (
    id SERIAL PRIMARY KEY,
    ano INTEGER,
    premiacao VARCHAR(150),
    jogo VARCHAR(200),
    status VARCHAR(50)
);
```

## Observação sobre o `id`

O arquivo `awards.csv` não possui uma coluna `id`.

Por isso, no PostgreSQL foi criada uma coluna automática:

```sql
id SERIAL PRIMARY KEY
```

Isso faz o próprio PostgreSQL gerar os ids automaticamente.

## Quantidade esperada de registros

```text
127 registros
```

---

# 5. Arquivo de schema SQL

Foi criado o arquivo:

```text
database/schema.sql
```

Esse arquivo registra a estrutura oficial inicial do banco.

Ele contém:

- explicação sobre o banco `aaa_archive`;
- criação das tabelas `games` e `awards`;
- comentários explicando as colunas;
- consultas úteis para conferência;
- fluxo atual do PostgreSQL no projeto.

Esse arquivo deve ser usado como referência para recriar a estrutura do banco em outro ambiente ou para explicar o banco para um próximo chat.

---

# 6. Script de importação para PostgreSQL

Foi criado o arquivo:

```text
scripts/import_to_postgres.py
```

Esse script faz o caminho:

```text
data/games.csv
data/awards.csv
       ↓
Python + Pandas
       ↓
PostgreSQL
       ↓
tabelas games e awards
```

Ele é responsável por:

- ler os arquivos CSV;
- conectar ao PostgreSQL;
- limpar os dados antigos das tabelas;
- importar os registros atualizados;
- conferir a quantidade final de registros.

Resultado esperado após rodar:

```text
Registros na tabela games: 66
Registros na tabela awards: 127
Importação concluída com sucesso!
```

---

# 7. Camada de leitura do banco

Foi criado o arquivo:

```text
scripts/database.py
```

Esse arquivo centraliza a conexão e leitura do PostgreSQL.

Ele faz o caminho:

```text
PostgreSQL
     ↓
Python
     ↓
DataFrame Pandas
```

Principais funções atuais:

```python
obter_configuracao_banco()
conectar_postgres()
executar_select(sql)
carregar_games_do_banco()
carregar_awards_do_banco()
contar_games_do_banco()
contar_awards_do_banco()
```

## Função do `database.py`

O `database.py` serve como uma camada entre o projeto e o banco de dados.

Em vez de cada parte do projeto criar conexão com o PostgreSQL sozinha, esse arquivo centraliza essa responsabilidade.

Isso ajuda a manter o projeto mais organizado.

Fluxo atual:

```text
API / Dashboard
       ↓
scripts/database.py
       ↓
PostgreSQL
```

---

# 8. Uso do arquivo `.env`

Foi criado um arquivo local:

```text
.env
```

Ele fica na raiz do projeto.

Exemplo de estrutura:

```env
POSTGRES_DB=aaa_archive
POSTGRES_USER=postgres
POSTGRES_PASSWORD=sua_senha
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

O objetivo do `.env` é guardar configurações locais e informações sensíveis, como a senha do PostgreSQL, fora do código Python.

## Por que usamos `.env`

Antes, a senha poderia ficar escrita diretamente no código ou precisava ser digitada manualmente no terminal.

Com o `.env`, o projeto consegue ler as informações automaticamente.

Fluxo:

```text
.env
↓
database.py
↓
PostgreSQL
```

Isso deixa o projeto:

- mais seguro;
- mais organizado;
- mais próximo de uma aplicação real;
- mais fácil de adaptar para API, dashboard e futura aplicação web.

---

# 9. Proteção do `.env`

O arquivo `.env` foi adicionado ao:

```text
.gitignore
```

Isso impede que ele seja enviado para o GitHub.

Motivo:

```text
O código pode ir para o GitHub.
A senha do banco não deve ir para o GitHub.
```

O `.gitignore` deve conter uma linha parecida com:

```gitignore
.env
```

---

# 10. Dependências adicionadas

O projeto passou a usar as seguintes bibliotecas para a fase PostgreSQL:

```text
psycopg[binary]
python-dotenv
```

O `requirements.txt` atual deve conter:

```txt
pandas
streamlit
fastapi[standard]
psycopg[binary]
python-dotenv
```

## Função de cada dependência

```text
psycopg[binary]
```

Permite o Python se conectar ao PostgreSQL.

```text
python-dotenv
```

Permite o Python ler as configurações salvas no arquivo `.env`.

---

# 11. Teste do banco

Foi criado o arquivo:

```text
scripts/test_database.py
```

Esse teste verifica se:

- o `.env` foi carregado corretamente;
- o Python consegue se conectar ao PostgreSQL;
- a tabela `games` possui 66 registros;
- a tabela `awards` possui 127 registros;
- os dados são carregados como DataFrames do Pandas.

Comando para rodar:

```bash
python scripts/test_database.py
```

Resultado esperado:

```text
The AAA Archive — Testes do PostgreSQL

Lendo configurações do arquivo .env...
Configurações do .env carregadas com sucesso.

Iniciando testes do banco...

Registros encontrados na tabela games: 66
Registros encontrados na tabela awards: 127
DataFrame de games carregado com 66 registros.
DataFrame de awards carregado com 127 registros.

TODOS OS TESTES DO BANCO PASSARAM!
```

---

# 12. API migrada para PostgreSQL

A API foi migrada para usar PostgreSQL como fonte principal de dados.

Antes, a API carregava os dados diretamente dos CSVs por meio do `load_data.py`.

Fluxo antigo:

```text
API
↓
scripts/load_data.py
↓
data/games.csv / data/awards.csv
```

Agora, a API usa o `database.py`.

Fluxo atual:

```text
API
↓
scripts/database.py
↓
.env
↓
PostgreSQL
```

## Arquivos alterados

```text
api/main.py
api/test_main.py
```

## Mudanças principais no `api/main.py`

O `api/main.py` passou a usar:

```python
carregar_games_do_banco()
carregar_awards_do_banco()
```

Essas funções vêm de:

```text
scripts/database.py
```

A API agora informa no endpoint inicial:

```json
{
  "mensagem": "The AAA Archive API está funcionando",
  "status": "online",
  "versao": "0.2.0",
  "fonte_dados": "PostgreSQL"
}
```

## Teste da API

O arquivo:

```text
api/test_main.py
```

foi atualizado para considerar:

- versão `0.2.0`;
- fonte de dados `PostgreSQL`;
- 66 jogos em `/games`;
- 127 registros em `/awards`;
- endpoints principais funcionando.

Comando para rodar:

```bash
python api/test_main.py
```

Resultado esperado:

```text
TODOS OS TESTES DA API PASSARAM!
```

---

# 13. Endpoints da API usando PostgreSQL

Os endpoints principais continuam os mesmos por fora.

A diferença é interna: agora eles buscam dados no PostgreSQL.

Endpoints de jogos:

```text
GET /
GET /games
GET /games/search?term=
GET /games/developer/{developer}
GET /games/genre/{genre}
GET /games/franchise/{franchise}
GET /games/year/{year}
GET /games/decade/{decade}
GET /games/historical
GET /games/influential
```

Endpoints de estatísticas:

```text
GET /stats/home
```

Endpoints de awards:

```text
GET /awards
GET /awards/winners
GET /awards/{year}
GET /awards/foundation/winners
GET /awards/foundation/nominees
GET /awards/foundation/outside
```

---

# 14. Dashboard migrado para PostgreSQL

O dashboard Streamlit também foi migrado para usar PostgreSQL como fonte principal de dados.

Antes, o dashboard carregava os CSVs por meio do `load_data.py`.

Fluxo antigo:

```text
Dashboard
↓
dashboard_helpers.py
↓
scripts/load_data.py
↓
data/games.csv / data/awards.csv
```

Agora, o dashboard usa o `database.py`.

Fluxo atual:

```text
Dashboard
↓
dashboard_helpers.py
↓
scripts/database.py
↓
.env
↓
PostgreSQL
```

## Arquivos alterados

```text
dashboard/app.py
dashboard/dashboard_helpers.py
```

## Mudanças principais no `dashboard_helpers.py`

O `dashboard_helpers.py` passou a usar:

```python
carregar_games_do_banco()
carregar_awards_do_banco()
```

Essas funções vêm de:

```text
scripts/database.py
```

As funções com cache continuam existindo:

```python
carregar_games_com_cache()
carregar_awards_com_cache()
```

Mas agora elas carregam os dados do PostgreSQL.

## Mudanças principais no `dashboard/app.py`

O `app.py` continua focado na interface visual.

A estrutura visual foi mantida:

- filtros na sidebar;
- busca textual;
- métricas;
- gráficos;
- tabelas;
- aba Foundation Collection;
- aba Awards History.

O rodapé foi atualizado para:

```text
Dashboard inicial — PostgreSQL + Pandas + Streamlit
```

## Comando para rodar o dashboard

```bash
streamlit run dashboard/app.py
```

Resultado esperado:

```text
O dashboard abre normalmente no navegador.
Os dados vêm do PostgreSQL.
```

---

# 15. Status atual da fase PostgreSQL

A fase PostgreSQL está concluída.

Status:

```text
PostgreSQL instalado ✅
pgAdmin funcionando ✅
Banco aaa_archive criado ✅
Tabela games criada ✅
Tabela awards criada ✅
schema.sql criado ✅
CSV importado para PostgreSQL ✅
database.py lendo dados do banco ✅
.env configurado ✅
.env ignorado pelo Git ✅
test_database.py passando ✅
API migrada para PostgreSQL ✅
api/test_main.py passando ✅
Dashboard migrado para PostgreSQL ✅
Streamlit abrindo com dados do PostgreSQL ✅
```

---

# 16. Fluxo final atual do projeto

## Importação de dados

```text
CSV
↓
scripts/import_to_postgres.py
↓
PostgreSQL
```

## Leitura pelo Python

```text
.env
↓
scripts/database.py
↓
PostgreSQL
↓
DataFrame Pandas
```

## API

```text
FastAPI
↓
scripts/database.py
↓
PostgreSQL
```

## Dashboard

```text
Streamlit
↓
dashboard_helpers.py
↓
scripts/database.py
↓
PostgreSQL
```

---

# 17. O papel dos CSVs agora

Os arquivos CSV ainda continuam no projeto.

Eles servem como:

- fonte original dos dados;
- base de edição manual;
- referência histórica do dataset;
- entrada para o script de importação.

Arquivos:

```text
data/games.csv
data/awards.csv
```

O PostgreSQL passou a ser a fonte principal usada pela API e pelo dashboard.

Fluxo de atualização atual:

```text
Editar CSV
↓
Rodar scripts/import_to_postgres.py
↓
Atualizar PostgreSQL
↓
API e dashboard passam a usar os novos dados
```

---

# 18. O que ainda não foi feito

A aplicação web/front-end final ainda não foi criada.

Até este checkpoint, o projeto possui:

```text
Backend/API ✅
Banco de dados ✅
Dashboard interno ✅
Documentação da fase PostgreSQL ✅
```

Ainda falta:

```text
Front-end/aplicação web final
Integração do front-end com a API
Polimento visual final
Deploy completo
```

---

# 19. Próxima fase recomendada

A próxima fase será criar a aplicação web final.

Fluxo desejado:

```text
Aplicação Web / Front-end
↓
API FastAPI
↓
scripts/database.py
↓
PostgreSQL
```

A aplicação web não deve acessar o banco diretamente.

Ela deve consumir os dados pela API.

---

# 20. Preparação antes do front-end

Antes de criar o front-end, ainda é recomendado preparar a API para ser consumida por uma aplicação externa.

Uma etapa provável será configurar CORS no FastAPI.

Isso permite que um front-end rodando em uma porta diferente consiga acessar a API.

Exemplo:

```text
Front-end:
http://localhost:5173

API:
http://127.0.0.1:8000
```

Sem CORS configurado, o navegador pode bloquear a comunicação entre o front-end e a API.

---

# 21. Roadmap da próxima fase

Ordem recomendada para a fase final:

```text
1. Configurar CORS na API.
2. Testar a API novamente.
3. Escolher a stack do front-end.
4. Criar estrutura inicial da aplicação web.
5. Criar Home.
6. Criar página/listagem de jogos.
7. Criar busca e filtros.
8. Criar página de detalhes do jogo.
9. Criar página de Awards.
10. Conectar o front-end com a API.
11. Polir visual e responsividade.
12. Planejar deploy.
```

---

# 22. Arquivos criados ou alterados nesta fase

Arquivos criados:

```text
database/schema.sql
scripts/import_to_postgres.py
scripts/database.py
scripts/test_database.py
docs/postgresql_checkpoint.md
.env
```

Arquivos alterados:

```text
.gitignore
requirements.txt
api/main.py
api/test_main.py
dashboard/app.py
dashboard/dashboard_helpers.py
```

Observação importante:

```text
.env não deve ir para o GitHub.
```

Ele existe apenas localmente no computador do desenvolvedor.

---

# 23. Comandos úteis

## Rodar importação dos CSVs para o PostgreSQL

```bash
python scripts/import_to_postgres.py
```

## Rodar teste de leitura do banco

```bash
python scripts/test_database.py
```

## Rodar testes da API

```bash
python api/test_main.py
```

## Subir a API

```bash
fastapi dev api/main.py
```

## Rodar dashboard

```bash
streamlit run dashboard/app.py
```

## Conferir status do Git

```bash
git status
```

## Commit sugerido para atualização deste checkpoint

```bash
git add docs/postgresql_checkpoint.md
git commit -m "docs: update postgresql checkpoint after api and dashboard migration"
git push
```

Caso os arquivos da migração ainda não tenham sido commitados, usar:

```bash
git add .gitignore requirements.txt database/schema.sql scripts/import_to_postgres.py scripts/database.py scripts/test_database.py docs/postgresql_checkpoint.md api/main.py api/test_main.py dashboard/app.py dashboard/dashboard_helpers.py
git commit -m "feat: complete postgresql integration"
git push
```

---

# 24. Resumo final

A fase PostgreSQL do projeto **The AAA Archive** foi concluída.

O projeto agora possui:

```text
PostgreSQL como banco local principal;
dados importados a partir dos CSVs;
camada database.py para leitura dos dados;
.env para configuração segura;
API consumindo PostgreSQL;
dashboard consumindo PostgreSQL;
testes principais passando;
documentação atualizada.
```

O projeto está pronto para iniciar a fase final:

```text
Front-end / aplicação web final
```