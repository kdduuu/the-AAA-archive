# PostgreSQL Plan — The AAA Archive

## Objetivo deste Documento

Este documento define o plano inicial para a migração do **The AAA Archive** de arquivos CSV para um banco de dados **PostgreSQL**.

O objetivo não é implementar tudo de uma vez.

O objetivo é entender com calma:

* onde o PostgreSQL entra no projeto;
* por que ele será usado;
* como ele se relaciona com os CSVs atuais;
* como os dados serão migrados;
* quais partes do projeto serão afetadas;
* quais cuidados devem ser tomados;
* qual será a ordem segura de implementação.

Esta fase deve ser feita de forma simples, didática e incremental.

---

## Contexto Atual do Projeto

Atualmente, o The AAA Archive utiliza arquivos CSV como fonte principal dos dados.

Os dois datasets principais são:

```text
data/games.csv
data/awards.csv
```

Esses arquivos são lidos com **Python** e **Pandas**.

Depois, os dados são utilizados por:

* módulos da pasta `scripts/`;
* testes;
* API FastAPI;
* dashboard Streamlit.

A arquitetura atual pode ser entendida assim:

```text
CSV
↓
Pandas
↓
Módulos Python
↓
API / Dashboard
```

Essa arquitetura funcionou bem até agora.

Ela foi importante para aprender:

* leitura de dados;
* organização de datasets;
* filtros;
* busca textual;
* estatísticas;
* API;
* dashboard.

Agora, o projeto está pronto para começar a planejar a próxima etapa: usar um banco de dados.

---

## O Que é PostgreSQL?

O **PostgreSQL** é um sistema de banco de dados relacional.

De forma simples, ele serve para guardar dados em tabelas organizadas.

Em vez de ter apenas arquivos como:

```text
games.csv
awards.csv
```

o projeto passará a ter tabelas dentro de um banco.

Exemplo conceitual:

```text
Banco de dados: aaa_archive

Tabelas:
  games
  awards
```

Cada tabela funciona de forma parecida com uma planilha.

A diferença é que um banco de dados oferece mais controle, segurança, organização e possibilidades de consulta.

---

## Por Que Usar PostgreSQL no Projeto?

O PostgreSQL será usado porque o The AAA Archive está deixando de ser apenas um conjunto de scripts e está se aproximando de um sistema mais completo.

Com PostgreSQL, o projeto poderá evoluir melhor para:

* uma API mais robusta;
* consultas mais organizadas;
* dados persistentes;
* futuras operações de cadastro, edição e exclusão;
* futura separação entre backend e frontend;
* possível website próprio;
* melhor estrutura para portfólio.

O banco de dados também aproxima o projeto de uma arquitetura mais real de mercado.

---

## O Que Muda Com PostgreSQL?

Hoje, os dados vivem principalmente nos CSVs.

Depois da migração, os dados passarão a viver no banco de dados.

A arquitetura futura será parecida com isto:

```text
PostgreSQL
↓
Python
↓
Módulos do Projeto
↓
API FastAPI
↓
Dashboard / Futuro Website
```

Ou seja:

* os CSVs deixam de ser a fonte principal da aplicação;
* o PostgreSQL passa a ser a fonte principal;
* os módulos Python passam a buscar dados no banco;
* a API continua retornando JSON;
* o dashboard continua exibindo dados;
* o projeto fica mais próximo de uma aplicação real.

---

## O Que Acontece com os CSVs?

Os CSVs não serão jogados fora imediatamente.

Eles ainda serão importantes.

Durante a migração, os CSVs terão o papel de **fonte inicial de importação**.

Ou seja:

```text
games.csv
awards.csv
↓
script de migração
↓
PostgreSQL
```

No começo, os CSVs continuarão sendo a base que alimenta o banco.

Depois que o banco estiver funcionando, os CSVs poderão assumir outro papel:

* backup simples dos dados;
* referência editorial;
* arquivo de importação inicial;
* histórico de como a base começou;
* forma fácil de revisar dados manualmente.

No futuro, quando o PostgreSQL estiver bem consolidado, o banco poderá se tornar a fonte principal definitiva.

