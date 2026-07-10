# Dashboard Checkpoint — The AAA Archive

## Objetivo deste Documento

Este documento registra o estado atual do dashboard do projeto **The AAA Archive**.

O objetivo é criar um checkpoint técnico da fase de visualização de dados com **Streamlit**, documentando:

* o que foi implementado;
* como o dashboard está organizado;
* qual é a fonte atual dos dados;
* quais módulos são reutilizados;
* quais funcionalidades estão disponíveis;
* como o dashboard foi migrado para PostgreSQL;
* como validar seu funcionamento;
* quais decisões técnicas foram tomadas;
* quais são suas limitações;
* quando ele deverá voltar a evoluir.

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

# Estado Atual da Fase

Status atual:

```text
Dashboard Streamlit concluído, organizado e integrado ao PostgreSQL
```

O dashboard está funcionando localmente e consegue exibir dados da:

* Foundation Collection;
* Awards History.

Arquivos principais:

```text
dashboard/app.py
dashboard/dashboard_helpers.py
```

Fonte operacional atual:

```text
PostgreSQL
```

O dashboard permanece somente de leitura.

Ele não cadastra, edita ou remove dados.

---

# Evolução do Dashboard

O dashboard passou por três etapas principais.

## Primeira Etapa — Criação Inicial

A primeira versão utilizava diretamente:

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
Streamlit
```

Essa etapa permitiu validar:

* criação da aplicação visual;
* organização com abas;
* carregamento de dados;
* uso de cache;
* filtros;
* pesquisa textual;
* métricas;
* gráficos;
* tabelas;
* exploração da Awards History.

---

## Segunda Etapa — Organização Interna

Inicialmente, toda a interface e parte da lógica auxiliar estavam concentradas em:

```text
dashboard/app.py
```

Com o crescimento do arquivo, foi criada uma organização mais clara:

```text
dashboard/
├── app.py
└── dashboard_helpers.py
```

A refatoração preservou:

* o visual;
* as abas;
* os filtros;
* a pesquisa;
* as métricas;
* os gráficos;
* as tabelas;
* o comportamento geral.

---

## Terceira Etapa — Migração para PostgreSQL

Após a conclusão da fase de banco de dados, o dashboard deixou de carregar diretamente os CSVs.

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
dashboard/dashboard_helpers.py
↓
dashboard/app.py
↓
Interface Streamlit
```

A migração preservou as funcionalidades existentes.

---

# Papel do Dashboard no Projeto

O dashboard representa a primeira camada visual e analítica do The AAA Archive.

Sua função é:

* apresentar dados;
* permitir exploração;
* aplicar filtros;
* realizar pesquisas;
* exibir estatísticas;
* gerar gráficos;
* comparar as duas bases;
* validar ideias visuais.

O dashboard não substitui:

* PostgreSQL;
* os módulos Python;
* a API FastAPI;
* a futura aplicação web.

---

# Diferença entre Dashboard e Aplicação Web

O dashboard possui foco principalmente analítico.

```text
Dashboard
→ análise e exploração dos dados
```

A futura aplicação web deverá possuir foco editorial e de navegação.

```text
Aplicação web
→ experiência principal do usuário
```

O Streamlit não representa necessariamente o visual final do projeto.

Ele funciona como:

* ferramenta analítica;
* interface interna;
* protótipo funcional;
* ambiente de exploração.

---

# Arquitetura Atual

A arquitetura do dashboard pode ser representada assim:

```text
PostgreSQL
↓
scripts/database.py
↓
dashboard/dashboard_helpers.py
↓
dashboard/app.py
↓
Navegador
```

Responsabilidades:

```text
PostgreSQL
→ armazena os dados operacionais

database.py
→ centraliza conexão e leitura

dashboard_helpers.py
→ prepara e filtra os dados

app.py
→ monta a interface visual
```

---

# Fonte de Dados Atual

O dashboard utiliza duas tabelas do PostgreSQL.

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

Quantidades esperadas atualmente:

```text
games  → 66 registros
awards → 127 registros
```

---

# Papel dos CSVs

Os arquivos:

```text
data/games.csv
data/awards.csv
```

continuam fazendo parte do projeto.

Eles são utilizados como:

* fonte editorial;
* base de edição manual;
* referência original;
* entrada do processo de importação;
* fonte para testes específicos.

O dashboard não os utiliza diretamente em sua versão atual.

---

# Fluxo de Atualização dos Dados

Quando os dados forem alterados:

```text
Editar os CSVs
↓
Executar import_to_postgres.py
↓
Atualizar PostgreSQL
↓
Limpar cache ou reiniciar Streamlit
↓
Visualizar dados atualizados
```

Comando de importação:

```bash
python scripts/import_to_postgres.py
```

---

# Estrutura Atual do Dashboard

```text
dashboard/
├── app.py
└── dashboard_helpers.py
```

Essa estrutura foi escolhida para manter:

* simplicidade;
* separação de responsabilidades;
* facilidade de aprendizado;
* leitura clara;
* possibilidade de crescimento futuro.

Ainda não existe necessidade de criar múltiplas páginas ou uma grande pasta de componentes.

---

# Responsabilidade de `app.py`

Arquivo:

```text
dashboard/app.py
```

Responsabilidades:

* configurar a página;
* apresentar título e introdução;
* criar a sidebar;
* organizar as abas;
* exibir métricas;
* exibir gráficos;
* exibir tabelas;
* criar expanders;
* controlar o fluxo visual;
* apresentar mensagens ao usuário.

O `app.py` deve permitir compreender claramente o que aparece na tela.

---

# Responsabilidade de `dashboard_helpers.py`

Arquivo:

```text
dashboard/dashboard_helpers.py
```

Responsabilidades:

* carregar os dados;
* aplicar cache;
* criar opções de filtros;
* aplicar filtros;
* aplicar pesquisa textual;
* preparar resultados;
* auxiliar consultas da Awards History;
* reutilizar módulos do backend;
* reduzir a lógica dentro do `app.py`.

O arquivo não deve concentrar componentes visuais completos sem necessidade.

---

# Camada de Banco Utilizada

O dashboard acessa o PostgreSQL por meio de:

```text
scripts/database.py
```

Funções relacionadas:

```python
carregar_games_do_banco()
carregar_awards_do_banco()
```

Essas funções retornam os registros como DataFrames Pandas.

Fluxo:

```text
PostgreSQL
↓
consulta SQL
↓
DataFrame
↓
Streamlit
```

---

# Variáveis de Ambiente

As configurações do banco são armazenadas em:

```text
.env
```

Estrutura esperada:

```env
POSTGRES_DB=aaa_archive
POSTGRES_USER=postgres
POSTGRES_PASSWORD=sua_senha
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

O dashboard não deve:

* mostrar essas variáveis;
* exibir a senha;
* imprimir credenciais;
* permitir acesso direto do usuário ao banco.

---

# Por que o Dashboard Não Consome a API?

O dashboard atual acessa diretamente a camada Python do banco.

Fluxo atual:

```text
Streamlit
↓
dashboard_helpers.py
↓
database.py
↓
PostgreSQL
```

Ele não utiliza:

```text
Streamlit
↓
requisição HTTP
↓
FastAPI
```

Essa decisão foi tomada porque:

* API e dashboard fazem parte do mesmo projeto;
* ambos são desenvolvidos em Python;
* a camada de banco já é reutilizável;
* chamadas HTTP internas adicionariam complexidade;
* o dashboard funciona como ferramenta analítica interna;
* o desacoplamento completo ainda não é necessário.

A futura aplicação web deverá preferencialmente consumir a API.

---

# Como Rodar o Dashboard

O comando deve ser executado na raiz do projeto:

```bash
streamlit run dashboard/app.py
```

Endereço local esperado:

```text
http://localhost:8501
```

O Streamlit normalmente abre o navegador automaticamente.

---

# Pré-Requisitos

Antes de iniciar o dashboard:

1. Python deve estar instalado.
2. As dependências devem estar instaladas.
3. PostgreSQL deve estar instalado.
4. O serviço PostgreSQL deve estar ativo.
5. O banco `aaa_archive` deve existir.
6. As tabelas devem ter sido criadas.
7. O `.env` deve estar configurado.
8. Os dados devem ter sido importados.

Comandos principais:

```bash
pip install -r requirements.txt
python scripts/import_to_postgres.py
python scripts/test_database.py
streamlit run dashboard/app.py
```

---

# Dependências

Dependências principais relacionadas ao dashboard:

```text
streamlit
pandas
psycopg
python-dotenv
```

Essas dependências devem estar registradas em:

```text
requirements.txt
```

---

# Organização Visual

O dashboard utiliza abas com:

```python
st.tabs()
```

Abas atuais:

```text
Foundation Collection
Awards History
```

Essa organização permite separar as duas bases sem criar múltiplas páginas.

---

# Cabeçalho Inicial

O dashboard apresenta:

* título do projeto;
* descrição breve;
* contexto da Foundation Collection;
* contexto da Awards History;
* indicação da proposta analítica.

O texto inicial deve ajudar o usuário a compreender o que está sendo apresentado.

---

# Aba Foundation Collection

A aba Foundation Collection é responsável pela exploração da coleção principal.

Ela possui:

* métricas;
* filtros;
* pesquisa textual;
* gráficos;
* tabela;
* quantidade de resultados;
* recorte editorial.

Fonte:

```text
PostgreSQL
└── games
```

---

# Métricas da Foundation Collection

Métricas exibidas:

```text
Jogos
Desenvolvedoras
Franquias
Gêneros
```

Essas métricas são calculadas dinamicamente.

Elas podem mudar de acordo com:

* filtros;
* pesquisa textual;
* quantidade de resultados.

Os valores não devem ser escritos manualmente.

---

# Filtros Interativos

Filtros disponíveis:

```text
Gênero
Desenvolvedora
Ano de lançamento
Franquia
```

Os filtros ficam na sidebar.

Eles podem ser utilizados em conjunto.

Exemplo:

```text
Gênero: Survival Horror
Desenvolvedora: Capcom
```

O resultado deve considerar todos os filtros ativos.

---

# Pesquisa Textual

O dashboard possui um campo de busca.

Exemplos de termos:

```text
zelda
rockstar
rpg
silent hill
naughty dog
```

Campos pesquisados:

```text
nome
genero
developer
franchise
descricao
```

A pesquisa também funciona em conjunto com os filtros.

---

# Resultado da Exploração

Após aplicar filtros ou pesquisa, o dashboard informa a quantidade de registros encontrados.

Exemplo:

```text
Jogos encontrados: 3
```

Quando uma busca estiver ativa, o termo também pode ser apresentado.

---

# Gráficos da Foundation Collection

Gráficos atuais:

```text
Jogos por Década
Jogos por Gênero
Desenvolvedoras com Mais Jogos
```

Os gráficos são calculados a partir dos dados filtrados.

Eles devem responder às perguntas analíticas do projeto.

Não devem ser adicionados apenas como decoração.

---

# Jogos por Década

Esse gráfico agrupa os jogos por períodos como:

```text
1990
2000
2010
2020
```

Ele ajuda a observar a distribuição histórica da coleção.

---

# Jogos por Gênero

Esse gráfico apresenta a quantidade de jogos por gênero principal.

Ele depende da padronização da coluna:

```text
genero
```

---

# Desenvolvedoras com Mais Jogos

Esse gráfico apresenta as desenvolvedoras com maior presença na coleção.

Ele utiliza:

```text
developer
```

e permite observar a concentração editorial da Foundation Collection.

---

# Tabela da Foundation Collection

A tabela principal pode apresentar:

```text
id
nome
ano_lancamento
genero
developer
franchise
metacritic
nota_kadu
nota_pavam
```

A tabela responde aos filtros e à pesquisa.

Ela deve apresentar apenas os registros encontrados.

---

# Recorte Editorial

A seção:

```text
Recorte Editorial
```

utiliza os campos:

```text
historico_importante
historico_influente
```

Ela pode apresentar:

* quantidade de jogos historicamente importantes;
* quantidade de jogos historicamente influentes;
* tabela de jogos importantes;
* tabela de jogos influentes.

---

# Campos Editoriais Ainda Vazios

Os campos:

```text
historico_importante
historico_influente
```

ainda podem estar nulos em todos ou em parte dos registros.

Por isso, a seção editorial pode apresentar:

```text
0 resultados
```

ou tabelas vazias.

Esse comportamento não significa necessariamente erro técnico.

---

# Aba Awards History

A aba Awards History apresenta o histórico de premiações.

Fonte:

```text
PostgreSQL
└── awards
```

Ela possui:

* métricas;
* consulta por ano;
* vencedor;
* indicados;
* tabela da edição;
* histórico de vencedores;
* comparação com a Foundation Collection.

---

# Métricas da Awards History

Métricas atuais:

```text
Registros no Awards
Anos catalogados
Vencedores
Fora da Foundation
```

Esses valores são calculados dinamicamente.

Quantidade atual de registros:

```text
127
```

---

# Consulta por Ano

O usuário pode escolher um ano disponível.

O dashboard apresenta:

* ano;
* premiação;
* vencedor;
* indicados;
* status de cada jogo;
* tabela da edição.

Essa funcionalidade permite consultar rapidamente uma edição específica.

---

# Histórico de Vencedores

O dashboard apresenta uma tabela com os vencedores catalogados.

Ela permite observar:

* linha histórica;
* mudança de nome das premiações;
* vencedores presentes na Foundation Collection;
* evolução dos eventos.

---

# Comparação entre Awards e Foundation Collection

O dashboard apresenta três comparações principais:

```text
Vencedores presentes na Foundation Collection
Indicados presentes na Foundation Collection
Jogos do Awards fora da Foundation Collection
```

A comparação utiliza:

```text
awards.jogo
games.nome
```

Essa análise ajuda a observar diferenças entre:

* reconhecimento institucional;
* curadoria editorial.

---

# Jogos Fora da Foundation Collection

A lista de jogos fora da coleção funciona como ferramenta de análise.

Ela não significa que todos os jogos listados devam ser incluídos futuramente.

A decisão editorial continua dependendo dos critérios da Foundation Collection.

---

# Cache

O dashboard utiliza:

```python
@st.cache_data
```

O cache evita que os dados sejam carregados novamente em toda interação.

Ele é utilizado durante:

* alteração de filtros;
* digitação na busca;
* mudança de abas;
* atualização de componentes;
* nova execução do script.

---

# Atualização do Cache

Depois de alterar os CSVs e importar os dados novamente, pode ser necessário limpar o cache.

Opções:

```text
Menu do Streamlit
→ Clear cache
```

ou:

```bash
CTRL + C
streamlit run dashboard/app.py
```

Também pode ser utilizado o botão de nova execução da interface quando disponível.

---

# Módulos Reutilizados

O dashboard reutiliza principalmente:

```text
scripts/database.py
scripts/filters.py
scripts/search.py
scripts/site_statistics.py
scripts/awards.py
```

Durante a primeira versão, utilizava diretamente:

```text
scripts/load_data.py
```

Atualmente, `load_data.py` não é a fonte operacional direta do dashboard.

---

# Funções Relacionadas aos Filtros

O dashboard pode reutilizar funções como:

```python
listar_jogos_por_developer()
listar_jogos_por_genero()
listar_jogos_por_franquia()
listar_jogos_por_ano()
```

Parte dos filtros também pode ser aplicada diretamente em funções auxiliares específicas da interface.

---

# Funções Relacionadas à Pesquisa

Funções relacionadas:

```python
pesquisar_jogos()
pesquisar_jogos_por_nome()
```

A pesquisa deve preservar o DataFrame original quando possível.

---

# Funções de Estatísticas

Funções relacionadas:

```python
gerar_estatisticas_home()
listar_jogos_historicos()
listar_jogos_influentes()
```

Essas funções permitem reutilizar as mesmas regras presentes na API.

---

# Funções da Awards History

Funções relacionadas:

```python
listar_anos_disponiveis()
listar_jogos_por_ano()
buscar_vencedor_por_ano()
listar_vencedores()
listar_vencedores_na_foundation()
listar_indicados_na_foundation()
listar_jogos_awards_fora_da_foundation()
```

---

# Conceitos Aprendidos

Durante a criação do dashboard, foram aplicados conceitos como:

* aplicações visuais com Python;
* execução reativa do Streamlit;
* configuração de página;
* métricas;
* colunas;
* sidebar;
* selectboxes;
* campos de texto;
* gráficos;
* DataFrames interativos;
* expanders;
* abas;
* cache;
* filtros combinados;
* separação entre interface e lógica;
* reutilização de módulos;
* integração com PostgreSQL;
* variáveis de ambiente;
* tratamento de valores nulos.

---

# Componentes Streamlit Utilizados

Exemplos:

```python
st.set_page_config()
st.title()
st.write()
st.metric()
st.columns()
st.sidebar
st.selectbox()
st.text_input()
st.bar_chart()
st.dataframe()
st.expander()
st.tabs()
```

---

# Testes Relacionados

O dashboard não possui atualmente um arquivo próprio de testes automatizados de interface.

A lógica utilizada por ele é validada por:

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

---

# Teste Manual do Dashboard

O principal teste da interface é executado com:

```bash
streamlit run dashboard/app.py
```

Durante a validação, conferir:

* navegador aberto;
* ausência de erro no terminal;
* título apresentado;
* abas funcionando;
* dados carregados;
* métricas exibidas;
* filtros funcionando;
* pesquisa funcionando;
* gráficos exibidos;
* tabela apresentada;
* recorte editorial visível;
* seleção por ano funcionando;
* vencedor apresentado;
* indicados apresentados;
* comparações funcionando.

---

# Teste de Conexão Antes do Streamlit

Antes de abrir o dashboard, executar:

```bash
python scripts/test_database.py
```

Resultado esperado:

```text
TODOS OS TESTES DO BANCO PASSARAM!
```

Isso ajuda a separar problemas de:

* conexão;
* interface;
* dados;
* cache.

---

# Erros Possíveis

O dashboard pode falhar caso:

* PostgreSQL esteja desligado;
* o banco não exista;
* as tabelas não existam;
* o `.env` esteja incorreto;
* a senha esteja errada;
* os dados não tenham sido importados;
* alguma coluna tenha sido renomeada;
* uma dependência esteja ausente.

---

# Mensagens de Erro

Mensagens apresentadas ao usuário devem:

* explicar o problema de maneira simples;
* evitar expor credenciais;
* indicar possíveis correções;
* diferenciar falha de conexão de ausência de dados.

Não apresentar:

* senha;
* conteúdo completo do `.env`;
* dados internos sensíveis;
* detalhes desnecessários da conexão.

---

# Decisões Técnicas

## 1. Utilizar Streamlit

Motivos:

* integração direta com Python;
* facilidade de criação;
* rapidez para prototipar;
* boa relação com Pandas;
* foco analítico;
* aprendizado acessível.

---

## 2. Utilizar Abas

O dashboard usa:

```python
st.tabs()
```

Motivos:

* separar as duas bases;
* evitar uma página excessivamente longa;
* preservar uma estrutura simples;
* evitar múltiplas páginas prematuramente.

---

## 3. Separar Funções Auxiliares

Foi criado:

```text
dashboard/dashboard_helpers.py
```

Motivos:

* reduzir o tamanho de `app.py`;
* organizar a lógica;
* facilitar manutenção;
* preservar a compreensão da interface.

---

## 4. Não Criar Estrutura Exagerada

Ainda não existem pastas como:

```text
dashboard/components/
dashboard/pages/
```

Motivos:

* o tamanho atual não exige;
* a estrutura simples ainda é suficiente;
* evitar complexidade prematura.

---

## 5. Utilizar PostgreSQL

O dashboard deixou de ler os CSVs diretamente.

Motivos:

* centralizar a fonte operacional;
* integrar as camadas do projeto;
* praticar banco de dados;
* preparar futuras interfaces;
* manter API e dashboard alinhados.

---

## 6. Continuar Utilizando Pandas

Mesmo com PostgreSQL, os dados são carregados como DataFrames.

Motivos:

* reaproveitar módulos;
* preservar filtros;
* preservar estatísticas;
* manter a migração incremental;
* evitar reescrever toda a lógica.

---

## 7. Não Consumir a API

O dashboard acessa diretamente a camada do banco.

Motivos:

* menos complexidade;
* ferramenta interna;
* mesma linguagem;
* reutilização direta;
* ausência de necessidade de chamadas HTTP.

---

## 8. Manter Somente Leitura

O dashboard não edita registros.

Motivos:

* os CSVs são a fonte editorial;
* evitar dois caminhos de alteração;
* manter segurança;
* manter foco analítico.

---

# Estrutura Atual do Projeto Relacionada

```text
The-AAA-Archive/
│
├── dashboard/
│   ├── app.py
│   └── dashboard_helpers.py
│
├── scripts/
│   ├── awards.py
│   ├── database.py
│   ├── filters.py
│   ├── import_to_postgres.py
│   ├── search.py
│   └── site_statistics.py
│
├── database/
│   └── schema.sql
│
├── data/
│   ├── games.csv
│   └── awards.csv
│
└── .env
```

---

# Limitações Atuais

O dashboard possui limitações conhecidas:

* depende do PostgreSQL local;
* não possui deploy;
* não possui testes visuais automatizados;
* não possui autenticação;
* não permite edição;
* não possui imagens;
* utiliza visual padrão do Streamlit;
* não consome a API;
* não representa o front-end final;
* parte dos campos editoriais está vazia.

Essas limitações são aceitáveis para a fase atual.

---

# Campos que Limitam Algumas Visualizações

Campos atualmente incompletos:

```text
descricao
metacritic
nota_kadu
nota_pavam
historico_importante
historico_influente
```

Isso limita:

* análises de notas;
* textos editoriais;
* quantidade de jogos históricos;
* quantidade de jogos influentes;
* páginas mais completas.

---

# Possíveis Melhorias Futuras

O dashboard poderá receber:

* gráficos mais avançados;
* análises de notas;
* análises de Metacritic;
* comparação entre notas;
* visualizações por franquia;
* visualizações por período;
* exportação de dados;
* tema visual próprio;
* múltiplas páginas;
* testes automatizados;
* deploy;
* consumo da API;
* filtros adicionais;
* controle manual de cache.

Essas melhorias não pertencem ao checkpoint atual.

---

# Critério para Adicionar um Novo Gráfico

Um novo gráfico deve:

1. responder a uma pergunta;
2. utilizar dados confiáveis;
3. possuir utilidade analítica;
4. não duplicar uma tabela;
5. ser compreensível;
6. reagir corretamente aos filtros;
7. ser documentado.

Não adicionar gráficos apenas para deixar a tela mais preenchida.

---

# Critério para Novas Funcionalidades

Uma funcionalidade só deverá ser adicionada quando:

* houver necessidade real;
* o dado necessário existir;
* a camada responsável estiver clara;
* o impacto for compreendido;
* puder ser validada;
* não pertencer melhor à aplicação web.

---

# Segurança

As credenciais ficam em:

```text
.env
```

O arquivo deve estar no:

```text
.gitignore
```

Cuidados:

* não enviar `.env` ao GitHub;
* não incluir `.env` em ZIP público;
* não mostrar credenciais no dashboard;
* não imprimir senha no terminal;
* não expor conexão ao navegador;
* utilizar `.env.example` sem senha real.

---

# Relação com a API

API e dashboard utilizam a mesma fonte operacional:

```text
PostgreSQL
```

Mas seguem caminhos diferentes.

API:

```text
FastAPI
↓
database.py
↓
PostgreSQL
```

Dashboard:

```text
Streamlit
↓
dashboard_helpers.py
↓
database.py
↓
PostgreSQL
```

Essa arquitetura evita que uma camada dependa diretamente da outra.

---

# Relação com o Front-End Futuro

Durante o planejamento da aplicação web, deverá ser decidido:

* quais métricas serão reaproveitadas;
* quais gráficos pertencem ao site;
* se o dashboard será público;
* se o dashboard continuará interno;
* se o Streamlit será publicado;
* se alguma parte consumirá a API;
* se o dashboard continuará no produto final.

Nenhuma dessas decisões precisa ser tomada neste checkpoint.

---

# Resultado da Primeira Versão

Antes:

```text
CSV
↓
Pandas
↓
Scripts
```

Depois:

```text
CSV
↓
Pandas
↓
Scripts
↓
Streamlit
```

---

# Resultado da Organização

Antes:

```text
app.py
→ interface e funções auxiliares
```

Depois:

```text
app.py
→ interface

