# Awards History Checkpoint — The AAA Archive

## Objetivo deste documento

Este documento registra a conclusão da primeira versão funcional da página **Awards History** do front-end do projeto **The AAA Archive**.

A implementação corresponde à:

```text
FASE 6 — AWARDS HISTORY
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

```text
Fase 6 — Awards History
Status: concluída, integrada e testada
```

A página está disponível em:

```text
/awards
```

---

## Arquivos principais

```text
frontend/src/pages/AwardsPage.tsx
frontend/src/pages/AwardsPage.css
frontend/src/types/Award.ts
frontend/src/services/api.ts
frontend/src/App.tsx
frontend/src/components/TopNavigation.tsx
```

---

## Arquitetura preservada

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

O React não acessa diretamente o CSV, o PostgreSQL ou módulos Python.

---

## Tipo Award

Arquivo:

```text
frontend/src/types/Award.ts
```

Campos utilizados:

```text
ano
premiacao
jogo
status
```

Status possíveis:

```text
Vencedor
Indicado
```

---

## Funções adicionadas ao serviço da API

Arquivo:

```text
frontend/src/services/api.ts
```

Funções utilizadas pela página:

```text
getAwards()
getAwardsByYear(year)
getFoundationAwardWinners()
getGames()
```

Endpoints relacionados:

```text
GET /awards
GET /awards/{year}
GET /awards/foundation/winners
GET /games
```

---

## Estrutura da página

A Awards History possui:

```text
hero introdutório
↓
Year Index
↓
Selected Year
↓
Foundation Status
↓
About the Award
↓
frase ambiental
```

A navegação lateral apresenta:

```text
AWARDS OVERVIEW
YEAR INDEX
SELECTED YEAR
FOUNDATION STATUS
ABOUT THE AWARD
```

---

## Carregamento inicial

Ao abrir a página, o React consulta:

```text
GET /awards
```

A resposta é utilizada para:

```text
montar o índice de anos
calcular o período do arquivo
mostrar a quantidade de registros
selecionar o primeiro ano disponível
```

Estado atual dos dados:

```text
127 registros
23 anos
período: 2003—2025
3 nomes de premiação
```

---

## Estados da coleção

A página representa:

```text
loading
success
empty
error
```

Mensagens principais:

```text
RETRIEVING AWARDS...
NO AWARDS RECORDS FOUND
ARCHIVE NODE UNAVAILABLE
```

Erros técnicos internos não são exibidos diretamente ao visitante.

---

## Year Index

Os anos disponíveis são obtidos dos registros reais da API.

Cada ano é apresentado como um botão acessível.

Comportamentos:

```text
clique
→ seleciona o ano

Tab
→ move o foco entre os anos

Enter ou Space
→ ativa o ano em foco
```

O ano selecionado possui estado visual ativo e foco visível.

---

## Selected Year

Quando um ano é selecionado, o React consulta:

```text
GET /awards/{year}
```

O painel apresenta:

```text
ano selecionado
nome da premiação
vencedor
indicados
quantidade de indicados
```

O primeiro ano disponível é selecionado automaticamente ao carregar a página.

---

## Vencedor e indicados

O vencedor é identificado por:

```text
status = Vencedor
```

Os demais registros do ano são apresentados como indicados:

```text
status = Indicado
```

Os indicados aparecem em uma lista numerada e preservam a ordem retornada pela API.

---

## Foundation Status

A página cruza o vencedor selecionado com a Foundation Collection.

Estados possíveis:

```text
CONFIRMED
NOT ARCHIVED
UNAVAILABLE
```

### Confirmed

O vencedor está presente na Foundation Collection.

A página apresenta:

```text
VIEW FOUNDATION RECORD
```

O botão abre:

```text
/games/{game.id}
```

### Not Archived

O vencedor não está presente na Foundation Collection.

Nenhum registro ou ID é inventado.

### Unavailable

A consulta necessária não pôde ser concluída.

---

## About the Award

O painel contextualiza a premiação relacionada ao ano selecionado.

Períodos utilizados:

```text
2003—2012
→ Spike Video Game Awards

2013
→ VGX

2014—2025
→ The Game Awards
```

O painel apresenta:

```text
nome da cerimônia
período relacionado
texto contextual curto
ano selecionado
nome registrado no banco
```

O conteúdo permanece resumido e informativo, respeitando a regra editorial do projeto.

---

## Identidade visual

A página preserva:

```text
fundo escuro
painéis em grafite
bordas finas
tipografia monoespaçada
scanlines discretas
contraste controlado
verde para estados confirmados
vermelho para falhas
```

O visual não tenta reproduzir uma cerimônia colorida ou uma loja de jogos.

A proposta permanece:

```text
a cerimônia terminou
↓
as pessoas foram embora
↓
restaram os registros
```

---

## Responsividade

Em telas grandes:

```text
Year Index
+
Selected Year
→ lado a lado
```

Em telas menores:

```text
Year Index
↓
Selected Year
↓
Foundation Status
↓
About the Award
```

Os botões de ano reorganizam suas colunas conforme o espaço disponível.

---

## Acessibilidade

A implementação possui:

```text
botões semânticos para os anos
aria-pressed no ano selecionado
foco visível
links reais para registros da Foundation
aria-live nos estados das requisições
respeito ao prefers-reduced-motion
```

---

## Testes realizados

Foram testados anos de diferentes períodos:

```text
2003
2013
2014
2018
2021
2022
2023
```

Também foram verificados:

```text
carregamento inicial
seleção por clique
seleção por teclado
vencedor e indicados
Foundation Status confirmado
vencedor fora da Foundation
link para a página individual
mudança do About the Award
responsividade inicial
```

Verificações técnicas:

```powershell
npm run lint
npm run build
```

Resultados:

```text
lint concluído sem erros ou avisos
build de produção concluído corretamente
```

---

## Limites preservados

Não foram adicionados:

```text
imagens definitivas das cerimônias
filtros avançados
busca por premiação
gráficos
favoritos
comentários
usuários
autenticação
bibliotecas adicionais
```

---

## Arquivo desta documentação

```text
docs/frontend/awards_history_checkpoint.md
```

---

## Estado final

```text
rota /awards
→ concluída

integração GET /awards
→ concluída

Year Index
→ concluído

seleção por ano
→ concluída

vencedor e indicados
→ concluídos

Foundation Status
→ concluído

link para registro individual
→ concluído

About the Award
→ concluído

loading, success, empty e error
→ concluídos

responsividade inicial
→ concluída

lint
→ aprovado

build
→ aprovado

documentação
→ concluída
```