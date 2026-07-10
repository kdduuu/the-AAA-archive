# Awards Dictionary — The AAA Archive

# Objetivo

Este documento especifica oficialmente a estrutura dos dados da **Awards History** do projeto **The AAA Archive**.

A base registra o histórico de vencedores e indicados à categoria **Game of the Year**, considerando diferentes fases das principais premiações da indústria dos videogames.

A especificação se aplica a:

```text
data/awards.csv
```

e à tabela:

```text
awards
```

no PostgreSQL.

Este documento funciona como o contrato oficial dos dados da Awards History.

Todas as funções, testes, scripts de importação, consultas ao banco, endpoints da API, componentes do dashboard e futuras interfaces deverão respeitar essa estrutura enquanto ela permanecer vigente.

---

# Escopo

A Awards History é independente da:

```text
Foundation Collection
```

Isso significa que:

* um jogo pode estar na Foundation Collection sem ter sido indicado a Game of the Year;
* um jogo pode estar na Awards History sem fazer parte da Foundation Collection;
* um jogo pode estar presente nas duas bases;
* vencer ou ser indicado não garante entrada automática na Foundation Collection;
* a Awards History não substitui a curadoria editorial do projeto.

As duas bases podem ser comparadas pelos nomes dos jogos.

---

# Objetivo Editorial

A Awards History busca preservar:

* vencedores;
* indicados;
* ano da edição;
* nome da premiação;
* mudanças históricas entre diferentes fases do evento;
* relação entre reconhecimento institucional e curadoria editorial.

A base não pretende representar todas as premiações da indústria.

O recorte atual está concentrado na categoria Game of the Year.

---

# Premiações Consideradas

A versão atual considera as seguintes premiações:

```text
Spike Video Game Awards
VGX
The Game Awards
```

Esses nomes representam fases diferentes da história das premiações.

A grafia deve permanecer padronizada exatamente dessa forma enquanto o contrato atual estiver vigente.

---

# Unidade dos Dados

Cada linha do arquivo `awards.csv` representa:

```text
um jogo em uma edição específica da premiação
```

Cada registro pode representar:

* um vencedor;
* um indicado.

Cada edição deve possuir apenas um registro marcado como vencedor.

---

# Fontes e Representações

A Awards History possui duas representações.

## Fonte Editorial

```text
data/awards.csv
```

O CSV é utilizado para:

* edição manual;
* manutenção histórica;
* conferência simples;
* preservação da base original;
* importação para PostgreSQL;
* testes baseados em arquivos.

---

## Fonte Operacional

```text
PostgreSQL
└── public.awards
```

A tabela `awards` é utilizada por:

* API FastAPI;
* dashboard Streamlit;
* camada Python de banco;
* testes de integração;
* futura aplicação web.

---

# Fluxo Oficial dos Dados

```text
Editar awards.csv
↓
Executar scripts/import_to_postgres.py
↓
Atualizar a tabela awards
↓
Executar testes
↓
API e dashboard utilizam os novos dados
```

Enquanto esse modelo estiver vigente, o CSV será a fonte principal de edição e o PostgreSQL será a fonte operacional.

---

# Arquivos Relacionados

```text
data/awards.csv
database/schema.sql
scripts/load_data.py
scripts/import_to_postgres.py
scripts/database.py
scripts/awards.py
scripts/test_awards.py
scripts/test_database.py
api/main.py
api/test_main.py
dashboard/dashboard_helpers.py
dashboard/app.py
```

---

# Estrutura do Dataset

## Estrutura no CSV

| Coluna      | Tipo no CSV/Pandas | Obrigatório |
| ----------- | ------------------ | ----------- |
| `ano`       | Integer            | Sim         |
| `premiacao` | String             | Sim         |
| `jogo`      | String             | Sim         |
| `status`    | String             | Sim         |

---

## Estrutura no PostgreSQL