dashboard_helpers.py
→ lógica auxiliar
```

---

# Resultado da Migração

Antes:

```text
Streamlit
↓
load_data.py
↓
CSV
```

Agora:

```text
Streamlit
↓
dashboard_helpers.py
↓
database.py
↓
PostgreSQL
```

---

# Critérios de Sucesso Atendidos

```text
Streamlit abre corretamente ✅
Foundation Collection é carregada ✅
Awards History é carregada ✅
PostgreSQL é utilizado ✅
Cache funciona ✅
Abas funcionam ✅
Filtros funcionam ✅
Pesquisa funciona ✅
Métricas são exibidas ✅
Gráficos são exibidos ✅
Tabelas são exibidas ✅
Recorte editorial está implementado ✅
Consulta por ano funciona ✅
Histórico de vencedores funciona ✅
Comparações funcionam ✅
dashboard_helpers.py foi criado ✅
Visual foi preservado ✅
Documentação foi atualizada ✅
```

---

# O que Não Fazer Agora

Durante o encerramento da fase atual, não é recomendado:

```text
adicionar funcionalidades grandes
transformar o dashboard no front-end final
adicionar autenticação
criar edição de dados
criar estrutura excessiva de componentes
alterar o schema sem planejamento
consumir a API sem necessidade
misturar mudanças do dashboard com o front-end
```

---

# Próximo Passo Relacionado ao Dashboard

O dashboard deve permanecer estável durante o planejamento da aplicação web.

Uma futura evolução deverá seguir:

```text
Identificar uma necessidade analítica
↓
Verificar se pertence ao dashboard
↓
Confirmar disponibilidade dos dados
↓
Planejar
↓
Implementar
↓
Validar
↓
Documentar
```

---

# Documentos Relacionados

```text
docs/dashboard_plan.md
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
Dashboard Streamlit concluído, organizado e integrado ao PostgreSQL
```

Fonte operacional:

```text
PostgreSQL
```

Arquivos:

```text
dashboard/app.py
dashboard/dashboard_helpers.py
```

Tipo de operação:

```text
Somente leitura
```

Validação:

```text
Testes dos módulos
Teste do banco
Teste manual no navegador
```

Próxima evolução:

```text
Somente depois do planejamento da aplicação web
```

---

# Status do Documento

```text
Checkpoint técnico atual do dashboard
```

Este documento deve ser atualizado quando houver mudanças relevantes em:

* fonte de dados;
* organização;
* funcionalidades;
* arquitetura;
* testes;
* deploy;
* relação com a aplicação web.
