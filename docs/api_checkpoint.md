# API Checkpoint — The AAA Archive

## Objetivo deste Documento

Este documento registra o estado atual da API do projeto **The AAA Archive**.

O objetivo é criar um checkpoint técnico da fase de backend com **FastAPI**, documentando:

* arquitetura atual;
* fonte de dados;
* endpoints existentes;
* módulos reutilizados;
* integração com PostgreSQL;
* testes;
* decisões técnicas;
* limitações;
* estado final da fase;
* condições para futuras evoluções.

Este checkpoint segue a metodologia adotada no projeto:

```text
implementar
↓
testar funcionando
↓
documentar
↓
criar checkpoint
↓
só depois evoluir
```

---

# Estado Atual

A API do The AAA Archive está:

```text
implementada
testada
documentada
integrada ao PostgreSQL
```

Arquivo principal:

```text
api/main.py
```

Arquivo de testes:

```text
api/test_main.py
```

Versão atual:

```text
0.2.0
```

Fonte operacional atual:

```text
PostgreSQL
```

Status:

```text
API FastAPI concluída para a fase atual
```

A API permanece somente de leitura.

Não há necessidade de adicionar novos endpoints antes do planejamento da aplicação web.

---

# Evolução da API

A API passou por duas etapas principais.

## Primeira Versão

A primeira versão utilizava:

```text
data/games.csv
data/awards.csv
```

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

Essa versão permitiu validar:

* criação da aplicação FastAPI;
* criação de endpoints;
* reutilização dos módulos;
* conversão de DataFrames;
* respostas JSON;
* testes com `TestClient`.

---

## Versão Atual

Após a fase PostgreSQL, a fonte operacional foi alterada.

