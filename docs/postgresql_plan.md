# PostgreSQL Plan — The AAA Archive

## Objetivo deste Documento

Este documento registra o planejamento inicial da migração do **The AAA Archive** de uma execução baseada diretamente em arquivos CSV para uma arquitetura com banco de dados **PostgreSQL**.

A fase foi planejada para compreender:

* onde o PostgreSQL entraria no projeto;
* por que ele seria utilizado;
* qual seria o papel dos CSVs;
* como os dados seriam importados;
* quais arquivos seriam afetados;
* como preservar os módulos existentes;
* como migrar a API;
* como migrar o dashboard;
* como testar cada etapa;
* como evitar complexidade prematura.

Este documento foi escrito antes da implementação da fase.

Atualmente, o plano já foi executado.

O resultado final está documentado em:

```text
docs/postgresql_checkpoint.md
```

Portanto, este arquivo deve ser entendido como:

```text
registro histórico do planejamento da fase PostgreSQL
```

Ele não representa sozinho o estado técnico mais recente do projeto.

---

# Status do Plano

Status:

```text
Plano executado
```

Resultado:

```text
PostgreSQL instalado, configurado e integrado ao projeto
```

Banco criado:

```text
aaa_archive
```

Schema utilizado:

```text
public
```

Tabelas criadas:

```text
games
awards
```

Integrações concluídas:

```text
Python
FastAPI
Streamlit
```

---

# Contexto Antes da Migração

Antes da implementação do PostgreSQL, o The AAA Archive utilizava os arquivos:

```text
data/games.csv
data/awards.csv
```

como fontes diretas de execução.

Fluxo anterior:

```text
CSV
↓
Pandas
↓
Módulos Python
↓
API / Dashboard
```

Essa arquitetura foi importante para aprender:

* leitura de arquivos;
* organização de datasets;
* Pandas;
* filtros;
* busca textual;
* estatísticas;
* módulos reutilizáveis;
* FastAPI;
* Streamlit;
* testes;
* documentação.

Ela permitiu construir uma base funcional antes da introdução do banco de dados.

---

# Por que o PostgreSQL Foi Adicionado?

O PostgreSQL foi adicionado porque o The AAA Archive deixou de ser apenas um conjunto de scripts independentes e passou a funcionar como um sistema composto por diferentes camadas.

O banco permite:

* armazenar dados de forma centralizada;
* utilizar consultas SQL;
* separar edição editorial de execução operacional;
* preparar o backend para uma aplicação web;
* criar uma fonte comum para API e dashboard;
* praticar banco de dados relacional;
* aproximar o projeto de uma arquitetura profissional;
* preparar futuras relações entre entidades;
* permitir expansões futuras.

A introdução do banco não teve como objetivo tornar o projeto imediatamente complexo.

A meta foi criar uma primeira integração simples e compreensível.

---

# O que é PostgreSQL?

O PostgreSQL é um sistema de gerenciamento de banco de dados relacional.

De forma simplificada, ele armazena informações em tabelas organizadas.

Estrutura do projeto:

```text
Banco: aaa_archive
│
└── Schema: public
    │
    ├── games
    └── awards
```

Cada tabela possui:

* colunas;
* tipos de dados;
* registros;
* chave primária;
* regras estruturais.

O banco permite consultar os dados com SQL.

Exemplos:

```sql
SELECT * FROM games;
SELECT * FROM awards;
```

---

# Objetivo Original da Migração

O objetivo principal era transformar este fluxo:

```text
CSV
↓
Pandas
↓
API / Dashboard
```

neste fluxo:

```text
CSV editorial
↓
Importação
↓
PostgreSQL
↓
Python
↓
API / Dashboard
```

Essa mudança foi concluída.

---

# Arquitetura Atual

A arquitetura resultante é:

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
Módulos Python
        ↓
FastAPI e Streamlit
```

Responsabilidades:

```text
CSV
→ fonte editorial

import_to_postgres.py
→ importação e sincronização

PostgreSQL
→ fonte operacional

database.py
→ conexão e leitura

módulos Python
→ lógica reutilizável

FastAPI
→ disponibilização em JSON

