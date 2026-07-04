# Dashboard Plan — The AAA Archive

## Objetivo deste Documento

Este documento define o plano de desenvolvimento e organização do dashboard do projeto **The AAA Archive**.

O dashboard é desenvolvido com **Streamlit** e tem como objetivo transformar os dados da **Foundation Collection** e da **Awards History** em uma visualização simples, clara e interativa.

A ideia é continuar o projeto de forma incremental, mantendo a mesma filosofia usada desde o início:

* clareza antes de complexidade;
* documentação antes de grandes mudanças;
* reaproveitamento dos módulos existentes;
* uma responsabilidade por arquivo;
* uma responsabilidade por função;
* evolução gradual do projeto;
* organização antes da migração para PostgreSQL.

Este documento também registra que a primeira versão funcional do dashboard já foi criada.

A fase atual não é mais criar o dashboard do zero, mas organizar melhor o arquivo `dashboard/app.py`, que cresceu bastante durante o desenvolvimento.

---

## O que é um Dashboard?

Um dashboard é uma tela visual que reúne informações importantes de um projeto.

No caso do **The AAA Archive**, o dashboard serve para visualizar dados como:

* quantidade total de jogos cadastrados;
* quantidade de desenvolvedoras;
* quantidade de franquias;
* quantidade de gêneros;
* jogos por gênero;
* jogos por desenvolvedora;
* jogos por franquia;
* jogos por década;
* jogos historicamente importantes;
* jogos historicamente influentes;
* vencedores e indicados de Game of the Year;
* relação entre Awards History e Foundation Collection.

Em vez de olhar apenas para arquivos CSV ou respostas da API, o dashboard permite enxergar os dados de forma mais organizada e visual.

---

## O que é Streamlit?

Streamlit é uma biblioteca do Python usada para criar interfaces visuais de forma simples.

Com ele, é possível transformar scripts Python em uma aplicação visual no navegador, sem precisar criar HTML, CSS ou JavaScript manualmente.

Isso combina bem com a fase atual do projeto, porque o The AAA Archive já possui:

* datasets em CSV;
* módulos Python com Pandas;
* funções de filtros;
* funções de busca;
* funções de estatísticas;
* funções relacionadas a premiações;
* API inicial com FastAPI;
* dashboard inicial com Streamlit.

O Streamlit é usado para mostrar esses dados visualmente.

---

## Papel do Streamlit no Projeto

O Streamlit é a primeira camada visual do The AAA Archive.

Ele não substitui a API.

Ele também não substitui os módulos Python.

A função dele é apresentar os dados de forma mais amigável e interativa.

A relação atual do projeto é:

```text
CSV
↓
Pandas
↓
Módulos Python
↓
Streamlit Dashboard
```

Atualmente, o dashboard consome diretamente os módulos internos do projeto.

Mais para frente, o projeto poderá evoluir para:

```text
PostgreSQL
↓
Backend/API
↓
Frontend/Web
```

Mas, neste momento, o foco ainda é consolidar a base atual antes da migração para banco de dados.

---

## Por que Ainda Não Usar PostgreSQL?

Ainda não é o momento ideal para iniciar a migração para PostgreSQL porque o projeto acabou de concluir duas etapas importantes:

* API inicial;
* dashboard inicial.

Antes de migrar para banco de dados, é importante garantir que:

* os CSVs estejam organizados;
* os módulos Python estejam funcionando;
* os testes estejam passando;
* a API esteja estável;
* o dashboard esteja funcionando;
* a documentação esteja alinhada;
* o `dashboard/app.py` esteja melhor organizado;
* o `requirements.txt` esteja revisado.

Quando essa base estiver mais madura, a migração para PostgreSQL fará mais sentido.

A ordem correta é:

```text
Organizar o projeto atual
↓
Revisar dependências
↓
Planejar PostgreSQL
↓
Migrar para PostgreSQL
```

---

## Por que Não Consumir a API Diretamente Agora?

Mesmo a API já estando funcionando, o dashboard atual reaproveita diretamente os módulos Python.

Isso deixa o aprendizado mais simples e evita uma camada extra de complexidade.

Nesta fase, o dashboard pode importar funções como:

```python
from scripts.load_data import carregar_dataset
from scripts.site_statistics import gerar_estatisticas_home
```

Dessa forma, o Streamlit trabalha diretamente com os dados e funções internas do projeto.

Consumir a própria API dentro do dashboard pode ser uma etapa futura, quando o projeto estiver mais maduro.

No momento, o objetivo principal é entender bem:

* leitura de dados;
* filtros;
* busca;
* estatísticas;
* visualização;
* organização do código.

---

## Estrutura Atual do Dashboard

