# API Plan — The AAA Archive

# Objetivo

Este documento registra o planejamento inicial da API do **The AAA Archive**.

A API foi planejada para disponibilizar os dados do projeto para outras partes do sistema, como:

* futura aplicação web;
* dashboard;
* ferramentas internas;
* futuras aplicações;
* consultas externas.

Este documento foi escrito de forma didática, considerando que a API seria construída passo a passo.

O plano inicial já foi executado.

A API foi:

* criada;
* testada;
* documentada;
* integrada inicialmente aos CSVs;
* posteriormente migrada para PostgreSQL.

O estado implementado da API está documentado em:

```text
docs/api_checkpoint.md
```

A migração da API para PostgreSQL também está registrada em:

```text
docs/postgresql_checkpoint.md
```

Portanto, este documento deve ser entendido como:

```text
registro histórico do planejamento inicial da API
```

Ele não representa sozinho o estado técnico mais recente do projeto.

---

# Status do Plano

Status atual:

```text
Plano executado
```

Resultado:

```text
API FastAPI criada, testada e migrada para PostgreSQL
```

Arquivo principal:

```text
api/main.py
```

Arquivo de testes:

```text
api/test_main.py
```

Versão atual da API:

```text
0.2.0
```

Fonte operacional atual:

```text
PostgreSQL
```

---

# Evolução da API

A API passou por duas etapas principais.

## Primeira Etapa

A primeira versão utilizava:

* CSV;
* Pandas;
* `load_data.py`;
* módulos da pasta `scripts/`;
* respostas em JSON;
* endpoints apenas de leitura.

Fluxo original:

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

---

## Segunda Etapa

Após a conclusão da fase PostgreSQL, a API foi migrada para utilizar:

* PostgreSQL;
* `scripts/database.py`;
* DataFrames Pandas;
* módulos da pasta `scripts/`;
* respostas em JSON;
* endpoints de leitura.

Fluxo atual:

```text
PostgreSQL
↓
scripts/database.py
↓
DataFrames Pandas
↓
Módulos Python
↓
FastAPI
↓
JSON
```

Os CSVs continuam existindo como fonte editorial e entrada do processo de importação, mas não são mais a fonte operacional direta da API.

---

# O que é uma API?

Uma **API** pode ser entendida como uma ponte entre sistemas.

No The AAA Archive, a API conecta:

```text
dados do projeto
↓
backend Python
↓
respostas em JSON
↓
interfaces
```

Sem a API, uma futura interface precisaria acessar diretamente:

* o PostgreSQL;
* os arquivos CSV;
* os módulos internos;
* a lógica Python.

Com a API, a interface pode enviar uma requisição para um endereço específico e receber uma resposta organizada.

Exemplo:

```text
O sistema pergunta:
"Quais são todos os jogos?"

A API responde:
"Aqui está a lista de jogos."
```

---

# Papel da API no Projeto

A API é responsável por:

* disponibilizar os dados;
* receber parâmetros de consulta;
* reutilizar a lógica existente;
* transformar resultados em JSON;
* criar uma camada de separação entre backend e interfaces.

A API não deve concentrar toda a lógica do projeto.

Sempre que possível:

```text
API
↓
chama módulo responsável
↓
módulo processa
↓
API retorna resposta
```

Essa separação evita:

* duplicação;
* rotas excessivamente longas;
* regras de negócio espalhadas;
* dependência direta da interface com o banco.

---

# O que é um Endpoint?

Um **endpoint** é um caminho da API.

Cada endpoint representa uma consulta ou recurso que a API sabe fornecer.

Exemplos:

```text
GET /games
GET /games/search
GET /stats/home
GET /awards/winners
```

Fluxo conceitual:

```text
GET /games
↓
API recebe a requisição
↓
carrega os dados
↓
converte o resultado
↓
retorna JSON
```

---

# O que Significa GET?

`GET` é um método HTTP utilizado para buscar informações.