| Coluna      | Tipo no PostgreSQL | Obrigatório |
| ----------- | ------------------ | ----------- |
| `id`        | `SERIAL`           | Sim         |
| `ano`       | `INTEGER`          | Sim         |
| `premiacao` | `VARCHAR(150)`     | Sim         |
| `jogo`      | `VARCHAR(200)`     | Sim         |
| `status`    | `VARCHAR(50)`      | Sim         |

O campo `id` existe apenas no PostgreSQL.

Ele é criado automaticamente durante a inserção dos registros.

---

# Estrutura da Tabela PostgreSQL

```sql
CREATE TABLE IF NOT EXISTS awards (
    id SERIAL PRIMARY KEY,
    ano INTEGER,
    premiacao VARCHAR(150),
    jogo VARCHAR(200),
    status VARCHAR(50)
);
```

A estrutura oficial também deve permanecer registrada em:

```text
database/schema.sql
```

---

# Regras Gerais

* Cada linha representa um jogo em uma edição.
* Cada registro deve possuir ano, premiação, jogo e status.
* Cada edição deve possuir apenas um vencedor.
* Os demais jogos da edição devem ser indicados.
* Os nomes das premiações devem ser padronizados.
* Os nomes dos jogos devem ser consistentes.
* Não devem existir registros duplicados.
* Alterações devem preservar a relação com a Foundation Collection.
* Os nomes das colunas não devem ser alterados sem planejamento.

---

# Regras de Preenchimento

# `id`

Identificador automático do registro no PostgreSQL.

## Tipo

```text
SERIAL
```

## Regras

* não existe no CSV;
* é gerado automaticamente pelo banco;
* funciona como chave primária;
* não possui significado editorial;
* não deve ser preenchido manualmente no arquivo CSV.

Exemplo:

```text
1
2
3
```

---

# `ano`