A estrutura atual do dashboard é:

```text
The-AAA-Archive/

dashboard/
  app.py
```

O arquivo principal do dashboard é:

```text
dashboard/app.py
```

Ele é responsável por montar a interface visual do projeto.

Atualmente, o `app.py` já concentra:

* carregamento dos dados;
* cache;
* sidebar;
* filtros;
* busca textual;
* abas;
* métricas;
* gráficos;
* tabelas;
* seções da Foundation Collection;
* seções da Awards History;
* comparação entre Awards History e Foundation Collection.

Como o arquivo cresceu bastante, a próxima etapa será organizar melhor esse código.

---

## Estrutura Recomendada para a Próxima Organização

A organização recomendada para a fase atual é simples:

```text
dashboard/
  app.py
  dashboard_helpers.py
```

O objetivo é manter o projeto fácil de entender.

Nesta fase, ainda não é necessário criar uma estrutura grande como:

```text
dashboard/
  components/
    sidebar.py
    foundation_tab.py
    awards_tab.py
```

Essa estrutura pode ser útil no futuro, mas agora ela adicionaria complexidade antes da hora.

A melhor decisão para o momento é criar apenas um arquivo auxiliar.

---

## Responsabilidade do `dashboard/app.py`

O arquivo `dashboard/app.py` deve continuar sendo o arquivo principal do dashboard.

Ele deve ser responsável por:

* configurar a página com `st.set_page_config()`;
* montar a interface visual;
* criar os títulos;
* organizar as abas;
* exibir métricas;
* exibir gráficos;
* exibir tabelas;
* controlar o fluxo visual da aplicação.

O `app.py` deve continuar mostrando claramente o que aparece na tela.

Como o projeto também tem objetivo de aprendizado, é importante que o arquivo principal ainda seja fácil de acompanhar.

---

## Responsabilidade do `dashboard_helpers.py`

O arquivo `dashboard_helpers.py` deve ser criado para guardar funções auxiliares do dashboard.

Ele pode concentrar funções como:

```python
carregar_games_com_cache()
carregar_awards_com_cache()
aplicar_busca_textual()
criar_opcoes_filtro()
aplicar_filtros_foundation()
```

O objetivo desse arquivo não é mudar o funcionamento do dashboard.

O objetivo é apenas tirar do `app.py` algumas partes repetitivas ou muito lógicas.

Assim, o `app.py` fica mais limpo e o dashboard continua funcionando do mesmo jeito.

---

## O que Não Deve Mudar na Organização Atual

Durante essa refatoração leve, não devemos mudar:

* visual do dashboard;
* textos principais;
* abas existentes;
* filtros existentes;
* métricas existentes;
* gráficos existentes;
* tabelas existentes;
* lógica principal das análises;
* endpoints da API;
* datasets;
* módulos principais da pasta `scripts/`.

Essa etapa é apenas uma organização interna.

A regra principal é:

```text
O dashboard deve continuar parecendo e funcionando igual.
```

A diferença deve estar apenas na organização do código.

---

## Primeira Versão do Dashboard

A primeira versão do dashboard já foi criada.

Ela deixou de ser apenas um plano e passou a ser uma parte funcional do projeto.

A primeira versão do dashboard possui:

* título do projeto;
* descrição do The AAA Archive;
* métricas principais da Foundation Collection;
* tabela com os jogos cadastrados;
* filtros interativos;
* busca textual;
* gráficos simples;
* aba Foundation Collection;
* aba Awards History;
* consulta por ano no Awards History;
* histórico de vencedores;
* comparação entre jogos do Awards e jogos da Foundation Collection.

Portanto, o status da primeira versão é:

```text
Dashboard inicial concluído
```

---

## Módulos Reaproveitados

O dashboard reaproveita os módulos já criados no backend.

Principalmente:

```text
scripts/load_data.py
scripts/site_statistics.py
scripts/filters.py
scripts/search.py
scripts/awards.py
```

Isso evita repetição de código.

A lógica continua nos módulos Python.

O Streamlit apenas exibe os resultados visualmente.

Essa separação é importante porque permite que os mesmos módulos sejam reutilizados por:

* testes;
* API;
* dashboard;
* futuro website;
* futura integração com PostgreSQL.

---

## Seções Atuais do Dashboard

O dashboard atual possui duas abas principais:

```text
Foundation Collection
Awards History
```

---

## Aba Foundation Collection

A aba **Foundation Collection** apresenta a coleção principal do The AAA Archive.

Ela possui:

* métricas principais;
* filtros;
* busca textual;
* tabela de jogos;
* gráficos simples;
* seção de Recorte Editorial;
* jogos historicamente importantes;
* jogos historicamente influentes.

