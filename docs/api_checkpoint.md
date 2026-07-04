# API Checkpoint — The AAA Archive

## Objetivo deste Documento

Este documento registra o estado atual da API do projeto **The AAA Archive**.

O objetivo é criar um checkpoint da fase de backend com **FastAPI**, documentando quais endpoints já existem, quais módulos são reutilizados, quais testes foram criados, quais decisões técnicas foram tomadas e qual deve ser o próximo foco do projeto.

Este checkpoint segue a lógica de desenvolvimento usada no projeto:

```text
implementar
↓
testar funcionando
↓
documentar
↓
só depois evoluir
```

---

## Estado Atual

A primeira versão da API do **The AAA Archive** está funcionando.

A API foi criada com **FastAPI** e atualmente reutiliza os módulos já existentes do backend.

Ela ainda utiliza os arquivos CSV como fonte de dados:

```text
data/games.csv
data/awards.csv
```

Status atual:

```text
API FastAPI inicial concluída, testada e documentada
```

A API inicial está fechada por enquanto.

Nesta fase, não há intenção de adicionar novos endpoints.

---

## Papel da API no Projeto

A API funciona como uma ponte entre os dados do projeto e futuras interfaces, como:

* website;
* dashboard;
* outras aplicações;
* consultas externas.

Nesta fase, a API apenas lê dados e retorna respostas em JSON.

Ela ainda não cadastra, edita ou remove informações.

A arquitetura atual da API pode ser entendida assim:

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

O dashboard atual ainda não consome a API diretamente.

Ele utiliza os módulos Python internos do projeto.

Isso foi decidido para manter a fase atual mais simples e didática.

No futuro, a API poderá ser usada por um website, por um dashboard mais desacoplado ou por outras interfaces.

---

## Estrutura Atual

A estrutura da API está concentrada na pasta:

```text
api/
```

Arquivos atuais:

```text
api/
  main.py
  test_main.py
```

O arquivo `main.py` contém os endpoints da API.

O arquivo `test_main.py` contém os testes dos endpoints principais.

---

## Arquivo Principal da API

O arquivo principal da API é:

```text
api/main.py
```

Ele é responsável por:

* criar a aplicação FastAPI;
* configurar os caminhos para importar os módulos da pasta `scripts/`;
* carregar dados dos CSVs;
* chamar funções já existentes do backend;
* converter DataFrames para JSON;
* disponibilizar endpoints de consulta.

---

## Fonte de Dados

A API utiliza dois datasets principais.

---

## Foundation Collection

Arquivo:

```text
data/games.csv
```

Esse dataset contém os jogos principais do projeto.

Ele é usado pelos endpoints relacionados a:

* listagem de jogos;
* busca textual;
* filtros por desenvolvedora;
* filtros por gênero;
* filtros por franquia;
* filtros por ano;
* filtros por década;
* estatísticas;
* jogos historicamente importantes;
* jogos historicamente influentes.

---

## Awards History

Arquivo:

```text
data/awards.csv
```

Esse dataset contém vencedores e indicados a Game of the Year.

Ele é usado pelos endpoints relacionados a:

* listagem de premiações;
* vencedores;
* consulta por ano;
* comparação com a Foundation Collection.

---

## Conversão para JSON

A API trabalha com dados em Pandas, mas uma API HTTP normalmente retorna dados em JSON.

Por isso, o arquivo `main.py` possui funções auxiliares para converter dados.

Funções auxiliares:

```python
dataframe_para_json()
dados_para_json()
```

---

## `dataframe_para_json()`

Essa função converte um DataFrame do Pandas em uma lista de dicionários.

Exemplo conceitual:

```text
DataFrame
↓
lista de dicionários
↓
JSON
```

Ela também trata valores vazios, convertendo valores incompatíveis com JSON para `None`.

No JSON, `None` vira `null`.

---

## `dados_para_json()`

Essa função converte diferentes tipos de dados para formatos compatíveis com JSON.

Ela é útil porque algumas funções do backend retornam:

* DataFrames;
* dicionários;
* listas;
* valores simples.

