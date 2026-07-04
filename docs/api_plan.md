# API Plan — The AAA Archive

# Objetivo

Este documento registra o planejamento inicial da API do **The AAA Archive**.

A API foi planejada para disponibilizar os dados do projeto para outras partes do sistema, como:

* website;
* dashboard;
* futuras aplicações;
* consultas externas.

Este documento foi escrito de forma didática, considerando que a API seria construída passo a passo.

Atualmente, este plano já foi executado.

A primeira versão da API foi criada, testada e documentada no arquivo:

```text
docs/api_checkpoint.md
```

Portanto, este documento deve ser entendido como um registro histórico do planejamento inicial da API.

---

# Status do Plano

Status atual:

```text
Plano executado
```

A API inicial foi implementada com **FastAPI**.

Ela está localizada em:

```text
api/main.py
```

Os testes da API estão localizados em:

```text
api/test_main.py
```

A API atual utiliza:

* CSV;
* Pandas;
* módulos da pasta `scripts/`;
* respostas em JSON;
* endpoints apenas de leitura.

A API inicial está fechada por enquanto.

Nesta fase, não há intenção de adicionar novos endpoints.

---

# O que é uma API?

Uma **API** pode ser entendida como uma ponte entre sistemas.

No caso do The AAA Archive, a API é a ponte entre:

```text
dados do projeto
↓
código Python
↓
respostas em JSON
↓
futuras interfaces
```

Sem API, uma interface precisaria lidar diretamente com os arquivos CSV ou com a lógica interna do projeto.

Com API, uma interface pode fazer uma chamada para um endereço específico e receber uma resposta organizada.

Exemplo:

```text
O sistema pergunta:
"Quais são todos os jogos?"

A API responde:
"Aqui está a lista de jogos."
```

---

# Exemplo Simples

Um dos endpoints da API é:

```text
GET /games
```

Esse endpoint significa:

```text
Quero buscar todos os jogos cadastrados.
```

A API então:

1. carrega os dados do projeto;
2. reutiliza os módulos Python existentes;
3. transforma os dados em um formato compatível;
4. retorna a resposta em JSON.

A resposta normalmente vem em formato **JSON**.

Exemplo simples de JSON:

```json
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

```text
GET /games
GET /games/search
GET /stats/home
GET /awards/winners
```

Cada um desses caminhos possui uma função por trás.

Exemplo conceitual:

```text
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

Na primeira versão da API do The AAA Archive, foram utilizados apenas endpoints `GET`, porque o objetivo inicial era consultar dados.

Exemplos:

```text
GET /games
GET /awards
GET /stats/home
```

Nesta fase, a API não cadastra, edita ou apaga dados.

Ela apenas lê os dados existentes e retorna respostas organizadas.

---

# Papel da API no The AAA Archive

A API não substitui os módulos atuais.

Ela reutiliza os módulos que já existem.

O fluxo da API é:

```text
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

```text
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

Essa lógica evita duplicação de código.

Os módulos continuam concentrando a lógica principal do projeto.

A API apenas expõe essa lógica para consulta externa.

---

# Módulos Reutilizados pela API

A API reutiliza os módulos já criados no projeto.

---

## `load_data.py`

Usado para carregar os datasets:

```text
games.csv
awards.csv
```

Funções principais:

```text
carregar_dataset()
carregar_awards()
```

---

## `filters.py`

Usado para endpoints de filtro da Foundation Collection.

Exemplos:

```text
jogos por gênero
jogos por desenvolvedora
jogos por franquia
jogos por ano
jogos por década
```

Funções principais:

```text
listar_jogos_por_developer()
listar_jogos_por_genero()
listar_jogos_por_franquia()
listar_jogos_por_ano()
listar_jogos_por_decada()
```

---

## `search.py`

Usado para endpoints de pesquisa textual.

Exemplo:

```text
buscar jogos que contenham "resident evil"
```

Funções principais:

```text
pesquisar_jogos()
pesquisar_jogos_por_nome()
```

---

## `site_statistics.py`

Usado para retornar estatísticas da Foundation Collection.

Exemplos:

```text
total de jogos
total de desenvolvedoras
total de franquias
total de gêneros
jogos por década
jogos historicamente importantes
jogos historicamente influentes
```

Funções principais:

```text
gerar_estatisticas_home()
listar_jogos_historicos()
listar_jogos_influentes()
```

---

## `awards.py`

