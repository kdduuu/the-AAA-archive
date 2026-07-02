# Dashboard Checkpoint — The AAA Archive

## Objetivo deste Documento

Este documento registra o estado atual do dashboard do projeto **The AAA Archive**.

O objetivo é criar um checkpoint da fase de visualização de dados com **Streamlit**, documentando o que já foi implementado, como o dashboard funciona, quais módulos ele utiliza, quais conceitos foram aprendidos e quais próximos passos podem ser feitos futuramente.

Este checkpoint segue a mesma lógica usada na API:

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

## Estado Atual da Fase

Status atual:

```text
Dashboard Streamlit inicial concluído
```

O dashboard já está rodando corretamente no navegador e consegue exibir dados da:

* Foundation Collection;
* Awards History.

Ele utiliza os arquivos CSV do projeto e reaproveita funções já criadas nos módulos Python da pasta `scripts/`.

---

## Papel do Dashboard no Projeto

O dashboard é a primeira camada visual do **The AAA Archive**.

Ele não substitui a API.

Ele também não substitui os módulos Python.

A função dele é apresentar os dados de forma visual, interativa e mais fácil de explorar.

A arquitetura atual do projeto pode ser entendida assim:

```text
CSV
↓
Pandas
↓
Módulos Python
↓
FastAPI
↓
Streamlit Dashboard
```

Nesta fase, o dashboard ainda acessa diretamente os módulos Python e os arquivos CSV.

Ele ainda não consome a API diretamente.

Essa decisão foi intencional para manter o aprendizado mais simples e evitar complexidade desnecessária.

---

## Arquivo Principal do Dashboard

O dashboard foi criado em:

```text
dashboard/app.py
```

Esse arquivo é responsável por:

* configurar a página Streamlit;
* carregar os dados;
* usar cache no carregamento dos CSVs;
* aplicar filtros;
* aplicar busca textual;
* gerar estatísticas;
* organizar o conteúdo em abas;
* exibir métricas;
* exibir gráficos;
* exibir tabelas;
* mostrar a seção editorial da Foundation Collection;
* mostrar a seção de Awards History.

---

## Como Rodar o Dashboard

Para rodar o dashboard, é necessário estar na raiz do projeto:

```text
The-AAA-Archive/
```

Depois, executar:

```bash
streamlit run dashboard/app.py
```

O Streamlit normalmente abre o navegador automaticamente.

O endereço local costuma ser:

```text
http://localhost:8501
```

---

## Dependência Necessária

O projeto agora utiliza a biblioteca:

```text
streamlit
```

Ela deve estar presente no arquivo:

```text
requirements.txt
```

Caso ainda não esteja instalada no ambiente, pode ser instalada com:

```bash
pip install streamlit
```

---

## Datasets Utilizados

O dashboard utiliza dois datasets principais.

---

## Foundation Collection

Arquivo:

```text
data/games.csv
```

Esse dataset representa a coleção principal de jogos AAA single-player historicamente relevantes.

Colunas principais:

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

---

## Awards History

Arquivo:

```text
data/awards.csv
```

Esse dataset representa o histórico de premiações de Game of the Year.

Colunas principais:

```text
ano
premiacao
jogo
status
```

---

## Módulos Reaproveitados

O dashboard reaproveita funções já existentes nos módulos Python do projeto.

Principais módulos utilizados:

```text
scripts/load_data.py
scripts/site_statistics.py
scripts/awards.py
```

---

## Funções Utilizadas

### `scripts/load_data.py`

Funções utilizadas:

```python
carregar_dataset()
carregar_awards()
```

Essas funções carregam os datasets principais do projeto.

No dashboard, essas funções são chamadas dentro de funções auxiliares com cache.

---

### `scripts/site_statistics.py`

Função utilizada:

```python
gerar_estatisticas_home()
```

Essa função gera estatísticas da Foundation Collection, como:

* total de jogos;
* total de desenvolvedoras;
* total de franquias;
* total de gêneros;
* quantidade por década;
* quantidade por gênero;
* quantidade por desenvolvedora;
* jogos historicamente importantes;
* jogos historicamente influentes.

---

### `scripts/awards.py`

Funções utilizadas:

```python
listar_anos_disponiveis()
listar_jogos_por_ano()
buscar_vencedor_por_ano()
listar_vencedores()
listar_vencedores_na_foundation()
listar_indicados_na_foundation()
listar_jogos_awards_fora_da_foundation()
```

Essas funções permitem consultar a base Awards History e comparar os jogos premiados com a Foundation Collection.

---

## Funcionalidades Implementadas

O dashboard já possui as seguintes funcionalidades.

---

## 1. Cabeçalho Inicial

O dashboard exibe:

* título do projeto;
* descrição breve do The AAA Archive;
* contexto da Foundation Collection e da Awards History.

---

## 2. Organização por Abas

O dashboard usa abas com:

```python
st.tabs()
```

As abas atuais são:

```text
Foundation Collection
Awards History
```

Essa organização deixa o dashboard mais limpo, separando a coleção principal da base de premiações.

---

## 3. Cache no Carregamento dos Dados

O dashboard utiliza:

```python
@st.cache_data
```

Esse recurso foi aplicado ao carregamento dos datasets:

* `games.csv`;
* `awards.csv`.

O objetivo é evitar que os CSVs sejam recarregados do zero toda vez que o usuário interage com filtros, abas ou campos de busca.

Funções criadas no dashboard:

```python
carregar_games_com_cache()
carregar_awards_com_cache()
```

Isso deixa o dashboard mais eficiente e introduz um conceito importante do Streamlit.

---

## 4. Filtros Interativos

O dashboard possui filtros na sidebar.

Filtros disponíveis:

```text
Gênero
Desenvolvedora
Ano de lançamento
Franquia
```

Esses filtros afetam a aba **Foundation Collection**.

Eles permitem explorar a Foundation Collection de forma prática.

---

## 5. Busca Textual

O dashboard possui um campo de busca textual.

A busca permite pesquisar por termos como:

```text
zelda
rockstar
rpg
silent hill
naughty dog
```

A busca é aplicada nas seguintes colunas:

```text
nome
genero
developer
franchise
descricao
```

Isso permite procurar jogos, gêneros, desenvolvedoras, franquias ou termos presentes na descrição.

---

## 6. Métricas da Foundation Collection

O dashboard mostra métricas principais da coleção de jogos.

Métricas exibidas:

```text
Jogos
Desenvolvedoras
Franquias
Gêneros
```

Essas métricas mudam dinamicamente de acordo com a busca textual e os filtros selecionados.

---

## 7. Resultado da Exploração

Após aplicar busca ou filtros, o dashboard mostra a quantidade de jogos encontrados.

Exemplo:

```text
Jogos encontrados: 3
```

Quando uma busca textual está ativa, o dashboard também mostra o termo pesquisado.

---

## 8. Gráficos da Foundation Collection

O dashboard exibe gráficos simples para análise da coleção.

Gráficos implementados:

```text
Jogos por Década
Jogos por Gênero
Desenvolvedoras com Mais Jogos
```

Esses gráficos mudam de acordo com os filtros e a busca textual.

---

## 9. Recorte Editorial

O dashboard possui uma seção chamada:

```text
Recorte Editorial
```

Essa seção destaca jogos marcados no dataset como:

```text
historicamente importantes
historicamente influentes
```

Ela usa as colunas:

```text
historico_importante
historico_influente
```

A seção possui duas métricas:

```text
Historicamente Importantes
Historicamente Influentes
```

E duas tabelas expansíveis:

```text
Jogos Historicamente Importantes
Jogos Historicamente Influentes
```

Esses resultados também mudam de acordo com a busca textual e os filtros selecionados.

---

## 10. Tabela de Jogos

O dashboard exibe uma tabela com os jogos cadastrados.

Colunas exibidas na tabela:

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

A tabela também reage aos filtros e à busca textual.

---

## 11. Seção Awards History

O dashboard possui uma aba dedicada ao histórico de premiações.

Essa seção utiliza o dataset:

```text
data/awards.csv
```

Ela permite visualizar dados relacionados aos vencedores e indicados de Game of the Year.

---

## 12. Métricas da Awards History

A seção de Awards exibe métricas próprias.

Métricas implementadas:

```text
Registros no Awards
Anos catalogados
Vencedores
Fora da Foundation
```

Essas métricas ajudam a entender a dimensão da base de premiações.

---

## 13. Consulta de Awards por Ano

O dashboard permite selecionar um ano específico da premiação.

Ao selecionar um ano, ele mostra:

* vencedor daquele ano;
* indicados daquele ano;
* premiação correspondente;
* status de cada jogo.

Essa funcionalidade ajuda a consultar rapidamente uma edição específica da premiação.

---

## 14. Histórico de Vencedores

O dashboard exibe uma tabela com todos os vencedores cadastrados na Awards History.

Essa tabela permite visualizar a linha histórica dos vencedores de Game of the Year.

---

## 15. Comparação Awards x Foundation Collection

O dashboard compara a base Awards History com a Foundation Collection.

Foram criadas três tabelas expansíveis:

```text
Vencedores presentes na Foundation Collection
Indicados presentes na Foundation Collection
Jogos do Awards fora da Foundation Collection
```

Essa comparação é importante porque ajuda a identificar:

* quais jogos premiados já fazem parte do arquivo principal;
* quais indicados já estão catalogados;
* quais jogos premiados ou indicados ainda podem ser analisados futuramente.

---

## Conceitos Aprendidos Nesta Fase

Durante esta fase, foram introduzidos conceitos importantes de Streamlit e dashboards.

Principais conceitos:

* criação de aplicação visual com Python;
* uso de `st.set_page_config`;
* uso de `st.title`;
* uso de `st.write`;
* uso de `st.metric`;
* uso de `st.columns`;
* uso de `st.sidebar`;
* uso de `st.selectbox`;
* uso de `st.text_input`;
* uso de `st.bar_chart`;
* uso de `st.dataframe`;
* uso de `st.expander`;
* uso de `st.tabs`;
* uso de `@st.cache_data`;
* atualização automática da página ao interagir com filtros;
* reaproveitamento de módulos Python existentes;
* separação entre lógica de dados e visualização.