Essa função verifica o tipo do dado e converte quando necessário.

Ela é especialmente importante para o endpoint:

```text
GET /stats/home
```

porque esse endpoint retorna um dicionário com vários dados dentro, incluindo DataFrames.

---

## Módulos Reutilizados

A API reutiliza os seguintes módulos da pasta `scripts/`:

```text
load_data.py
filters.py
search.py
site_statistics.py
awards.py
```

Isso evita duplicação de lógica.

A API não recria filtros, buscas, estatísticas ou comparações.

Ela apenas chama funções que já existem no backend.

---

## Funções Reutilizadas

### `load_data.py`

Funções utilizadas:

```python
carregar_dataset()
carregar_awards()
```

Essas funções carregam os datasets principais do projeto.

---

### `search.py`

Função utilizada:

```python
pesquisar_jogos()
```

Essa função faz busca textual na Foundation Collection.

---

### `filters.py`

Funções utilizadas:

```python
listar_jogos_por_developer()
listar_jogos_por_genero()
listar_jogos_por_franquia()
listar_jogos_por_ano()
listar_jogos_por_decada()
```

Essas funções filtram jogos por:

* desenvolvedora;
* gênero;
* franquia;
* ano de lançamento;
* década.

---

### `site_statistics.py`

Funções utilizadas:

```python
gerar_estatisticas_home()
listar_jogos_historicos()
listar_jogos_influentes()
```

Essas funções geram estatísticas gerais e também retornam jogos marcados como historicamente importantes ou historicamente influentes.

---

### `awards.py`

Funções utilizadas:

```python
listar_jogos_por_ano()
listar_vencedores()
listar_vencedores_na_foundation()
listar_indicados_na_foundation()
listar_jogos_awards_fora_da_foundation()
```

Essas funções consultam a base Awards History e comparam os dados de premiação com a Foundation Collection.

---

## Endpoints Atuais

A API possui endpoints organizados em quatro grupos principais:

```text
Inicial
Jogos
Estatísticas
Awards
```

---

# 1. Endpoint Inicial

```text
GET /
```

Verifica se a API está online.

Retorna uma resposta simples com:

* mensagem;
* status;
* versão da API.

Exemplo de retorno:

```json
{
  "mensagem": "The AAA Archive API está funcionando",
  "status": "online",
  "versao": "0.1.0"
}
```

---

# 2. Endpoints de Jogos

Os endpoints de jogos consultam a **Foundation Collection**.

---

## Listar todos os jogos

```text
GET /games
```

Retorna todos os jogos cadastrados em `data/games.csv`.

---

## Pesquisar jogos

```text
GET /games/search?term=zelda
```

Pesquisa jogos por termo textual.

A busca considera campos como:

```text
nome
genero
developer
franchise
descricao
```

Exemplo:

```text
/games/search?term=zelda
```

---

## Filtrar jogos por desenvolvedora

```text
GET /games/developer/{developer}
```

Retorna jogos de uma desenvolvedora específica.

Exemplo:

```text
/games/developer/Capcom
```

---

## Filtrar jogos por gênero

```text
GET /games/genre/{genre}
```

Retorna jogos de um gênero específico.

Exemplo:

```text
/games/genre/Survival Horror
```

---

## Filtrar jogos por franquia

```text
GET /games/franchise/{franchise}
```

Retorna jogos de uma franquia específica.

Exemplo:

```text
/games/franchise/Resident Evil
```

Esse endpoint usa a função:

```python
listar_jogos_por_franquia()
```

do módulo:

```text
scripts/filters.py
```

---

## Filtrar jogos por ano

```text
GET /games/year/{year}
```

Retorna jogos lançados em um ano específico.

Exemplo:

```text
/games/year/2018
```

---

## Filtrar jogos por década

```text
GET /games/decade/{decade}
```

Retorna jogos lançados em uma década específica.

Exemplo:

```text
/games/decade/2000
```

Nesse exemplo, a API retorna jogos lançados entre:

```text
2000 e 2009
```

Esse endpoint usa a função:

```python
listar_jogos_por_decada()
```