Streamlit
→ visualização e análise
```

---

# O que Mudou com PostgreSQL?

Antes da migração:

* API carregava CSVs;
* dashboard carregava CSVs;
* `load_data.py` era a principal porta de entrada;
* a fonte operacional estava distribuída em arquivos.

Depois da migração:

* API carrega dados do PostgreSQL;
* dashboard carrega dados do PostgreSQL;
* `database.py` centraliza o acesso;
* os CSVs alimentam o banco;
* o PostgreSQL é a fonte operacional;
* os módulos continuam trabalhando com DataFrames.

---

# O que Permaneceu Igual?

A migração preservou:

* endpoints;
* filtros;
* pesquisa;
* estatísticas;
* consultas da Awards History;
* estrutura visual do dashboard;
* DataFrames Pandas;
* arquivos CSV;
* módulos Python;
* testes anteriores.

A principal mudança foi:

```text
origem dos dados
```

Antes:

```text
CSV
```

Agora:

```text
PostgreSQL
```

---

# Papel Atual dos CSVs

Os CSVs não foram removidos.

Arquivos:

```text
data/games.csv
data/awards.csv
```

Eles continuam sendo utilizados como:

* fonte editorial;
* forma principal de edição manual;
* base de importação;
* referência original;
* histórico da coleção;
* fonte para alguns testes;
* cópia simples dos dados.

O fluxo atual de atualização é:

```text
Editar CSV
↓
Executar import_to_postgres.py
↓
Atualizar PostgreSQL
↓
Executar testes
↓
API e dashboard usam os dados atualizados
```

---

# Decisão de Modelagem

A primeira versão com PostgreSQL foi propositalmente simples.

Foram criadas apenas duas tabelas:

```text
games
awards
```

A estrutura respeita os datasets atuais:

```text
data/games.csv
→ public.games

data/awards.csv
→ public.awards
```

Essa decisão evitou:

* normalização prematura;
* muitas tabelas;
* relacionamentos complexos;
* necessidade de reescrever todos os módulos;
* dificuldade excessiva durante o aprendizado inicial.

---

# Banco de Dados

Nome:

```text
aaa_archive
```

Schema:

```text
public
```

O banco deve existir antes da execução dos scripts de importação e dos componentes que dependem dele.

---

# Tabela `games`

A tabela `games` representa a Foundation Collection.

Fonte:

```text
data/games.csv
```

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
66 registros
```

---

# Tabela `awards`

A tabela `awards` representa a Awards History.

Fonte:

```text
data/awards.csv
```

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

O campo `id` é gerado automaticamente pelo PostgreSQL.

Ele não existe no CSV original.

---

# Arquivo de Schema

A estrutura oficial das tabelas está registrada em:

```text
database/schema.sql
```

Esse arquivo permite:

* consultar o modelo;
* recriar tabelas;
* documentar tipos;
* manter código SQL versionado;
* evitar dependência exclusiva de configurações manuais no pgAdmin.

Mudanças futuras no banco devem ser refletidas nesse arquivo.

---

# Por que Não Normalizar Tudo?

Um modelo mais normalizado poderia utilizar:

```text
games
developers
genres
franchises
awards
award_editions
award_nominees
```

Porém, esse modelo exigiria:

* novas chaves;
* relacionamentos;
* joins;
* tabelas auxiliares;
* mudanças no importador;
* mudanças nos módulos;
* mudanças na API;
* mudanças no dashboard.

A estrutura atual é suficiente para a primeira integração.

Normalização só deverá ser realizada quando trouxer benefício real.

---

# Comparação entre CSV e PostgreSQL

## CSV

Vantagens:

* simples;
* fácil de editar;
* fácil de visualizar;
* adequado para curadoria manual;
* integrado ao Pandas;
* fácil de versionar.

Limitações:

* pouca garantia de integridade;
* ausência de consultas SQL;
* dificuldade de relacionamentos;
* pouca adequação para escrita concorrente;
* menor separação entre dados e aplicação.

---

## PostgreSQL

Vantagens:

* armazenamento centralizado;
* tipos de dados;
* chaves primárias;
* consultas SQL;
* possibilidade de relacionamentos;
* integração com aplicações;
* melhor preparação para crescimento;
* persistência operacional.

Custos:

* instalação;
* configuração;
* credenciais;
* gerenciamento do serviço;
* maior complexidade;
* dependência de conexão.

Por isso, os dois formatos possuem papéis diferentes no projeto atual.

---

# Estratégia de Migração Adotada

A estratégia planejada foi:

```text
1. Criar o banco.
2. Criar as tabelas.
3. Importar os CSVs.
4. Testar consultas SQL.
5. Criar conexão Python.
6. Retornar dados como DataFrames.
7. Comparar banco e CSV.
8. Migrar a API.
9. Migrar o dashboard.
10. Executar os testes.
11. Documentar o resultado.
```

Essa estratégia foi seguida com sucesso.

---

# Fase 1 — Instalação e Primeiro Contato

Objetivo original:

* instalar PostgreSQL;
* utilizar ferramenta visual;
* compreender servidor;
* compreender banco;
* compreender schema;
* compreender tabela;
* executar SQL simples.

