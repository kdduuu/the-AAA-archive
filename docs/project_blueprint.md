# Project Blueprint — The AAA Archive

> **Este documento representa a visão oficial do The AAA Archive.**
>
> Antes de implementar novas funcionalidades, alterar a arquitetura ou iniciar uma nova conversa sobre o projeto, este documento deve ser utilizado como principal referência.

---

# O que é o The AAA Archive?

O **The AAA Archive** é um projeto pessoal de desenvolvimento de software cujo objetivo é construir um arquivo digital dedicado à preservação, organização e exploração da história dos videogames AAA single-player.

O projeto nasceu como uma forma de estudar Python e análise de dados utilizando Pandas, mas evoluiu para algo maior: a construção de um software completo, composto por backend, API, banco de dados, website e dashboard.

A **Foundation Collection** representa o núcleo principal do projeto. Ela reúne uma seleção cuidadosamente curada de jogos considerados relevantes para a história da indústria, servindo como base para filtros, buscas, estatísticas e análises.

Além da Foundation Collection, o projeto também possui uma base independente chamada **Awards History**, responsável por armazenar vencedores e indicados a Game of the Year.

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

# Bases Principais do Projeto

O projeto trabalha atualmente com duas bases em CSV.

## Foundation Collection

Arquivo:

```text
data/games.csv
```

Representa o núcleo principal do The AAA Archive.

Cada linha representa um jogo da coleção principal.

Essa base será usada por:

* filtros;
* busca textual;
* estatísticas;
* página Archive;
* página Home;
* API;
* dashboard.

---

## Awards History

Arquivo:

```text
data/awards.csv
```

Representa o histórico de vencedores e indicados a Game of the Year.

Essa base é independente da Foundation Collection.

Isso significa que um jogo pode aparecer no histórico de premiações mesmo sem fazer parte da coleção principal.

No entanto, ambas as bases podem ser comparadas pelo nome do jogo:

```text
awards.csv → jogo
games.csv  → nome
```

Essa comparação permite identificar:

* vencedores que já estão na Foundation Collection;
* indicados que já estão na Foundation Collection;
* jogos premiados ou indicados que ainda estão fora da coleção principal.

---

# Arquitetura Geral

O projeto será desenvolvido em camadas.

```text
Datasets CSV
│
├── games.csv
│   └── Foundation Collection
│
├── awards.csv
│   └── Awards History
│
▼
load_data.py
│
▼
Módulos do Projeto
│
├── filters.py
├── search.py
├── site_statistics.py
├── awards.py
└── ...
│
▼
API
│
▼
Website / Dashboard
```

No futuro, os arquivos CSV poderão ser substituídos por um banco de dados PostgreSQL sem alterar a lógica principal dos módulos.

A ideia é que a fonte dos dados mude, mas os módulos continuem tendo responsabilidades claras.

---

# Estrutura do Website

O website foi planejado para ser simples, intuitivo e de fácil manutenção.

Ao invés de possuir dezenas de páginas independentes, a maior parte das funcionalidades será concentrada em poucas páginas dinâmicas.

---

## Home

A Home será responsável por apresentar uma visão geral do The AAA Archive.

Ela poderá exibir:

* total de jogos da Foundation Collection;
* total de desenvolvedoras;
* total de franquias;
* total de gêneros;
* linha do tempo da coleção;
* jogos históricos;
* jogos influentes;
* destaques da coleção.

### Backend responsável

```text
site_statistics.py
```

---

## Archive

O **Archive** será o coração do website.

Nele estarão todos os jogos da Foundation Collection.

O usuário poderá:

* pesquisar;
* aplicar filtros;
* ordenar resultados;
* abrir a página individual de qualquer jogo.

Ao selecionar um jogo, as informações poderão ser carregadas dinamicamente.

Cada jogo poderá apresentar:

* capa;
* descrição;
* ano de lançamento;
* desenvolvedora;
* franquia;
* gênero;
* notas;
* importância histórica;
* influência histórica;
* jogos relacionados.

### Backend responsável

```text
filters.py
search.py
```

---

## Awards

A seção **Awards** apresentará o histórico de vencedores e indicados a Game of the Year.

Ela utilizará a base independente `awards.csv`.