Usado para endpoints relacionados ao histórico de premiações.

Exemplos:

```text
listar vencedores
listar indicados por ano
listar premiações
comparar Awards History com Foundation Collection
```

Funções principais:

```text
listar_jogos_por_ano()
listar_vencedores()
listar_vencedores_na_foundation()
listar_indicados_na_foundation()
listar_jogos_awards_fora_da_foundation()
```

---

# Primeira Versão da API

A primeira versão da API foi planejada para ser simples.

O objetivo não era criar uma arquitetura complexa.

O objetivo era provar que:

```text
os dados podem sair dos CSVs
passar pelos módulos Python
e chegar até uma resposta de API
```

Esse objetivo foi atingido.

A API inicial foi criada, testada e documentada.

---

# Estrutura Planejada

A estrutura inicial planejada era:

```text
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

A estrutura final da primeira versão ficou assim:

```text
The-AAA-Archive/

api/
  main.py
  test_main.py

scripts/
  load_data.py
  filters.py
  search.py
  site_statistics.py
  awards.py
```

A decisão foi manter todos os endpoints em:

```text
api/main.py
```

Isso foi feito para manter a API simples, visível e fácil de entender durante a primeira fase.

No futuro, a API poderá ser separada em routers, como:

```text
api/
  main.py
  routes_games.py
  routes_awards.py
  routes_stats.py
