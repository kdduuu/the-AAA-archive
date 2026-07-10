# Project Conventions — The AAA Archive

# Objetivo

Este documento define os padrões adotados durante o desenvolvimento do **The AAA Archive**.

Seu objetivo é garantir:

* consistência;
* organização;
* clareza;
* segurança;
* facilidade de manutenção;
* evolução controlada;
* alinhamento entre código e documentação.

O documento deve servir como referência para:

* novas implementações;
* alterações no banco;
* criação de módulos;
* mudanças na API;
* evolução do dashboard;
* desenvolvimento futuro do front-end;
* testes;
* documentação;
* commits;
* revisões gerais.

O The AAA Archive é um projeto pessoal e educacional, mas deve ser desenvolvido com uma mentalidade próxima à de um projeto profissional.

Isso significa que cada arquivo, função, módulo, tabela e documento deve existir por um motivo claro dentro do sistema.

---

# Filosofia do Projeto

O **The AAA Archive** é um projeto pessoal desenvolvido por **Kadu Almeida** para estudar e aplicar:

* Python;
* Pandas;
* análise de dados;
* PostgreSQL;
* SQL;
* engenharia de software;
* backend;
* APIs;
* dashboards;
* Git e GitHub;
* documentação;
* testes;
* futuramente, desenvolvimento web.

Embora o projeto possua finalidade educacional, todas as decisões devem buscar organização, clareza e evolução incremental.

O projeto não deve crescer de maneira descontrolada.

Antes de adicionar qualquer funcionalidade, deve-se perguntar:

> Essa alteração resolve uma necessidade real do projeto ou apenas aumenta a complexidade?

Toda funcionalidade implementada deve possuir uma aplicação concreta dentro do sistema.

O projeto deve priorizar:

* clareza antes de complexidade;
* organização antes de velocidade;
* aprendizado antes de atalhos;
* evolução gradual antes de grandes refatorações;
* código simples antes de estruturas exageradas;
* documentação antes de mudanças amplas;
* testes antes de avançar;
* segurança antes de conveniência.

---

# Princípios Gerais

As decisões do projeto devem seguir estes princípios:

1. Uma responsabilidade principal por arquivo.
2. Uma responsabilidade principal por função.
3. Evitar duplicação de lógica.
4. Não adicionar tecnologia sem necessidade.
5. Não modificar várias camadas ao mesmo tempo.
6. Preservar o funcionamento antes de refatorar.
7. Testar mudanças importantes.
8. Atualizar a documentação após alterações.
9. Criar checkpoints ao concluir fases.
10. Manter informações sensíveis fora do repositório.
11. Preservar a simplicidade enquanto ela for suficiente.
12. Toda funcionalidade deve possuir utilidade real no produto.

---

# Stack Tecnológica

## Stack Atual

Atualmente, o projeto utiliza:

* Python;
* Pandas;
* CSV;
* PostgreSQL;
* SQL;
* psycopg;
* python-dotenv;
* FastAPI;
* Streamlit;
* Git;
* GitHub;
* VS Code.

---

## Dados

Os dados editoriais originais são armazenados em:

```text
data/games.csv
data/awards.csv
```

Os dados operacionais são armazenados no PostgreSQL.

Tabelas:

```text
games
awards
```

Os CSVs funcionam como fontes editoriais.

O PostgreSQL funciona como fonte principal para:

* API;
* dashboard;
* testes de integração;
* futura aplicação web.

---

## API

A API atual utiliza:

* FastAPI;
* Pandas;
* PostgreSQL;
* JSON;
* `scripts/database.py`;
* módulos da pasta `scripts/`.

A API realiza operações de leitura.

Ela ainda não possui:

* cadastro;
* edição;
* exclusão;
* autenticação;
* painel administrativo;
* routers separados;
* paginação;
* ordenação avançada;
* filtros combinados.

Novas funcionalidades deverão ser adicionadas apenas quando houver necessidade real da aplicação.

---

## Dashboard

O dashboard utiliza:

* Streamlit;
* Pandas;
* PostgreSQL;
* `st.tabs()`;
* `st.sidebar`;
* `st.metric`;
* gráficos;
* `st.dataframe`;
* cache com `@st.cache_data`;
* funções auxiliares em `dashboard_helpers.py`.

