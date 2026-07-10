# Data Dictionary — The AAA Archive

# Objetivo

Este documento especifica oficialmente a estrutura dos dados da **Foundation Collection** do projeto **The AAA Archive**.

Ele define:

* colunas;
* tipos de dados;
* regras de preenchimento;
* valores permitidos;
* campos obrigatórios;
* campos opcionais;
* convenções editoriais;
* correspondência entre CSV e PostgreSQL.

A especificação se aplica a:

```text
data/games.csv
```

e à tabela:

```text
games
```

no PostgreSQL.

Este documento funciona como o **contrato oficial dos dados** da Foundation Collection.

Todos os módulos, testes, scripts de importação, consultas ao banco, endpoints da API, componentes do dashboard e futuras interfaces deverão respeitar essa estrutura enquanto ela permanecer vigente.

---

# Escopo

Este documento descreve exclusivamente os dados da:

```text
Foundation Collection
```

A Foundation Collection é a coleção editorial principal do The AAA Archive.

Os critérios de seleção e inclusão dos jogos são documentados em:

```text
docs/foundation_collection.md
```

A base de premiações possui uma estrutura independente, documentada em:

```text
docs/awards_dictionary.md
```

---

# Unidade dos Dados

Cada linha do arquivo `games.csv` representa:

```text
um jogo
```

Cada registro da tabela `games` também representa:

```text
um jogo
```

Cada coluna representa uma característica técnica, editorial ou classificatória desse jogo.

---

# Fontes e Representações

A Foundation Collection possui atualmente duas representações.

## Fonte Editorial

```text
data/games.csv
```

O CSV é utilizado para:

* edição manual;
* manutenção editorial;
* visualização simples;
* preservação da base original;
* importação para PostgreSQL;
* testes de módulos baseados em arquivos.

---

## Fonte Operacional

```text
PostgreSQL
└── public.games
```

A tabela `games` é utilizada por:

* API FastAPI;
* dashboard Streamlit;
* camada Python de banco;
* testes de integração;
* futura aplicação web.

---

# Fluxo Oficial dos Dados

```text
Editar games.csv
↓
Executar scripts/import_to_postgres.py
↓
Atualizar a tabela games
↓
Executar testes
↓
API e dashboard utilizam os novos dados
```

Enquanto esse modelo estiver vigente, o CSV será a fonte principal de edição e o PostgreSQL será a fonte operacional da aplicação.

Não se deve editar apenas o banco e esquecer de atualizar o CSV.

---

# Arquivos Relacionados

```text
data/games.csv
database/schema.sql
scripts/load_data.py
scripts/import_to_postgres.py
scripts/database.py
scripts/filters.py
scripts/search.py
scripts/site_statistics.py
scripts/test_database.py
api/main.py
dashboard/dashboard_helpers.py
```

---

# Estrutura do Dataset

| Coluna                 | Tipo no CSV/Pandas | Tipo no PostgreSQL | Obrigatório |
| ---------------------- | ------------------ | ------------------ | ----------- |
| `id`                   | Integer            | `INTEGER`          | Sim         |
| `nome`                 | String             | `VARCHAR(200)`     | Sim         |
| `ano_lancamento`       | Integer            | `INTEGER`          | Sim         |
| `genero`               | String             | `VARCHAR(100)`     | Sim         |
| `developer`            | String             | `VARCHAR(150)`     | Sim         |
| `franchise`            | String             | `VARCHAR(150)`     | Sim         |
| `descricao`            | Text/String        | `TEXT`             | Não         |
| `metacritic`           | Integer            | `INTEGER`          | Não         |
| `nota_kadu`            | Float              | `NUMERIC(3,1)`     | Não         |
| `nota_pavam`           | Float              | `NUMERIC(3,1)`     | Não         |
| `historico_importante` | Boolean            | `BOOLEAN`          | Não         |
| `historico_influente`  | Boolean            | `BOOLEAN`          | Não         |

Os nomes dessas colunas constituem o contrato atual da Foundation Collection.

O código deve utilizar exatamente essa nomenclatura enquanto o schema não for oficialmente alterado.

---

# Estrutura da Tabela PostgreSQL