```

Mas isso não faz parte da fase atual.

---

# Endpoints Planejados e Implementados

## Endpoint inicial

```text
GET /
```

Objetivo:

Verificar se a API está funcionando.

Status:

```text
Implementado
```

---

## Jogos

### `GET /games`

Retorna todos os jogos da Foundation Collection.

Módulo usado:

```text
load_data.py
```

Status:

```text
Implementado
```

---

### `GET /games/search?term={term}`

Pesquisa jogos por termo textual.

Exemplo:

```text
/games/search?term=zelda
```

Módulo usado:

```text
search.py
```

Status:

```text
Implementado
```

---

### `GET /games/developer/{developer}`

Retorna jogos de uma desenvolvedora específica.

Exemplo:

```text
/games/developer/Capcom
```

Módulo usado:

```text
filters.py
```

Status:

```text
Implementado
```

---

### `GET /games/genre/{genre}`

Retorna jogos de um gênero específico.

Exemplo:

```text
/games/genre/Survival Horror
```

Módulo usado:

```text
filters.py
```

Status:

```text
Implementado
```

---

### `GET /games/franchise/{franchise}`

Retorna jogos de uma franquia específica.

Exemplo:

```text
/games/franchise/Resident Evil
```

Módulo usado:

```text
filters.py
```

Status:

```text
Implementado
```

Observação:

Este endpoint foi adicionado durante a evolução da primeira versão da API, pois a função já existia no módulo `filters.py`.

---

### `GET /games/year/{year}`

Retorna jogos lançados em um ano específico.

Exemplo:

```text
/games/year/2018
```

Módulo usado:

```text
filters.py
```

Status:

```text
Implementado
```

---

### `GET /games/decade/{decade}`

Retorna jogos lançados em uma década específica.

Exemplo:

```text
/games/decade/2000
```

Módulo usado:

```text
filters.py
```

Status:

```text
Implementado
```

Observação:

Este endpoint foi adicionado durante a evolução da primeira versão da API, pois a função já existia no módulo `filters.py`.

---

### `GET /games/historical`

Retorna jogos marcados como historicamente importantes.

Módulo usado:

```text
site_statistics.py
```

Status:

```text
Implementado
```

Observação:

Este endpoint foi adicionado para expor o recorte editorial da Foundation Collection.

---

### `GET /games/influential`

Retorna jogos marcados como historicamente influentes.

Módulo usado:

```text
site_statistics.py
```

Status:

```text
Implementado
```

Observação:

Este endpoint foi adicionado para expor o recorte editorial da Foundation Collection.

---

# Estatísticas

### `GET /stats/home`

Retorna estatísticas gerais para a Home, API, dashboard e futuras interfaces.

Exemplo de informações:

```text
total de jogos
total de desenvolvedoras
total de franquias
total de gêneros
jogos por gênero
jogos por desenvolvedora
jogos por franquia
jogos por década
jogos historicamente importantes
jogos historicamente influentes
```

Módulo usado:

```text
site_statistics.py
```

Status:

```text
Implementado
```

---

# Awards

### `GET /awards`

Retorna todos os registros da base Awards History.

Módulo usado:

```text
load_data.py
```

Status:

```text
Implementado
```

---

### `GET /awards/{year}`

Retorna vencedor e indicados de um ano específico.

Exemplo:

```text
/awards/2018
```

Módulo usado:

```text
awards.py
```

Status:

```text
Implementado
```

---

### `GET /awards/winners`

Retorna todos os vencedores de Game of the Year.

Módulo usado:

```text
awards.py
```

Status:

```text
Implementado
```

---

### `GET /awards/foundation/winners`

Retorna vencedores de Game of the Year que também estão na Foundation Collection.

Módulo usado:

```text
awards.py
```

Status:

```text
Implementado
```

---

### `GET /awards/foundation/nominees`

Retorna indicados a Game of the Year que também estão na Foundation Collection.

Módulo usado:

```text
awards.py
```

Status:

```text
Implementado
```

---

### `GET /awards/foundation/outside`

Retorna jogos presentes no Awards History, mas ausentes da Foundation Collection.

Módulo usado:

```text
awards.py
```

Status:

```text
Implementado
```

---

# Resumo dos Endpoints Implementados

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

# O que a API Não Faz Nesta Primeira Versão

A primeira versão da API não faz:

* cadastro de novos jogos;
* edição de jogos;
* exclusão de jogos;
* alteração de arquivos CSV;
* conexão com banco de dados;
* autenticação;
* login;
* painel administrativo;
* paginação;
* ordenação avançada;
* filtros combinados por query params;
* separação em routers.

Essas funcionalidades podem existir no futuro, mas não fazem parte da primeira versão.

---

# Testes da API

A API possui testes próprios em:

```text
api/test_main.py
```

Esses testes verificam se os endpoints principais respondem corretamente.

Comando para rodar os testes da API:

```bash
python api/test_main.py
```

Além disso, o projeto possui testes dos módulos principais:

```text
scripts/test_filters.py
scripts/test_search.py
scripts/test_site_statistics.py
scripts/test_awards.py
```

Comando para rodar todos os testes:

```bash
python scripts/test_filters.py
python scripts/test_search.py
python scripts/test_site_statistics.py
python scripts/test_awards.py
python api/test_main.py
```

---

# Como Rodar a API

Para rodar a API, execute o comando na raiz do projeto:

```bash
fastapi dev api/main.py
```

A API será iniciada localmente.

O endereço padrão costuma ser:

```text
http://127.0.0.1:8000
```

A documentação automática do FastAPI pode ser acessada em:

```text
http://127.0.0.1:8000/docs
```

---

# Resultado do Plano

O plano inicial da API foi executado com sucesso.

O projeto conseguiu sair deste estágio:

```text
CSV
↓
Pandas
↓
Módulos Python
```

Para este estágio:

```text
CSV
↓
Pandas
↓
Módulos Python
↓
FastAPI
↓
JSON
```

A API inicial agora serve como uma camada de consulta para os dados do The AAA Archive.

---

# Relação com o API Checkpoint

Este documento registra o plano inicial.

O estado final da API inicial está documentado em:

```text
docs/api_checkpoint.md
```

O `api_checkpoint.md` deve ser usado como referência principal para entender:

* quais endpoints existem;
* quais módulos são reutilizados;
* quais testes foram criados;
* quais decisões técnicas foram tomadas;
* por que a API está fechada por enquanto;
* qual é o próximo passo recomendado do projeto.

---

# Próximo Passo Após Este Plano

Como este plano já foi executado, o próximo passo não é criar novos endpoints.

A API inicial está fechada por enquanto.

A próxima etapa recomendada do projeto é:

```text
Organizar dashboard/app.py sem alterar visual nem adicionar funcionalidades grandes.
```

A organização recomendada para o dashboard é simples:

```text
dashboard/
  app.py
  dashboard_helpers.py
```

Depois disso, a sequência recomendada é:

```text
revisar requirements.txt
↓
criar docs/postgresql_plan.md
↓
planejar migração para PostgreSQL
↓
só depois iniciar a migração
```

---

# Status Final

Status final deste plano:

```text
API Plan executado
```

Resultado:

```text
API FastAPI inicial criada, testada, documentada e fechada por enquanto
```

Próxima fase do projeto:

```text
Organização leve do dashboard antes da revisão do requirements.txt e do planejamento do PostgreSQL
```
