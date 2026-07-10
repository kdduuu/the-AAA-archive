# Dashboard Plan — The AAA Archive

## Objetivo deste Documento

Este documento registra o planejamento de desenvolvimento e organização do dashboard do projeto **The AAA Archive**.

O dashboard foi desenvolvido com **Streamlit** para transformar os dados da:

```text
Foundation Collection
Awards History
```

em uma visualização:

* simples;
* clara;
* interativa;
* analítica;
* reutilizável;
* didática.

Este documento foi criado inicialmente como um plano de implementação.

Atualmente, o plano já foi executado.

O dashboard foi:

* criado;
* testado;
* organizado;
* documentado;
* integrado inicialmente aos CSVs;
* posteriormente migrado para PostgreSQL.

O estado implementado do dashboard está registrado em:

```text
docs/dashboard_checkpoint.md
```

A migração para PostgreSQL também está documentada em:

```text
docs/postgresql_checkpoint.md
```

Portanto, este arquivo deve ser entendido como:

```text
registro histórico do planejamento do dashboard
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
Dashboard Streamlit criado, organizado e migrado para PostgreSQL
```

Arquivos atuais:

```text
dashboard/app.py
dashboard/dashboard_helpers.py
```

Fonte operacional atual:

```text
PostgreSQL
```

Status da fase:

```text
Dashboard concluído para a etapa atual
```

---

# Filosofia de Desenvolvimento

O planejamento do dashboard seguiu a filosofia geral do projeto:

* clareza antes de complexidade;
* documentação antes de grandes mudanças;
* reaproveitamento dos módulos existentes;
* uma responsabilidade principal por arquivo;
* uma responsabilidade principal por função;
* evolução gradual;
* testes antes de avançar;
* organização antes de expansão;
* simplicidade antes de estruturas exageradas.

O objetivo não era criar imediatamente uma interface visual definitiva.

O dashboard foi planejado como:

```text
primeira camada visual e analítica
```

do The AAA Archive.

---

# O que é um Dashboard?

Um dashboard é uma interface visual que reúne informações importantes de um sistema.

No caso do The AAA Archive, ele permite visualizar dados como:

* quantidade total de jogos;
* quantidade de desenvolvedoras;
* quantidade de franquias;
* quantidade de gêneros;
* jogos por gênero;
* jogos por desenvolvedora;
* jogos por franquia;
* jogos por década;
* jogos historicamente importantes;
* jogos historicamente influentes;
* vencedores de Game of the Year;
* indicados;
* relação entre Awards History e Foundation Collection.

Em vez de observar apenas:

* arquivos CSV;
* tabelas do PostgreSQL;
* DataFrames;
* respostas JSON;
* código Python;

o dashboard apresenta os dados de forma visual e interativa.

---

# O que é Streamlit?

Streamlit é uma biblioteca Python utilizada para criar aplicações visuais no navegador.

Ele permite transformar scripts Python em interfaces sem exigir, nessa fase:

* HTML;
* CSS;
* JavaScript;
* framework front-end;
* configuração complexa de servidor.

O Streamlit foi escolhido porque o projeto já possuía:

* dados estruturados;
* DataFrames Pandas;
* módulos de filtros;
* módulos de pesquisa;
* estatísticas;
* consultas de premiações;
* API FastAPI;
* testes.

O dashboard pôde reutilizar essa base em vez de criar uma lógica separada.

---

# Papel do Streamlit no Projeto

O Streamlit representa a primeira camada visual do The AAA Archive.

Ele não substitui:

* PostgreSQL;
* módulos Python;
* API;
* futura aplicação web.

Sua função é:

* apresentar dados;
* permitir exploração;
* mostrar métricas;
* criar gráficos;
* disponibilizar filtros;
* validar ideias visuais;
* apoiar análises.

O dashboard também funciona como uma prova de conceito da experiência de exploração dos dados.

---

# Evolução da Fonte de Dados

O dashboard passou por duas etapas.

## Primeira Etapa

Na primeira versão, o dashboard utilizava:

```text
data/games.csv
data/awards.csv
```

Fluxo inicial:

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

* carregamento dos dados;
* cache;
* métricas;
* filtros;
* busca;
* gráficos;
* tabelas;
* abas;
* comparação entre as bases.

---

## Segunda Etapa

Após a integração com PostgreSQL, o fluxo passou a ser:

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
```

O dashboard atualmente utiliza PostgreSQL como fonte operacional.

Os CSVs continuam sendo a fonte editorial e a entrada do processo de importação.

---

# Arquitetura Atual do Dashboard

```text
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

