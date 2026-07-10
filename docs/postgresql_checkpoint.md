# PostgreSQL Checkpoint — The AAA Archive

## Objetivo deste checkpoint

Este documento registra o estado atual da integração do projeto **The AAA Archive** com PostgreSQL.

Ele serve para documentar:

- o banco criado;
- as tabelas criadas;
- os arquivos relacionados ao PostgreSQL;
- o fluxo de importação dos dados;
- o fluxo de leitura dos dados pelo Python;
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

## Explicação das principais colunas

```text
id
```

Identificador único de cada jogo. Ele vem do próprio `games.csv`.

```text
nome
```

Nome do jogo.

```text
ano_lancamento
```

Ano em que o jogo foi lançado.

```text
genero
```

Gênero principal usado no dataset.

```text
developer
```

Desenvolvedora do jogo.

```text
franchise
```

Franquia à qual o jogo pertence.

```text
descricao
```

Descrição editorial do jogo dentro do projeto.

```text
metacritic
```

Nota do jogo no Metacritic.

```text
nota_kadu
```

Nota pessoal do Kadu.

```text
nota_pavam
```

Nota pessoal do Pavam.

```text
historico_importante
```

Indica se o jogo é considerado historicamente importante.

```text
historico_influente
```

Indica se o jogo é considerado historicamente influente.

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

## Explicação das colunas

```text
id
```

Identificador único criado automaticamente pelo PostgreSQL.

```text
ano
```

Ano da premiação.

```text
premiacao
```

Nome da premiação.

Exemplos:

```text
Spike Video Game Awards
VGX
The Game Awards
```

```text
jogo
```

Nome do jogo indicado ou vencedor.

```text
status
```

Status do jogo naquela premiação.

Exemplos:

```text
Vencedor
Indicado
```

## Observação sobre o `id`

O arquivo `awards.csv` não possui uma coluna `id`.

Por isso, no PostgreSQL foi criada uma coluna automática:

```sql
id SERIAL PRIMARY KEY
```

Isso faz o próprio PostgreSQL gerar os ids automaticamente.

Exemplo:

```text
primeiro registro  -> id 1
segundo registro   -> id 2
terceiro registro  -> id 3
```

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

Exemplo de fluxo futuro:

```text
API
↓
database.py
↓
PostgreSQL
```

E também:

```text
Dashboard
↓
database.py
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
- mais fácil de adaptar para API e dashboard.

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

Resultado obtido:

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

# 12. Status atual da fase PostgreSQL

A fase inicial do PostgreSQL está funcionando.

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
```

---

# 13. Fluxo atual do projeto

## Importação

```text
CSV
↓
scripts/import_to_postgres.py
↓
PostgreSQL
```

## Leitura

```text
.env
↓
scripts/database.py
↓
PostgreSQL
↓
DataFrame Pandas
```

---

# 14. O que ainda não foi alterado

Até este checkpoint, a API e o dashboard ainda não foram migrados para PostgreSQL.

Eles ainda podem estar usando os arquivos CSV como fonte principal.

Arquivos ainda não migrados para PostgreSQL:

```text
api/main.py
dashboard/app.py
dashboard/dashboard_helpers.py
scripts/load_data.py
```

Essa decisão foi intencional para evitar quebrar o projeto.

Primeiro validamos o PostgreSQL isoladamente.

Depois adaptaremos API e dashboard com segurança.

---

# 15. Próximas etapas recomendadas

A próxima fase será adaptar a API para usar PostgreSQL.

Ordem recomendada:

```text
1. Manter o CSV funcionando como referência.
2. Adaptar a API para buscar dados via database.py.
3. Testar todos os endpoints da API.
4. Garantir que os endpoints continuam iguais para o usuário.
5. Depois adaptar o dashboard.
```

Endpoints da API que provavelmente serão adaptados depois:

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
GET /stats/home
GET /awards
GET /awards/winners
GET /awards/{year}
GET /awards/foundation/winners
GET /awards/foundation/nominees
GET /awards/foundation/outside
```

---

# 16. Resumo final

O projeto agora possui uma primeira integração real com PostgreSQL.

O banco `aaa_archive` contém os dados principais do projeto, importados a partir dos CSVs.

O Python já consegue:

```text
conectar ao banco;
ler configurações pelo .env;
consultar tabelas;
transformar os dados em DataFrames;
validar a quantidade de registros.
```

A fase PostgreSQL inicial está concluída e pronta para servir como base da futura migração da API e do dashboard.

---

# 17. Arquivos criados ou alterados nesta fase

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
```

Observação importante:

```text
.env não deve ir para o GitHub.
```

Ele existe apenas localmente no computador do desenvolvedor.

---

# 18. Comandos úteis desta fase

## Rodar importação dos CSVs para o PostgreSQL

```bash
python scripts/import_to_postgres.py
```

## Rodar teste de leitura do banco

```bash
python scripts/test_database.py
```

## Conferir status do Git

```bash
git status
```

## Commit sugerido para este checkpoint

```bash
git add docs/postgresql_checkpoint.md
git commit -m "docs: add postgresql checkpoint"
git push
```

Caso os outros arquivos da fase PostgreSQL ainda não tenham sido commitados, usar:

```bash
git add .gitignore requirements.txt database/schema.sql scripts/import_to_postgres.py scripts/database.py scripts/test_database.py docs/postgresql_checkpoint.md
git commit -m "feat: add postgresql integration"
git push
```