```sql
CREATE TABLE IF NOT EXISTS games (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(200) NOT NULL,
    ano_lancamento INTEGER,
    genero VARCHAR(100),
    developer VARCHAR(150),
    franchise VARCHAR(150),
    descricao TEXT,
    metacritic INTEGER,
    nota_kadu NUMERIC(3, 1),
    nota_pavam NUMERIC(3, 1),
    historico_importante BOOLEAN,
    historico_influente BOOLEAN
);
```

A estrutura oficial também deve permanecer registrada em:

```text
database/schema.sql
```

Qualquer mudança futura nas colunas deverá ser refletida em:

* `games.csv`;
* `schema.sql`;
* script de importação;
* camada de banco;
* módulos dependentes;
* testes;
* API;
* dashboard;
* documentação.

---

# Regras Gerais

* Cada jogo deve possuir um `id` único.
* Cada linha deve representar somente um jogo.
* Os nomes das colunas não devem ser alterados sem planejamento.
* Os tipos de dados devem seguir esta especificação.
* Os dados devem ser padronizados.
* Valores opcionais podem permanecer vazios.
* Novos jogos devem ser adicionados de forma incremental.
* A entrada de um jogo depende dos critérios editoriais da Foundation Collection.
* Alterações relevantes devem ser testadas antes de serem consideradas concluídas.

---

# Regras de Preenchimento

# `id`

Identificador único do jogo.

## Tipo

```text
Integer
```

## Regras

* obrigatório;
* número inteiro;
* único;
* não pode se repetir;
* deve permanecer estável;
* não deve ser alterado apenas para reorganizar a ordem do CSV;
* não deve ser reutilizado para representar outro jogo.

Exemplo:

```text
1
2
3
```

O campo é utilizado como chave primária na tabela `games`.

```sql
id INTEGER PRIMARY KEY
```

---

# `nome`

Nome oficial do jogo.

## Tipo

```text
String
```

## Regras

* obrigatório;
* utilizar o nome oficial internacional;
* preservar subtítulos;
* preservar algarismos romanos quando fizerem parte do título;
* evitar abreviações informais;
* utilizar grafia consistente em todas as bases.

Exemplos:

```text
Final Fantasy VII
Resident Evil 4
The Witcher 3: Wild Hunt
Red Dead Redemption 2
```

O campo `nome` também é utilizado na comparação com:

```text
awards.jogo
```

Por isso, diferenças de grafia podem impedir que um jogo seja reconhecido como presente nas duas bases.

---

# `ano_lancamento`

Ano do lançamento original do jogo.

## Tipo

```text
Integer
```

## Formato

```text
YYYY
```

Exemplos:

```text
1998
2005
2018
```

## Regras

* utilizar o ano do lançamento original;
* não utilizar o ano de remasterizações;
* não utilizar o ano de relançamentos;
* não utilizar datas completas nesta coluna;
* manter somente números inteiros.

Esse campo é utilizado em:

* filtros por ano;
* filtros por década;
* linhas do tempo;
* estatísticas históricas;
* gráficos.

---

# `genero`

Gênero principal do jogo.

## Tipo

```text
String
```

## Regra Principal

Cada jogo deve possuir apenas:

```text
um gênero principal
```

A escolha de um único gênero simplifica:

* filtros;
* agrupamentos;
* gráficos;
* estatísticas;
* comparação entre registros.

## Gêneros previstos

```text
RPG
Action-Adventure
Survival Horror
First-Person Shooter
Third-Person Shooter
Stealth
Platform
Hack and Slash
Open World
Puzzle
Adventure
Fighting
Racing
```

A lista pode evoluir quando um novo jogo exigir uma classificação ainda não contemplada.

Novos gêneros devem ser adicionados com padronização e sem criar variações equivalentes.

Exemplo de inconsistência a evitar:

```text
Action Adventure
Action-Adventure
Action adventure
```

O padrão atual utiliza:

```text
Action-Adventure
```

---

# `developer`

Desenvolvedora principal responsável pelo jogo.

## Tipo

```text
String
```

## Regras

* utilizar um nome padronizado;
* manter a mesma grafia em todos os registros da empresa;
* evitar abreviações não oficiais;
* evitar variações de maiúsculas e minúsculas;
* registrar apenas a desenvolvedora principal nesta versão do dataset.