---

## Stack Futura

Futuramente, o projeto poderá utilizar:

* HTML;
* CSS;
* JavaScript;
* biblioteca ou framework front-end;
* ferramentas de deploy;
* routers no FastAPI;
* normalização adicional no banco;
* autenticação;
* painel administrativo;
* armazenamento de imagens.

Tecnologias futuras devem ser escolhidas somente após planejamento.

---

# Arquitetura Atual

```text
CSV
↓
import_to_postgres.py
↓
PostgreSQL
↓
database.py
↓
Módulos Python
↓
API FastAPI e Dashboard Streamlit
↓
Futura aplicação web
```

Responsabilidades:

* CSV: edição e preservação editorial;
* importador: sincronização com o banco;
* PostgreSQL: armazenamento operacional;
* `database.py`: conexão e leitura;
* módulos: lógica reutilizável;
* API: disponibilização em JSON;
* dashboard: análise e visualização;
* front-end futuro: experiência principal do usuário.

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
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

A estrutura poderá evoluir, mas deve preservar a separação de responsabilidades.

---

# Convenções de Nomenclatura

## Arquivos

Utilizar **snake_case** para arquivos Python e documentos internos.

Exemplos:

```text
load_data.py
database.py
import_to_postgres.py
site_statistics.py
api_plan.md
postgresql_checkpoint.md
project_context.md
```

Evitar nomes genéricos ou temporários.

Exemplos ruins:

```text
coisas.py
teste2.py
arquivo_novo.py
dados_final_final.csv
```

---

## Pastas

Pastas devem possuir nomes simples, objetivos e em letras minúsculas.

Exemplos:

```text
api/
dashboard/
data/
database/
docs/
scripts/
assets/
```

---

## Variáveis

Utilizar **snake_case**.

Exemplos:

```python
nome_jogo
ano_lancamento
jogos_filtrados
dados_awards
configuracao_banco
```

Variáveis devem indicar claramente o valor armazenado.

Evitar abreviações desnecessárias.

---

## Funções

Utilizar **snake_case**.

Exemplos:

```python
carregar_dataset()
conectar_postgres()
listar_jogos_por_genero()
buscar_vencedor_por_ano()
gerar_estatisticas_home()
```

Os nomes devem representar:

```text
ação + alvo
```

Evitar nomes vagos:

```python
fazer()
pegar()
coisa()
processar()
```

---

## Classes

Caso classes sejam utilizadas, empregar **PascalCase**.

Exemplos:

```python
Game
Developer
GameAward
DatabaseConnection
```

Classes devem ser introduzidas apenas quando trouxerem uma vantagem real.

Não se deve transformar módulos simples em classes apenas por preferência arquitetural.

---

## Constantes

Utilizar **UPPER_CASE**.

Exemplos:

```python
PROJECT_ROOT
GAMES_CSV_PATH
AWARDS_CSV_PATH
DEFAULT_LIMIT
PROJECT_VERSION
```

Constantes devem representar valores fixos e reutilizados.

---

## Tabelas e Colunas SQL

Utilizar nomes em letras minúsculas e `snake_case`.

Exemplos:

```text
games
awards
ano_lancamento
nota_kadu
historico_importante
```

Evitar:

* espaços;
* acentos;
* nomes ambíguos;
* nomes excessivamente abreviados.

---

## Endpoints

Endpoints devem utilizar nomes em inglês, minúsculos e previsíveis.

Exemplos:

```text
GET /games
GET /games/search
GET /games/year/{year}
GET /awards/winners
```

Os endpoints devem representar recursos ou consultas claras.

---

# Organização do Código

Cada arquivo deve possuir uma responsabilidade principal.

## `load_data.py`

Responsável por carregar os arquivos CSV diretamente.

Esse módulo não deve conter:

* regras de API;
* conexão com PostgreSQL;
* componentes do dashboard.

---

## `import_to_postgres.py`

Responsável por importar os CSVs para PostgreSQL.

Esse módulo pode:

* ler CSVs;
* transformar valores;
* limpar tabelas quando necessário;
* inserir registros;
* validar quantidades.