Fluxo atual:

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
FastAPI
↓
JSON
```

Os endpoints principais foram preservados.

A migração alterou a fonte dos dados sem exigir a reconstrução completa da API.

Isso confirma que a separação entre:

* dados;
* conexão;
* lógica;
* endpoints;

funcionou corretamente.

---

# Papel da API no Projeto

A API funciona como uma ponte entre o backend e futuras interfaces.

Ela poderá ser utilizada por:

* aplicação web;
* ferramentas internas;
* futuras aplicações;
* consultas externas;
* possíveis integrações.

Fluxo planejado para a aplicação final:

```text
Usuário
↓
Aplicação web
↓
API FastAPI
↓
PostgreSQL
```

A interface não deverá precisar conhecer:

* senha do banco;
* comandos SQL;
* estrutura interna dos módulos;
* localização dos CSVs;
* configurações do PostgreSQL.

---

# Responsabilidade da API

A API é responsável por:

* receber requisições HTTP;
* interpretar parâmetros;
* carregar dados;
* chamar módulos reutilizáveis;
* converter resultados;
* retornar JSON;
* apresentar respostas previsíveis.

A API não deve concentrar regras que já pertencem a outros módulos.

Exemplo:

```text
GET /games/search?term=zelda
↓
API recebe o termo
↓
carrega os jogos
↓
chama search.py
↓
search.py realiza a pesquisa
↓
API retorna JSON
```

Essa separação evita duplicação.

---

# Estrutura Atual

```text
api/
├── main.py
└── test_main.py
```

Arquivos relacionados:

```text
scripts/
├── awards.py
├── database.py
├── filters.py
├── search.py
└── site_statistics.py
```

Também fazem parte da integração:

```text
database/schema.sql
scripts/import_to_postgres.py
scripts/test_database.py
.env
```

---

# Arquivo Principal

O arquivo principal é:

```text
api/main.py
```

Ele é responsável por:

* criar a aplicação FastAPI;
* configurar os imports internos;
* declarar os endpoints;
* carregar dados do PostgreSQL;
* chamar os módulos de lógica;
* converter DataFrames para JSON;
* tratar valores nulos;
* retornar as respostas.

---

# Arquivo de Testes

Os testes estão em:

```text
api/test_main.py
```

Eles utilizam:

```python
TestClient
```

do FastAPI.

Isso permite testar os endpoints sem precisar abrir manualmente o servidor no navegador.

---

# Fonte de Dados Atual

A API utiliza PostgreSQL como fonte operacional.

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

---

# Papel dos CSVs

Os CSVs continuam fazendo parte do projeto:

```text
data/games.csv
data/awards.csv
```

Porém, eles não são mais carregados diretamente pela API.

Eles funcionam como:

* fonte editorial;
* base de edição manual;
* referência original;
* entrada do script de importação;
* fonte para testes específicos dos módulos.

Fluxo de atualização:

```text
Editar CSV
↓
Executar import_to_postgres.py
↓
Atualizar PostgreSQL
↓
API utiliza os dados atualizados
```

---

# Camada de Banco

A conexão com PostgreSQL é centralizada em:

```text
scripts/database.py
```

Funções principais:

```python
obter_configuracao_banco()
conectar_postgres()
executar_select()
carregar_games_do_banco()
carregar_awards_do_banco()
contar_games_do_banco()
contar_awards_do_banco()
```

A API utiliza principalmente:

```python
carregar_games_do_banco()
carregar_awards_do_banco()
```

Essas funções retornam DataFrames Pandas.

---

# Por que Centralizar a Conexão?

Sem uma camada centralizada, a API precisaria repetir:

* host;
* porta;
* nome do banco;
* usuário;
* senha;
* abertura da conexão;
* execução de consultas;
* fechamento da conexão.

Com `database.py`, o fluxo permanece organizado:

```text
API
↓
database.py
↓
PostgreSQL
```

---

# Variáveis de Ambiente

As configurações do banco são armazenadas em:

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

O arquivo `.env`:

* não deve ir para o GitHub;
* não deve ser incluído em ZIPs públicos;
* não deve ser mostrado na documentação;
* não deve ter seu conteúdo impresso pela API.

O projeto deve compartilhar apenas:

```text
.env.example
```

sem credenciais reais.

---

# Conversão para JSON

Os módulos trabalham com DataFrames Pandas.

Uma API HTTP precisa retornar formatos compatíveis com JSON.

O `main.py` possui funções auxiliares para essa conversão.

Funções:

```python
dataframe_para_json()
dados_para_json()
```

---

# `dataframe_para_json()`

Responsável por converter:

```text
DataFrame
↓
lista de dicionários
↓
JSON
```

A função também trata valores vazios.

Valores como:

```text
NaN
```

precisam ser convertidos para:

```python
None
```

No JSON, `None` é representado como:

```json
null
```

---

# `dados_para_json()`

Responsável por tratar diferentes formatos retornados pelos módulos.

Ela pode receber:

* DataFrames;
* dicionários;
* listas;
* valores simples.

Essa função é especialmente importante em:

```text
GET /stats/home
```

porque esse endpoint retorna um dicionário contendo vários tipos de dados.

---

# Módulos Reutilizados

A API reutiliza módulos da pasta:

```text
scripts/
```

Principais módulos:

```text
database.py
filters.py
search.py
site_statistics.py
awards.py
```

---

# `database.py`

Responsabilidade:

* conexão;
* configuração;
* consultas;
* leitura das tabelas;
* retorno como DataFrame.

A API não deve repetir lógica de conexão.

---

# `filters.py`

Funções reutilizadas:

```python
listar_jogos_por_developer()
listar_jogos_por_genero()
listar_jogos_por_franquia()
listar_jogos_por_ano()
listar_jogos_por_decada()
```

Responsável pelos filtros da Foundation Collection.

---

# `search.py`

Função principal utilizada:

```python
pesquisar_jogos()
```

Responsável pela pesquisa textual.

A pesquisa pode considerar:

```text
nome
genero
developer
franchise
descricao
```

---

# `site_statistics.py`

Funções utilizadas:

```python
gerar_estatisticas_home()
listar_jogos_historicos()
listar_jogos_influentes()
```

Responsável por:

* métricas;
* agrupamentos;
* estatísticas;
* recortes editoriais.

---

# `awards.py`

Funções reutilizadas:

```python
listar_jogos_por_ano()
listar_vencedores()
listar_vencedores_na_foundation()
listar_indicados_na_foundation()
listar_jogos_awards_fora_da_foundation()
```

Responsável pela Awards History e sua comparação com a Foundation Collection.

---

# Grupos de Endpoints

A API possui quatro grupos principais:

```text
Inicial
Games
Estatísticas
Awards
```

---

# Endpoint Inicial

```text
GET /
```

Objetivo:

* confirmar que a API está online;
* informar o estado;
* apresentar a versão;
* informar a fonte de dados.

Exemplo de resposta:

```json
{
  "mensagem": "The AAA Archive API está funcionando",
  "status": "online",
  "versao": "0.2.0",
  "fonte_dados": "PostgreSQL"
}
```

---

# Endpoints de Games

Os endpoints de Games consultam a Foundation Collection.

Fonte:

```text
PostgreSQL
└── games
```

Quantidade atual esperada:

```text
66 jogos
```

---

## Listar Todos os Jogos

```text
GET /games
```

Retorna todos os registros da tabela `games`.

Resposta:

```text
lista de jogos em JSON
```

---

## Pesquisar Jogos

```text
GET /games/search?term={term}
```

Exemplo:

```text
GET /games/search?term=zelda
```

A busca pode considerar:

```text
nome
genero
developer
franchise
descricao
```

Módulo utilizado:

```text
scripts/search.py
```

---

## Filtrar por Desenvolvedora

```text
GET /games/developer/{developer}
```

Exemplo:

```text
GET /games/developer/Capcom
```

Módulo:

```text
scripts/filters.py
```

---

## Filtrar por Gênero

```text
GET /games/genre/{genre}
```

Exemplo:

```text
GET /games/genre/Survival Horror
```

Módulo:

```text
scripts/filters.py
```

---

## Filtrar por Franquia

```text
GET /games/franchise/{franchise}
```

Exemplo:

```text
GET /games/franchise/Resident Evil
```

Função:

```python
listar_jogos_por_franquia()
```

---

## Filtrar por Ano

```text
GET /games/year/{year}
```

Exemplo:

```text
GET /games/year/2018
```

Função:

```python
listar_jogos_por_ano()
```

---

## Filtrar por Década

```text
GET /games/decade/{decade}
```

Exemplo:

```text
GET /games/decade/2000
```

Esse exemplo retorna jogos lançados entre:

```text
2000 e 2009
```

Função:

```python
listar_jogos_por_decada()
```

---

## Jogos Historicamente Importantes

```text
GET /games/historical
```

Utiliza:

```text
historico_importante
```

Função:

```python
listar_jogos_historicos()
```

Os campos editoriais ainda estão em preenchimento.

Por isso, esse endpoint pode retornar uma lista vazia mesmo funcionando corretamente.

---

## Jogos Historicamente Influentes

```text
GET /games/influential
```

Utiliza:

```text
historico_influente
```

Função:

```python
listar_jogos_influentes()
```

Esse endpoint também pode retornar uma lista vazia enquanto os dados editoriais não forem preenchidos.

---

# Endpoint de Estatísticas

```text
GET /stats/home
```

Retorna estatísticas da Foundation Collection.

Dados possíveis:

* total de jogos;
* total de desenvolvedoras;
* total de franquias;
* total de gêneros;
* quantidade por gênero;
* quantidade por desenvolvedora;
* quantidade por franquia;
* quantidade por década;
* jogos historicamente importantes;
* jogos historicamente influentes.

Módulo:

```text
scripts/site_statistics.py
```

---

# Endpoints de Awards

Fonte:

```text
PostgreSQL
└── awards
```

Quantidade atual esperada:

```text
127 registros
```

---

## Listar Todos os Registros

```text
GET /awards
```

Retorna todos os registros da Awards History.

---

## Listar Vencedores

```text
GET /awards/winners
```

Retorna todos os registros com:

```text
status = Vencedor
```

---

## Consultar uma Edição

```text
GET /awards/{year}
```

Exemplo:

```text
GET /awards/2018
```

Retorna:

* ano;
* premiação;
* vencedor;
* indicados.

---

## Vencedores na Foundation Collection

```text
GET /awards/foundation/winners
```

Retorna os vencedores que também fazem parte da Foundation Collection.

Comparação:

```text
awards.jogo
games.nome
```

---

## Indicados na Foundation Collection

```text
GET /awards/foundation/nominees
```

Retorna os indicados que também fazem parte da Foundation Collection.

---

## Jogos Fora da Foundation Collection

```text
GET /awards/foundation/outside
```

Retorna jogos presentes na Awards History e ausentes da Foundation Collection.

Esse endpoint não determina automaticamente quais jogos devem entrar na coleção.

Ele serve como ferramenta de análise.

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
GET /awards/winners
```