do módulo:

```text
scripts/filters.py
```

---

## Listar jogos historicamente importantes

```text
GET /games/historical
```

Retorna jogos marcados como historicamente importantes na Foundation Collection.

Esse endpoint usa a função:

```python
listar_jogos_historicos()
```

do módulo:

```text
scripts/site_statistics.py
```

Ele utiliza a coluna:

```text
historico_importante
```

---

## Listar jogos historicamente influentes

```text
GET /games/influential
```

Retorna jogos marcados como historicamente influentes na Foundation Collection.

Esse endpoint usa a função:

```python
listar_jogos_influentes()
```

do módulo:

```text
scripts/site_statistics.py
```

Ele utiliza a coluna:

```text
historico_influente
```

---

# 3. Endpoint de Estatísticas

```text
GET /stats/home
```

Retorna estatísticas gerais da Foundation Collection para a futura Home do site, para a API e para possíveis interfaces futuras.

Exemplos de dados retornados:

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

Esse endpoint usa a função:

```python
gerar_estatisticas_home()
```

do módulo:

```text
scripts/site_statistics.py
```

---

# 4. Endpoints de Awards

Os endpoints de Awards consultam a base:

```text
data/awards.csv
```

---

## Listar todos os registros da Awards History

```text
GET /awards
```

Retorna todos os registros cadastrados na base Awards History.

---

## Listar vencedores

```text
GET /awards/winners
```

Retorna todos os vencedores de Game of the Year cadastrados.

---

## Consultar premiação por ano

```text
GET /awards/{year}
```

Retorna vencedor e indicados de um ano específico.

Exemplo:

```text
/awards/2018
```

---

## Listar vencedores presentes na Foundation Collection

```text
GET /awards/foundation/winners
```

Retorna vencedores de Game of the Year que também estão na Foundation Collection.

---

## Listar indicados presentes na Foundation Collection

```text
GET /awards/foundation/nominees
```

Retorna indicados a Game of the Year que também estão na Foundation Collection.

---

## Listar jogos do Awards fora da Foundation Collection

```text
GET /awards/foundation/outside
```

Retorna jogos presentes na Awards History, mas ausentes da Foundation Collection.

Esse endpoint ajuda a identificar jogos que podem ser analisados futuramente para possível entrada na coleção principal.

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

## Como Rodar a API

Para rodar a API, execute o comando na raiz do projeto:

```bash
fastapi dev api/main.py
```

A API será iniciada localmente.

O endereço padrão costuma ser:

```text
http://127.0.0.1:8000
```

---

## Documentação Automática

O FastAPI gera automaticamente uma documentação interativa da API.

Ela pode ser acessada em:

```text
http://127.0.0.1:8000/docs
```

Nessa página é possível:

* visualizar todos os endpoints;
* testar chamadas;
* verificar parâmetros;
* analisar respostas.

---

## Testes da API

A API possui testes próprios em:

```text
api/test_main.py
```

Esses testes utilizam:

```python
TestClient
```

do FastAPI.

O objetivo é testar se os endpoints respondem corretamente e se os dados retornados fazem sentido.

---

## Endpoints Testados

O arquivo `api/test_main.py` testa:

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

---

## Comando para Rodar Apenas os Testes da API

```bash
python api/test_main.py
```

Se todos os testes passarem, será exibida a mensagem:

```text
TODOS OS TESTES DA API PASSARAM!
```

---

## Testes dos Módulos

Além dos testes da API, o projeto mantém os testes dos módulos principais:

```text
scripts/test_filters.py
scripts/test_search.py
scripts/test_site_statistics.py
scripts/test_awards.py
```

---

## Comando para Rodar Todos os Testes

```bash
python scripts/test_filters.py
python scripts/test_search.py
python scripts/test_site_statistics.py
python scripts/test_awards.py
python api/test_main.py
```

Se todos os testes passarem, os módulos principais do backend e os endpoints da API estão funcionando corretamente.

---

## Decisões Técnicas

Algumas decisões foram tomadas para manter a API simples e didática.

---