Resultado:

```text
Concluído
```

Foram utilizados conceitos como:

```sql
SELECT * FROM games;
SELECT * FROM awards;
```

---

# Fase 2 — Criação do Banco e das Tabelas

Objetivo:

* criar `aaa_archive`;
* utilizar o schema `public`;
* criar `games`;
* criar `awards`;
* reproduzir a estrutura dos CSVs.

Resultado:

```text
Concluído
```

---

# Fase 3 — Importação dos CSVs

Objetivo:

```text
games.csv
→ games

awards.csv
→ awards
```

Arquivo criado:

```text
scripts/import_to_postgres.py
```

Resultado:

```text
Concluído
```

O script é responsável por:

* carregar os CSVs;
* preparar os dados;
* tratar valores nulos;
* conectar ao banco;
* inserir registros;
* validar quantidades;
* apresentar mensagem de conclusão.

---

# Fase 4 — Conexão entre Python e PostgreSQL

Objetivo:

```text
Python
↓
PostgreSQL
↓
SELECT
↓
DataFrame
```

Resultado:

```text
Concluído
```

Bibliotecas relacionadas:

```text
psycopg
python-dotenv
pandas
```

---

# Fase 5 — Criação do Módulo de Banco

Arquivo criado:

```text
scripts/database.py
```

Responsabilidades:

* carregar configurações;
* conectar ao PostgreSQL;
* executar consultas;
* retornar DataFrames;
* contar registros;
* evitar repetição de conexão.

Resultado:

```text
Concluído
```

---

# Funções do Módulo de Banco

Funções implementadas:

```python
obter_configuracao_banco()
conectar_postgres()
executar_select()
carregar_games_do_banco()
carregar_awards_do_banco()
contar_games_do_banco()
contar_awards_do_banco()
```

Essas funções centralizam o acesso operacional ao banco.

---

# Fase 6 — Carregamento em DataFrames

O plano previa manter o uso de Pandas durante a transição.

Resultado:

```text
Concluído
```

Fluxo:

```text
PostgreSQL
↓
consulta SQL
↓
DataFrame Pandas
↓
módulos existentes
```

Essa decisão evitou reescrever:

* filtros;
* pesquisa;
* estatísticas;
* comparações;
* conversão para JSON;
* lógica do dashboard.

---

# Fase 7 — Migração da API

Objetivo:

* manter os endpoints;
* trocar apenas a origem dos dados;
* informar PostgreSQL como fonte;
* manter respostas JSON;
* preservar os testes.

Antes:

```text
FastAPI
↓
load_data.py
↓
CSV
```

Depois:

```text
FastAPI
↓
database.py
↓
PostgreSQL
```

Resultado:

```text
Concluído
```

Versão atual:

```text
0.2.0
```

---

# Fase 8 — Migração do Dashboard

Objetivo:

* manter o visual;
* preservar filtros;
* preservar métricas;
* preservar gráficos;
* utilizar PostgreSQL;
* reutilizar `database.py`.

Antes:

```text
Streamlit
↓
load_data.py
↓
CSV
```

Depois:

```text
Streamlit
↓
dashboard_helpers.py
↓
database.py
↓
PostgreSQL
```

Resultado:

```text
Concluído
```

---

# Fase 9 — Revisão dos Testes

O plano previa manter os testes existentes e adicionar testes específicos do banco.

Arquivo criado:

```text
scripts/test_database.py
```

Resultado:

```text
Concluído
```

O projeto possui atualmente:

```text
scripts/test_filters.py
scripts/test_search.py
scripts/test_site_statistics.py
scripts/test_awards.py
scripts/test_database.py
api/test_main.py
```

---

# Teste do Banco

Comando:

```bash
python scripts/test_database.py
```

O teste verifica:

* leitura do `.env`;
* conexão;
* acesso às tabelas;
* retorno como DataFrame;
* quantidade de registros;
* presença das colunas esperadas.

Resultado esperado:

```text
TODOS OS TESTES DO BANCO PASSARAM!
```

---

# Teste da API

Comando:

```bash
python api/test_main.py
```

O teste verifica:

* rota inicial;
* versão;
* fonte de dados;
* endpoints;
* filtros;
* pesquisa;
* estatísticas;
* Awards History;
* quantidades esperadas.

Resultado esperado:

```text
TODOS OS TESTES DA API PASSARAM!
```

---

# Sequência Recomendada de Testes

```bash
python scripts/test_filters.py
python scripts/test_search.py
python scripts/test_site_statistics.py
python scripts/test_awards.py
python scripts/test_database.py
python api/test_main.py
```

Depois:

```bash
streamlit run dashboard/app.py
```

para validação manual do dashboard.

---

# Variáveis de Ambiente

As configurações do PostgreSQL são armazenadas em:

```text
.env
```

Variáveis:

```env
POSTGRES_DB=aaa_archive
POSTGRES_USER=postgres
POSTGRES_PASSWORD=sua_senha
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

Essa decisão evita inserir credenciais diretamente no código.

---

# `.env.example`

O projeto deve possuir um arquivo público de exemplo:

```text
.env.example
```

Conteúdo esperado:

```env
POSTGRES_DB=aaa_archive
POSTGRES_USER=postgres
POSTGRES_PASSWORD=sua_senha_aqui
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

Esse arquivo não deve conter credenciais reais.

---

# Segurança

O arquivo `.env` deve permanecer:

* fora do Git;
* fora de ZIPs públicos;
* fora de screenshots;
* fora da documentação;
* fora de mensagens compartilhadas.

Também não devem ser compartilhados:

```text
.git/
.venv/
__pycache__/
```

Caso uma senha seja exposta, ela deve ser alterada.

---

# Arquivos Criados na Fase

```text
database/schema.sql
scripts/database.py
scripts/import_to_postgres.py
scripts/test_database.py
docs/postgresql_plan.md
docs/postgresql_checkpoint.md
```

Também foram alterados:

```text
api/main.py
api/test_main.py
dashboard/dashboard_helpers.py
requirements.txt
.gitignore
```

---

# Partes do Projeto Afetadas

## `load_data.py`

Continua responsável por carregar os CSVs.

Não foi substituído.

Seu papel atual é:

* leitura editorial;
* testes;
* validação dos arquivos originais.

---

## `filters.py`

Continua trabalhando com DataFrames.

Não foi necessário substituí-lo por SQL nesta fase.

---

## `search.py`

Continua utilizando Pandas.

Busca diretamente nos DataFrames carregados do banco.

---

## `site_statistics.py`

Continua calculando estatísticas com Pandas.

---

## `awards.py`

Continua comparando DataFrames da Awards History e da Foundation Collection.

---

## `api/main.py`

Foi alterado para carregar os dados por `database.py`.

---

## `dashboard/dashboard_helpers.py`

Foi alterado para carregar os dados por `database.py`.

---

# Decisão de Preservar DataFrames

A migração não converteu toda a lógica para SQL.

Essa decisão permitiu:

* reaproveitar os módulos;
* reduzir riscos;
* manter os testes;
* aprender PostgreSQL gradualmente;
* separar migração de refatoração;
* manter a interface funcionando.

No futuro, algumas operações poderão ser executadas diretamente no banco.

Isso não é necessário agora.

---

# Decisão de Preservar os Endpoints

Os endpoints foram mantidos.

Exemplo:

```text
GET /games
```

Antes:

```text
dados do CSV
```

Agora:

```text
dados do PostgreSQL
```

Para quem utiliza a API, a estrutura principal permanece estável.

---

# Decisão de Preservar o Dashboard

A migração não alterou:

* abas;
* filtros;
* pesquisa;
* métricas;
* gráficos;
* tabelas;
* recorte editorial.

Apenas a origem dos dados foi modificada.

---

# Decisão sobre Normalização

A normalização completa foi adiada.

Possíveis tabelas futuras:

```text
developers
genres
franchises
platforms
award_editions
award_nominees
```

Essa evolução dependerá de necessidades concretas da aplicação.

---

# Estrutura Atual Relacionada ao Banco

```text
The-AAA-Archive/
│
├── database/
│   └── schema.sql
│
├── scripts/
│   ├── database.py
│   ├── import_to_postgres.py
│   └── test_database.py
│
├── data/
│   ├── games.csv
│   └── awards.csv
│
├── api/
│   ├── main.py
│   └── test_main.py
│
├── dashboard/
│   ├── app.py
│   └── dashboard_helpers.py
│
└── .env
```

---

# Critérios de Sucesso Planejados

O plano definia que a migração seria considerada bem-sucedida quando:

* PostgreSQL estivesse instalado;
* o banco `aaa_archive` existisse;
* a tabela `games` existisse;
* a tabela `awards` existisse;
* os dados fossem importados;
* consultas SQL funcionassem;
* Python conectasse ao banco;
* os dados fossem carregados em DataFrames;
* banco e CSV apresentassem quantidades compatíveis;
* API utilizasse o banco;
* dashboard utilizasse o banco;
* testes passassem.

Todos esses critérios foram atendidos.

---

# Critérios de Sucesso Atendidos