A versão atual da API utiliza apenas endpoints `GET`.

Exemplos:

```text
GET /games
GET /awards
GET /stats/home
```

Isso significa que a API atualmente:

* consulta;
* filtra;
* pesquisa;
* calcula;
* retorna dados.

Ela não:

* cadastra;
* edita;
* remove;
* altera registros.

---

# Exemplo de Resposta JSON

Exemplo simplificado:

```json
{
  "id": 1,
  "nome": "Resident Evil 4",
  "ano_lancamento": 2005,
  "developer": "Capcom"
}
```

JSON é um formato utilizado para troca de dados entre sistemas.

Sua estrutura é semelhante a dicionários e listas em Python.

---

# Arquitetura Inicial Planejada

A estrutura inicial planejada era:

```text
The-AAA-Archive/
│
├── api/
│   └── main.py
│
└── scripts/
    ├── load_data.py
    ├── filters.py
    ├── search.py
    ├── site_statistics.py
    └── awards.py
```

A estrutura implementada na primeira versão ficou:

```text
The-AAA-Archive/
│
├── api/
│   ├── main.py
│   └── test_main.py
│
└── scripts/
    ├── load_data.py
    ├── filters.py
    ├── search.py
    ├── site_statistics.py
    └── awards.py
```

---

# Estrutura Atual Relacionada à API

Após a integração com PostgreSQL:

```text
The-AAA-Archive/
│
├── api/
│   ├── main.py
│   └── test_main.py
│
├── database/
│   └── schema.sql
│
└── scripts/
    ├── awards.py
    ├── database.py
    ├── filters.py
    ├── import_to_postgres.py
    ├── load_data.py
    ├── search.py
    ├── site_statistics.py
    └── test_database.py
```

---

# Decisão sobre Routers

Os endpoints continuam concentrados em:

```text
api/main.py
```

Essa decisão foi tomada para:

* facilitar o aprendizado;
* manter a estrutura visível;
* evitar abstração prematura;
* permitir compreensão completa do fluxo.

Uma estrutura futura poderá utilizar:

```text
api/
├── main.py
├── routers/
│   ├── games.py
│   ├── awards.py
│   └── stats.py
└── schemas/
```

Essa organização só deverá ser adotada quando o tamanho ou a complexidade da API justificar a mudança.

---

# Fonte de Dados Inicial

Na primeira versão, a API utilizava:

```text
load_data.py
↓
games.csv
awards.csv
```

Essa abordagem permitiu validar:

* leitura dos arquivos;
* funcionamento dos módulos;
* conversão para JSON;
* criação dos primeiros endpoints;
* testes da API.

---

# Fonte de Dados Atual

Atualmente, a API utiliza:

```text
scripts/database.py
↓
PostgreSQL
```

Fluxo:

```text
api/main.py
↓
scripts/database.py
↓
.env
↓
PostgreSQL
```

As funções principais relacionadas são:

```python
carregar_games_do_banco()
carregar_awards_do_banco()
```

Os resultados são retornados como DataFrames e reutilizados pelos módulos da aplicação.

---

# Módulos Reutilizados pela API

# `database.py`

Responsável pela fonte operacional atual dos dados.

Funções principais:

```text
obter_configuracao_banco()
conectar_postgres()
executar_select()
carregar_games_do_banco()
carregar_awards_do_banco()
contar_games_do_banco()
contar_awards_do_banco()
```

A API não deve repetir as configurações de conexão.

---

# `load_data.py`

Responsável por carregar os arquivos CSV diretamente.

Funções:

```text
carregar_dataset()
carregar_awards()
```

Esse módulo foi utilizado diretamente pela primeira versão da API.

Atualmente, continua útil para:

* testes baseados nos CSVs;
* operações editoriais;
* validação da fonte original;
* módulos independentes.

---

# `filters.py`

Responsável pelos filtros da Foundation Collection.

Funções:

```text
listar_jogos_por_developer()
listar_jogos_por_genero()
listar_jogos_por_franquia()
listar_jogos_por_ano()
listar_jogos_por_decada()
```

Consultas relacionadas:

```text
jogos por desenvolvedora
jogos por gênero
jogos por franquia
jogos por ano
jogos por década
```

---

# `search.py`

Responsável pela pesquisa textual.

Funções:

```text
pesquisar_jogos()
pesquisar_jogos_por_nome()
```

A busca pode considerar:

* nome;
* gênero;
* desenvolvedora;
* franquia;
* descrição.

---

# `site_statistics.py`

Responsável pelas estatísticas da Foundation Collection.

Funções utilizadas:

```text
gerar_estatisticas_home()
listar_jogos_historicos()
listar_jogos_influentes()
```

Informações possíveis:

* total de jogos;
* total de desenvolvedoras;
* total de franquias;
* total de gêneros;
* jogos por gênero;
* jogos por desenvolvedora;
* jogos por franquia;
* jogos por década;
* jogos históricos;
* jogos influentes.

---

# `awards.py`

Responsável pelas consultas da Awards History.

Funções:

```text
listar_jogos_por_ano()
listar_vencedores()
listar_vencedores_na_foundation()
listar_indicados_na_foundation()
listar_jogos_awards_fora_da_foundation()
```

Esse módulo também compara:

```text
Foundation Collection
Awards History
```

---

# Objetivo da Primeira Versão

A primeira versão foi planejada para provar que:

```text
dados em CSV
↓
módulos Python
↓
API FastAPI
↓
respostas JSON
```

Esse objetivo foi concluído.

A API inicial demonstrou que os módulos existentes poderiam ser reutilizados por uma camada HTTP.

---

# Objetivo da Migração para PostgreSQL

A migração teve como objetivo provar que a fonte operacional poderia mudar sem alterar completamente a API.

Fluxo alcançado:

```text
CSV como fonte editorial
↓
importação
↓
PostgreSQL
↓
database.py
↓
API
```

A estrutura de endpoints foi preservada.

Isso demonstrou que a separação entre:

* dados;
* conexão;
* lógica;
* rotas;

funcionou corretamente.

---

# Endpoints Planejados e Implementados

# Endpoint Inicial

```text
GET /
```

Objetivo:

* verificar se a API está online;
* apresentar status;
* apresentar versão;
* informar a fonte dos dados.

Status:

```text
Implementado
```

Exemplo atual:

```json
{
  "mensagem": "The AAA Archive API está funcionando",
  "status": "online",
  "versao": "0.2.0",
  "fonte_dados": "PostgreSQL"
}
```

---

# Games

## `GET /games`

Retorna todos os jogos da Foundation Collection.

Fonte atual:

```text
PostgreSQL
```

Status:

```text
Implementado
```

Quantidade atual esperada:

```text
66 jogos
```

---

## `GET /games/search?term={term}`

Pesquisa jogos por termo textual.

Exemplo:

```text
/games/search?term=zelda
```

Módulo:

```text
search.py
```

Status:

```text
Implementado
```

---

## `GET /games/developer/{developer}`

Retorna jogos de uma desenvolvedora.

Exemplo:

```text
/games/developer/Capcom
```

Módulo:

```text
filters.py
```

Status:

```text
Implementado
```

---

## `GET /games/genre/{genre}`

Retorna jogos de um gênero.

Exemplo:

```text
/games/genre/Survival Horror
```

Módulo:

```text
filters.py
```

Status:

```text
Implementado
```

---

## `GET /games/franchise/{franchise}`

Retorna jogos de uma franquia.

Exemplo:

```text
/games/franchise/Resident Evil
```

Módulo:

```text
filters.py
```

Status:

```text
Implementado
```

Esse endpoint foi adicionado durante a evolução da API porque a função já existia no módulo de filtros.

---

## `GET /games/year/{year}`