Nesse momento, o fluxo será:

```text
PostgreSQL
↓
API
↓
Dashboard / Website
```

E os CSVs podem ficar apenas como apoio, exportação ou backup.

---

## Decisão Importante

A primeira versão com PostgreSQL deve ser simples.

Não vamos começar criando dezenas de tabelas.

A primeira migração deve respeitar a estrutura atual dos CSVs.

Ou seja, no começo, o banco pode ter apenas duas tabelas principais:

```text
games
awards
```

Essas tabelas serão parecidas com os arquivos atuais:

```text
data/games.csv  → tabela games
data/awards.csv → tabela awards
```

Isso facilita o aprendizado e evita complexidade cedo demais.

---

## Tabela Inicial: `games`

A tabela `games` representará a Foundation Collection.

Ela será baseada no arquivo:

```text
data/games.csv
```

Colunas atuais do CSV:

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

Na primeira versão do banco, essas colunas podem virar colunas da tabela `games`.

Exemplo conceitual:

```text
games

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

Essa abordagem é simples e combina com a fase atual.

---

## Tabela Inicial: `awards`

A tabela `awards` representará o Awards History.

Ela será baseada no arquivo:

```text
data/awards.csv
```

Colunas atuais do CSV:

```text
ano
premiacao
jogo
status
```

Na primeira versão do banco, essas colunas podem virar colunas da tabela `awards`.

Exemplo conceitual:

```text
awards