```text
PostgreSQL instalado ✅
Banco aaa_archive criado ✅
Schema public utilizado ✅
Tabela games criada ✅
Tabela awards criada ✅
schema.sql criado ✅
CSV games importado ✅
CSV awards importado ✅
66 jogos importados ✅
127 registros de awards importados ✅
Conexão Python criada ✅
database.py criado ✅
DataFrames retornados ✅
test_database.py criado ✅
Teste do banco passando ✅
API migrada ✅
API 0.2.0 ✅
Testes da API passando ✅
Dashboard migrado ✅
Dashboard validado ✅
CSV preservado ✅
Documentação criada ✅
```

---

# Limitações Atuais

A primeira integração ainda possui limitações:

* PostgreSQL depende do ambiente local;
* não existe banco de produção;
* não existe banco separado para testes;
* a API continua somente de leitura;
* o dashboard continua somente de leitura;
* filtros ainda são aplicados principalmente com Pandas;
* não há relacionamentos por chave estrangeira;
* as tabelas ainda não estão normalizadas;
* não há migrations automatizadas;
* não há deploy;
* as quantidades estão fixas em alguns testes.

Essas limitações são aceitáveis para esta fase.

---

# O que Não Foi Implementado

Não fazem parte desta primeira integração:

* autenticação;
* painel administrativo;
* criação de registros pela API;
* edição;
* exclusão;
* migrations com ferramenta externa;
* ORM;
* SQLAlchemy;
* normalização completa;
* banco em nuvem;
* deploy;
* controle de usuários;
* permissões avançadas;
* backup automatizado.

---

# Possíveis Evoluções Futuras

Depois que houver necessidade real, poderão ser avaliados:

* normalização;
* chaves estrangeiras;
* consultas SQL para filtros;
* busca textual no PostgreSQL;
* índices;
* paginação;
* banco de testes;
* migrations;
* ORM;
* operações de escrita;
* painel administrativo;
* autenticação;
* deploy;
* backups;
* relacionamentos entre awards e games por ID.

Essas melhorias não devem ser implementadas todas ao mesmo tempo.

---

# O que Não Fazer Agora

Durante o fechamento da fase, não é recomendado:

```text
normalizar todo o banco
criar dezenas de tabelas
reescrever todos os módulos em SQL
adicionar autenticação
criar operações de escrita
adicionar ORM sem necessidade
alterar o dashboard
alterar endpoints
iniciar o front-end antes de fechar a documentação
```

---

# Resultado do Plano

Estado anterior:

```text
CSV
↓
Pandas
↓
API / Dashboard
```

Estado alcançado:

```text
CSV editorial
↓
Importação
↓
PostgreSQL
↓
Camada Python
↓
API / Dashboard
```

O objetivo principal da fase foi concluído.

---

# Relação com o PostgreSQL Checkpoint

Este documento registra:

```text
o que foi planejado
```

O documento:

```text
docs/postgresql_checkpoint.md
```

registra:

```text
o que foi implementado
```

O checkpoint deve ser utilizado como principal referência técnica da fase concluída.

---

# Ordem Original Recomendada

A ordem planejada foi:

```text
1. Criar o plano.
2. Entender PostgreSQL.
3. Instalar PostgreSQL.
4. Criar o banco.
5. Criar as tabelas.
6. Importar os CSVs.
7. Testar SQL.
8. Criar conexão Python.
9. Retornar DataFrames.
10. Comparar CSV e banco.
11. Adaptar a API.
12. Adaptar o dashboard.
13. Revisar testes.
14. Documentar.
```

Essa ordem foi executada.

---

# Estado Atual do Projeto Após o Plano

```text
Foundation Collection definida
Awards History definida
CSV editorial preservado
PostgreSQL operacional
Importador funcionando
Camada de banco funcionando
API integrada
Dashboard integrado
Testes passando
Documentação em atualização final
```

---

# Próxima Etapa

A próxima etapa não é continuar expandindo o PostgreSQL.

Antes de qualquer nova fase:

```text
Finalizar documentação
↓
Criar .env.example
↓
Revisar .gitignore
↓
Executar testes finais
↓
Criar commit de checkpoint
```

Somente depois:

```text
Planejar a aplicação web
```

---

# Status Final

Status deste plano:

```text
Executado
```

Resultado:

```text
Migração para PostgreSQL concluída
```

Arquitetura atual:

```text
CSV editorial
↓
PostgreSQL
↓
Python
↓
FastAPI / Streamlit
```

---

# Status do Documento

```text
Documento histórico de planejamento concluído
```

Este arquivo deve ser preservado como registro das decisões, expectativas e etapas que orientaram a primeira integração do The AAA Archive com PostgreSQL.