Cada ano poderá exibir:

* premiação;
* vencedor;
* indicados.

Nesta primeira versão, o objetivo é preservar apenas as informações principais das premiações.

A base Awards History será independente da Foundation Collection.

Isso significa que um jogo poderá aparecer como indicado ou vencedor mesmo sem fazer parte da coleção principal.

Quando um jogo existir nas duas bases, o sistema poderá conectá-las automaticamente por meio do nome do jogo.

### Backend responsável

```text
awards.py
```

---

## Dashboard

Área destinada às análises gráficas do projeto.

Exemplos:

* distribuição dos gêneros;
* quantidade de jogos por desenvolvedora;
* evolução da coleção ao longo dos anos;
* distribuição por década;
* distribuição das notas;
* relação entre jogos da Foundation Collection e jogos indicados ou vencedores de Game of the Year.

Todo o dashboard deverá reutilizar os mesmos módulos desenvolvidos para o restante do sistema.

---

# Estrutura dos Módulos

Cada módulo possui apenas uma responsabilidade.

---

## load_data.py

Responsável por carregar os datasets oficiais do projeto.

Atualmente carrega:

* `games.csv`;
* `awards.csv`.

Funções principais:

```text
carregar_dataset()
carregar_awards()
```

---

## filters.py

Centraliza todos os filtros utilizados pelo **Archive**.

Exemplos:

* filtrar por gênero;
* filtrar por desenvolvedora;
* filtrar por franquia;
* filtrar por ano;
* filtrar por década.

---

## search.py

Responsável pela pesquisa textual do **Archive**.

A busca poderá considerar campos como:

* nome;
* gênero;
* desenvolvedora;
* franquia;
* descrição.

---

## site_statistics.py

Responsável por gerar todas as estatísticas apresentadas na Home, API e dashboard.

Nenhuma informação estatística exibida na página inicial deverá ser escrita manualmente.

As estatísticas devem ser calculadas a partir da base de dados.

---

## awards.py

Responsável por consultar os vencedores e indicados das premiações de Game of the Year.

Também é responsável por comparar a base Awards History com a Foundation Collection.

Exemplos de consultas:

* listar premiações cadastradas;
* listar anos disponíveis;
* buscar vencedor por ano;
* listar indicados por ano;
* listar todos os vencedores;
* filtrar por premiação;
* listar vencedores que estão na Foundation Collection;
* listar indicados que estão na Foundation Collection;
* listar jogos do Awards que ainda estão fora da Foundation Collection.

---

# Filosofia de Desenvolvimento

O desenvolvimento do The AAA Archive seguirá alguns princípios fundamentais.

* Cada módulo deve possuir apenas uma responsabilidade.
* Toda função criada deve possuir uma utilização real dentro do website, API ou dashboard.
* Antes de criar uma função, deve-se definir qual parte do sistema irá utilizá-la.
* O backend será desenvolvido antes da interface.
* Os módulos devem ser reutilizáveis pela API, website e dashboard.
* O código deve permanecer simples, organizado e bem documentado.
* Sempre que possível, evitar duplicação de lógica.
* A estrutura do projeto deve crescer de forma incremental.
* O projeto deve priorizar clareza antes de complexidade.

---

# Fluxo de Desenvolvimento

Novas funcionalidades deverão seguir a seguinte sequência:

```text
Definir a funcionalidade

↓

Identificar onde ela será utilizada no sistema

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

* Foundation Collection consolidada;
* Awards History organizada;
* backend modular em Python;
* banco de dados PostgreSQL;
* API para disponibilização dos dados;
* website completo para exploração da coleção;
* dashboard analítico.

Mais do que um catálogo de jogos, o projeto pretende se tornar um arquivo digital organizado, escalável e preparado para evoluir continuamente sem perder sua simplicidade.

---

# Próximos Passos

A fase atual do projeto é:

```text
Datasets CSV
↓
Backend modular com Pandas
↓
Testes simples com assert
```

A próxima fase será planejar e iniciar a API.

Antes disso, é importante manter a documentação alinhada com os módulos atuais do projeto.

O módulo oficial de premiações é:

```text
awards.py
```

O antigo nome `goty.py` não deve mais ser usado na documentação.