id
ano
premiacao
jogo
status
```

Mesmo que o CSV atual não tenha uma coluna `id`, pode ser interessante criar um `id` no banco para identificar cada registro de forma única.

---

## Por Que Não Normalizar Tudo Agora?

Em banco de dados, é comum separar informações em várias tabelas.

Por exemplo:

```text
games
developers
genres
franchises
awards
```

Esse modelo pode ser melhor no futuro.

Mas ele também é mais complexo.

Como esta será a primeira experiência do projeto com PostgreSQL, a melhor escolha é começar simples.

Primeiro:

```text
games
awards
```

Depois, quando o funcionamento estiver claro, o projeto poderá evoluir para uma estrutura mais profissional.

Exemplo futuro:

```text
games
developers
genres
franchises
game_genres
awards
award_nominees
```

Mas isso não faz parte da primeira migração.

---

## Diferença Entre CSV e Banco de Dados

## CSV

Um CSV é um arquivo de texto em formato de tabela.

Vantagens:

* simples;
* fácil de abrir;
* fácil de editar;
* bom para começar;
* funciona bem com Pandas.

Limitações:

* não é ideal para sistemas maiores;
* não controla bem relacionamentos;
* não possui consultas avançadas como SQL;
* não é o melhor formato para cadastro, edição e exclusão;
* pode ficar difícil de manter conforme o projeto cresce.

---

## PostgreSQL

O PostgreSQL é um banco de dados.

Vantagens:

* organiza dados em tabelas;
* permite consultas com SQL;
* suporta relacionamentos;
* é mais adequado para aplicações reais;
* funciona melhor com API;
* permite crescimento do projeto;
* é muito usado profissionalmente.

Limitações para esta fase:

* exige instalação e configuração;
* exige aprender SQL;
* exige conexão entre Python e banco;
* aumenta a complexidade do projeto.

Por isso, a migração precisa ser feita aos poucos.

---

## Onde o PostgreSQL Será Aplicado?

O PostgreSQL será aplicado na camada de dados do projeto.

Hoje a camada de dados é:

```text
data/games.csv
data/awards.csv
```

Depois, ela passará a ser:

```text
PostgreSQL
Banco: aaa_archive
Tabelas: games, awards
```

A ideia é que os dados deixem de ser lidos diretamente dos CSVs e passem a ser consultados no banco.

---

## O Que Continua Igual?

Mesmo com PostgreSQL, muita coisa do projeto deve continuar parecida.

A API continuará existindo.

O dashboard continuará existindo.

Os módulos continuarão existindo.

O que muda é a origem dos dados.

Antes:

```text
carregar_dataset()
↓
lê games.csv
```

Depois:

```text
carregar_dataset()
↓
busca dados na tabela games
```

Ou talvez sejam criadas novas funções, como:

```text
carregar_games_do_banco()
carregar_awards_do_banco()
```

Essa decisão será tomada durante a implementação.

---

## Partes do Projeto Que Serão Afetadas

A migração para PostgreSQL poderá afetar:

```text
scripts/load_data.py
```

Porque hoje ele carrega CSVs.

No futuro, poderá carregar dados do banco.

```text
scripts/filters.py
```

Pode continuar filtrando DataFrames no começo, ou futuramente ser substituído por consultas SQL.

```text
scripts/search.py
```

Pode continuar pesquisando com Pandas no começo, ou futuramente usar SQL.

```text
scripts/site_statistics.py
```

Pode continuar calculando estatísticas com Pandas no começo, ou futuramente usar queries SQL.

```text
scripts/awards.py
```

Pode continuar comparando DataFrames no começo, ou futuramente usar consultas SQL.

```text
api/main.py
```

A API precisará buscar dados vindos do banco em vez dos CSVs.

```text
dashboard/app.py
dashboard/dashboard_helpers.py
```

O dashboard poderá continuar usando os módulos, mas os módulos passarão a receber dados vindos do banco.

---

## Estratégia Mais Segura

A estratégia mais segura é não trocar tudo de uma vez.

Em vez disso, a migração pode seguir uma ordem gradual.

A ideia é:

```text
1. Criar o banco
2. Criar as tabelas
3. Importar os CSVs para o banco
4. Testar consultas simples
5. Criar funções Python para ler o banco
6. Comparar os dados do banco com os dados dos CSVs
7. Só depois conectar API e dashboard ao banco
```

Isso evita quebrar o projeto inteiro.

---

## Fase 1 — Instalação e Primeiro Contato

Objetivo:

Instalar e abrir o PostgreSQL com calma.

Nesta fase, o foco será entender:

* o que é um servidor PostgreSQL;
* o que é um banco de dados;
* o que é uma tabela;
* o que é uma query SQL;
* como abrir o banco;
* como executar comandos simples.

Exemplos de comandos que serão aprendidos futuramente:

```sql
SELECT * FROM games;
SELECT * FROM awards;
```

Nesta fase, ainda não será necessário mexer na API ou no dashboard.

---

## Fase 2 — Criar Banco e Tabelas

Objetivo:

Criar o banco do projeto.

Nome sugerido:

```text
aaa_archive
```

Tabelas iniciais:

```text
games
awards
```

A estrutura inicial deve seguir os CSVs atuais.

Isso torna a migração mais fácil de entender.

---

## Fase 3 — Importar CSVs para o PostgreSQL

Objetivo:

Pegar os dados atuais dos CSVs e colocar dentro do banco.

Fluxo:

```text
data/games.csv
↓
tabela games

