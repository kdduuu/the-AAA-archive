# Data Dictionary — The AAA Archive

# Objetivo

Este documento especifica oficialmente a estrutura do arquivo **`games.csv`**, utilizado na **Fase 1** do projeto **The AAA Archive**.

Seu objetivo é definir os tipos de dados, regras de preenchimento, convenções e padrões adotados durante o desenvolvimento do backend.

Todas as análises, filtros, estatísticas, API e futuras migrações para PostgreSQL utilizarão esta especificação como referência.

---

# Unidade do Dataset

Cada linha do dataset representa **um jogo**.

Cada coluna representa **uma característica desse jogo**.

---

# Estratégia de Desenvolvimento

## Fase 1

* Dataset em CSV (`games.csv`)
* Manipulação dos dados com Pandas
* Desenvolvimento do backend
* Implementação das primeiras funcionalidades do sistema

## Fase 2

* Migração para PostgreSQL
* Normalização do banco de dados
* Integração completa do backend

## Fase 3

* Desenvolvimento da API
* Construção do Website
* Desenvolvimento do Dashboard

---

# Escopo

Este documento descreve exclusivamente a estrutura do dataset da **Foundation Collection**.

Os critérios editoriais da coleção são definidos em **`foundation_collection.md`**.

O histórico do **Game Awards** será documentado em uma base independente.

---

# Regras Gerais

* Cada jogo possui um identificador único (`id`).
* Os dados devem seguir rigorosamente os padrões definidos neste documento.
* O dataset será expandido de forma incremental.
* Sempre que possível, os dados deverão ser padronizados para facilitar filtros, pesquisas e análises futuras.

---

# Arquivo Principal

```text
data/
└── games.csv
```

---

# Estrutura do Dataset

| Coluna               | Tipo    | Obrigatório |
| -------------------- | ------- | ----------- |
| id                   | Integer | Sim         |
| nome                 | String  | Sim         |
| ano_lancamento       | Integer | Sim         |
| genero               | String  | Sim         |
| developer            | String  | Sim         |
| franchise            | String  | Sim         |
| descricao            | Text    | Não         |
| metacritic           | Integer | Não         |
| nota_kadu            | Float   | Não         |
| nota_pavam           | Float   | Não         |
| historico_importante | Boolean | Não         |
| historico_influente  | Boolean | Não         |

Os nomes das colunas definidos neste documento constituem o **contrato oficial dos dados** da Fase 1.

Todas as funções do backend deverão utilizar exatamente essa nomenclatura.

---

# Regras de Preenchimento

## id

* Número inteiro.
* Sequencial.
* Nunca repetir.
* Nunca reutilizar um identificador removido.

Exemplo:

```text
1
2
3
```

---

## nome

Utilizar sempre o nome oficial internacional do jogo.

Exemplos:

* Final Fantasy VII
* Resident Evil 4
* The Witcher 3: Wild Hunt

---

## ano_lancamento

Representa o ano de lançamento original.

Formato:

```text
YYYY
```

Exemplo:

```text
1998
```

---

## genero

Cada jogo deve possuir **apenas um gênero principal**.

Essa padronização simplifica agrupamentos, estatísticas e filtros.

### Gêneros permitidos

* RPG
* Action-Adventure
* Survival Horror
* First-Person Shooter
* Third-Person Shooter
* Stealth
* Platform
* Hack and Slash
* Open World
* Puzzle
* Adventure
* Fighting
* Racing

---

## developer

Representa a desenvolvedora responsável pelo jogo.

Sempre utilizar o **nome oficial atual da empresa**, mesmo que no lançamento ela possuísse outra denominação.

Exemplos:

* Square Enix
* Rockstar North
* Capcom
* Naughty Dog
* Remedy Entertainment
* FromSoftware

Essa padronização facilita agrupamentos e consultas.

---

## franchise

Representa a propriedade intelectual (IP) ou franquia oficial do jogo.

Sempre utilizar o nome oficial da franquia.

Quando um jogo não fizer parte de uma franquia consolidada, utilizar o próprio nome do jogo.

Exemplos:

| Jogo               | Franchise        |
| ------------------ | ---------------- |
| Final Fantasy VII  | Final Fantasy    |
| Resident Evil 4    | Resident Evil    |
| Grand Theft Auto V | Grand Theft Auto |
| Bloodborne         | Bloodborne       |
| Elden Ring         | Elden Ring       |
| Control            | Control          |

Essa abordagem elimina valores especiais e facilita filtros e estatísticas.

---

## descricao

Campo editorial produzido exclusivamente para o The AAA Archive.

Cada descrição deverá seguir o padrão:

1. Apresentação do jogo.
2. Breve sinopse.
3. Importância histórica.

Não utilizar textos copiados de outras fontes.

---

## metacritic

Representa a nota oficial do Metacritic.

Características:

* Número inteiro.
* Intervalo entre 0 e 100.

Durante a construção inicial do dataset este campo poderá permanecer vazio.

---

## nota_kadu

Avaliação pessoal do autor do projeto.

Escala:

```text
0.0 → 10.0
```

Utilizar uma casa decimal.

Exemplos:

```text
9.8
8.5
10.0
```

---

## nota_pavam

Avaliação pessoal do colaborador do projeto.

Escala:

```text
0.0 → 10.0
```

Caso ainda não exista avaliação, deixar o campo vazio.

---

## historico_importante

Indica se o jogo possui importância histórica reconhecida.

Valores permitidos:

* TRUE
* FALSE

---

## historico_influente

Indica se o jogo influenciou outros jogos ou gêneros.

Valores permitidos:

* TRUE
* FALSE

---

# Valores Nulos

Durante a construção inicial do dataset, alguns campos permanecerão vazios de forma intencional.

Isso faz parte da evolução incremental do projeto e não caracteriza inconsistência nos dados.

Os campos que poderão permanecer nulos são:

* descricao
* metacritic
* nota_kadu
* nota_pavam
* historico_importante
* historico_influente

Essas informações serão preenchidas gradualmente conforme o projeto evoluir.

---

# Uso dos Dados

As informações documentadas neste arquivo serão utilizadas por:

* Backend em Python;
* API;
* Website;
* Dashboard;
* Estudos e análises em Pandas.

Toda nova funcionalidade deverá utilizar esta estrutura como referência.

---

# Fontes Oficiais

## IGDB

Responsável por:

* Nome oficial
* Ano de lançamento
* Desenvolvedora
* Franquia
* Gênero

---

## Metacritic

Responsável por:

* Nota Metacritic

---

## Produção Editorial

Responsável por:

* Descrição
* Nota Kadu
* Nota Pavã
* Histórico Importante
* Histórico Influente

---

# Princípios de Modelagem

Durante todo o projeto serão adotados os seguintes princípios:

* Consistência acima da precisão histórica.
* Padronização acima da conveniência.
* Simplicidade acima da complexidade.
* Dados preparados para análise.
* Estrutura preparada para futura normalização em PostgreSQL.

---

# Versionamento

**Versão:** 1.1

Este documento representa a especificação oficial do dataset da **Fase 1** do The AAA Archive e serve como contrato de dados para todo o desenvolvimento do sistema.