## 1. Manter todos os endpoints em `main.py`

Por enquanto, todos os endpoints continuam no arquivo:

```text
api/main.py
```

Motivo:

```text
facilitar o aprendizado
evitar complexidade cedo demais
manter tudo visível em uma primeira versão
```

Futuramente, a API pode ser refatorada com routers.

---

## 2. Reutilizar os módulos da pasta `scripts/`

A API não recria lógica.

Ela reutiliza funções já existentes.

Motivo:

```text
evitar duplicação
manter uma responsabilidade por função
preservar organização do backend
```

---

## 3. Manter a API apenas como leitura

Nesta fase, a API apenas retorna dados.

Ela não altera nenhum arquivo CSV.

Motivo:

```text
segurança
simplicidade
foco em consulta
```

---

## 4. Ainda não usar PostgreSQL

A API ainda utiliza CSV como fonte de dados.

Motivo:

```text
o projeto ainda está consolidando a base atual
a migração para banco deve ser planejada com calma
PostgreSQL será uma fase futura
```

Antes da migração para PostgreSQL, o projeto deve passar por uma fase curta de organização.

---

## 5. Adicionar endpoints editoriais antes de refatorar

Foram adicionados os endpoints:

```text
GET /games/historical
GET /games/influential
```

Motivo:

```text
o dashboard passou a destacar o recorte editorial
a API também deve expor esse tipo de consulta
os dados já existiam no backend
a implementação foi pequena e reaproveitou funções prontas
```

---

## 6. Completar filtros principais da Foundation Collection

Foram adicionados os endpoints:

```text
GET /games/franchise/{franchise}
GET /games/decade/{decade}
```

Motivo:

```text
as funções já existiam no módulo filters.py
o dashboard já trabalha com franquia e década
a API fica mais completa para consultar a Foundation Collection
a implementação mantém o padrão dos endpoints anteriores
```

---

## O Que a API Ainda Não Faz

Nesta fase, a API ainda não possui:

* banco de dados PostgreSQL;
* cadastro de novos jogos;
* edição de dados;
* exclusão de dados;
* autenticação;
* login;
* painel administrativo;
* separação em routers;
* paginação;
* ordenação avançada;
* filtros combinados por query params.

Essas funcionalidades podem ser consideradas futuramente.

Elas não fazem parte da fase atual.

---

## Possíveis Próximos Passos Futuros da API

A API atual está funcional, testada e documentada.

Possíveis melhorias futuras da API:

```text
melhorar documentação dos endpoints no Swagger
adicionar filtros combinados com query params
adicionar ordenação por ano, nota ou Metacritic
adicionar paginação
refatorar a API com routers
integrar a API ao PostgreSQL
permitir operações de escrita em uma fase futura
```

Esses pontos são melhorias futuras.

Eles não devem ser tratados agora.

A API inicial foi fechada para evitar que o projeto fique preso adicionando endpoints antes de organizar a próxima fase.

---

## Próximo Passo Recomendado do Projeto

O README já foi atualizado com os endpoints finais da API inicial, incluindo:

```text
GET /games/franchise/{franchise}
GET /games/decade/{decade}
```

Portanto, a API inicial pode ser considerada fechada por enquanto.

O próximo passo recomendado do projeto não é criar novos endpoints.

A próxima etapa recomendada é:

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

## O Que Não Fazer Agora

Nesta fase, não é recomendado:

```text
adicionar novos endpoints
refatorar a API em routers
criar autenticação
criar cadastro, edição ou exclusão
migrar direto para PostgreSQL sem plano
consumir a API dentro do dashboard
misturar refatoração do dashboard com mudanças na API
```

O foco atual é organização.

A API deve permanecer estável enquanto o dashboard é organizado.

---

## Status Final do Checkpoint

Status final:

```text
API FastAPI inicial concluída, testada, documentada e atualizada com endpoints completos de consulta
```

Situação atual:

```text
API inicial fechada por enquanto
```

Próxima etapa do projeto:

```text
Organização leve do dashboard/app.py antes da revisão do requirements.txt e do planejamento do PostgreSQL
```