---

## Decisões Técnicas

Algumas decisões foram tomadas para manter o projeto simples e didático.

---

### 1. Não consumir a API diretamente ainda

Mesmo com a API funcionando, o dashboard ainda acessa diretamente os módulos Python.

Motivo:

```text
menos complexidade
mais clareza
melhor para aprendizado inicial de Streamlit
```

Consumir a API dentro do dashboard pode ser uma etapa futura.

---

### 2. Não usar PostgreSQL ainda

O projeto ainda está usando CSV.

Motivo:

```text
os dados ainda estão em fase de consolidação
o foco atual é aprender visualização
a migração para banco deve vir depois
```

---

### 3. Não criar múltiplas páginas ainda

O dashboard está concentrado em um único arquivo:

```text
dashboard/app.py
```

Motivo:

```text
manter simplicidade
evitar estrutura complexa cedo demais
facilitar manutenção inicial
```

Futuramente, o dashboard pode ser dividido em múltiplas páginas ou componentes.

---

### 4. Não refatorar a API em routers ainda

A API continua funcionando como estava.

Motivo:

```text
a fase atual é Streamlit
não há necessidade de mexer na API agora
```

---

### 5. Usar abas antes de múltiplas páginas

O dashboard utiliza `st.tabs()` para separar visualmente Foundation Collection e Awards History.

Motivo:

```text
melhorar organização visual
sem aumentar a complexidade da estrutura
sem criar múltiplos arquivos agora
```

---

### 6. Usar cache no carregamento dos CSVs

O dashboard utiliza `@st.cache_data` no carregamento dos datasets.

Motivo:

```text
evitar recarregamento desnecessário dos CSVs
melhorar eficiência
ensinar um conceito importante do Streamlit
```

---

## Estado Atual da Arquitetura

A arquitetura atual do projeto está assim:

```text
The-AAA-Archive/

data/
  games.csv
  awards.csv

scripts/
  load_data.py
  filters.py
  search.py
  site_statistics.py
  awards.py

api/
  main.py
  test_main.py

dashboard/
  app.py

docs/
  api_checkpoint.md
  api_plan.md
  awards_dictionary.md
  dashboard_checkpoint.md
  dashboard_plan.md
  data_dictionary.md
  foundation_collection.md
  project_blueprint.md
  project_context.md
  project_conventions.md
```

---

## Comando de Teste Manual

O teste manual principal do dashboard é rodar:

```bash
streamlit run dashboard/app.py
```

E verificar se:

* o navegador abre corretamente;
* as abas aparecem;
* a aba Foundation Collection funciona;
* a aba Awards History funciona;
* as métricas aparecem;
* os gráficos aparecem;
* os filtros funcionam;
* a busca textual funciona;
* a tabela de jogos aparece;
* a seção Recorte Editorial aparece;
* os expansores de jogos históricos e influentes funcionam;
* a consulta por ano em Awards funciona;
* as tabelas comparativas aparecem.

---

## Observação Sobre Cache

Como o dashboard agora usa `@st.cache_data`, pode acontecer de alterações feitas manualmente nos CSVs não aparecerem imediatamente se o Streamlit já estiver aberto.

Se isso acontecer, é possível:

```text
limpar o cache pelo menu do Streamlit
```

Ou parar o servidor com:

```bash
CTRL + C
```

E rodar novamente:

```bash
streamlit run dashboard/app.py
```

---

## Critério de Sucesso da Fase

A fase inicial do dashboard pode ser considerada concluída porque:

* o Streamlit abre corretamente;
* o dataset `games.csv` é carregado;
* o dataset `awards.csv` é carregado;
* o carregamento dos dados usa cache;
* as abas organizam o dashboard;
* as métricas principais são exibidas;
* os filtros interativos funcionam;
* a busca textual funciona;
* os gráficos são exibidos;
* a tabela da Foundation Collection é exibida;
* a seção Recorte Editorial foi adicionada;
* os jogos históricos e influentes são exibidos;
* a seção Awards History foi adicionada;
* a comparação entre Awards e Foundation Collection funciona.

---

## Próximos Passos Possíveis

Os próximos passos possíveis são:

```text
explicar o código do dashboard em detalhes
melhorar a organização interna do app.py
criar funções auxiliares para reduzir repetição
adicionar gráficos mais bem formatados
melhorar a apresentação da Awards History
criar seção visual para notas pessoais
pensar em múltiplas páginas no Streamlit
criar testes simples para funções auxiliares do dashboard
planejar migração para PostgreSQL
```

---

## O que Não Fazer Ainda

Nesta fase, ainda não é necessário:

```text
migrar para PostgreSQL
consumir a API dentro do Streamlit
refatorar a API em routers
criar frontend separado
fazer deploy do dashboard
criar autenticação
complicar a estrutura do projeto
```

Essas etapas podem ser feitas futuramente, mas ainda não são prioridade.

---

## Status Final do Checkpoint

Status final:

```text
Dashboard Streamlit inicial concluído, testado manualmente e documentado
```

Próxima etapa recomendada:

```text
Entender o código do dashboard/app.py em detalhes
```
