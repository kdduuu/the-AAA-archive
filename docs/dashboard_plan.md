# Dashboard Plan — The AAA Archive

## Objetivo deste Documento

Este documento define o plano inicial para a criação do dashboard do projeto **The AAA Archive**.

O dashboard será desenvolvido com **Streamlit** e terá como objetivo transformar os dados da Foundation Collection e da Awards History em uma visualização simples, clara e interativa.

A ideia é continuar o projeto de forma incremental, mantendo a mesma filosofia usada até agora:

* clareza antes de complexidade;
* documentação antes de implementação;
* reaproveitamento dos módulos existentes;
* uma responsabilidade por arquivo;
* uma responsabilidade por função;
* evolução gradual do projeto.

---

## O que é um Dashboard?

Um dashboard é uma tela visual que reúne informações importantes de um projeto.

No caso do **The AAA Archive**, o dashboard servirá para visualizar dados como:

* quantidade total de jogos cadastrados;
* quantidade de desenvolvedoras;
* quantidade de franquias;
* quantidade de gêneros;
* jogos por gênero;
* jogos por desenvolvedora;
* jogos por década;
* jogos historicamente importantes;
* jogos historicamente influentes;
* vencedores e indicados de Game of the Year.

Em vez de olhar apenas para arquivos CSV ou respostas da API, o dashboard permite enxergar os dados de forma mais organizada.

---

## O que é Streamlit?

Streamlit é uma biblioteca do Python usada para criar interfaces visuais de forma simples.

Com ele, conseguimos transformar scripts Python em uma aplicação visual no navegador, sem precisar criar HTML, CSS ou JavaScript manualmente.

Isso combina bem com a fase atual do projeto, porque o The AAA Archive já possui:

* datasets em CSV;
* módulos Python com Pandas;
* funções de filtros;
* funções de busca;
* funções de estatísticas;
* funções relacionadas a premiações.

O Streamlit será usado para mostrar esses dados visualmente.

---

## Papel do Streamlit no Projeto

O Streamlit será a primeira camada visual do The AAA Archive.

Ele não substitui a API.

Ele também não substitui os módulos Python.

A função dele será apenas apresentar os dados de forma mais amigável.

A relação atual do projeto será:

```text
CSV
↓
Pandas
↓
Módulos Python
↓
Streamlit Dashboard
```

Mais para frente, o projeto poderá evoluir para:

```text
PostgreSQL
↓
Backend/API
↓
Frontend/Web
```

Mas, neste momento, o foco ainda é aprender e consolidar a base.

---

## Por que ainda não usar PostgreSQL?

Ainda não é o momento ideal para usar PostgreSQL porque o projeto ainda está consolidando a fase de visualização dos dados.

Antes de migrar para banco de dados, é importante garantir que:

* os CSVs estejam organizados;
* os módulos Python estejam funcionando;
* as estatísticas estejam corretas;
* a API esteja estável;
* o dashboard consiga representar bem os dados.

Quando essa base estiver mais madura, a migração para PostgreSQL fará mais sentido.

---

## Por que não consumir a API diretamente agora?

Mesmo a API já estando funcionando, o primeiro dashboard pode reaproveitar diretamente os módulos Python.

Isso deixa o aprendizado mais simples.

Nesta fase, o dashboard pode importar funções como:

```python
from scripts.load_data import carregar_dataset
from scripts.site_statistics import gerar_estatisticas_home
```

Dessa forma, o Streamlit trabalha diretamente com os dados e funções internas do projeto.

Consumir a própria API dentro do dashboard pode ser uma etapa futura, quando o projeto estiver mais maduro.

---

## Estrutura Planejada

A estrutura inicial será:

```text
The-AAA-Archive/

dashboard/
  app.py
```

O arquivo principal do dashboard será:

```text
dashboard/app.py
```

Ele será responsável por montar a primeira interface visual do projeto.

---

## Primeira Versão do Dashboard

A primeira versão do dashboard deve ser simples.

Ela deve conter:

1. título do projeto;
2. breve descrição do The AAA Archive;
3. métricas principais da Foundation Collection;
4. tabela com os jogos cadastrados;
5. primeiras visualizações simples dos dados.

As primeiras métricas podem incluir:

* total de jogos;
* total de desenvolvedoras;
* total de franquias;
* total de gêneros.

Essas informações já podem vir da função:

```python
gerar_estatisticas_home()
```

---

## Módulos que serão Reaproveitados

O dashboard deve reaproveitar os módulos já criados no backend.

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

O Streamlit apenas exibe os resultados.

---

## Responsabilidade do `dashboard/app.py`

O arquivo `dashboard/app.py` deve ter como responsabilidade principal:

* carregar os dados;
* chamar funções já existentes;
* organizar a interface visual;
* exibir métricas, tabelas e gráficos.

Ele não deve concentrar regras complexas de negócio.

Sempre que uma lógica ficar grande demais, ela deve ser movida para um módulo dentro de `scripts/`.

---

## Possíveis Seções do Dashboard

No futuro, o dashboard pode ter seções como:

### Home

Visão geral do arquivo.

Pode mostrar:

* total de jogos;
* total de desenvolvedoras;
* total de franquias;
* total de gêneros;
* jogos históricos;
* jogos influentes.

### Foundation Collection

Tabela principal com os jogos cadastrados.

Pode permitir filtros por:

* nome;
* ano;
* gênero;
* desenvolvedora;
* franquia.

### Estatísticas

Área com gráficos e contagens.

Pode mostrar:

* jogos por década;
* jogos por gênero;
* jogos por desenvolvedora;
* jogos por franquia.

### Awards History

Área dedicada às premiações.

Pode mostrar:

* vencedores por ano;
* indicados por ano;
* jogos premiados que estão na Foundation Collection;
* jogos premiados que ainda estão fora da Foundation Collection.

---

## Primeira Meta Técnica

A primeira meta técnica será criar um dashboard mínimo funcionando.

O objetivo não é deixar bonito.

O objetivo é fazer funcionar.

A primeira versão deve responder a esta pergunta:

```text
Consigo abrir o dashboard no navegador e visualizar os dados principais do The AAA Archive?
```

Se a resposta for sim, a primeira etapa estará concluída.

---

## Comando para Rodar o Dashboard

Quando o arquivo `dashboard/app.py` for criado, o dashboard poderá ser executado com:

```bash
streamlit run dashboard/app.py
```

O Streamlit abrirá uma aplicação no navegador.

Normalmente, o endereço será parecido com:

```text
http://localhost:8501
```

---

## Ordem de Desenvolvimento

A ordem recomendada para esta fase é:

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

---

## O que Não Fazer Agora

Nesta fase, ainda não devemos:

* migrar para PostgreSQL;
* refatorar a API em routers;
* criar frontend com HTML/CSS/JavaScript;
* consumir a API dentro do dashboard;
* criar autenticação;
* fazer deploy;
* complicar a estrutura do projeto.

Essas etapas podem ser importantes no futuro, mas agora o foco é aprender Streamlit de forma simples e prática.

---

## Critério de Sucesso da Primeira Versão

A primeira versão do dashboard será considerada concluída quando:

* o Streamlit abrir corretamente;
* os dados do `games.csv` forem carregados;
* as estatísticas principais forem exibidas;
* a tabela de jogos aparecer na tela;
* o código estiver simples e compreensível.

---

## Status da Fase

Status atual:

```text
Dashboard planejado
```

Próxima etapa:

```text
Criar dashboard/app.py
```
