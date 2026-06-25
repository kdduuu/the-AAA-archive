# Awards Dictionary — The AAA Archive

# Objetivo

Este documento especifica oficialmente a estrutura do arquivo **`awards.csv`**, utilizado para registrar o histórico de premiações relacionadas à categoria **Game of the Year** dentro do projeto **The AAA Archive**.

O objetivo desta base é preservar uma linha histórica de vencedores e indicados ao prêmio de Jogo do Ano, considerando diferentes fases da premiação.

---

# Escopo

Esta base é independente da **Foundation Collection**.

Isso significa que:

* um jogo pode estar na Foundation Collection sem ter sido indicado ao Game of the Year;
* um jogo pode estar em `awards.csv` sem fazer parte da Foundation Collection;
* futuramente, as duas bases poderão ser relacionadas pelo nome do jogo.

---

# Premiações Consideradas

A primeira versão da base considera o histórico da categoria Game of the Year nas seguintes premiações:

* Spike Video Game Awards
* VGX
* The Game Awards

Essas premiações representam fases diferentes da história dos eventos de premiação da indústria dos videogames.

---

# Arquivo Principal

```text
data/
└── awards.csv
```

---

# Estrutura do Dataset

| Coluna    | Tipo    | Obrigatório |
| --------- | ------- | ----------- |
| ano       | Integer | Sim         |
| premiacao | String  | Sim         |
| jogo      | String  | Sim         |
| status    | String  | Sim         |

Os nomes das colunas definidos neste documento constituem o contrato oficial da base de premiações.

Todas as funções do módulo `awards.py` deverão utilizar exatamente essa nomenclatura.

---

# Regras de Preenchimento

## ano

Representa o ano da edição da premiação.

Formato:

```text
YYYY
```

Exemplo:

```text
2018
```

---

## premiacao

Representa o nome da premiação responsável pela indicação ou vitória daquele jogo.

Valores permitidos:

* Spike Video Game Awards
* VGX
* The Game Awards

---

## jogo

Representa o nome do jogo indicado ou vencedor.

Sempre que possível, utilizar o nome oficial internacional do jogo.

Exemplos:

* Resident Evil 4
* Grand Theft Auto V
* The Last of Us
* God of War
* Baldur's Gate 3

---

## status

Indica se o jogo venceu ou foi indicado à categoria Game of the Year naquele ano.

Valores permitidos:

* Vencedor
* Indicado

Cada ano deve possuir apenas um jogo marcado como **Vencedor**.

Os demais jogos daquele ano devem ser marcados como **Indicado**.

---

# Exemplo de Estrutura

```csv
ano,premiacao,jogo,status
2018,The Game Awards,God of War,Vencedor
2018,The Game Awards,Red Dead Redemption 2,Indicado
2018,The Game Awards,Marvel's Spider-Man,Indicado
```

---

# Relação com a Foundation Collection

A base `awards.csv` não substitui nem altera o arquivo `games.csv`.

O relacionamento futuro entre as duas bases poderá ser feito comparando:

```text
awards.csv → jogo
games.csv  → nome
```

Esse cruzamento permitirá identificar:

* vencedores presentes na Foundation Collection;
* indicados presentes na Foundation Collection;
* jogos premiados que ainda não fazem parte da coleção principal.

---

# Uso dos Dados

As informações documentadas neste arquivo serão utilizadas por:

* módulo `awards.py`;
* seção Awards do website;
* API;
* Dashboard;
* análises históricas da premiação.

---

# Princípios de Modelagem

Durante o desenvolvimento desta base serão adotados os seguintes princípios:

* Simplicidade acima da complexidade.
* Separação entre coleção editorial e histórico de premiações.
* Dados preparados para análise.
* Estrutura pronta para futura integração com PostgreSQL.
* Evolução incremental.

---

# Status

**Versão:** 1.0

Este documento representa a especificação oficial da base de premiações do The AAA Archive.