deve ser reconhecida antes de:

```text
GET /awards/{year}
```

Caso contrário, a palavra `winners` poderia ser interpretada como valor do parâmetro `year`.

---

# Como Rodar a API

Na raiz do projeto:

```bash
fastapi dev api/main.py
```

Endereço padrão:

```text
http://127.0.0.1:8000
```

---

# Documentação Automática

Swagger:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

Na documentação automática é possível:

* visualizar endpoints;
* consultar parâmetros;
* realizar testes manuais;
* observar respostas;
* verificar códigos HTTP.

---

# Pré-Requisitos

Antes de iniciar a API:

1. PostgreSQL deve estar instalado.
2. O serviço do PostgreSQL deve estar ativo.
3. O banco `aaa_archive` deve existir.
4. As tabelas devem estar criadas.
5. O `.env` deve estar configurado.
6. Os CSVs devem ter sido importados.
7. As dependências devem estar instaladas.

Comandos principais:

```bash
pip install -r requirements.txt
python scripts/import_to_postgres.py
python scripts/test_database.py
fastapi dev api/main.py
```

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

Resultado esperado:

```text
TODOS OS TESTES DA API PASSARAM!
```

---

# Endpoints Testados

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

# Validações Atuais dos Testes

Os testes verificam pontos como:

* código de resposta;
* estrutura do JSON;
* mensagem da rota inicial;
* versão `0.2.0`;
* fonte `PostgreSQL`;
* quantidade de jogos;
* quantidade de registros de awards;
* resultados de pesquisas;
* resultados de filtros;
* consulta por ano;
* endpoints editoriais;
* comparações entre as bases.

---

# Dependência do Banco nos Testes

Os testes atuais da API dependem do banco local.

Antes de executar:

```bash
python api/test_main.py
```

é recomendado executar:

```bash
python scripts/test_database.py
```

O teste da API poderá falhar caso:

* PostgreSQL esteja desligado;
* o `.env` esteja incorreto;
* as tabelas não existam;
* os dados não tenham sido importados;
* as quantidades tenham sido alteradas sem atualizar os testes.

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

# Resultados Esperados

Banco:

```text
TODOS OS TESTES DO BANCO PASSARAM!
```

API:

```text
TODOS OS TESTES DA API PASSARAM!
```

---

# Decisões Técnicas

## 1. Manter os Endpoints em `main.py`

Todos os endpoints continuam em:

```text
api/main.py
```

Motivos:

* facilitar o aprendizado;
* manter o fluxo visível;
* evitar complexidade prematura;
* tamanho atual ainda administrável.

Routers poderão ser adotados futuramente.

---

## 2. Reutilizar os Módulos

A API não recria:

* filtros;
* pesquisas;
* estatísticas;
* comparações;
* conexão com o banco.

Motivos:

* evitar duplicação;
* facilitar testes;
* preservar responsabilidades;
* reutilizar código.

---

## 3. API Somente de Leitura

A API utiliza apenas:

```text
GET
```

Ela não altera o banco.

Motivos:

* os CSVs continuam sendo a fonte editorial;
* evitar dois caminhos de edição;
* reduzir risco de inconsistência;
* manter o foco em exploração.

---

## 4. PostgreSQL como Fonte Operacional

A API não lê mais os CSVs diretamente.

Ela utiliza:

```text
scripts/database.py
```

Motivos:

* centralizar os dados;
* praticar banco relacional;
* preparar o projeto para interfaces externas;
* separar edição editorial de consumo operacional.

---

## 5. Pandas Continua no Fluxo

Mesmo com PostgreSQL, os registros são retornados como DataFrames.

Motivos:

* reaproveitar os módulos existentes;
* manter filtros e estatísticas;
* realizar a migração de forma incremental;
* evitar reescrever toda a lógica.

---

## 6. Preservar os Endpoints

A migração manteve as mesmas rotas.

Isso evita quebrar futuras interfaces e confirma que a troca da fonte foi bem isolada.

---

## 7. Campos Editoriais Podem Estar Vazios

Os endpoints:

```text
GET /games/historical
GET /games/influential
```

estão implementados.

Porém, os campos correspondentes ainda podem estar nulos.

Uma lista vazia não significa necessariamente falha da API.

---

# O que a API Ainda Não Faz

A versão atual não possui:

* cadastro de jogos;
* edição;
* exclusão;
* autenticação;
* login;
* painel administrativo;
* routers;
* paginação;
* filtros combinados;
* ordenação configurável;
* upload de imagens;
* modelos Pydantic completos;
* banco de testes separado;
* deploy;
* versionamento de URL;
* CORS configurado para uma aplicação externa.

---

# Limitações Atuais

## Quantidades Fixas nos Testes

Os testes esperam:

```text
66 jogos
127 registros de awards
```

Quando os datasets forem alterados, os testes também precisarão ser atualizados.

---

## Banco Local

A API depende do PostgreSQL local.

Ainda não existe:

* banco publicado;
* ambiente de produção;
* configuração de deploy;
* banco separado para testes.

---

## Campos Vazios

Parte dos dados editoriais ainda não está preenchida.

Isso limita:

* descrições;
* notas;
* Metacritic;
* recortes históricos;
* recortes de influência.

---

## Arquivo Único de Rotas

Todos os endpoints estão em `main.py`.

Isso é suficiente agora, mas poderá exigir refatoração se a API crescer.

---

## Ausência de Paginação

O endpoint:

```text
GET /games
```

retorna todos os jogos.

Com 66 registros, isso ainda é aceitável.

Se o volume crescer, paginação poderá ser necessária.

---

# Tratamento de Erros

A API deve apresentar respostas compreensíveis quando:

* não houver resultados;
* um ano não existir;
* o termo estiver vazio;
* um parâmetro for inválido;
* o banco estiver indisponível.

As respostas não devem expor:

* senha;
* usuário sensível;
* conteúdo do `.env`;
* rastros internos desnecessários;
* detalhes de conexão.

---

# Segurança

A senha do PostgreSQL não fica no código.

Ela é lida a partir do:

```text
.env
```

O `.env` está listado no:

```text
.gitignore
```

Cuidados obrigatórios:

* não enviar `.env` ao GitHub;
* não incluir `.env` em arquivos ZIP;
* não mostrar a senha em screenshots;
* não imprimir a configuração completa;
* utilizar `.env.example` para documentação.

---

# Relação com o Dashboard

O dashboard atual não consome a API diretamente.

Fluxo atual do dashboard:

```text
Streamlit
↓
dashboard_helpers.py
↓
database.py
↓
PostgreSQL
```

Essa decisão mantém o dashboard simples durante a fase atual.

O dashboard e a API compartilham a mesma fonte operacional, mas seguem fluxos independentes.

---

# Relação com a Aplicação Web

A futura aplicação web deverá preferencialmente consumir a API.

Fluxo:

```text
Front-end
↓
HTTP
↓
FastAPI
↓
PostgreSQL
```

Durante o planejamento do front-end, será necessário avaliar:

* CORS;
* endereço da API;
* estrutura das respostas;
* paginação;
* filtros combinados;
* rota individual por jogo;
* tratamento de carregamento;
* tratamento de erros.

---

# Critério para Novos Endpoints

Um novo endpoint só deve ser criado quando:

1. uma tela ou funcionalidade precisar dele;
2. os endpoints existentes não forem suficientes;
3. o formato da resposta estiver definido;
4. a responsabilidade estiver clara;
5. houver teste planejado;
6. a documentação for atualizada.

Não se deve criar endpoints apenas para tornar a API aparentemente maior.

---

# Possíveis Melhorias Futuras

Melhorias que poderão ser avaliadas:

```text
routers
schemas Pydantic
paginação
ordenação
filtros combinados
endpoint individual por ID
endpoint individual por slug
tratamento global de erros
CORS
pytest
banco de testes
documentação Swagger detalhada
versionamento
cache
deploy
autenticação
operações administrativas
```

Essas melhorias não fazem parte do checkpoint atual.

---

# Critério para Refatoração com Routers

Routers poderão ser introduzidos quando:

* `main.py` ficar difícil de navegar;
* o número de endpoints aumentar;
* existirem grupos maiores de recursos;
* a aplicação web exigir novas rotas;
* testes e manutenção se tornarem mais difíceis.

Estrutura possível:

```text
api/
├── main.py
├── routers/
│   ├── games.py
│   ├── awards.py
│   └── stats.py
└── schemas/
```

Não há necessidade de realizar essa mudança agora.

---

# Resultado da Migração

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

A migração foi concluída sem alterar o contrato principal dos endpoints.

---

# Estado Final da Fase

```text
FastAPI instalada ✅
api/main.py criado ✅
Endpoints implementados ✅
Conversão para JSON funcionando ✅
Módulos reutilizados ✅
TestClient configurado ✅
Testes da API passando ✅
PostgreSQL integrado ✅
database.py integrado ✅
Versão atualizada para 0.2.0 ✅
Fonte de dados identificada como PostgreSQL ✅
66 jogos retornados ✅
127 registros de awards retornados ✅
Documentação atualizada ✅
```

---

# O que Não Fazer Agora

Durante o fechamento desta fase, não é recomendado:

```text
adicionar endpoints sem necessidade
criar autenticação
criar operações de escrita
refatorar para routers sem motivo
adicionar paginação prematuramente
alterar o schema
misturar mudanças da API com front-end
expor o banco diretamente ao navegador
```

---

# Próximo Passo Relacionado à API

A API deve permanecer estável enquanto a documentação geral é finalizada.

Depois, durante o planejamento do front-end, deverá ser feita uma análise de compatibilidade:

```text
Telas planejadas
↓
Dados necessários
↓
Endpoints existentes
↓
Lacunas reais
↓
Possíveis ajustes na API
```

Só então novos endpoints ou refatorações deverão ser considerados.

---

# Documentos Relacionados

```text
docs/api_plan.md
docs/postgresql_plan.md
docs/postgresql_checkpoint.md
docs/project_context.md
docs/project_blueprint.md
docs/project_conventions.md
docs/data_dictionary.md
docs/awards_dictionary.md
```

---

# Status Final do Checkpoint

Status:

```text
API FastAPI concluída, testada e integrada ao PostgreSQL
```

Versão:

```text
0.2.0
```

Fonte de dados:

```text
PostgreSQL
```

Tipo de operação:

```text
Somente leitura
```

Próxima evolução:

```text
Somente após o planejamento da aplicação web
```

---

# Status do Documento

```text
Checkpoint técnico atual da API
```

Este documento deve ser atualizado sempre que houver mudanças relevantes em:

* versão;
* fonte de dados;
* endpoints;
* arquitetura;
* testes;
* segurança;
* limitações.