Exemplos:

```text
Square Enix
Rockstar North
Capcom
Naughty Dog
Remedy Entertainment
FromSoftware
```

## Observação sobre nomes históricos

A regra atual prioriza consistência para filtros e agrupamentos.

Quando uma empresa tiver mudado de nome, deve-se escolher uma única forma padronizada para o dataset e documentar exceções relevantes.

Essa decisão poderá ser revisada futuramente caso o banco seja normalizado e passe a armazenar nomes históricos separadamente.

---

# `franchise`

Franquia ou propriedade intelectual à qual o jogo pertence.

## Tipo

```text
String
```

## Regras

* utilizar o nome oficial da franquia;
* manter grafia consistente;
* não utilizar valores como `Sem franquia`, `N/A` ou `None`;
* quando o jogo não pertencer a uma franquia consolidada, utilizar o próprio nome do jogo.

Exemplos:

| Jogo               | Franchise        |
| ------------------ | ---------------- |
| Final Fantasy VII  | Final Fantasy    |
| Resident Evil 4    | Resident Evil    |
| Grand Theft Auto V | Grand Theft Auto |
| Bloodborne         | Bloodborne       |
| Elden Ring         | Elden Ring       |
| Control            | Control          |

Essa abordagem permite:

* filtros sem valores especiais;
* contagem de franquias;
* agrupamentos;
* identificação de títulos independentes dentro da coleção.

---

# `descricao`

Descrição editorial do jogo.

## Tipo

```text
Text
```

## Obrigatório

```text
Não
```

## Origem

Conteúdo produzido especificamente para o The AAA Archive.

Não utilizar textos integralmente copiados de:

* lojas;
* Wikipédia;
* páginas de publishers;
* sites jornalísticos;
* bancos de dados externos.

## Estrutura recomendada

A descrição poderá conter:

1. apresentação do jogo;
2. premissa ou sinopse breve;
3. características principais;
4. importância histórica;
5. relação com a proposta da Foundation Collection.

## Diretrizes

* priorizar clareza;
* evitar spoilers importantes;
* diferenciar fatos de opinião;
* manter identidade editorial;
* evitar texto promocional;
* não transformar a descrição em uma análise excessivamente longa.

Esse campo poderá ser utilizado futuramente em:

* páginas individuais;
* cards;
* buscas;
* destaques editoriais;
* metadados da aplicação.

---

# `metacritic`

Nota registrada no Metacritic.

## Tipo

```text
Integer
```

## Intervalo

```text
0 a 100
```

## Obrigatório

```text
Não
```

## Regras

* utilizar valor inteiro;
* registrar a versão principal ou uma plataforma de referência definida;
* manter o campo vazio quando não houver confirmação;
* não inventar valores;
* revisar a fonte antes do preenchimento.

Como diferentes plataformas podem possuir notas diferentes, a metodologia de escolha deverá ser documentada antes do preenchimento completo da coluna.

Até essa definição, valores podem permanecer nulos.

---

# `nota_kadu`

Avaliação pessoal de Kadu.

## Tipo

```text
Float
```

No PostgreSQL:

```text
NUMERIC(3,1)
```

## Intervalo

```text
0.0 a 10.0
```

## Regras

* utilizar no máximo uma casa decimal;
* manter vazio quando ainda não houver avaliação;
* registrar opinião pessoal;
* não confundir com nota crítica;
* não preencher apenas para completar o dataset.

Exemplos:

```text
8.5
9.8
10.0
```

Esse campo representa avaliação editorial pessoal e não um dado objetivo.

---

# `nota_pavam`

Avaliação pessoal do colaborador Pavam.

## Tipo

```text
Float
```

No PostgreSQL:

```text
NUMERIC(3,1)
```

## Intervalo

```text
0.0 a 10.0
```

## Regras

* utilizar no máximo uma casa decimal;
* deixar vazio quando não houver avaliação;
* não presumir uma nota;
* não copiar automaticamente a nota de Kadu;
* manter a autoria da avaliação clara.

---

# `historico_importante`

Indica se o jogo é considerado historicamente importante dentro da proposta editorial.