data/awards.csv
↓
tabela awards
```

Essa importação pode ser feita de duas formas:

* manualmente, com ferramenta visual;
* via script Python.

Para o projeto, a opção mais educativa será provavelmente criar um script Python de importação.

Exemplo futuro de arquivo:

```text
scripts/import_to_postgres.py
```

Esse script poderá:

* ler `games.csv`;
* ler `awards.csv`;
* conectar no PostgreSQL;
* inserir os dados nas tabelas.

---

## Fase 4 — Criar Conexão Python com PostgreSQL

Objetivo:

Ensinar o Python a conversar com o banco.

Para isso, o projeto poderá usar uma biblioteca de conexão com PostgreSQL.

A conexão permitirá que o Python execute comandos SQL e receba os dados de volta.

Exemplo conceitual:

```text
Python
↓
conecta no PostgreSQL
↓
executa SELECT
↓
recebe dados
↓
transforma em DataFrame
```

No começo, a ideia pode ser continuar usando DataFrames.

Isso permite manter boa parte da lógica atual funcionando.

---

## Fase 5 — Criar Módulo de Banco

Objetivo:

Criar um módulo separado para lidar com a conexão ao banco.

Possível arquivo futuro:

```text
scripts/database.py
```

Responsabilidade:

* guardar a lógica de conexão;
* evitar repetir conexão em vários arquivos;
* centralizar configurações do banco.

Possíveis funções futuras:

```python
conectar_banco()
carregar_games_do_banco()
carregar_awards_do_banco()
```

Essa separação é importante para não bagunçar os módulos atuais.

---

## Fase 6 — Adaptar a Leitura de Dados

Objetivo:

Fazer o projeto conseguir carregar dados do PostgreSQL.

Hoje:

```text
carregar_dataset()
↓
games.csv
```

Futuro:

```text
carregar_games_do_banco()
↓
tabela games
```

No começo, o retorno pode continuar sendo um DataFrame.

Isso facilita a transição, porque os módulos atuais já trabalham com DataFrames.

Assim, a mudança fica menos agressiva.

---

## Fase 7 — Conectar a API ao Banco

Objetivo:

Fazer a API buscar dados vindos do PostgreSQL.

A API deixaria de depender diretamente dos CSVs.

Fluxo futuro:

```text
PostgreSQL
↓
Python
↓
FastAPI
↓
JSON
```

Nesta fase, os endpoints atuais devem continuar os mesmos.

Ou seja, a URL não precisa mudar.

Exemplo:

```text
GET /games
```

Antes retornava dados do CSV.

Depois passará a retornar dados do PostgreSQL.

Para quem usa a API, o comportamento deve parecer igual.

---

## Fase 8 — Conectar o Dashboard ao Banco

Objetivo:

Fazer o dashboard utilizar dados vindos do PostgreSQL.

O dashboard não precisa conversar diretamente com o banco no começo.

Ele pode continuar usando funções auxiliares.

O ideal é que a mudança fique escondida nos módulos de carregamento.

Exemplo:

```text
dashboard/app.py
↓
carregar_games_com_cache()
↓
carregar_games_do_banco()
↓
PostgreSQL
```

Assim, o dashboard continua parecido visualmente.

A diferença fica na origem dos dados.

---

## Fase 9 — Revisar Testes

Objetivo:

Garantir que tudo continua funcionando.

Os testes atuais verificam:

```text
filters.py
search.py
site_statistics.py
awards.py
api/test_main.py
```

Com PostgreSQL, será necessário decidir:

* quais testes continuam usando CSV;
* quais testes passam a usar banco;
* se será criado um banco de teste;
* se os testes vão comparar CSV e banco.

No começo, o mais simples pode ser manter os testes atuais e criar testes novos apenas para a conexão com o banco.

---

## Fase 10 — Pensar em Evoluções Futuras

Depois que o PostgreSQL estiver funcionando, o projeto poderá evoluir para:

* tabelas mais normalizadas;
* relacionamentos entre tabelas;
* filtros feitos com SQL;
* busca textual no banco;
* API com operações de escrita;
* painel administrativo;
* cadastro de novos jogos;
* edição de dados;
* deploy com banco real;
* website conectado à API.

Essas etapas são futuras.

Elas não devem ser feitas agora.

---

## Estrutura Futura Possível

Uma estrutura futura simples pode ser:

```text
The-AAA-Archive/

scripts/
  load_data.py
  database.py
  import_to_postgres.py
  filters.py
  search.py
  site_statistics.py
  awards.py

api/
  main.py
  test_main.py

dashboard/
  app.py
  dashboard_helpers.py

data/
  games.csv
  awards.csv

docs/
  postgresql_plan.md