Retorna jogos lançados em determinado ano.

Exemplo:

```text
/games/year/2018
```

Módulo:

```text
filters.py
```

Status:

```text
Implementado
```

---

## `GET /games/decade/{decade}`

Retorna jogos lançados em determinada década.

Exemplo:

```text
/games/decade/2000
```

Intervalo:

```text
2000 até 2009
```

Módulo:

```text
filters.py
```

Status:

```text
Implementado
```

---

## `GET /games/historical`

Retorna jogos marcados como historicamente importantes.

Campo:

```text
historico_importante
```

Módulo:

```text
site_statistics.py
```

Status:

```text
Implementado
```

Como o preenchimento editorial ainda está pendente, o endpoint pode retornar uma lista vazia.

---

## `GET /games/influential`

Retorna jogos marcados como historicamente influentes.

Campo:

```text
historico_influente
```

Módulo:

```text
site_statistics.py
```

Status:

```text
Implementado
```

Como o preenchimento editorial ainda está pendente, o endpoint pode retornar uma lista vazia.

---

# Estatísticas

## `GET /stats/home`

Retorna estatísticas gerais da Foundation Collection.

Informações possíveis:

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

Módulo:

```text
site_statistics.py
```

Status:

```text
Implementado
```

---

# Awards

## `GET /awards`

Retorna todos os registros da Awards History.

Fonte atual:

```text
PostgreSQL
```

Status:

```text
Implementado
```

Quantidade atual esperada:

```text
127 registros
```

---

## `GET /awards/{year}`

Retorna vencedor e indicados de determinado ano.

Exemplo:

```text
/awards/2018
```

Módulo:

```text
awards.py
```

Status:

```text
Implementado
```

---

## `GET /awards/winners`

Retorna todos os vencedores de Game of the Year.

Módulo:

```text
awards.py
```

Status:

```text
Implementado
```

---

## `GET /awards/foundation/winners`

Retorna vencedores também presentes na Foundation Collection.

Módulo:

```text
awards.py
```

Status:

```text
Implementado
```

---

## `GET /awards/foundation/nominees`

Retorna indicados também presentes na Foundation Collection.

Módulo:

```text
awards.py
```

Status:

```text
Implementado
```

---

## `GET /awards/foundation/outside`

Retorna jogos da Awards History ausentes da Foundation Collection.

Módulo:

```text
awards.py
```

Status:

```text
Implementado
```

---

# Resumo dos Endpoints

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

# Ordem das Rotas

Rotas específicas devem ser declaradas antes de rotas dinâmicas quando houver possibilidade de conflito.

Exemplo:

```text
/awards/winners
```

deve ser tratado corretamente em relação a:

```text
/awards/{year}
```

A organização das rotas deve impedir que palavras como `winners` sejam interpretadas como parâmetros de ano.

---

# Conversão para JSON

Os módulos trabalham principalmente com DataFrames Pandas.

Antes de retornar uma resposta, os dados precisam ser convertidos para uma estrutura compatível com JSON.

Fluxo:

```text
DataFrame
↓
lista de dicionários
↓
resposta JSON
```

Valores nulos também devem ser tratados de forma compatível com JSON.

---

# O que a API Não Faz Atualmente

A API atual não possui:

* cadastro de jogos;
* edição de jogos;
* exclusão de jogos;
* alteração direta dos CSVs;
* alteração direta do PostgreSQL;
* autenticação;
* login;
* painel administrativo;
* upload de imagens;
* paginação;
* ordenação avançada;
* filtros combinados;
* routers separados;
* modelos Pydantic completos para todas as respostas.

Essas funcionalidades poderão ser avaliadas futuramente.

---

# Por que a API é Somente de Leitura?

A API atual foi criada para:

* explorar dados;
* alimentar interfaces;
* apresentar filtros;
* retornar estatísticas;
* consultar premiações.

O processo editorial ainda acontece nos CSVs.