Essa aba utiliza principalmente os dados de:

```text
data/games.csv
```

E reaproveita funções dos módulos:

```text
load_data.py
filters.py
search.py
site_statistics.py
```

---

## Aba Awards History

A aba **Awards History** apresenta os vencedores e indicados a Game of the Year.

Ela possui:

* consulta de premiações por ano;
* exibição de vencedor;
* exibição de indicados;
* histórico de vencedores;
* comparação entre Awards History e Foundation Collection;
* jogos vencedores que estão na Foundation Collection;
* jogos indicados que estão na Foundation Collection;
* jogos do Awards que ainda estão fora da Foundation Collection.

Essa aba utiliza principalmente os dados de:

```text
data/awards.csv
```

E reaproveita funções do módulo:

```text
awards.py
```

---

## Possíveis Melhorias Futuras do Dashboard

No futuro, o dashboard poderá receber melhorias como:

* gráficos mais elaborados;
* análise de notas;
* análise por década;
* análise por franquia;
* análise por desenvolvedora;
* filtros combinados mais avançados;
* páginas separadas;
* componentes internos;
* consumo da API;
* deploy online.

Essas melhorias não fazem parte da fase atual.

Elas devem ser consideradas apenas depois da organização do código e da fase de PostgreSQL.

---

## Comando para Rodar o Dashboard

O dashboard pode ser executado com:

```bash
streamlit run dashboard/app.py
```

O Streamlit abrirá uma aplicação no navegador.

Normalmente, o endereço será parecido com:

```text
http://localhost:8501
```

---

## Ordem de Desenvolvimento Original

A ordem inicial planejada para criação do dashboard era:

```text
Criar docs/dashboard_plan.md
↓
Criar dashboard/app.py
↓
Exibir título e descrição
↓
Carregar dados com Pandas
↓
Exibir métricas principais
↓
Exibir tabela de jogos
↓
Adicionar gráficos simples
↓
Adicionar filtros básicos
↓
Adicionar seção de Awards
```

Essa etapa já foi executada.

---

## Ordem Atual de Organização

A ordem atual recomendada é:

```text
Atualizar project_context.md
↓
Atualizar project_blueprint.md
↓
Atualizar project_conventions.md
↓
Atualizar dashboard_plan.md
↓
Ajustar o final de dashboard_checkpoint.md
↓
Ajustar o final de api_checkpoint.md
↓
Marcar api_plan.md como plano já executado
↓
Organizar dashboard/app.py
↓
Revisar requirements.txt
↓
Criar docs/postgresql_plan.md
↓
Planejar migração para PostgreSQL
```

Essa ordem evita misturar documentação, refatoração e banco de dados ao mesmo tempo.

---

## O que Não Fazer Agora

Nesta fase, ainda não devemos:

* migrar para PostgreSQL;
* refatorar a API em routers;
* criar novos endpoints na API;
* criar frontend com HTML/CSS/JavaScript;
* consumir a API dentro do dashboard;
* criar autenticação;
* fazer deploy;
* mudar o visual do dashboard;
* adicionar funcionalidades grandes;
* criar estrutura exagerada de componentes.

Essas etapas podem ser importantes no futuro, mas agora o foco é organizar o que já existe.

---

## Critério de Sucesso da Primeira Versão

A primeira versão do dashboard foi considerada concluída quando:

* o Streamlit abriu corretamente;
* os dados do `games.csv` foram carregados;
* os dados do `awards.csv` foram carregados;
* as estatísticas principais foram exibidas;
* a tabela de jogos apareceu na tela;
* os filtros funcionaram;
* a busca textual funcionou;
* os gráficos simples apareceram;
* a seção Awards History funcionou;
* a comparação entre Awards History e Foundation Collection funcionou.

Esses critérios já foram atendidos.

---

## Critério de Sucesso da Próxima Organização

A próxima organização será considerada concluída quando:

* o dashboard continuar funcionando;
* o visual não for alterado;
* as funcionalidades principais continuarem iguais;
* parte da lógica auxiliar sair do `app.py`;
* o arquivo `dashboard_helpers.py` for criado;
* o `app.py` ficar mais fácil de ler;
* os testes existentes continuarem passando;
* a documentação continuar alinhada com o estado real do projeto.

---

## Status da Fase

Status atual:

```text
Dashboard inicial concluído
```

Fase atual:

```text
Organização leve antes do PostgreSQL
```

Próxima etapa:

```text
Organizar dashboard/app.py sem alterar visual nem adicionar funcionalidades grandes.
```

Depois disso:

```text
Revisar requirements.txt
↓
Criar docs/postgresql_plan.md
↓
Planejar migração para PostgreSQL
```