```

Essa estrutura ainda mantém os CSVs no projeto, mas adiciona arquivos específicos para banco de dados.

---

## Cuidados Importantes

Durante a migração, alguns cuidados são importantes.

## 1. Não apagar os CSVs

Os CSVs devem continuar no projeto por enquanto.

Eles servem como:

* fonte original;
* backup;
* referência;
* base de comparação.

---

## 2. Não mudar tudo ao mesmo tempo

Não é recomendado alterar API, dashboard, módulos e banco de uma vez.

A migração deve ser feita em etapas pequenas.

---

## 3. Testar sempre

Depois de cada etapa, é importante testar.

Exemplos:

```bash
python scripts/test_filters.py
python scripts/test_search.py
python scripts/test_site_statistics.py
python scripts/test_awards.py
python api/test_main.py
```

---

## 4. Manter os endpoints iguais

A API não deve mudar de aparência para o usuário final.

Exemplo:

```text
GET /games
```

Deve continuar existindo.

A diferença será interna:

```text
antes: dados do CSV
depois: dados do PostgreSQL
```

---

## 5. Manter o dashboard visualmente igual no começo

A migração para banco não deve ser usada como desculpa para mudar o visual do dashboard.

Primeiro, trocar a origem dos dados.

Depois, pensar em melhorias visuais.

---

## 6. Evitar normalização cedo demais

Separar tudo em muitas tabelas pode parecer mais profissional, mas pode atrapalhar o aprendizado inicial.

A primeira versão deve ser simples:

```text
games
awards
```

Depois, com mais segurança, o modelo pode evoluir.

---

## O Que Não Fazer Agora

Nesta fase, ainda não devemos:

* apagar os CSVs;
* criar dezenas de tabelas;
* refatorar toda a API;
* refatorar todo o dashboard;
* criar autenticação;
* criar painel administrativo;
* permitir cadastro, edição e exclusão;
* fazer deploy;
* normalizar completamente o banco;
* substituir tudo por SQL de uma vez.

O foco é planejar e entender.

---

## Critério de Sucesso da Primeira Migração

A primeira migração para PostgreSQL será considerada bem-sucedida quando:

* o PostgreSQL estiver instalado e acessível;
* o banco `aaa_archive` existir;
* a tabela `games` existir;
* a tabela `awards` existir;
* os dados do `games.csv` estiverem na tabela `games`;
* os dados do `awards.csv` estiverem na tabela `awards`;
* for possível fazer consultas simples com SQL;
* o Python conseguir se conectar ao banco;
* o Python conseguir carregar os dados do banco em DataFrames;
* os dados carregados do banco baterem com os dados dos CSVs.

Depois disso, o projeto poderá avançar para conectar API e dashboard ao banco.

---

## Ordem Recomendada

A ordem recomendada para esta fase é:

```text
1. Criar este documento: docs/postgresql_plan.md
2. Entender o papel do PostgreSQL no projeto
3. Instalar PostgreSQL e ferramenta visual
4. Criar o banco aaa_archive
5. Criar as tabelas games e awards
6. Importar os CSVs para o banco
7. Testar consultas SQL simples
8. Criar conexão Python com PostgreSQL
9. Carregar dados do banco em DataFrames
10. Comparar banco com CSV
11. Adaptar a API
12. Adaptar o dashboard
13. Revisar testes
14. Só depois pensar em melhorias maiores
```

---

## Status Atual

Status atual:

```text
PostgreSQL em fase de planejamento
```

A API inicial já foi concluída.

O dashboard inicial já foi concluído.

O dashboard já passou por uma organização leve com:

```text
dashboard/
  app.py
  dashboard_helpers.py
```

O `requirements.txt` já foi revisado para manter apenas as dependências principais do projeto.

Agora, o próximo passo é iniciar a preparação para PostgreSQL com calma.

---

## Próxima Etapa

A próxima etapa prática será preparar o ambiente PostgreSQL.

Antes de escrever código, será necessário entender:

* como instalar o PostgreSQL;
* como acessar o banco;
* como criar um banco de dados;
* como criar uma tabela;
* como fazer um `SELECT`;
* como importar dados;
* como conectar Python ao banco.

A implementação deve começar simples.

Primeiro objetivo prático:

```text
Criar o banco aaa_archive e conseguir visualizar uma tabela simples no PostgreSQL.
```

---

## Objetivo Final da Fase PostgreSQL

O objetivo final desta fase é fazer o The AAA Archive deixar de depender dos CSVs como fonte principal de execução.

A longo prazo, o fluxo ideal será:

```text
PostgreSQL
↓
Python
↓
FastAPI
↓
Dashboard / Website
```

Mas essa mudança será feita aos poucos.

Nesta fase, o mais importante é aprender bem a base de banco de dados e migrar o projeto com segurança.
