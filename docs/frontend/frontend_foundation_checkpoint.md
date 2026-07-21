# Foundation Collection Checkpoint — The AAA Archive

## Objetivo deste documento

Este documento registra a conclusão da **Fase 4 — Foundation Collection** do front-end do projeto **The AAA Archive**.

A Foundation Collection é a primeira página da aplicação React que utiliza diretamente os dados reais armazenados no PostgreSQL e disponibilizados pela FastAPI.

A metodologia utilizada durante esta fase continuou sendo:

```text
planejar
↓
implementar uma etapa pequena
↓
testar
↓
documentar
↓
só depois avançar
```

---

## Estado atual da fase

Status:

```text
Fase 4 — Foundation Collection
Status: concluída, integrada e testada
```

A página está disponível em:

```text
/foundation
```

Ela consegue:

- carregar os jogos reais da Foundation Collection;
- comunicar-se com a FastAPI;
- apresentar os registros em um grid;
- pesquisar jogos;
- filtrar jogos;
- ordenar os registros;
- representar estados de carregamento;
- representar respostas vazias;
- representar falhas de comunicação;
- restaurar a coleção completa;
- funcionar sem acesso direto ao CSV ou ao PostgreSQL.

---

## Arquitetura utilizada

A Foundation respeita a arquitetura oficial do projeto:

```text
React
↓
Fetch API
↓
FastAPI
↓
database.py
↓
PostgreSQL
```

O React nunca acessa diretamente:

```text
data/games.csv
PostgreSQL
scripts/database.py
```

Toda comunicação passa pela FastAPI.

Fluxo principal:

```text
FoundationPage
↓
services/api.ts
↓
Fetch API
↓
FastAPI
↓
PostgreSQL
↓
JSON
↓
estado do React
↓
GameCard
```

---

## Configuração de CORS

A primeira comunicação entre React e FastAPI revelou a necessidade de configurar CORS.

Durante o desenvolvimento local, os servidores utilizam origens diferentes:

```text
React
http://localhost:5173

FastAPI
http://127.0.0.1:8000
```

Foi adicionada à FastAPI a configuração:

```python
CORSMiddleware
```

Origem autorizada:

```text
http://localhost:5173
```

Essa configuração permite que o navegador aceite as requisições realizadas pelo front-end.

Nenhuma biblioteca adicional foi instalada para isso.

---

## Tipo Game

Foi criado o arquivo:

```text
frontend/src/types/Game.ts
```

Ele representa o formato dos jogos retornados pela FastAPI.

Campos disponíveis:

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

Alguns campos aceitam:

```text
null
```

Isso reflete corretamente o estado atual dos dados e permite que a interface trate informações ausentes sem quebrar.

---

## Serviço central da API

Foi criado e desenvolvido o arquivo:

```text
frontend/src/services/api.ts
```

Ele centraliza as requisições relacionadas aos jogos.

Funções implementadas:

```text
getGames()
searchGames(term)
getGamesByDecade(decade)
getGamesByYear(year)
getGamesByGenre(genre)
getGamesByDeveloper(developer)
getGamesByFranchise(franchise)
```

Também foi criada uma função auxiliar interna:

```text
requestGames(endpoint)
```

Ela centraliza:

```text
fetch
↓
validação da resposta
↓
conversão para JSON
↓
retorno como Game[]
```

Isso evita repetir o mesmo processo em cada requisição.

---

## Endpoint principal

A coleção completa é carregada por:

```text
GET /games
```

Resultado atual:

```text
66 registros
```

A resposta da API é uma lista de objetos JSON.

Exemplo conceitual:

```json
[
  {
    "id": 1,
    "nome": "Final Fantasy VII",
    "ano_lancamento": 1997,
    "genero": "RPG",
    "developer": "Square",
    "franchise": "Final Fantasy"
  }
]
```

---

## Página Foundation

O arquivo principal da página é:

```text
frontend/src/pages/FoundationPage.tsx
```