Ele não deve assumir funções da API ou do dashboard.

---

## `database.py`

Responsável por:

* carregar variáveis do ambiente;
* criar conexão;
* executar consultas de leitura;
* retornar DataFrames;
* centralizar acesso ao PostgreSQL.

Ele não deve conter:

* componentes visuais;
* regras editoriais;
* rotas da API;
* filtros específicos de interface.

---

## `filters.py`

Responsável pelos filtros da Foundation Collection.

---

## `search.py`

Responsável pela pesquisa textual.

---

## `site_statistics.py`

Responsável pelas estatísticas da Foundation Collection.

---

## `awards.py`

Responsável pelas consultas e comparações da Awards History.

---

## `api/main.py`

Responsável por:

* criar a aplicação FastAPI;
* declarar endpoints;
* validar parâmetros;
* chamar os módulos necessários;
* retornar respostas JSON.

O arquivo não deve repetir lógica já existente em outros módulos.

---

## `dashboard/app.py`

Responsável pela estrutura visual principal do dashboard.

Deve conter:

* configuração da página;
* título;
* abas;
* componentes visuais;
* organização da interface.

---

## `dashboard/dashboard_helpers.py`

Responsável por:

* carregar dados;
* aplicar cache;
* executar filtros auxiliares;
* preparar dados para visualização;
* reutilizar lógica do backend.

Esse arquivo deve evitar virar um segundo `app.py`.

---

# Organização das Funções

Cada função deve resolver um problema específico.

Uma função deve, sempre que possível:

1. receber dados ou parâmetros;
2. executar uma tarefa clara;
3. retornar um resultado previsível.

Funções pequenas são mais fáceis de:

* testar;
* reutilizar;
* compreender;
* manter.

Antes de criar uma função, responder:

> Onde esta função será utilizada?

---

# Tipagem

Sempre que for útil e compreensível, utilizar type hints.

Exemplo:

```python
def listar_jogos_por_ano(df: pd.DataFrame, ano: int) -> pd.DataFrame:
    ...
```

A tipagem deve ajudar na leitura.

Ela não deve tornar o código desnecessariamente complexo.

---

# Docstrings

Funções importantes podem utilizar docstrings.

Exemplo:

```python
def carregar_games_do_banco() -> pd.DataFrame:
    """
    Carrega todos os registros da tabela games
    e retorna os dados como DataFrame.
    """
```

Docstrings devem explicar:

* objetivo;
* parâmetros relevantes;
* retorno;
* comportamento especial.

---

# Comentários

Os comentários possuem finalidade didática e técnica.

Eles devem:

* explicar decisões;
* contextualizar lógica;
* facilitar a manutenção;
* apresentar conceitos importantes;
* justificar escolhas menos óbvias.

Evitar comentários que apenas repetem o código.

Exemplo ruim:

```python
# Soma 1
x = x + 1
```

Exemplo melhor:

```python
# Criamos uma cópia para evitar alterações acidentais
# no DataFrame original usado por outras funções.
resultado = df[filtro].copy()
```

Comentários extensos devem ser usados com moderação.

---

# Formatação do Código

O código deve seguir um padrão visual consistente.

Regras gerais:

* quatro espaços de indentação;
* linhas separadas por responsabilidade;
* imports organizados;
* evitar linhas excessivamente longas;
* utilizar espaços ao redor de operadores;
* separar blocos importantes com comentários;
* evitar código morto;
* remover prints temporários após testes.

Organização recomendada dos imports:

```python
# Bibliotecas padrão
from pathlib import Path
import sys

# Bibliotecas externas
import pandas as pd
from fastapi import FastAPI

# Módulos internos
from scripts.database import carregar_games_do_banco
```

---

# Organização dos Dados

## Foundation Collection

Arquivo editorial:

```text
data/games.csv
```

Tabela operacional:

```text
games
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

A documentação oficial fica em:

```text
docs/data_dictionary.md
```

---

## Awards History

Arquivo editorial:

```text
data/awards.csv
```

Tabela operacional:

```text
awards
```

Colunas no CSV:

```text
ano
premiacao
jogo
status
```

A tabela também possui o campo:

```text
id
```

A documentação oficial fica em:

```text
docs/awards_dictionary.md
```

---

# Relação entre CSV e PostgreSQL

O projeto mantém duas representações dos dados:

```text
CSV
→ fonte editorial

PostgreSQL
→ fonte operacional
```

O fluxo oficial de atualização é:

```text
Editar CSV
↓
Executar import_to_postgres.py
↓
Validar quantidades
↓
Executar testes
↓
Utilizar dados na API e no dashboard
```

Não se deve editar manualmente o PostgreSQL e esquecer de atualizar os CSVs.

Enquanto o projeto seguir esse modelo, os CSVs são a fonte principal de edição.

---

# Regras para o Banco de Dados

## Schema

A estrutura oficial está em:

```text
database/schema.sql
```

Mudanças em tabelas devem ser refletidas nesse arquivo.

---

## Chaves Primárias

Toda tabela deve possuir uma chave primária.

Atualmente:

```text
games.id
awards.id
```

---

## Valores Nulos

Campos opcionais podem aceitar `NULL`.

Campos essenciais devem utilizar `NOT NULL`.

Exemplo:

```sql
nome VARCHAR(200) NOT NULL
```

---

## Tipos de Dados

Escolher tipos compatíveis com o conteúdo.

Exemplos:

```text
INTEGER
VARCHAR
TEXT
NUMERIC
BOOLEAN
SERIAL
```

Não utilizar texto para valores que deveriam ser numéricos ou booleanos.

---

## Alterações no Schema

Antes de alterar o schema:

1. definir a necessidade;
2. atualizar a documentação;
3. atualizar `schema.sql`;
4. ajustar os CSVs, se necessário;
5. ajustar o importador;
6. ajustar o código;
7. atualizar testes;
8. validar o banco;
9. registrar a alteração.

---

# Variáveis de Ambiente

As configurações sensíveis devem ficar em:

```text
.env
```

Exemplo:

```env
POSTGRES_DB=aaa_archive
POSTGRES_USER=postgres
POSTGRES_PASSWORD=sua_senha
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

O `.env` nunca deve ser:

* enviado ao GitHub;
* incluído em ZIP público;
* mostrado em documentação;
* compartilhado com credenciais reais;
* copiado para exemplos.

---

## `.env.example`

O projeto deve possuir:

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

Esse arquivo pode ser versionado porque não contém credenciais reais.

---

# Segurança

Arquivos e pastas que não devem ser compartilhados publicamente:

```text
.env
.venv/
__pycache__/
.git/
```

Outros cuidados:

* não escrever senha dentro do código;
* não imprimir senha no terminal;
* não registrar credenciais em commits;
* não inserir credenciais em screenshots;
* revisar ZIPs antes de compartilhar;
* trocar senhas expostas acidentalmente;
* utilizar variáveis de ambiente.

---

# Fontes dos Dados

Sempre que possível, utilizar fontes oficiais ou verificáveis.

## Dados técnicos dos jogos

Possíveis fontes:

* páginas oficiais;
* IGDB;
* Metacritic;
* documentações públicas;
* sites reconhecidos da indústria;
* materiais das desenvolvedoras e publishers.

---

## Dados de premiações

Possíveis fontes:

* páginas oficiais;
* registros das premiações;
* arquivos públicos confiáveis;
* veículos jornalísticos reconhecidos.

---

## Conteúdo editorial

Conteúdo produzido para o Archive:

* descrições;
* notas;
* marcações históricas;
* marcações de influência;
* critérios de curadoria;
* textos explicativos;
* justificativas de inclusão.

Informações factuais e opiniões editoriais devem ser diferenciadas.

---

# Regras Editoriais

A Foundation Collection é uma curadoria.

A entrada de um jogo deve considerar:

* relevância histórica;
* influência;
* impacto cultural;
* reconhecimento;
* importância dentro de uma franquia;
* contribuição para a indústria;
* coerência com o recorte AAA single-player.

Vencer ou ser indicado a um prêmio não garante inclusão automática.

A Awards History não deve controlar a Foundation Collection.

---

# API

A API está em:

```text
api/main.py
```

A versão atual:

* utiliza PostgreSQL;
* retorna JSON;
* realiza operações de leitura;
* reutiliza os módulos;
* possui versão `0.2.0`.

Ela ainda não possui:

* criação;
* edição;
* exclusão;
* autenticação;
* routers;
* paginação;
* filtros combinados;
* ordenação avançada.

Novos endpoints devem nascer de necessidades reais da aplicação web.

---

# Endpoints Atuais

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

O dashboard está em:

```text
dashboard/app.py
```

As funções auxiliares ficam em:

```text
dashboard/dashboard_helpers.py
```

O dashboard atual está concluído para esta fase.

Ele não deve receber grandes funcionalidades antes do planejamento da aplicação web.

Mudanças futuras devem preservar:

* clareza;
* reutilização;
* separação da interface;
* funcionamento dos filtros;
* conexão com PostgreSQL.

---

# Testes

Sempre que uma função relevante for criada ou alterada, seu teste deve ser criado ou atualizado.

Testes atuais:

```text
scripts/test_filters.py
scripts/test_search.py
scripts/test_site_statistics.py
scripts/test_awards.py
scripts/test_database.py
api/test_main.py
```

Comandos:

```bash
python scripts/test_filters.py
python scripts/test_search.py
python scripts/test_site_statistics.py
python scripts/test_awards.py
python scripts/test_database.py
python api/test_main.py
```

Os testes de banco e API dependem do PostgreSQL configurado.

---

## Convenções dos Testes

Os testes devem:

* validar comportamento real;
* possuir mensagens claras;
* evitar dependências desnecessárias;
* utilizar dados previsíveis;
* testar casos de sucesso;
* testar listas vazias quando relevante;
* testar parâmetros inválidos quando necessário.

Os testes que validam quantidades fixas devem ser atualizados quando o dataset crescer.

---

# Requirements

O arquivo de dependências é:

```text
requirements.txt
```

Ele deve conter apenas pacotes necessários para executar o projeto.

Dependências principais esperadas:

```text
pandas
fastapi
uvicorn
streamlit
psycopg
python-dotenv
```

Não inserir comandos dentro do arquivo.

Exemplo incorreto:

```text
pip freeze > requirements.txt
```

---

# Documentação

Documentos gerais devem representar o estado atual.

Documentos de plano podem preservar decisões históricas, desde que indiquem que a fase foi concluída.

Categorias:

```text
Contexto
Blueprint
Convenções
Dicionários
Planos
Checkpoints
README
```

---

## Documentos de Estado Atual

Devem ser mantidos atualizados:

```text
README.md
project_context.md
project_blueprint.md
project_conventions.md
```

---

## Documentos de Planejamento

Exemplos:

```text
api_plan.md
dashboard_plan.md
postgresql_plan.md
```

Ao concluir uma fase, adicionar uma observação indicando que o documento representa o planejamento anterior.

---

## Checkpoints

Exemplos:

```text
api_checkpoint.md
dashboard_checkpoint.md
postgresql_checkpoint.md
```

Checkpoints devem registrar:

* o que foi feito;
* estado final;
* arquivos envolvidos;
* testes;
* decisões;
* limitações;
* próximos passos.

---

# Padrão dos Commits

Utilizar mensagens curtas, objetivas e descritivas.

Formato recomendado:

```text
tipo: descrição
```

Tipos:

```text
docs
feat
fix
refactor
test
data
chore
```

Exemplos:

```text
docs: update project context
docs: align PostgreSQL documentation
feat: add database connection layer
feat: migrate api to PostgreSQL
refactor: organize dashboard helpers
fix: correct awards comparison
data: update foundation collection
test: add database tests
chore: add env example
```

Um commit deve representar um conjunto coerente de alterações.

Evitar misturar:

* documentação;
* nova funcionalidade;
* refatoração;
* grandes mudanças de dados;

no mesmo commit, quando puderem ser separados.

---

# Git

Antes de iniciar uma nova fase:

```bash
git status
```

Confirmar:

* arquivos alterados;
* arquivos novos;
* `.env` não rastreado;
* ausência de arquivos temporários;
* testes executados.