## Tipo

```text
Boolean
```

## Valores permitidos

```text
TRUE
FALSE
```

Também pode permanecer vazio enquanto a classificação ainda não tiver sido definida.

## Interpretação

Um jogo historicamente importante pode representar:

* um marco da indústria;
* uma mudança tecnológica;
* um momento cultural relevante;
* um título central para determinado período;
* uma obra decisiva para uma franquia;
* uma contribuição relevante para o desenvolvimento dos videogames.

O campo não deve ser marcado apenas porque o jogo é popular ou bem avaliado.

---

# `historico_influente`

Indica se o jogo influenciou diretamente outros jogos, gêneros, mecânicas, estruturas ou tendências da indústria.

## Tipo

```text
Boolean
```

## Valores permitidos

```text
TRUE
FALSE
```

Também pode permanecer vazio enquanto a classificação estiver pendente.

## Interpretação

Um jogo historicamente influente pode:

* estabelecer uma estrutura copiada posteriormente;
* redefinir um gênero;
* popularizar uma mecânica;
* influenciar design de níveis;
* influenciar narrativa;
* influenciar sistemas;
* servir como referência para outros estúdios.

Um jogo pode ser:

* importante e influente;
* importante, mas não fortemente influente;
* influente, mas não necessariamente central culturalmente;
* nenhum dos dois segundo a classificação atual.

---

# Valores Nulos

Alguns campos podem permanecer vazios de forma intencional.

Campos opcionais:

```text
descricao
metacritic
nota_kadu
nota_pavam
historico_importante
historico_influente
```

A presença de valores nulos nesses campos não representa, por si só, erro ou corrupção.

Ela pode indicar:

* conteúdo editorial ainda não produzido;
* avaliação ainda não realizada;
* dado ainda não verificado;
* classificação histórica ainda não definida;
* preenchimento previsto para uma etapa futura.

---

# Representação dos Valores Nulos

## No CSV

O campo deve permanecer vazio.

Exemplo conceitual:

```csv
1,Final Fantasy VII,1997,RPG,Square Enix,Final Fantasy,,,,,,
```

Não utilizar valores como:

```text
N/A
None
null
desconhecido
-
```

salvo se uma regra futura definir o contrário.

---

## No Pandas

Campos vazios podem ser interpretados como:

```text
NaN
```

ou valores nulos equivalentes, dependendo do tipo da coluna.

---

## No PostgreSQL

Campos vazios devem ser importados como:

```text
NULL
```

O script de importação é responsável por converter corretamente valores ausentes.

---

# Validações Esperadas

O dataset deve respeitar as seguintes validações:

* `id` não pode se repetir;
* `nome` não deve estar vazio;
* `ano_lancamento` deve ser inteiro;
* `genero` deve seguir a padronização;
* `developer` deve possuir grafia consistente;
* `franchise` não deve estar vazia;
* `metacritic` deve estar entre 0 e 100;
* notas pessoais devem estar entre 0.0 e 10.0;
* campos históricos devem aceitar booleanos ou nulos;
* as colunas devem permanecer na estrutura esperada.

---

# Exemplo de Registro

```csv
id,nome,ano_lancamento,genero,developer,franchise,descricao,metacritic,nota_kadu,nota_pavam,historico_importante,historico_influente
1,Final Fantasy VII,1997,RPG,Square Enix,Final Fantasy,Descrição editorial do jogo,92,10.0,9.0,TRUE,TRUE
```

Esse exemplo é apenas estrutural.

Valores reais devem ser confirmados antes de serem inseridos no dataset oficial.

---

# Uso dos Dados

Os dados são utilizados por:

* scripts Python;
* Pandas;
* filtros;
* pesquisa textual;
* estatísticas;
* PostgreSQL;
* API FastAPI;
* dashboard Streamlit;
* testes;
* futura aplicação web;
* futuras análises editoriais.

---

# Relação com os Módulos

## `load_data.py`

Carrega o arquivo:

```text
data/games.csv
```

e retorna um DataFrame.

---

## `import_to_postgres.py`

Importa os dados do CSV para a tabela:

```text
games
```

---

## `database.py`