Os estilos estão em:

```text
frontend/src/pages/FoundationPage.css
```

A página utiliza a estrutura compartilhada:

```text
ArchiveShell
├── TopNavigation
├── ContextSidebar
└── conteúdo da Foundation
```

---

## Estrutura visual da página

A Foundation possui atualmente:

```text
header da coleção
↓
área visual atmosférica
↓
Search Terminal
↓
Filter Terminal
↓
Sort Terminal
↓
painel de registros
↓
grid de jogos
↓
frase ambiental
```

O visual segue a identidade aprovada:

- fundo quase preto;
- painéis em grafite;
- bordas finas;
- tipografia monoespaçada;
- títulos em caixa alta;
- informações técnicas em inglês;
- textos editoriais em português;
- pequenos estados em verde ou vermelho;
- scanlines e vinheta discretas;
- aparência de arquivo tecnológico antigo.

---

## Header da Foundation

O header apresenta:

```text
// FOUNDATION / COLLECTION
FOUNDATION COLLECTION
```

Texto editorial:

```text
Registros preservados de jogos que ajudaram
a construir o meio.
Explorar, pesquisar, lembrar.
```

Também existe um indicador de integridade:

```text
collection integrity: stable
```

Estados possíveis:

```text
retrieving
stable
empty
unavailable
```

A área atmosférica ainda utiliza uma representação visual temporária:

```text
FOUNDATION STORAGE FEED
ARCHIVE VAULT 01
```

A imagem definitiva será adicionada posteriormente junto com os outros assets visuais do projeto.

---

## Componente GameCard

Foi criado o componente:

```text
frontend/src/components/GameCard.tsx
```

Seus estilos estão em:

```text
frontend/src/components/GameCard.css
```

O componente recebe um objeto por meio de props:

```tsx
<GameCard game={game} />
```

Informações exibidas atualmente:

```text
identificação do registro
ano de lançamento
nome do jogo
desenvolvedora
representação visual temporária
```

Exemplo:

```text
REC-001
[1997]

Final Fantasy VII
Square
```

Campos ausentes possuem textos alternativos:

```text
YEAR UNKNOWN
DEVELOPER UNKNOWN
```

O componente ainda não é clicável porque a página individual dos jogos ainda não foi criada.

---

## Grid de jogos

Os registros são apresentados utilizando:

```tsx
games.map(...)
```

Fluxo:

```text
lista recebida pela API
↓
map percorre os objetos
↓
um GameCard é criado para cada jogo
```

A propriedade:

```tsx
key={game.id}
```

permite que o React identifique cada registro de maneira única.

Quantidade atual:

```text
66 GameCards
```

---

## Estados da coleção

A página representa quatro estados principais:

```text
loading
success
empty
error
```

### Loading

Apresentado durante a comunicação com o servidor:

```text
RETRIEVING RECORDS...
```

### Success

Apresentado quando os registros são recebidos corretamente:

```text
66 RECORDS
DISPLAYING 66 RECORDS
```

### Empty

Apresentado quando a consulta retorna uma lista vazia:

```text
NO RECORDS FOUND
```

### Error

Apresentado quando a comunicação não pode ser concluída:

```text
ARCHIVE NODE UNAVAILABLE
```

Erros técnicos crus não são exibidos ao visitante.

---

## Search Terminal

O Search Terminal utiliza:

```text
GET /games/search?term=
```

A função do serviço é:

```typescript
searchGames(term)
```

O campo aceita pesquisas por informações como:

- nome;
- desenvolvedora;
- gênero;
- franquia;
- descrição ou palavra-chave, conforme a lógica atual do backend.

Exemplo:

```text
silent
↓
GET /games/search?term=silent
↓
Silent Hill
```

Quando nenhum resultado é encontrado:

```text
NO RECORDS FOUND
```

Ao utilizar:

```text
CLEAR SEARCH
```

a coleção completa é restaurada sem uma nova requisição.

Isso é possível porque o React mantém duas listas:

```text
allGames
→ coleção completa

displayedGames
→ registros apresentados no momento
```

---

## Filter Terminal

O Filter Terminal utiliza os endpoints reais da FastAPI.

Tipos disponíveis:

```text
DECADE
YEAR
GENRE
DEVELOPER
FRANCHISE
```

### Década

```text
GET /games/decade/{decade}
```

Função:

```typescript
getGamesByDecade(decade)
```

Exemplo:

```text
DECADE / 2000
```

### Ano

```text
GET /games/year/{year}
```

Função:

```typescript
getGamesByYear(year)
```

Exemplo:

```text
YEAR / 2018
```

### Gênero

```text
GET /games/genre/{genre}
```

Função:

```typescript
getGamesByGenre(genre)
```

Exemplo:

```text
GENRE / Survival Horror
```

### Desenvolvedora

```text
GET /games/developer/{developer}
```

Função:

```typescript
getGamesByDeveloper(developer)
```

Exemplo:

```text
DEVELOPER / Capcom
```

### Franquia

```text
GET /games/franchise/{franchise}
```

Função:

```typescript
getGamesByFranchise(franchise)
```

Exemplo:

```text
FRANCHISE / Resident Evil
```

---

## Validação dos filtros numéricos

Ano e década são validados antes da requisição.

Ano válido:

```text
2018
```

Ano inválido:

```text
18
abc
20188
```

Década válida:

```text
2000
2010
2020
```

Década inválida:

```text
2005
20
abcd
```

A década precisa:

```text
possuir quatro números
+
terminar em zero
```

Quando o valor é inválido:

```text
INVALID FILTER VALUE
```

Nenhuma requisição desnecessária é enviada para a FastAPI.

---

## Relação entre busca e filtros

Na primeira versão, busca e filtros não são combinados.

Regra atual:

```text
nova busca
→ limpa o filtro ativo

novo filtro
→ limpa a busca ativa
```

Exemplo:

```text
Busca:
God of War
↓
grid mostra os resultados da busca

Depois:
DECADE / 2000
↓
a busca é removida
↓
a API retorna todos os jogos da década de 2000
```

O filtro não é aplicado somente sobre os resultados anteriores.

Essa decisão mantém a interface e os endpoints simples.

Uma combinação avançada entre busca e filtros não faz parte do escopo atual.

---

## Ordenação

Foi criado o utilitário:

```text
frontend/src/utils/sortGames.ts
```

A ordenação acontece localmente no React.

Nenhuma nova requisição é feita para:

```text
FastAPI
PostgreSQL
```

Opções disponíveis:

```text
ARCHIVE ORDER
TITLE: A–Z
OLDEST FIRST
NEWEST FIRST
METACRITIC: HIGHEST
```

### Archive Order

Utiliza o ID dos registros:

```text
REC-001
REC-002
REC-003
...
```

### Title: A–Z

Utiliza:

```typescript
localeCompare()
```

para ordenar alfabeticamente.

### Oldest First

Apresenta os jogos mais antigos primeiro.

### Newest First

Apresenta os jogos mais recentes primeiro.

### Metacritic: Highest

Apresenta as maiores notas primeiro.

Jogos sem ano ou sem nota são enviados para o final da lista.

---

## Preservação da lista original

O método:

```typescript
Array.sort()
```

modifica diretamente o array em que é executado.

Para evitar alterações no estado original do React, o utilitário cria uma cópia:

```typescript
const sortedGames = [...games]
```

Fluxo:

```text
displayedGames
→ lista recebida ou filtrada

sortedDisplayedGames
→ cópia ordenada utilizada no grid
```

---

## useMemo

A lista ordenada utiliza:

```typescript
useMemo
```

Ela é recalculada quando:

```text
displayedGames muda
ou
sortOption muda
```

Isso mantém separado:

```text
dados exibidos
↓
ordenação visual
```

A ordenação pode ser aplicada sobre:

- a coleção completa;
- resultados de pesquisa;
- resultados de filtro.

---

## Navegação contextual

A lateral da Foundation possui atualmente:

```text
ALL RECORDS
SEARCH ARCHIVE
FILTER ARCHIVE
SORT ARCHIVE
```

Cada item leva até o painel correspondente.

Essa organização simplifica os itens conceituais originalmente planejados:

```text
DECADES
YEARS
GENRES
DEVELOPERS
FRANCHISES
```

Todos esses tipos permanecem disponíveis dentro do Filter Terminal.

Não foi necessário criar cinco painéis separados.

---

## Navegação superior

O item:

```text
FOUNDATION
```

foi ativado na navegação superior.

Rotas funcionais atuais:

```text
/
→ Introdução

/home
→ Home

/foundation
→ Foundation Collection
```

Itens ainda indisponíveis:

```text
AWARDS
DATA ROOM
```

Eles serão ativados somente quando suas páginas forem implementadas.

---

## Responsividade inicial

A Foundation possui adaptação inicial para diferentes larguras.

### Desktop

```text
header em duas colunas
sidebar visível
terminais horizontais
grid com até quatro colunas
```

### Larguras intermediárias

```text
grid com três ou duas colunas
terminais reorganizados
header adaptado
```

### Mobile

```text
header em uma coluna
campos dos terminais empilhados
feedback reorganizado
grid com uma coluna
espaçamentos reduzidos
```

A revisão responsiva global e definitiva será realizada na fase específica de responsividade.

---

## Arquivos criados

Durante a Fase 4 foram criados:

```text
frontend/src/types/Game.ts
frontend/src/services/api.ts
frontend/src/utils/sortGames.ts
frontend/src/components/GameCard.tsx
frontend/src/components/GameCard.css
frontend/src/pages/FoundationPage.tsx
frontend/src/pages/FoundationPage.css
docs/frontend/foundation_checkpoint.md
```

---

## Arquivos modificados

Também foram modificados:

```text
api/main.py
frontend/src/App.tsx
frontend/src/components/TopNavigation.tsx
```

### api/main.py

Alterações:

```text
configuração de CORS
autorização do servidor React local
```

### App.tsx

Alteração:

```text
criação da rota /foundation
```

### TopNavigation.tsx

Alterações:

```text
HOME transformado em navegação funcional
FOUNDATION transformado em navegação funcional
indicação visual da rota ativa
```

---

## Testes dos endpoints

Foram testados manualmente pela documentação interativa da FastAPI:

```text
GET /games
GET /games/search
GET /games/decade/{decade}
GET /games/year/{year}
GET /games/genre/{genre}
GET /games/developer/{developer}
GET /games/franchise/{franchise}
```

Comportamentos confirmados:

```text
consulta com correspondência
→ lista com registros

consulta sem correspondência
→ []

falha de comunicação
→ estado de erro no React
```

---

## Testes da interface

Foram testados:

- carregamento dos 66 jogos;
- criação dos 66 GameCards;
- busca por título;
- busca por desenvolvedora;
- pesquisa sem resultados;
- restauração da coleção;
- filtro por década;
- filtro por ano;
- filtro por gênero;
- filtro por desenvolvedora;
- filtro por franquia;
- filtro sem resultados;
- valor numérico inválido;
- substituição de busca por filtro;
- substituição de filtro por busca;
- ordenação pelos IDs;
- ordenação alfabética;
- ordenação por ano crescente;
- ordenação por ano decrescente;
- ordenação por Metacritic;
- ordenação de resultados de busca;
- ordenação de resultados de filtro;
- falha da FastAPI;
- navegação entre Home e Foundation;
- rolagem pelos itens da lateral.

---

## Lint

Comando utilizado:

```powershell
npm run lint
```

Resultado:

```text
nenhum erro encontrado
```

---

## Build

Comando utilizado:

```powershell
npm run build
```

Resultado:

```text
build concluído corretamente
```

---

