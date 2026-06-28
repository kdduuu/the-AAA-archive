# API Plan — The AAA Archive

# Objetivo

Este documento define o planejamento inicial da API do **The AAA Archive**.

A API será responsável por disponibilizar os dados do projeto para outras partes do sistema, como:

* website;
* dashboard;
* futuras aplicações;
* consultas externas.

Este documento foi escrito de forma didática, considerando que a API será construída passo a passo.

---

# O que é uma API?

Uma **API** pode ser entendida como uma ponte entre sistemas.

No caso do The AAA Archive, a API será a ponte entre:

```text id="n7crrm"
dados do projeto
↓
código Python
↓
website / dashboard / usuário
```

Sem API, o site precisaria lidar diretamente com os arquivos CSV ou com a lógica interna do projeto.

Com API, o site apenas faz uma pergunta para um endereço específico e recebe uma resposta organizada.

Exemplo:

```text id="79x5ke"
O site pergunta:
"Quais são todos os jogos?"

A API responde:
"Aqui está a lista de jogos."
```

---

# Exemplo Simples

Imagine que a API tenha este endereço:

```text id="asr7qc"
GET /games
```

Esse endereço significa:

```text id="kd7mmp"
Quero buscar todos os jogos cadastrados.
```

A API então:

1. carrega o `games.csv`;
2. transforma os dados em uma estrutura utilizável;
3. retorna os dados para quem pediu.

A resposta normalmente vem em formato **JSON**.

Exemplo simples de JSON:

```json id="tahauy"
{
  "id": 1,
  "nome": "Resident Evil 4",
  "ano_lancamento": 2005,
  "developer": "Capcom"
}
```

JSON é um formato muito usado para troca de dados entre sistemas.

Ele se parece com um dicionário do Python.

---

# O que é um Endpoint?

Um **endpoint** é um caminho da API.

Cada endpoint representa uma pergunta que o sistema sabe responder.

Exemplos:

```text id="ox05px"
GET /games
GET /games/search
GET /stats/home
GET /awards/winners
```

Cada um desses caminhos terá uma função por trás.

Exemplo conceitual:

```text id="wzj9t3"
GET /games
↓
chama uma função Python
↓
carrega os jogos
↓
retorna os jogos em JSON
```

---

# O que significa GET?

`GET` é um tipo de requisição.

Ele significa que estamos apenas buscando informações.

No The AAA Archive, a primeira versão da API usará apenas `GET`, porque o objetivo inicial será consultar dados.

Exemplos:

```text id="oiy09l"
GET /games
GET /awards
GET /stats/home
```

Nesta fase, a API não vai cadastrar, editar ou apagar dados.

Ela apenas vai ler os dados existentes.

---

# Papel da API no The AAA Archive

A API não substituirá os módulos atuais.

Ela irá reutilizar os módulos que já existem.

O fluxo será:

```text id="sueayx"
Usuário acessa um endpoint
↓
API recebe o pedido
↓
API chama um módulo existente
↓
Módulo processa os dados
↓
API devolve uma resposta em JSON
```

Exemplo:

```text id="lt7ly6"
GET /games/search?term=zelda
↓
API recebe o termo "zelda"
↓
API chama search.py
↓
search.py pesquisa no games.csv
↓
API retorna os jogos encontrados
```

---

# Módulos que a API irá reutilizar

A API deverá reutilizar os módulos já criados no projeto.

## `load_data.py`

Será usado para carregar os datasets:

```text id="e68wjj"
games.csv
awards.csv
```

## `filters.py`

Será usado para endpoints de filtro da Foundation Collection.

Exemplos:

```text id="cjfxvr"
jogos por gênero
jogos por desenvolvedora
jogos por ano
jogos por década
```

## `search.py`

Será usado para endpoints de pesquisa textual.

Exemplo:

```text id="ldoj7o"
buscar jogos que contenham "resident evil"
```

## `site_statistics.py`

Será usado para retornar estatísticas da Home e do Dashboard.

Exemplo:

```text id="hsl5ac"
total de jogos
total de desenvolvedoras
jogos por década
```

## `awards.py`

Será usado para endpoints relacionados ao histórico de premiações.

Exemplos:

```text id="3s882y"
listar vencedores
listar indicados por ano
listar premiações
comparar Awards History com Foundation Collection
```

---

# Primeira Versão da API

A primeira versão da API deve ser simples.

O objetivo não é criar uma arquitetura complexa.

O objetivo é provar que:

```text id="6fozoj"
os dados podem sair dos CSVs
passar pelos módulos Python
e chegar até uma resposta de API
```