Responsabilidades:

```text
database.py
→ conexão e leitura do banco

dashboard_helpers.py
→ carregamento, cache, busca, filtros e preparação dos dados

app.py
→ estrutura visual e componentes da interface
```

---

# Por que o Dashboard Não Consome a API?

O dashboard atual não realiza chamadas HTTP para a própria API.

Fluxo atual:

```text
Streamlit
↓
database.py
↓
PostgreSQL
```

Essa decisão foi mantida porque:

* API e dashboard estão no mesmo projeto;
* ambos utilizam Python;
* a camada de banco já é reutilizável;
* chamadas HTTP internas adicionariam complexidade;
* o dashboard funciona como ferramenta analítica interna;
* o objetivo atual não exige desacoplamento total.

A futura aplicação web deverá preferencialmente consumir a API.

---

# Estrutura Inicial

A primeira estrutura era:

```text
dashboard/
└── app.py
```

O arquivo `app.py` concentrava:

* carregamento;
* cache;
* sidebar;
* filtros;
* busca;
* abas;
* métricas;
* gráficos;
* tabelas;
* Foundation Collection;
* Awards History;
* comparações.

Essa estrutura foi útil durante a criação inicial, pois deixava todo o fluxo visível em um único arquivo.

---

# Problema Identificado

Conforme o dashboard cresceu, o `app.py` passou a concentrar responsabilidades demais.

Isso dificultava:

* leitura;
* manutenção;
* identificação da lógica;
* reaproveitamento;
* entendimento da interface;
* futuras alterações.

A solução planejada foi uma refatoração leve.

---

# Estrutura Planejada para Organização

A estrutura recomendada foi:

```text
dashboard/
├── app.py
└── dashboard_helpers.py
```

Essa organização foi implementada.

Não foi criada uma estrutura maior como:

```text
dashboard/
└── components/
    ├── sidebar.py
    ├── foundation_tab.py
    └── awards_tab.py
```

porque isso adicionaria complexidade antes da necessidade real.

---

# Responsabilidade de `dashboard/app.py`

O arquivo:

```text
dashboard/app.py
```

permanece responsável pela interface principal.

Ele deve concentrar:

* `st.set_page_config()`;
* títulos;
* textos;
* sidebar;
* abas;
* métricas;
* gráficos;
* tabelas;
* expanders;
* organização visual;
* fluxo da aplicação.

O `app.py` deve permitir que o leitor entenda:

```text
o que aparece na tela
```

sem precisar procurar toda a interface em diversos arquivos.

---

# Responsabilidade de `dashboard_helpers.py`

O arquivo:

```text
dashboard/dashboard_helpers.py
```

concentra funções auxiliares.

Responsabilidades:

* carregar os dados do banco;
* aplicar cache;
* preparar opções de filtros;
* aplicar pesquisa textual;
* aplicar filtros combinados do dashboard;
* preparar dados da Awards History;
* reutilizar módulos existentes;
* reduzir a quantidade de lógica dentro do `app.py`.

Funções auxiliares podem incluir comportamentos equivalentes a:

```python
carregar_games_com_cache()
carregar_awards_com_cache()
aplicar_busca_textual()
criar_opcoes_filtro()
aplicar_filtros_foundation()
```

Os nomes exatos devem seguir o código implementado.

---

# Regra da Refatoração

A organização do dashboard deveria preservar:

* visual;
* abas;
* filtros;
* busca;
* métricas;
* gráficos;
* tabelas;
* textos;
* comportamento;
* resultados.

Regra principal:

```text
O dashboard deve continuar parecendo e funcionando igual.
```

A mudança deveria ocorrer apenas na organização interna.

Esse objetivo foi atingido.

---

# Primeira Versão do Dashboard

A primeira versão funcional possuía:

* título;
* apresentação do projeto;
* métricas da Foundation Collection;
* tabela de jogos;
* filtros;
* pesquisa textual;
* gráficos;
* aba Foundation Collection;
* aba Awards History;
* consulta por ano;
* histórico de vencedores;
* comparação entre Awards History e Foundation Collection.

Status:

```text
Dashboard inicial concluído
```

---

# Versão Atual do Dashboard

A versão atual preserva as funcionalidades iniciais e utiliza PostgreSQL.

Ela possui:

* duas abas principais;
* cache;
* filtros interativos;
* pesquisa;
* métricas;
* gráficos;
* tabelas;
* recorte editorial;
* consulta de premiações;
* histórico de vencedores;
* comparações entre as bases.

Status:

```text
Dashboard organizado e integrado ao PostgreSQL
```

---