Portanto, operações de escrita pela API criariam dois caminhos diferentes de atualização:

```text
edição no CSV
edição pela API
```

Isso poderia gerar inconsistência.

Enquanto o CSV permanecer como fonte editorial, a API deve continuar somente de leitura.

---

# Testes da API

Arquivo:

```text
api/test_main.py
```

Comando:

```bash
python api/test_main.py
```

O teste verifica:

* endpoint inicial;
* versão;
* fonte de dados;
* quantidade de jogos;
* quantidade de registros de premiações;
* filtros;
* pesquisas;
* estatísticas;
* consultas da Awards History;
* comparações com a Foundation Collection.

Resultado esperado:

```text
TODOS OS TESTES DA API PASSARAM!
```

---

# Dependência do PostgreSQL nos Testes

A versão atual dos testes da API depende de:

* PostgreSQL instalado;
* banco `aaa_archive`;
* tabelas criadas;
* dados importados;
* `.env` configurado;
* servidor PostgreSQL ativo.

Antes de executar:

```bash
python api/test_main.py
```

é recomendado executar:

```bash
python scripts/test_database.py
```

---

# Testes Relacionados

```text
scripts/test_filters.py
scripts/test_search.py
scripts/test_site_statistics.py
scripts/test_awards.py
scripts/test_database.py
api/test_main.py
```

Sequência recomendada:

```bash
python scripts/test_filters.py
python scripts/test_search.py
python scripts/test_site_statistics.py
python scripts/test_awards.py
python scripts/test_database.py
python api/test_main.py
```

---

# Como Rodar a API

Na raiz do projeto:

```bash
fastapi dev api/main.py
```

Endereço local:

```text
http://127.0.0.1:8000
```

Documentação Swagger:

```text
http://127.0.0.1:8000/docs
```

Documentação alternativa do FastAPI:

```text
http://127.0.0.1:8000/redoc
```

---

# Pré-Requisitos

Antes de iniciar a API:

1. instalar as dependências;
2. configurar PostgreSQL;
3. criar o banco;
4. criar as tabelas;
5. configurar o `.env`;
6. importar os CSVs;
7. testar a conexão.

Comandos principais:

```bash
pip install -r requirements.txt
python scripts/import_to_postgres.py
python scripts/test_database.py
fastapi dev api/main.py
```

---

# Documentação Automática

O FastAPI gera documentação interativa automaticamente.

A interface em:

```text
/docs
```

permite:

* visualizar endpoints;
* consultar parâmetros;
* executar requisições;
* observar respostas;
* identificar códigos HTTP.

A documentação poderá ser aprimorada futuramente com:

* descrições mais detalhadas;
* tags;
* modelos de resposta;
* exemplos;
* códigos de erro;
* schemas Pydantic.

---

# Tratamento de Erros

A API deve apresentar respostas compreensíveis quando:

* nenhum jogo for encontrado;
* o ano não existir;
* o termo estiver vazio;
* o parâmetro for inválido;
* o banco estiver indisponível;
* a tabela não existir.

As mensagens não devem revelar:

* senhas;
* credenciais;
* conteúdo do `.env`;
* detalhes internos sensíveis.

---

# Segurança

A API utiliza variáveis de ambiente para acessar o PostgreSQL.

Arquivo local:

```text
.env
```

Esse arquivo não deve ser:

* versionado;
* compartilhado;
* incluído em ZIP público;
* mostrado na documentação.

O projeto deverá disponibilizar apenas:

```text
.env.example
```

sem credenciais reais.

---

# Decisões Técnicas

As principais decisões foram:

* utilizar FastAPI;
* começar com endpoints `GET`;
* reutilizar módulos existentes;
* manter a primeira versão em um único `main.py`;
* testar os endpoints;
* utilizar Pandas para tratamento;
* migrar a fonte operacional para PostgreSQL;
* centralizar conexão em `database.py`;
* manter os CSVs como fontes editoriais;
* evitar escrita pela API nesta fase.

