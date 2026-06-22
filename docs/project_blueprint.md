# Project Blueprint — The AAA Archive

> **Este documento representa a visão oficial do The AAA Archive.**
>
> Antes de implementar novas funcionalidades, alterar a arquitetura ou iniciar uma nova conversa sobre o projeto, este documento deve ser utilizado como principal referência.

---

# O que é o The AAA Archive?

O **The AAA Archive** é um projeto pessoal de desenvolvimento de software cujo objetivo é construir um arquivo digital dedicado à preservação e organização da história dos videogames.

O projeto nasceu como uma forma de estudar Python e análise de dados utilizando Pandas, mas evoluiu para algo maior: a construção de um software completo, composto por backend, API, banco de dados e website.

A Foundation Collection representa o núcleo do projeto. Ela reúne uma seleção cuidadosamente curada de jogos considerados relevantes para a história da indústria, servindo como base para todas as análises, estatísticas e funcionalidades do sistema.

O objetivo não é catalogar todos os jogos existentes, mas construir uma coleção consistente, organizada e preparada para crescer ao longo do tempo.

---

# Objetivos do Projeto

O desenvolvimento do The AAA Archive possui quatro objetivos principais.

* Construir uma Foundation Collection organizada e bem documentada.
* Desenvolver um backend reutilizável utilizando Python e Pandas.
* Disponibilizar os dados através de uma API.
* Criar um website moderno para exploração da coleção.

Todo código desenvolvido deverá possuir uma finalidade prática dentro do produto.

---

# Arquitetura Geral

O projeto será desenvolvido em camadas.

```text
Foundation Collection (CSV)
            │
            ▼
      load_data.py
            │
            ▼
     Módulos do Projeto
            │
            ├── filters.py
            ├── site_statistics.py
            ├── search.py
            ├── goty.py
            └── ...
            │
            ▼
            API
            │
            ▼
         Website
```

No futuro, o CSV será substituído por um banco de dados PostgreSQL sem alterar a organização dos módulos.

---

# Estrutura do Website

O website foi planejado para ser simples, intuitivo e de fácil manutenção.

Ao invés de possuir dezenas de páginas independentes, a maior parte das funcionalidades será concentrada em poucas páginas dinâmicas.

---

## 🏠 Home

A Home será responsável por apresentar uma visão geral do The AAA Archive.

Ela poderá exibir:

* Total de jogos da Foundation Collection.
* Total de desenvolvedoras.
* Total de franquias.
* Total de gêneros.
* Linha do tempo da coleção.
* Jogos históricos.
* Jogos influentes.
* Últimos jogos adicionados.
* Destaques da coleção.

### Backend responsável

`site_statistics.py`

---

## 🎮 Archive

O **Archive** será o coração do website.

Nele estarão todos os jogos da Foundation Collection.

O usuário poderá:

* pesquisar;
* aplicar filtros;
* ordenar resultados;
* abrir a página individual de qualquer jogo.

Ao selecionar um jogo, as informações serão carregadas dinamicamente, sem necessidade de uma nova seção dedicada apenas para isso.

Cada jogo poderá apresentar:

* capa;
* descrição;
* ano de lançamento;
* desenvolvedora;
* franquia;
* gênero;
* notas;
* curiosidades;
* jogos relacionados.

### Backend responsável

* `filters.py`
* `search.py`

---

## 🏆 Game Awards

Esta seção apresentará o histórico do prêmio **Game of the Year**.

Cada ano exibirá apenas:

* vencedor;
* indicados.

Nesta primeira versão, o objetivo é preservar apenas as informações principais do prêmio.

O histórico do Game Awards será independente da Foundation Collection.

Isso significa que um jogo poderá aparecer como indicado ao GOTY mesmo sem fazer parte da coleção principal.

No futuro, caso esse jogo seja adicionado à Foundation Collection, ambas as informações poderão ser conectadas automaticamente.

### Backend responsável

`goty.py`

---

## 📊 Dashboard

Área destinada às análises gráficas do projeto.

Exemplos:

* distribuição dos gêneros;
* quantidade de jogos por desenvolvedora;
* evolução da coleção ao longo dos anos;
* distribuição das notas.

Todo o dashboard reutilizará os mesmos módulos desenvolvidos para o restante do sistema.

---

# Estrutura dos Módulos

Cada módulo possui apenas uma responsabilidade.

## load_data.py

Responsável por carregar a Foundation Collection para um DataFrame.

---

## filters.py

Centraliza todos os filtros utilizados pelo **Archive**.

Exemplos:

* filtrar por gênero;
* desenvolvedora;
* franquia;
* ano;
* década.

---

## site_statistics.py

Responsável por gerar todas as estatísticas apresentadas na Home.

Nenhuma informação exibida na página inicial deverá ser escrita manualmente.

---

## search.py

Responsável pela pesquisa textual do **Archive**.

---

## goty.py

Responsável por consultar os vencedores e indicados do Game Awards.

---

# Filosofia de Desenvolvimento

O desenvolvimento do The AAA Archive seguirá alguns princípios fundamentais.

* Cada módulo deve possuir apenas uma responsabilidade.
* Toda função criada deve possuir uma utilização real dentro do website.
* Antes de criar uma função, deve-se definir qual parte do sistema irá utilizá-la.
* O backend será desenvolvido antes da interface.
* Os módulos devem ser reutilizáveis pela API, website e dashboard.
* O código deve permanecer simples, organizado e bem documentado.
* Sempre que possível, evitar duplicação de lógica.

---

# Fluxo de Desenvolvimento

Novas funcionalidades deverão seguir a seguinte sequência:

```text
Definir a funcionalidade

↓

Identificar onde ela será utilizada no website

↓

Definir o módulo responsável

↓

Implementar a função

↓

Criar testes

↓

Documentar
```

Esse fluxo garante que o projeto cresça de forma organizada e que todo código desenvolvido possua uma finalidade clara.

---

# Visão de Longo Prazo

Ao final do desenvolvimento, o The AAA Archive deverá possuir:

* Foundation Collection consolidada.
* Backend modular em Python.
* Banco de dados PostgreSQL.
* API para disponibilização dos dados.
* Website completo para exploração da coleção.
* Dashboard analítico.

Mais do que um catálogo de jogos, o projeto pretende se tornar um arquivo digital organizado, escalável e preparado para evoluir continuamente sem perder sua simplicidade.