# Módulos Reutilizados

O dashboard reutiliza módulos do backend.

Principais arquivos:

```text
scripts/database.py
scripts/filters.py
scripts/search.py
scripts/site_statistics.py
scripts/awards.py
```

Durante a primeira versão, também utilizava diretamente:

```text
scripts/load_data.py
```

Atualmente, a leitura operacional ocorre por:

```text
scripts/database.py
```

Essa separação evita que o Streamlit recrie:

* conexão;
* filtros;
* pesquisa;
* estatísticas;
* comparações.

---

# Abas Atuais

O dashboard possui duas abas principais:

```text
Foundation Collection
Awards History
```

---

# Aba Foundation Collection

A aba Foundation Collection apresenta a coleção principal do projeto.

Ela possui:

* métricas;
* filtros;
* busca textual;
* gráficos;
* tabela de jogos;
* seção de recorte editorial;
* jogos historicamente importantes;
* jogos historicamente influentes.

Fonte operacional:

```text
PostgreSQL
└── games
```

---

# Métricas da Foundation Collection

Métricas principais:

```text
Jogos
Desenvolvedoras
Franquias
Gêneros
```

Essas métricas são calculadas a partir dos registros disponíveis.

Elas não devem ser escritas manualmente.

---

# Filtros

Filtros atuais:

```text
Gênero
Desenvolvedora
Ano de lançamento
Franquia
```

Os filtros podem ser combinados.

O resultado deve atualizar:

* métricas relacionadas;
* tabela;
* recortes;
* quantidade de resultados;
* componentes dependentes.

---

# Pesquisa Textual

A pesquisa pode considerar campos como:

```text
nome
genero
developer
franchise
descricao
```

A pesquisa é aplicada em conjunto com os filtros.

---

# Gráficos

Gráficos principais:

```text
Jogos por Década
Jogos por Gênero
Desenvolvedoras com Mais Jogos
```

Os gráficos têm finalidade analítica.

Eles não devem ser adicionados apenas para preencher a tela.

---

# Tabela da Foundation Collection

A tabela apresenta os jogos que correspondem aos filtros e à busca.

Ela deve permitir observar campos como:

* nome;
* ano;
* gênero;
* desenvolvedora;
* franquia;
* notas;
* classificações editoriais.

A seleção exata das colunas pode variar conforme a interface atual.

---

# Recorte Editorial

A seção de recorte editorial utiliza:

```text
historico_importante
historico_influente
```

Ela pode apresentar:

* quantidade de jogos importantes;
* quantidade de jogos influentes;
* tabelas específicas;
* listas expansíveis.

Como esses campos ainda estão em preenchimento, a seção pode aparecer vazia sem que isso represente falha técnica.

---

# Aba Awards History

A aba Awards History apresenta o histórico de premiações.

Fonte operacional:

```text
PostgreSQL
└── awards
```

Ela possui:

* métricas;
* seleção por ano;
* vencedor;
* tabela da edição;
* histórico de vencedores;
* comparação com a Foundation Collection.

---

# Métricas da Awards History

Métricas principais:

```text
Registros no Awards
Anos catalogados
Vencedores
Fora da Foundation
```

Esses valores devem ser calculados a partir da base.

---

# Consulta por Ano

O usuário pode selecionar uma edição.

O dashboard apresenta:

* ano;
* premiação;
* vencedor;
* indicados;
* tabela completa da edição.

---

# Histórico de Vencedores

A seção apresenta os vencedores catalogados ao longo dos anos.

Ela permite observar:

* continuidade histórica;
* mudanças de premiação;
* relação com a Foundation Collection.

---

# Comparação entre as Bases

Comparações atuais:

```text
Vencedores presentes na Foundation Collection
Indicados presentes na Foundation Collection
Jogos da Awards History fora da Foundation Collection
```

A comparação utiliza:

```text
awards.jogo
games.nome
```

A presença na Awards History não determina automaticamente a entrada na Foundation Collection.

---

# Cache

O dashboard utiliza:

```python
@st.cache_data
```

O cache reduz recarregamentos desnecessários.

Ele é útil durante:

* alteração de filtros;
* pesquisa;
* mudança de abas;
* reexecução do script;
* atualização de componentes.

O cache deve ser invalidado quando necessário após mudanças nos dados.

---

# Comando para Rodar

Na raiz do projeto:

```bash
streamlit run dashboard/app.py
```

Endereço local esperado:

```text
http://localhost:8501
```

---

# Pré-Requisitos

Antes de iniciar o dashboard:

1. instalar dependências;
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
streamlit run dashboard/app.py
```

---

# Dependência do PostgreSQL

O dashboard atual depende do PostgreSQL local.

Ele pode falhar caso:

* o serviço esteja desligado;
* o `.env` esteja incorreto;
* o banco não exista;
* as tabelas não existam;
* os dados não tenham sido importados;
* a senha esteja incorreta.

Mensagens de erro devem ajudar a identificar a causa sem expor credenciais.

---

# Ordem de Desenvolvimento Original

A ordem inicial planejada foi:

```text
Criar dashboard_plan.md
↓
Criar dashboard/app.py
↓
Exibir título e descrição
↓
Carregar dados
↓
Exibir métricas
↓
Exibir tabela
↓
Adicionar gráficos
↓
Adicionar filtros
↓
Adicionar Awards History
```

Essa etapa foi executada.

---

# Ordem da Organização Interna

Depois da primeira versão:

```text
Identificar responsabilidades do app.py
↓
Criar dashboard_helpers.py
↓
Mover funções auxiliares
↓
Preservar visual
↓
Preservar comportamento
↓
Testar novamente
↓
Documentar
```

Essa etapa também foi executada.

---

# Ordem da Migração para PostgreSQL

A migração seguiu:

```text
Planejar PostgreSQL
↓
Criar banco e tabelas
↓
Criar importador
↓
Criar database.py
↓
Testar leitura
↓
Migrar API
↓
Migrar dashboard_helpers.py
↓
Validar Streamlit
↓
Atualizar checkpoint
```

Essa etapa foi concluída.

---

# Critério de Sucesso da Primeira Versão

A primeira versão foi considerada concluída quando:

* Streamlit abriu corretamente;
* `games.csv` foi carregado;
* `awards.csv` foi carregado;
* métricas apareceram;
* tabela apareceu;
* filtros funcionaram;
* pesquisa funcionou;
* gráficos apareceram;
* Awards History funcionou;
* comparações funcionaram.

Esses critérios foram atendidos.

---

# Critério de Sucesso da Organização

A organização foi considerada concluída quando:

* o dashboard continuou funcionando;
* o visual foi preservado;
* as funcionalidades permaneceram;
* `dashboard_helpers.py` foi criado;
* parte da lógica saiu do `app.py`;
* o `app.py` ficou mais legível;
* os módulos continuaram funcionando;
* a documentação foi atualizada.

Esses critérios foram atendidos.

---

# Critério de Sucesso da Migração

A migração foi considerada concluída quando:

* o dashboard deixou de carregar os CSVs diretamente;
* `database.py` foi reutilizado;
* os dados vieram do PostgreSQL;
* as duas abas funcionaram;
* filtros funcionaram;
* pesquisa funcionou;
* gráficos funcionaram;
* métricas funcionaram;
* comparações funcionaram;
* o Streamlit abriu sem erros.

Esses critérios foram atendidos.

---

# Testes Relacionados

O dashboard não possui atualmente um arquivo de testes visuais automatizados próprio.

Sua lógica depende de módulos testados por:

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

Além disso, o dashboard deve ser validado manualmente com:

```bash
streamlit run dashboard/app.py
```

---

# Validação Manual

Durante a validação, verificar:

* abertura da aplicação;
* título;
* abas;
* carregamento dos dados;
* métricas;
* filtros;
* busca;
* gráficos;
* tabelas;
* seleção de ano;
* vencedor;
* indicados;
* comparação entre bases;
* ausência de erros no terminal.

---

# O que o Dashboard Não É

O dashboard não deve ser confundido com:

* aplicação web final;
* painel administrativo;
* catálogo público definitivo;
* frontend principal;
* substituto da API;
* substituto do PostgreSQL.

Ele é uma camada analítica e visual.

---

# Relação com a Futura Aplicação Web

A futura aplicação web terá objetivo diferente.

Dashboard:

```text
analisar e visualizar dados
```

Aplicação web:

```text
apresentar a experiência editorial principal
```

Algumas métricas e gráficos poderão ser incorporados ao site, mas a aplicação final não precisa reproduzir todo o Streamlit.

---

# Possíveis Melhorias Futuras

Melhorias possíveis:

* gráficos mais elaborados;
* análise de notas;
* análise de Metacritic;
* visualizações históricas;
* filtros mais avançados;
* novas comparações;
* exportação de dados;
* componentes reutilizáveis;
* deploy;
* tema visual próprio;
* testes automatizados;
* páginas do Streamlit;
* consumo da API;
* cache mais controlado.

Essas melhorias não fazem parte do plano atual concluído.

---

# Critério para Novas Funcionalidades

Uma funcionalidade só deverá ser adicionada quando:

1. responder a uma pergunta analítica;
2. utilizar dados disponíveis;
3. possuir utilidade clara;
4. não duplicar uma visualização existente;
5. tiver impacto compreendido;
6. puder ser testada;
7. for documentada.

Não adicionar gráficos apenas para aumentar a quantidade de componentes.

---

# Limitações Atuais

O dashboard possui algumas limitações:

* depende do PostgreSQL local;
* não está publicado;
* não possui testes visuais automatizados;
* não consome a API;
* os campos editoriais ainda estão vazios;
* o visual ainda é baseado nos componentes padrão do Streamlit;
* não possui autenticação;
* não possui edição de dados;
* não possui imagens;
* não representa a aplicação final.

Essas limitações são aceitáveis na fase atual.

---

# Segurança

O dashboard acessa o banco por meio de:

```text
scripts/database.py
```

As credenciais ficam no:

```text
.env
```

O `.env` não deve ser:

* enviado ao GitHub;
* incluído em ZIP público;
* exibido no dashboard;
* impresso no terminal;
* inserido em documentação.

---

# Decisões Técnicas

As principais decisões foram:

* utilizar Streamlit;
* começar com uma única página;
* organizar o conteúdo em abas;
* reutilizar módulos Python;
* não duplicar filtros;
* utilizar cache;
* separar funções auxiliares;
* não criar componentes excessivos;
* não consumir a API internamente;
* migrar a fonte para PostgreSQL;
* manter o dashboard somente de leitura;
* preservar a simplicidade.

---

# Resultado do Plano Inicial

Antes:

```text
CSV
↓
Pandas
↓
Scripts Python
```

Depois da primeira implementação:

```text
CSV
↓
Pandas
↓
Scripts Python
↓
Dashboard Streamlit
```

---

# Resultado da Organização

Antes:

```text
dashboard/app.py
→ interface e lógica auxiliar
```

Depois:

```text
dashboard/app.py
→ interface