Ano da edição da premiação.

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
2003
2013
2018
2023
```

## Regras

* obrigatório;
* deve conter somente o ano;
* não utilizar data completa;
* deve representar o ano oficial da edição;
* todos os registros da mesma edição devem possuir o mesmo valor.

Esse campo é utilizado para:

* consulta por edição;
* ordenação histórica;
* linha do tempo;
* filtros;
* agrupamentos;
* histórico de vencedores.

---

# `premiacao`

Nome da premiação responsável pela indicação ou vitória.

## Tipo

```text
String
```

## Valores Permitidos

```text
Spike Video Game Awards
VGX
The Game Awards
```

## Regras

* obrigatório;
* utilizar exatamente a grafia oficial padronizada;
* todos os registros do mesmo ano devem possuir a premiação correspondente;
* não criar abreviações como `TGA` ou `VGA` dentro do dataset;
* mudanças históricas de nome devem ser preservadas.

Exemplos incorretos:

```text
The Games Awards
Game Awards
TGA
Spike VGA
```

Exemplos corretos:

```text
Spike Video Game Awards
VGX
The Game Awards
```

---

# `jogo`

Nome oficial internacional do jogo indicado ou vencedor.

## Tipo

```text
String
```

## Regras

* obrigatório;
* utilizar nome oficial;
* preservar subtítulos;
* manter grafia consistente;
* evitar abreviações;
* evitar diferenças desnecessárias em pontuação;
* tentar manter compatibilidade com `games.nome`.

Exemplos:

```text
Resident Evil 4
Grand Theft Auto V
The Last of Us
God of War
Baldur's Gate 3
```

A consistência deste campo é importante porque ele é utilizado na comparação com:

```text
games.nome
```

Diferenças de grafia podem impedir o reconhecimento entre as bases.

---

# `status`

Situação do jogo naquela edição.

## Tipo

```text
String
```

## Valores Permitidos

```text
Vencedor
Indicado
```

## Regras

* obrigatório;
* cada edição deve possuir exatamente um vencedor;
* todos os demais registros devem ser indicados;
* não utilizar variações como `Winner`, `Nominee`, `Ganhador` ou `Finalista`;
* preservar a capitalização definida.

Exemplo correto:

```text
Vencedor
Indicado
```

---

# Regra de Integridade por Edição

Cada combinação de:

```text
ano + premiacao
```

deve possuir:

```text
1 Vencedor
1 ou mais Indicados
```

Exemplo:

```csv
ano,premiacao,jogo,status
2018,The Game Awards,God of War,Vencedor
2018,The Game Awards,Red Dead Redemption 2,Indicado
2018,The Game Awards,Marvel's Spider-Man,Indicado
```

Uma edição com dois vencedores seria considerada inconsistente, salvo se uma premiação oficial tiver registrado empate e essa exceção for documentada.

---

# Duplicatas

Não deve existir mais de um registro com a mesma combinação:

```text
ano
premiacao
jogo
status
```

Também não deve existir o mesmo jogo repetido duas vezes na mesma edição.

Exemplo incorreto:

```csv
2018,The Game Awards,God of War,Vencedor
2018,The Game Awards,God of War,Vencedor
```

---

# Valores Nulos

Na versão atual, todos os campos editoriais do CSV são obrigatórios:

```text
ano
premiacao
jogo
status
```

Não devem existir linhas com campos vazios.

O campo `id` é gerado automaticamente pelo PostgreSQL.

---

# Exemplo Completo

```csv
ano,premiacao,jogo,status
2018,The Game Awards,God of War,Vencedor
2018,The Game Awards,Red Dead Redemption 2,Indicado
2018,The Game Awards,Marvel's Spider-Man,Indicado
2018,The Game Awards,Assassin's Creed Odyssey,Indicado
2018,The Game Awards,Monster Hunter: World,Indicado
2018,The Game Awards,Celeste,Indicado
```

---

# Relação com a Foundation Collection

A Awards History não substitui nem modifica diretamente:

```text
data/games.csv
```

As bases são relacionadas por:

```text
awards.jogo
games.nome
```

ou, na representação original:

```text
awards.csv → jogo
games.csv  → nome
```

Esse cruzamento permite identificar:

* vencedores presentes na Foundation Collection;
* indicados presentes na Foundation Collection;
* vencedores fora da coleção;
* indicados fora da coleção;
* jogos reconhecidos institucionalmente;
* diferenças entre premiação e curadoria.

---

# Regras de Comparação

Para que a comparação funcione corretamente:

* nomes devem possuir grafia equivalente;
* subtítulos devem ser preservados;
* apóstrofos devem ser consistentes;
* algarismos romanos e números devem seguir o título oficial;
* remakes devem ser diferenciados quando necessário;
* edições especiais não devem substituir o título principal sem justificativa.

Exemplo de possível inconsistência:

```text
Marvel's Spider-Man
Marvel’s Spider-Man
```

Apesar de visualmente semelhantes, apóstrofos diferentes podem afetar comparações exatas.

Quando necessário, a lógica de comparação pode normalizar:

* maiúsculas e minúsculas;
* espaços;
* acentos;
* sinais de pontuação.

Ainda assim, o dataset deve permanecer o mais consistente possível.

---

# Uso dos Dados

Os dados são utilizados por:

* `scripts/awards.py`;
* Pandas;
* PostgreSQL;
* API FastAPI;
* dashboard Streamlit;
* testes;
* análises históricas;
* futura seção Awards da aplicação web.

---

# Relação com os Módulos

## `load_data.py`

Carrega:

```text
data/awards.csv
```

e retorna os dados como DataFrame.

---

## `import_to_postgres.py`

Importa os registros para:

```text
public.awards
```

---

## `database.py`

Carrega os registros da tabela `awards`.

---

## `awards.py`

Responsável por consultas como:

```python
listar_premiacoes()
listar_anos_disponiveis()
listar_jogos_por_ano()
buscar_vencedor_por_ano()
listar_indicados_por_ano()
listar_vencedores()
listar_jogos_por_premiacao()
listar_vencedores_na_foundation()
listar_indicados_na_foundation()
listar_jogos_awards_fora_da_foundation()
```

---

# Uso na API

Endpoints relacionados:

```text
GET /awards
GET /awards/winners
GET /awards/{year}
GET /awards/foundation/winners
GET /awards/foundation/nominees
GET /awards/foundation/outside
```

---

# Uso no Dashboard

A aba Awards History utiliza os dados para apresentar:

* quantidade de registros;
* quantidade de anos;
* quantidade de vencedores;
* consulta por ano;
* vencedor da edição;
* indicados;
* histórico de vencedores;
* jogos presentes na Foundation Collection;
* jogos fora da Foundation Collection.

---

# Validações Esperadas

A base deve respeitar:

* ano inteiro;
* premiação válida;
* nome do jogo preenchido;
* status válido;
* apenas um vencedor por edição;
* ausência de registros duplicados;
* compatibilidade de nomes com a Foundation Collection;
* quantidade de registros esperada após importação.

---

# Testes Relacionados

Arquivos:

```text
scripts/test_awards.py
scripts/test_database.py
api/test_main.py
```

Os testes podem verificar:

* premiações disponíveis;
* anos disponíveis;
* vencedor por ano;
* indicados por ano;
* quantidade de vencedores;
* comparação com Foundation Collection;
* registros fora da coleção;
* quantidade na tabela PostgreSQL;
* funcionamento dos endpoints.

---

# Quantidade Atual

A base possui atualmente:

```text
127 registros
```

A quantidade deve ser atualizada quando novos anos ou registros forem adicionados.

Testes que esperam valores fixos também deverão ser revisados.

---

# Fontes dos Dados

Sempre que possível, utilizar fontes oficiais ou verificáveis.

Fontes recomendadas:

* páginas oficiais das premiações;
* arquivos históricos oficiais;
* The Game Awards;
* registros públicos da Spike;
* veículos jornalísticos reconhecidos;
* páginas especializadas confiáveis.

Quando fontes divergirem, a decisão adotada deve ser documentada.

---

# Princípios de Modelagem

Durante a manutenção da Awards History, seguir:

* simplicidade acima de complexidade;
* consistência entre edições;
* separação entre premiação e curadoria;
* dados preparados para análise;
* padronização de nomes;
* compatibilidade entre CSV e PostgreSQL;
* evolução incremental;
* documentação alinhada aos dados.

---

# Alterações na Estrutura

Não adicionar, remover ou renomear colunas sem revisar o impacto.

Antes de uma mudança:

```text
1. Definir a necessidade.
2. Atualizar este documento.
3. Atualizar awards.csv.
4. Atualizar database/schema.sql.
5. Atualizar import_to_postgres.py.
6. Atualizar database.py, se necessário.
7. Atualizar awards.py.
8. Atualizar testes.
9. Atualizar API e dashboard.
10. Importar novamente.
11. Validar os registros.
12. Registrar a mudança em commit.
```

---

# Normalização Futura

Atualmente, o nome da premiação e o nome do jogo são armazenados diretamente na tabela `awards`.

Futuramente, poderão ser avaliadas estruturas como:

```text
award_events
award_editions
award_nominees
games
```

Também poderá ser criado um relacionamento por identificador entre Awards History e Foundation Collection.

Essa normalização não é necessária na fase atual.

Ela só deve ocorrer quando trouxer benefício real para:

* integridade;
* relacionamento entre entidades;
* expansão da base;
* desempenho;
* manutenção.

---

# Campos Futuros Possíveis

Campos que poderão ser avaliados:

```text
categoria
cerimonia_data
game_id
fonte_url
observacao
```

Esses campos não fazem parte do contrato atual.

---

# Versionamento

**Versão:** 2.0

Esta versão atualiza o documento para representar:

* o CSV editorial;
* a tabela PostgreSQL;
* o campo `id` automático;
* o fluxo de importação;
* a integração com a API;
* a integração com o dashboard;
* as regras de integridade;
* a comparação com a Foundation Collection.

---

# Status do Documento

```text
Contrato de dados atual da Awards History
```

Este documento deve ser revisado sempre que houver mudanças na estrutura, nas premiações consideradas ou nas regras de preenchimento.