## Pendência editorial — Silent Hill 2

Durante os testes de busca foi identificado que:

```text
Silent Hill
→ está presente na Foundation Collection

Silent Hill 2
→ ainda não está presente
```

Silent Hill 2 já aparece na proposta editorial e visual do projeto, mas não existe atualmente no banco de dados da Foundation.

Foi decidido não interromper o desenvolvimento do front-end para modificar somente esse registro.

A correção será realizada em uma futura revisão editorial da coleção.

Fluxo planejado:

```text
revisar a Foundation completa
↓
adicionar Silent Hill 2
↓
avaliar outros jogos ausentes
↓
atualizar games.csv
↓
reimportar PostgreSQL
↓
atualizar testes
↓
atualizar contagens
↓
atualizar documentação
```

Até essa revisão:

```text
Foundation Records: 66
```

continua sendo a contagem oficial utilizada pela aplicação.

---

## Assets visuais pendentes

Os jogos ainda utilizam:

```text
IMAGE NOT ARCHIVED
```

O header também utiliza uma representação atmosférica criada com CSS.

As imagens definitivas serão adicionadas posteriormente na estrutura:

```text
frontend/public/assets/
```

Organização planejada:

```text
assets/
├── games/
├── history/
├── awards/
├── interface/
├── textures/
├── placeholders/
└── hidden/
```

A ausência dos assets não impede o funcionamento técnico da Foundation.

---

## Decisões preservadas

Durante a implementação:

- nenhuma biblioteca adicional foi instalada;
- Axios não foi utilizado;
- Redux não foi utilizado;
- Tailwind não foi utilizado;
- Bootstrap não foi utilizado;
- nenhuma biblioteca de componentes foi utilizada;
- nenhuma biblioteca de animação foi utilizada;
- o React não acessa diretamente o banco;
- a API continua centralizada em `services/api.ts`;
- não foi criada paginação;
- não foi criado carregamento infinito;
- não foram criados filtros combinados;
- não foi criado sistema de favoritos;
- não foi criada página individual antecipadamente;
- não foi criado `GET /games/{id}` antecipadamente;
- campos inexistentes não foram inventados;
- plataforma não foi exibida porque não existe no retorno atual da API;
- imagens não foram adicionadas sem uma estrutura oficial de assets.

---

## Conceitos praticados

Nesta fase foram praticados:

```text
tipos TypeScript
props
useState
useEffect
useMemo
FormEvent
fetch
async e await
try e catch
listas
map
slice
estado controlado
formulários controlados
condicionais
renderização condicional
tratamento de null
encodeURIComponent
funções auxiliares
tipos union
Exclude
ordenação de arrays
localeCompare
cópia de arrays com spread
integração React e FastAPI
CORS
```

---

## Resultado da fase

A Foundation Collection agora possui:

```text
integração real com a FastAPI
↓
dados reais do PostgreSQL
↓
66 registros
↓
GameCards reutilizáveis
↓
Search Terminal
↓
Filter Terminal
↓
Sort Terminal
↓
loading, success, empty e error
↓
grid responsivo inicial
```

Resultado final:

```text
Foundation Collection funcional
API integrada
busca funcional
filtros funcionais
ordenação funcional
estados tratados
lint concluído
build concluído
```

---

## Próxima fase

O próximo passo será:

```text
Fase 5 — Página individual do jogo
```

A implementação seguirá esta ordem:

```text
criar GET /games/{id}
↓
testar o endpoint
↓
criar getGameById(id)
↓
criar a rota /games/:id
↓
transformar GameCard em navegação
↓
criar GamePage
↓
tratar loading, success, not found e error
↓
ocultar campos vazios
↓
exibir notas discretamente
↓
testar
↓
documentar
```

O novo endpoint não será criado antes de sua utilização.

---

## Status final

```text
Fase 4 — Foundation Collection
Status: concluída, integrada, testada e documentada

Próxima etapa:
Fase 5 — Página individual do jogo
```