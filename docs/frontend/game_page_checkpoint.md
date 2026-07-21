# Game Page Checkpoint — The AAA Archive

## Objetivo deste documento

Este documento registra a conclusão da primeira versão visual da página individual dos jogos do projeto **The AAA Archive**.

A implementação faz parte da:

```text
FASE 5 — PÁGINA INDIVIDUAL DO JOGO
```

A metodologia utilizada continuou sendo:

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
Fase 5 — Página Individual do Jogo
Status: estrutura técnica e visual inicial concluídas
```

A página individual está disponível pela rota:

```text
/games/:id
```

Exemplos:

```text
/games/1
/games/25
/games/66
```

---

## Arquivos principais

A página utiliza:

```text
frontend/src/pages/GamePage.tsx
frontend/src/pages/GamePage.css
```

A navegação até ela acontece pelo componente:

```text
frontend/src/components/GameCard.tsx
```

Cada GameCard abre:

```text
/games/{game.id}
```

---

## Arquitetura preservada

A página mantém a arquitetura oficial:

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

O React não acessa diretamente:

```text
games.csv
PostgreSQL
módulos Python
```

---

## Carregamento do jogo

O ID do jogo é obtido pela URL utilizando:

```text
useParams()
```

Exemplo:

```text
/games/25
↓
id = "25"
↓
Number(id)
↓
25
```

Antes de realizar a requisição, o ID é validado.

Um ID válido precisa:

```text
ser um número inteiro
+
ser maior que zero
```

Exemplos inválidos:

```text
/games/abc
/games/0
/games/-1
```

---

## Serviço utilizado

A página utiliza a função:

```text
getGameById(id)
```

Localizada em:

```text
frontend/src/services/api.ts
```

Comportamento:

```text
status 200
→ retorna o jogo

status 404
→ retorna null

outra falha
→ lança erro
```

---

## Estados representados

A página representa quatro estados:

```text
loading
success
not found
error
```

### Loading

Apresentado enquanto o React aguarda a FastAPI:

```text
RETRIEVING RECORD...
```

### Success

Apresentado quando o registro é encontrado.

A página mostra os dados disponíveis do jogo.

### Not Found

Apresentado quando o ID não corresponde a nenhum registro:

```text
RECORD NOT FOUND
```

### Error

Apresentado quando ocorre uma falha de comunicação:

```text
ARCHIVE NODE UNAVAILABLE
```

Erros técnicos internos não são exibidos diretamente ao visitante.

---

## Estrutura visual atual

A GamePage possui:

```text
link de retorno
↓
identificação do registro
↓
título do jogo
↓
resumo principal
↓
área visual temporária
↓
descrição editorial
↓
marcações históricas
↓
dados do arquivo
↓
frase ambiental
```

---

## Identificação do registro

O ID é formatado com três números.

Exemplo:

```text
1
→ REC-001

25
→ REC-025

66
→ REC-066
```

---

## Resumo principal

Quando os dados existem, o hero apresenta:

```text
ano
desenvolvedora
gênero
franquia
```

Campos vazios não são exibidos.

Regra:

```text
campo null
→ não renderizar
```

---

## Área visual temporária

As imagens definitivas ainda não foram adicionadas.

Por isso, a página utiliza temporariamente:

```text
FOUNDATION IMAGE FEED
individual image awaiting local asset
```

Essa área poderá receber futuramente os assets reais dos jogos.

Nenhuma imagem externa é carregada nesta fase.

---

## Descrição editorial

Quando o campo:

```text
descricao
```

possui conteúdo, a página apresenta o painel:

```text
EDITORIAL DESCRIPTION
```

Quando a descrição é nula, o painel não aparece.

---

## Marcações históricas

A página utiliza os campos:

```text
historico_importante
historico_influente
```

Quando verdadeiros, eles geram as classificações:

```text
HISTORICAL IMPORTANCE
→ CONFIRMED

INFLUENCE & LEGACY
→ CONFIRMED
```

Nenhum texto histórico novo foi inventado no front-end.

A interface apenas representa as classificações já armazenadas no banco.

---

## Archive Data

O painel:

```text
ARCHIVE DATA
```

pode apresentar:

```text
record ID
ano de lançamento
desenvolvedora
gênero
franquia
Metacritic
nota Kadu
nota Pavam
```

Cada informação é exibida somente quando está disponível.

A propriedade:

```text
nota_pavam
```

foi preservada, conforme o planejamento oficial.

---

## Navegação contextual

A barra lateral adapta seus itens de acordo com os dados existentes.

Itens possíveis:

```text
RECORD OVERVIEW
EDITORIAL DESCRIPTION
HISTORICAL NOTES
ARCHIVE DATA
ARCHIVE STATUS
```

Painéis inexistentes não são adicionados à navegação.

---

## Navegação de retorno

A página possui link para:

```text
/foundation
```

O retorno aparece:

```text
no topo da página
+
nos estados de erro
+
nos registros não encontrados
```

---

## Acessibilidade

A implementação atual possui:

```text
navegação por links reais
foco visível
aria-live nos estados da requisição
estrutura semântica
respeito ao prefers-reduced-motion
```

---

## Responsividade inicial

A página se adapta para telas menores.

Em telas grandes:

```text
conteúdo principal
+
imagem temporária
→ lado a lado
```

Em telas menores:

```text
conteúdo principal
↓
imagem temporária
```

Os painéis internos também passam de duas colunas para uma coluna.

---

## Testes realizados

Foram testadas páginas com diferentes IDs:

```text
/games/1
/games/25
/games/66
```

Também foram verificadas:

```text
navegação pelos GameCards
carregamento dos registros
representação dos dados
responsividade inicial
```

Verificações técnicas:

```powershell
npm run lint
npm run build
```

Resultados:

```text
lint concluído sem erros
build de produção concluído corretamente
```

O funcionamento no navegador também foi confirmado.

---

## Arquivos alterados na Fase 5

```text
frontend/src/App.tsx
frontend/src/services/api.ts
frontend/src/components/GameCard.tsx
frontend/src/components/GameCard.css
frontend/src/pages/GamePage.tsx
frontend/src/pages/GamePage.css
api/main.py
api/test_main.py
```

---

## Arquivo criado nesta documentação

```text
docs/frontend/game_page_checkpoint.md
```

---

## Limites preservados

Ainda não foram adicionados:

```text
imagens definitivas
contexto detalhado da era
premiações relacionadas
registros relacionados
galeria
carrossel
favoritos
comentários
usuários
autenticação
```

Nenhuma biblioteca adicional foi instalada.

---

## Estado final

```text
endpoint GET /games/{game_id}
→ concluído

testes automáticos do endpoint
→ concluídos

getGameById(id)
→ concluído

rota /games/:id
→ concluída

GameCard como navegação
→ concluído

estrutura visual inicial da GamePage
→ concluída

estados loading, success, not found e error
→ concluídos

lint
→ aprovado

build
→ aprovado

documentação
→ concluída
```