---

# Estrutura Inicial Planejada

A estrutura inicial será:

```text id="wk0j5b"
The-AAA-Archive/

api/
  main.py

scripts/
  load_data.py
  filters.py
  search.py
  site_statistics.py
  awards.py
```

Nesta primeira versão, começaremos apenas com:

```text id="42yv8q"
api/main.py
```

Depois, se a API crescer muito, poderemos separar em arquivos menores.

Exemplo futuro:

```text id="exti7m"
api/
  main.py
  routes_games.py
  routes_awards.py
  routes_stats.py
```

Mas isso não será feito no início para evitar complexidade desnecessária.

---

# Endpoints Planejados para a Primeira Versão

## Endpoint inicial

```text id="1pj3fy"
GET /
```

Objetivo:

Verificar se a API está funcionando.

Resposta esperada:

```json id="xs0z58"
{
  "mensagem": "The AAA Archive API está funcionando"
}
```

---

## Jogos

### `GET /games`

Retorna todos os jogos da Foundation Collection.

Módulo usado:

```text id="sk4g02"
load_data.py
```

---

### `GET /games/search`

Pesquisa jogos por termo.

Exemplo:

```text id="cjhq0o"
/games/search?term=zelda
```

Módulo usado:

```text id="npduqq"
search.py
```

---

### `GET /games/developer/{developer}`

Retorna jogos de uma desenvolvedora específica.

Exemplo:

```text id="q54omq"
/games/developer/Capcom
```

Módulo usado:

```text id="k8en10"
filters.py
```

---

### `GET /games/genre/{genre}`

Retorna jogos de um gênero específico.

Exemplo:

```text id="zgcj2z"
/games/genre/Survival Horror
```

Módulo usado:

```text id="8fzw94"
filters.py
```

---

### `GET /games/year/{year}`

Retorna jogos lançados em um ano específico.

Exemplo:

```text id="bdd8ep"
/games/year/2018
```

Módulo usado:

```text id="cnp808"
filters.py
```

---

## Estatísticas

### `GET /stats/home`

Retorna estatísticas gerais para a Home.

Exemplo de informações:

```text id="r34abq"
total de jogos
total de desenvolvedoras
total de franquias
total de gêneros
jogos por década
```

Módulo usado:

```text id="1r9btb"
site_statistics.py
```

---

## Awards

### `GET /awards`

Retorna todos os registros da base Awards History.

Módulo usado:

```text id="xozlel"
load_data.py
```

---

### `GET /awards/{year}`

Retorna vencedor e indicados de um ano específico.

Exemplo:

```text id="aw6f1f"
/awards/2018
```

Módulo usado:

```text id="v53ivx"
awards.py
```

---

### `GET /awards/winners`

Retorna todos os vencedores de Game of the Year.

Módulo usado:

```text id="dewn0h"
awards.py
```

---

### `GET /awards/foundation/winners`

Retorna vencedores de Game of the Year que também estão na Foundation Collection.

Módulo usado:

```text id="oc80cq"
awards.py
```

---

### `GET /awards/foundation/nominees`

Retorna indicados a Game of the Year que também estão na Foundation Collection.

Módulo usado:

```text id="03b4io"
awards.py
```

---

### `GET /awards/foundation/outside`

Retorna jogos presentes no Awards History, mas ausentes da Foundation Collection.

Módulo usado:

```text id="f6l4uv"
awards.py
```

---

# O que a API não fará nesta primeira versão

A primeira versão da API não irá:

* cadastrar novos jogos;
* editar jogos;
* apagar jogos;
* alterar arquivos CSV;
* conectar com banco de dados;
* autenticar usuários;
* ter login;
* ter painel administrativo.

Essas funcionalidades podem existir no futuro, mas não fazem parte da primeira versão.

---

# Resumo da Primeira Versão

A primeira versão da API terá como objetivo:

```text id="5bouox"
ler dados
reutilizar os módulos existentes
retornar respostas em JSON
servir de ponte para o futuro website e dashboard
```

Ela será simples, didática e incremental.

O foco inicial será entender o funcionamento prático de uma API antes de expandir a arquitetura.

---

# Próximo Passo Após Este Documento

Depois deste planejamento, o próximo passo será criar a estrutura inicial:

```text id="09l7p3"
api/
  main.py
```

Em seguida, será criado o primeiro endpoint:

```text id="0humqh"
GET /
```

Esse endpoint servirá apenas para testar se a API está funcionando.

Depois disso, os endpoints serão adicionados aos poucos.