---

# Resultado do Plano Inicial

O plano inicial levou o projeto de:

```text
CSV
↓
Pandas
↓
Módulos Python
```

para:

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

Esse objetivo foi concluído.

---

# Resultado da Evolução Posterior

Após a fase PostgreSQL, o fluxo passou a ser:

```text
CSV editorial
↓
Importação
↓
PostgreSQL
↓
database.py
↓
Módulos Python
↓
FastAPI
↓
JSON
```

Essa evolução também foi concluída.

---

# Relação com os Checkpoints

## API Checkpoint

```text
docs/api_checkpoint.md
```

Registra:

* implementação inicial;
* endpoints;
* testes;
* decisões;
* estrutura;
* limitações.

---

## PostgreSQL Checkpoint

```text
docs/postgresql_checkpoint.md
```

Registra:

* banco;
* tabelas;
* importação;
* camada de conexão;
* migração da API;
* migração do dashboard;
* testes.

---

# Limitações Atuais

A API ainda possui algumas limitações planejadas:

* todos os endpoints estão em um único arquivo;
* não há paginação;
* não há ordenação configurável;
* não há filtros combinados;
* não há autenticação;
* não há operações de escrita;
* não há deploy público;
* alguns campos editoriais estão vazios;
* quantidades esperadas estão fixas nos testes;
* as respostas ainda podem ser refinadas com schemas.

Essas limitações não impedem o uso atual.

---

# Melhorias Futuras Possíveis

Melhorias que poderão ser avaliadas:

* routers;
* schemas Pydantic;
* paginação;
* ordenação;
* filtros combinados;
* tratamento global de exceções;
* documentação Swagger mais detalhada;
* testes com pytest;
* banco de testes separado;
* cache;
* versionamento de endpoints;
* autenticação;
* operações administrativas;
* deploy;
* CORS para o front-end;
* relacionamentos por ID.

Nenhuma dessas melhorias deve ser implementada sem uma necessidade concreta.

---

# Relação com o Front-End

A futura aplicação web deverá utilizar o seguinte fluxo:

```text
Aplicação web
↓
requisição HTTP
↓
API FastAPI
↓
PostgreSQL
↓
resposta JSON
```

A API será responsável por impedir que o front-end precise conhecer:

* credenciais do banco;
* SQL;
* estrutura interna do backend;
* localização dos CSVs;
* detalhes dos módulos Python.

---

# Critério para Novos Endpoints

Um novo endpoint só deve ser criado quando:

1. uma tela ou funcionalidade precisar dele;
2. os endpoints atuais não atenderem à necessidade;
3. a responsabilidade estiver clara;
4. a resposta esperada estiver definida;
5. o impacto nos testes for conhecido;
6. a documentação for atualizada.

Não devem ser criados endpoints apenas para aumentar a quantidade de rotas.

---

# Status Final

Status deste plano:

```text
Executado
```

Resultado inicial:

```text
API FastAPI criada e testada
```

Evolução posterior:

```text
API migrada para PostgreSQL
```

Estado atual:

```text
API 0.2.0
Somente leitura
PostgreSQL
Endpoints testados
Fase concluída
```

---

# Próximo Passo Relacionado à API

A API não precisa receber novas funcionalidades neste momento.

O próximo avanço relacionado a ela deverá acontecer somente após o planejamento da aplicação web.

Nesse momento será possível identificar:

* quais endpoints já atendem ao front-end;
* quais respostas precisam ser ajustadas;
* se será necessário adicionar paginação;
* se filtros combinados serão úteis;
* se routers serão necessários;
* se será necessário configurar CORS;
* se a API será publicada.

Até lá, a versão atual deve permanecer estável.

---

# Status do Documento

```text
Documento histórico de planejamento concluído
```

Este arquivo deve ser preservado como registro da construção inicial da API e atualizado apenas quando for necessário esclarecer o resultado do plano.
