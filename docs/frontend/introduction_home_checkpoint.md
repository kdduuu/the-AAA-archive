# Introduction and Home Checkpoint — The AAA Archive

## Objetivo deste documento

Este documento registra o estado concluído da **Fase 3 — Introdução e Home** do front-end do projeto **The AAA Archive**.

Nesta fase foram implementadas as primeiras páginas reais da aplicação:

```text
/
→ Introdução

/home
→ Home
```

A metodologia continua sendo:

```text
implementar
↓
testar
↓
documentar
↓
versionar
↓
só depois avançar
```

---

## Estado atual

```text
Fase 3 — Introdução e Home
Status: concluída e testada
```

A Introdução e a Home estão funcionando localmente.

Os testes de lint, build e execução do servidor foram concluídos sem erros.

---

## Introdução

A página de Introdução está disponível na rota:

```text
/
```

Arquivo principal:

```text
frontend/src/pages/IntroductionPage.tsx
```

Estilos:

```text
frontend/src/pages/IntroductionPage.css
```

A página apresenta:

- identificação `THE AAA ARCHIVE`;
- subtítulo `digital preservation system`;
- sequência progressiva de mensagens;
- registros totais da Foundation e Awards;
- nível de acesso do visitante;
- mensagem `ACCESS GRANTED`;
- botão `UNLOCK ARCHIVE`;
- opção para pular a sequência;
- frase ambiental final.

Sequência utilizada:

```text
signal detected
restoring archive node
database integrity verified
foundation records: 66
awards logs: 127
access level: visitor
```

---

## Funcionamento da sequência

As mensagens aparecem progressivamente utilizando:

```text
useState
useEffect
setInterval
clearInterval
```

A sequência pode ser concluída imediatamente pelo botão:

```text
SKIP SEQUENCE
```

Quando todas as mensagens aparecem, o botão:

```text
UNLOCK ARCHIVE
```

é liberado.

Ao clicar nele, o visitante é enviado para:

```text
/home
```

---

## Controle da sessão

A Introdução utiliza:

```text
sessionStorage
```

Chave utilizada:

```text
the-aaa-archive-access-granted
```

Durante a mesma sessão do navegador, um visitante que já desbloqueou o arquivo é redirecionado diretamente para a Home.

A Introdução não depende da FastAPI ou do PostgreSQL.

---

## Home

A Home está disponível na rota:

```text
/home
```

Arquivo principal:

```text
frontend/src/pages/HomePage.tsx
```

Estilos:

```text
frontend/src/pages/HomePage.css
```

A página utiliza a estrutura global:

```text
ArchiveShell
├── TopNavigation
├── ContextSidebar
└── conteúdo da Home
```

---

## Conteúdo da Home

A Home possui as seguintes áreas:

```text
ARCHIVE OVERVIEW
SYSTEM EVOLUTION
FEATURED RECORDS
ARCHIVE STATUS
DIRECT ACCESS
```

### Archive Overview

O hero principal apresenta:

- título do projeto;
- texto editorial;
- estado de integridade do arquivo;
- espaço visual reservado para uma imagem atmosférica.

Texto principal:

```text
Preservamos o que o tempo esquece.
Fragmentos de código, arte e som —
memórias de mundos antes jogados.
É aqui que eles continuam.
```

---

## System Evolution

A seção apresenta uma visão resumida da evolução dos videogames:

```text
1972—1982
EARLY ARCADES / ATARI

1983—1992
8 & 16-BIT ERA

1993—1998
3D TRANSITION

1999—2006
SIXTH GENERATION

2007—2013
HD ERA

2014—PRESENT
MODERN SYSTEMS
```

Os textos são editoriais e permanecem dentro do React.

Eles não precisam ser carregados pelo banco de dados.

---

## Featured Records

A Home possui quatro registros em destaque:

```text
Super Mario 64
Metal Gear Solid
Silent Hill 2
The Last of Us
```

Nesta etapa, os dados desses registros ainda estão declarados temporariamente dentro do arquivo `HomePage.tsx`.

Na integração futura:

```text
IDs selecionados
↓
FastAPI
↓
PostgreSQL
↓
dados reais no React
```

As informações não serão mantidas manualmente em duplicidade na versão final.

---

## Archive Status

O painel apresenta atualmente:

```text
Foundation Records: 66
Awards Logs: 127
Archive Period: 1993—2025
Node Status: Stable
```

Esses valores correspondem ao estado real atual do projeto, mas ainda estão declarados temporariamente no front-end.

Posteriormente deverão ser carregados pelo endpoint:

```text
GET /stats/home
```

---

## Direct Access

A Home possui os acessos:

```text
ENTER FOUNDATION
OPEN AWARDS LOG
ENTER DATA ROOM
```

Nesta fase eles permanecem bloqueados porque suas respectivas páginas ainda não foram implementadas.

Cada acesso será ativado quando sua rota estiver funcionando.

---

## Dados estáticos e dados da API

A separação planejada permanece:

### Conteúdo estático no React

```text
textos editoriais
navegação
mensagens do sistema
System Evolution
frases ambientais
configurações visuais
```

### Conteúdo carregado pela API

```text
jogos da Foundation
dados dos Featured Records
métricas reais
premiações
página individual dos jogos
estatísticas da Data Room
```

Arquitetura preservada:

```text
CSV
↓
PostgreSQL
↓
FastAPI
↓
JSON
↓
Fetch API
↓
React
```

O React não acessará diretamente o CSV ou o PostgreSQL.

---

## Assets pendentes

O hero da Home e os registros em destaque ainda utilizam representações visuais temporárias.

As imagens definitivas serão armazenadas em:

```text
frontend/public/assets/
```

Estrutura planejada:

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

A ausência dessas imagens não impede o funcionamento atual da página.

---

## Arquivos criados

```text
frontend/src/pages/
├── HomePage.css
├── HomePage.tsx
├── IntroductionPage.css
└── IntroductionPage.tsx
```

O arquivo temporário:

```text
HomePreviewPage.tsx
```

foi removido.

---

## Rotas atuais

```text
/
→ Introdução

/home
→ Home
```

As demais rotas ainda não existem:

```text
/foundation
/games/:id
/awards
/data-room
/creator-log
```

---

## Testes realizados

### Lint

```powershell
npm run lint
```

Resultado:

```text
Nenhum erro encontrado
```

### Build

```powershell
npm run build
```

Resultado:

```text
Build concluído corretamente
```

### Servidor local

```powershell
npm run dev
```

Resultado:

```text
Introdução disponível em http://localhost:5173/
Home disponível em http://localhost:5173/home
```

Também foram testados:

- revelação progressiva das mensagens;
- botão para pular a sequência;
- liberação do botão de desbloqueio;
- navegação entre `/` e `/home`;
- armazenamento de acesso durante a sessão;
- carregamento da Home;
- responsividade inicial.

---

## Próxima fase

O próximo passo será:

```text
Fase 4 — Foundation Collection
```

A fase deverá:

```text
conectar o React à FastAPI
↓
configurar CORS
↓
criar os tipos dos jogos
↓
centralizar requisições em services/api.ts
↓
carregar os 66 registros
↓
criar GameCard
↓
tratar loading, success, empty e error
↓
adicionar busca, filtros e ordenação
```

A Foundation será a primeira página a utilizar diretamente os dados reais vindos do PostgreSQL por meio da FastAPI.

---

## Status final

```text
Fase 3 — Introdução e Home
Status: concluída, testada e documentada

Próxima etapa:
Fase 4 — Foundation Collection
```