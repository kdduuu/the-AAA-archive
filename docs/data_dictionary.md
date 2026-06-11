# Data Dictionary - The AAA Archive

## Objetivo

Este documento define oficialmente a estrutura dos dados utilizados pelo projeto **The AAA Archive**.

Seu objetivo é garantir consistência durante todas as fases do desenvolvimento, servindo como referência para a criação do dataset, análises em Pandas e futura migração para PostgreSQL.

---

# Unidade do Dataset

Cada linha do dataset representa **um jogo**.

Cada coluna representa **uma característica desse jogo**.

---

# Estratégia de Desenvolvimento

## Fase 1

* Dataset em CSV
* Arquivo único (`games.csv`)
* Estudos com Pandas
* Limpeza e exploração dos dados

## Fase 2

* Migração para PostgreSQL
* Normalização do banco de dados
* Separação em múltiplas tabelas
* Integração com Streamlit

---

# Escopo Editorial

O The AAA Archive não possui como objetivo catalogar todos os jogos já produzidos.

O projeto consiste em uma coleção editorial dedicada aos jogos AAA Single Player considerados relevantes para a evolução da indústria dos videogames.

A coleção inicial recebe o nome de **Foundation Collection**.

Novos títulos poderão ser adicionados futuramente através das **Expansion Collections**, sem alterar a composição da Foundation Collection.

---

# Critérios de Inclusão

Um jogo poderá fazer parte da coleção caso atenda a um ou mais dos critérios abaixo:

* Ser um jogo AAA.
* Possuir foco principal em Single Player.
* Ter relevância histórica para a indústria.
* Ter influenciado outros jogos ou gêneros.
* Possuir reconhecimento crítico significativo.
* Fazer parte da proposta editorial do projeto.

---

# Regras Gerais

* Cada jogo possui um identificador único (`id`).
* Os dados devem seguir rigorosamente os padrões definidos neste documento.
* O dataset será expandido de forma incremental.
* Sempre que possível, os dados devem ser padronizados para facilitar análises futuras.

---

# Arquivo Principal

```
games.csv
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

---

# Regras de Preenchimento

## id

* Número inteiro.
* Sequencial.
* Nunca repetir.
* Nunca reutilizar um identificador removido.

Exemplo:

```
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

```
YYYY
```

Exemplo:

```
1998
```

---

## genero

Cada jogo deve possuir **apenas um gênero principal**.

O objetivo é manter consistência durante as análises.

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

Essa padronização facilita agrupamentos, estatísticas e futuras consultas.

---

## franchise

Representa a propriedade intelectual (IP) ou franquia oficial do jogo.

Sempre utilizar o nome oficial da franquia.

Caso o jogo não pertença a uma franquia:

```
Original
```

Exemplos:

| Jogo               | Franchise        |
| ------------------ | ---------------- |
| Final Fantasy VII  | Final Fantasy    |
| Resident Evil 4    | Resident Evil    |
| Grand Theft Auto V | Grand Theft Auto |
| Bloodborne         | Bloodborne       |
| Elden Ring         | Elden Ring       |
| Control            | Control          |

---

## descricao

Campo editorial produzido exclusivamente para o projeto.

As descrições deverão seguir sempre o mesmo padrão:

1. Apresentação do jogo.
2. Breve sinopse.
3. Importância histórica.

Não utilizar textos copiados de outras fontes.

---

## metacritic

Representa a nota oficial do Metacritic.

Características:

* Número inteiro.
* Intervalo de 0 a 100.

Durante a construção inicial do dataset este campo poderá permanecer vazio.

---

## nota_kadu

Avaliação pessoal do autor do projeto.

Escala:

```
0.0 → 10.0
```

Utilizar uma casa decimal.

Exemplos:

```
9.8
8.5
10.0
```

---

## nota_pavam

Avaliação pessoal do colaborador do projeto.

Escala:

```
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

Os seguintes campos poderão permanecer vazios durante a construção inicial do dataset:

* descricao
* metacritic
* nota_kadu
* nota_pavam
* historico_importante
* historico_influente

Esses dados serão preenchidos gradualmente conforme o projeto evoluir.

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

* Consistência acima de precisão histórica.
* Padronização acima de conveniência.
* Simplicidade acima de complexidade.
* Dados preparados para análise.
* Estrutura preparada para futura normalização em PostgreSQL.

---

# Versionamento

**Versão:** 1.0

Este documento representa a especificação oficial do dataset da Fase 1 do The AAA Archive.