Depois:

```bash
git add .
git commit -m "mensagem"
git push
```

O comando `git add .` deve ser utilizado apenas após revisar o `git status`.

---

# `.gitignore`

O `.gitignore` deve incluir, quando aplicável:

```gitignore
.env
.venv/
venv/
__pycache__/
*.pyc
.pytest_cache/
```

Pastas ou arquivos gerados automaticamente não devem ser versionados.

---

# Ordem Recomendada Antes de Grandes Mudanças

Antes de iniciar uma nova fase:

```text
1. Verificar o estado atual.
2. Confirmar que a documentação está alinhada.
3. Executar os testes.
4. Corrigir problemas encontrados.
5. Confirmar o git status.
6. Criar um commit estável.
7. Planejar a próxima fase.
8. Só depois implementar.
```

---

# Fluxo de Desenvolvimento

Toda funcionalidade deve seguir:

```text
Identificar necessidade
↓
Definir onde será usada
↓
Definir camada responsável
↓
Planejar
↓
Implementar
↓
Testar
↓
Documentar
↓
Criar checkpoint
```

---

# Refatorações

Refatorações devem:

* preservar comportamento;
* acontecer separadamente de novas funcionalidades;
* manter testes passando;
* ser documentadas quando alterarem estrutura;
* evitar abstrações desnecessárias.

Não criar:

* classes;
* camadas;
* pastas;
* padrões complexos;

sem uma justificativa clara.

---

# Tratamento de Erros

Funções de conexão, leitura e importação devem apresentar erros compreensíveis.

Evitar esconder exceções sem explicação.

Mensagens devem ajudar a identificar:

* variável ausente;
* banco desligado;
* tabela inexistente;
* arquivo ausente;
* coluna incorreta;
* falha de importação.

Não expor senhas ou credenciais nas mensagens.

---

# Fase Atual do Projeto

A fase PostgreSQL foi concluída.

Concluído:

* datasets;
* módulos;
* testes;
* API;
* dashboard;
* PostgreSQL;
* schema;
* importador;
* camada de banco;
* migração da API;
* migração do dashboard;
* checkpoints da fase.

A fase atual é o alinhamento final da documentação e da segurança do repositório.

Atividades atuais:

* atualizar documentos gerais;
* revisar dicionários;
* marcar planos concluídos;
* criar `.env.example`;
* revisar `.gitignore`;
* executar testes;
* criar commit de checkpoint.

---

# Diretrizes da Fase Atual

Durante esta fase:

* não iniciar front-end;
* não adicionar endpoints;
* não alterar o schema;
* não expandir o dashboard;
* não remover os CSVs;
* não mudar a fonte operacional;
* não adicionar autenticação;
* não normalizar o banco;
* não expor credenciais.

O objetivo é encerrar a fase PostgreSQL de maneira estável.

---

# Próxima Fase

Após o encerramento atual:

```text
Planejamento do front-end
```

Nessa fase serão definidos:

* objetivo da aplicação;
* experiência;
* identidade visual;
* páginas;
* navegação;
* conteúdo;
* consumo da API;
* stack;
* deploy futuro.

Nenhuma tecnologia de front-end deve ser escolhida antes desse planejamento.

---

# Princípios Finais

Durante todo o desenvolvimento:

* clareza acima da complexidade;
* organização acima da velocidade;
* qualidade acima da quantidade;
* documentação antes de grandes mudanças;
* evolução incremental;
* código compreensível;
* código reutilizável;
* responsabilidade clara por módulo;
* testes simples, mas úteis;
* segurança de credenciais;
* projeto orientado a produto;
* projeto orientado a aprendizado;
* estrutura simples enquanto for suficiente.

---

# Objetivo Final

Construir um sistema capaz de preservar, organizar, analisar e disponibilizar informações sobre videogames por meio de:

* curadoria editorial;
* datasets estruturados;
* PostgreSQL;
* backend modular;
* API;
* dashboard;
* aplicação web;
* documentação consistente;
* testes;
* evolução técnica controlada.

O The AAA Archive deve evoluir continuamente sem perder:

* consistência;
* identidade;
* clareza;
* simplicidade;
* organização.