Carrega os registros da tabela `games` e os retorna como DataFrame.

---

## `filters.py`

Utiliza campos como:

```text
developer
genero
franchise
ano_lancamento
```

---

## `search.py`

Pode utilizar:

```text
nome
genero
developer
franchise
descricao
```

---

## `site_statistics.py`

Utiliza os dados para calcular:

* quantidade de jogos;
* quantidade de gêneros;
* quantidade de desenvolvedoras;
* quantidade de franquias;
* distribuição por década;
* jogos importantes;
* jogos influentes.

---

## API

A API disponibiliza os registros e consultas da Foundation Collection em JSON.

---

## Dashboard

O dashboard utiliza os registros para criar:

* métricas;
* filtros;
* gráficos;
* tabelas;
* recortes editoriais.

---

# Fontes dos Dados

Sempre que possível, dados factuais devem ser obtidos de fontes oficiais ou verificáveis.

## Informações Técnicas

Podem ser consultadas em:

* páginas oficiais dos jogos;
* páginas das desenvolvedoras;
* páginas das publishers;
* IGDB;
* Metacritic;
* bases reconhecidas da indústria;
* veículos especializados confiáveis.

---

## Metacritic

Responsável por:

```text
metacritic
```

A metodologia de escolha entre plataformas deverá ser definida antes do preenchimento completo.

---

## Produção Editorial

Responsável por:

```text
descricao
nota_kadu
nota_pavam
historico_importante
historico_influente
```

Esses campos representam a identidade editorial do Archive.

---

# Princípios de Modelagem

Durante a manutenção dos dados, devem ser seguidos os princípios:

* consistência acima de variações desnecessárias;
* padronização acima da conveniência;
* simplicidade enquanto for suficiente;
* dados preparados para análise;
* separação entre fatos e opinião;
* edição editorial centralizada;
* compatibilidade entre CSV e PostgreSQL;
* documentação alinhada ao schema;
* mudanças estruturais somente após planejamento.

---

# Alterações na Estrutura

Não adicionar, remover ou renomear colunas sem revisar o impacto.

Antes de uma alteração estrutural:

```text
1. Definir a necessidade.
2. Atualizar este dicionário.
3. Atualizar games.csv.
4. Atualizar database/schema.sql.
5. Atualizar import_to_postgres.py.
6. Atualizar database.py, se necessário.
7. Atualizar módulos dependentes.
8. Atualizar testes.
9. Atualizar API e dashboard.
10. Importar novamente.
11. Validar os dados.
12. Registrar a mudança em commit.
```

---

# Normalização Futura

A tabela `games` ainda possui valores como gênero, desenvolvedora e franquia armazenados diretamente no registro do jogo.

Futuramente, poderão ser avaliadas tabelas como:

```text
developers
franchises
genres
platforms
```

Essa normalização não é necessária na fase atual.

Ela só deverá acontecer quando trouxer benefício real para:

* consultas;
* manutenção;
* consistência;
* expansão da aplicação;
* relacionamento entre entidades.

---

# Campos Futuros Possíveis

Campos que poderão ser avaliados em outra fase:

```text
publisher
director
data_lancamento
plataformas
capa_url
background_url
texto_historico
justificativa_inclusao
slug
```

Esses campos não fazem parte do contrato atual.

Eles não devem ser adicionados apenas porque podem ser úteis no futuro.

---

# Estado Atual dos Dados

A Foundation Collection possui atualmente:

```text
66 jogos
```

Os campos estruturais principais estão preenchidos.

Os campos editoriais e avaliativos ainda podem permanecer vazios:

```text
descricao
metacritic
nota_kadu
nota_pavam
historico_importante
historico_influente
```

O preenchimento será realizado gradualmente.

---

# Versionamento

**Versão:** 2.0

Esta versão atualiza o documento para representar:

* o CSV editorial;
* a tabela `games`;
* a integração com PostgreSQL;
* o fluxo atual de importação;
* o uso pela API;
* o uso pelo dashboard;
* as regras de segurança e manutenção dos dados.

---

# Status do Documento

```text
Contrato de dados atual da Foundation Collection
```

Este documento deve ser revisado sempre que houver mudança estrutural nos dados.