dashboard/dashboard_helpers.py
→ lógica auxiliar
```

---

# Resultado da Migração

Antes:

```text
Dashboard
↓
load_data.py
↓
CSV
```

Agora:

```text
Dashboard
↓
dashboard_helpers.py
↓
database.py
↓
PostgreSQL
```

---

# Estado Final da Fase

```text
Streamlit instalado ✅
dashboard/app.py criado ✅
Foundation Collection exibida ✅
Awards History exibida ✅
Métricas implementadas ✅
Filtros implementados ✅
Pesquisa implementada ✅
Gráficos implementados ✅
Tabelas implementadas ✅
Recorte editorial implementado ✅
Comparações implementadas ✅
dashboard_helpers.py criado ✅
Refatoração leve concluída ✅
PostgreSQL integrado ✅
Cache funcionando ✅
Dashboard validado no navegador ✅
Documentação atualizada ✅
```

---

# O que Não Fazer Agora

Durante o fechamento da fase atual, não é recomendado:

```text
expandir o dashboard sem necessidade
transformá-lo em aplicação final
adicionar autenticação
criar edição de registros
adicionar componentes excessivos
alterar o schema
consumir a API sem motivo
misturar mudanças do dashboard com front-end
```

---

# Próximo Passo Relacionado ao Dashboard

O dashboard deve permanecer estável durante o planejamento da aplicação web.

Durante essa futura fase, será necessário decidir:

* quais análises pertencem ao site;
* se o dashboard será publicado;
* se permanecerá como ferramenta interna;
* se continuará usando o banco diretamente;
* se algum componente deverá consumir a API;
* se o Streamlit continuará fazendo parte do produto público.

Nenhuma dessas decisões precisa ser tomada agora.

---

# Documentos Relacionados

```text
docs/dashboard_checkpoint.md
docs/postgresql_plan.md
docs/postgresql_checkpoint.md
docs/project_context.md
docs/project_blueprint.md
docs/project_conventions.md
docs/data_dictionary.md
docs/awards_dictionary.md
```

---

# Status Final

Status deste plano:

```text
Executado
```

Resultado inicial:

```text
Dashboard Streamlit criado
```

Organização posterior:

```text
dashboard_helpers.py implementado
```

Evolução posterior:

```text
Dashboard migrado para PostgreSQL
```

Estado atual:

```text
Dashboard funcional
PostgreSQL
Somente leitura
Fase concluída
```

---

# Status do Documento

```text
Documento histórico de planejamento concluído
```

Este arquivo deve ser preservado como registro do processo de criação, organização e migração do dashboard.
