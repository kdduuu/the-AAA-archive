# Front-end Visual Base Checkpoint — The AAA Archive

## Objetivo deste documento

Este documento registra a conclusão da **Fase 2 — Base visual** do front-end do projeto **The AAA Archive**.

O objetivo desta fase foi criar os fundamentos visuais e estruturais compartilhados pelas páginas internas antes da implementação da Introdução, Home, Foundation Collection, Awards History, Data Room e página individual dos jogos.

A metodologia utilizada continua sendo:

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
Fase 2 — Base visual concluída
```

A aplicação já possui:

- identidade visual global inicial;
- paleta centralizada em variáveis CSS;
- tipografia monoespaçada;
- fundo escuro;
- scanlines discretas;
- vinheta;
- estrutura compartilhada entre páginas;
- navegação superior;
- navegação contextual lateral;
- painel de estado do sistema;
- relógio em tempo real;
- painel reutilizável;
- adaptação inicial para telas menores.

A tela exibida atualmente ainda é uma prévia estrutural.

Ela não representa a Home definitiva.

---

## Fundamentos visuais globais

O arquivo:

```text
frontend/src/index.css
```

passou a concentrar os estilos globais da aplicação.

Foram criadas variáveis para:

```text
cores de fundo
cores de painéis
cores de bordas
cores de texto
estados do sistema
tipografia
espaçamentos
dimensões gerais
transições
sombras
```

Exemplos conceituais:

```text
--color-background
--color-surface
--color-border
--color-text
--color-text-muted
--color-stable
--color-error
--sidebar-width
--header-height
```

Essa centralização permitirá alterar a identidade do site sem procurar valores repetidos em vários arquivos.

---

## Paleta visual

A base visual utiliza:

```text
preto
grafite
cinza escuro
branco envelhecido
```

As cores de destaque permanecem raras e funcionais.

O verde é usado principalmente para representar:

```text
stable
online
connected
```

Cores de alerta e erro também foram previstas, mas ainda não estão sendo utilizadas nas páginas atuais.

---

## Tipografia

A interface utiliza uma pilha de fontes monoespaçadas:

```text
Consolas
Lucida Console
Courier New
monospace
```

A tipografia busca transmitir:

- terminal;
- sistema antigo;
- arquivo tecnológico;
- interface da internet antiga;
- organização técnica;
- elegância sem aparência corporativa.

Os títulos utilizam:

- caixa alta;
- peso leve;
- espaçamento entre letras;
- contraste controlado.

---

## Texturas e atmosfera

Foram adicionados efeitos globais discretos:

```text
scanlines
vinheta
granulação suave
gradientes escuros
profundidade entre diferentes tons de preto
```

Esses efeitos foram implementados principalmente utilizando:

```css
body::before
body::after
```

As camadas utilizam:

```css
pointer-events: none;
```

Dessa forma, elas não bloqueiam cliques ou interações do usuário.

Os efeitos foram mantidos discretos para não prejudicar a leitura.

---

## Normalização global

Também foram configurados estilos básicos para:

- cálculo previsível de dimensões com `box-sizing`;
- altura mínima da aplicação;
- imagens responsivas;
- fontes herdadas por formulários;
- seleção de texto;
- barra de rolagem;
- foco visível;
- redução de movimento.

A aplicação respeita a configuração:

```text
prefers-reduced-motion
```

Quando o visitante solicita menos movimento, animações e transições futuras serão reduzidas automaticamente.

---

## Estrutura global da interface

Foi criado o componente:

```text
frontend/src/components/ArchiveShell.tsx
```

Ele representa o esqueleto compartilhado pelas páginas internas.

Estrutura conceitual:

```text
ArchiveShell
│
├── identificação do arquivo
├── navegação superior
├── navegação contextual
└── conteúdo específico da página
```

O conteúdo da página é recebido por meio de:

```text
children
```

Isso permite que diferentes páginas utilizem a mesma estrutura sem repetir o cabeçalho e a lateral.

Exemplo conceitual:

```tsx
<ArchiveShell>
  conteúdo da página
</ArchiveShell>
```

---

## Navegação superior

Foi criado:

```text
frontend/src/components/TopNavigation.tsx
```

A navegação superior apresenta as áreas principais:

```text
HOME
FOUNDATION
AWARDS
DATA ROOM
```

Nesta fase, os itens ainda não realizam navegação entre páginas.

As rotas serão ativadas quando as páginas reais forem implementadas.

Também existe um painel de estado contendo:

```text
SYSTEM TIME
ARCHIVE NODE ONLINE
```

---

## Relógio do sistema

Foi criado:

```text
frontend/src/components/SystemClock.tsx
```

O componente:

- obtém o horário local;
- formata o horário;
- atualiza a informação uma vez por segundo;
- encerra corretamente o intervalo quando deixa de existir.

Conceitos utilizados:

```text
useState
useEffect
setInterval
clearInterval
```

O relógio representa o primeiro comportamento dinâmico simples do front-end.

---

## Navegação contextual

Foi criado:

```text
frontend/src/components/ContextSidebar.tsx
```

A lateral não possui mais itens fixos.

Ela recebe informações por propriedades:

```text
title
items
activeItem
```

Isso permite reutilizar a mesma lateral em diferentes páginas.

Exemplo para a Home:

```text
MAIN TERMINAL

ARCHIVE OVERVIEW
SYSTEM EVOLUTION
FEATURED RECORDS
COLLECTION ACCESS
```

Exemplo futuro para a Foundation:

```text
FOUNDATION COLLECTION

ALL RECORDS
SEARCH ARCHIVE
DECADES
YEARS
GENRES
DEVELOPERS
FRANCHISES
```

Cada página poderá controlar seus próprios itens sem duplicar a estrutura da lateral.

---

## Painel reutilizável

Foi criado:

```text
frontend/src/components/ArchivePanel.tsx
```

O componente centraliza o formato comum dos painéis:

```text
borda
cabeçalho
título
código opcional
conteúdo interno
```

Propriedades disponíveis:

```text
id
title
code
className
children
```

O componente não controla o conteúdo interno.

Cada página continua responsável por preencher seus próprios dados e textos.

Isso evita tanto repetição de estrutura quanto fragmentação excessiva.

---

## Organização atual dos componentes

Estrutura atual:

```text
frontend/
└── src/
    ├── components/
    │   ├── ArchivePanel.tsx
    │   ├── ArchiveShell.tsx
    │   ├── ContextSidebar.tsx
    │   ├── SystemClock.tsx
    │   └── TopNavigation.tsx
    │
    ├── App.css
    ├── App.tsx
    ├── index.css
    └── main.tsx
```

Foram criados somente componentes com função clara e reutilizável.

Não foram criados componentes excessivamente pequenos para títulos, parágrafos ou detalhes isolados.

---

## Prévia estrutural atual

O arquivo:

```text
frontend/src/App.tsx
```

ainda exibe uma prévia temporária contendo:

```text
hero estrutural
System Evolution reservado
Featured Records reservado
Collection Access reservado
frase final
```

Essa tela serviu para testar:

- o shell;
- a navegação superior;
- a lateral;
- os painéis;
- o relógio;
- os espaçamentos;
- a composição geral;
- o comportamento inicial em diferentes larguras.

A prévia será substituída durante a próxima fase.

---

## Responsividade inicial

A construção continua seguindo uma estratégia desktop-first.

Nesta fase já existe uma adaptação básica:

### Desktop

```text
sidebar visível
navegação superior completa
conteúdo distribuído em colunas
```

### Tablet

```text
sidebar removida
identificação exibida no topo
painéis reorganizados
```

### Mobile

```text
espaçamentos reduzidos
status simplificado
conteúdo em uma coluna
hero reorganizado
```

Essa ainda não representa a responsividade definitiva das páginas.

Cada página será posteriormente ajustada individualmente.

---

## Testes realizados

### Servidor de desenvolvimento

Comando:

```powershell
npm run dev
```

Resultado:

```text
Aplicação iniciada corretamente
Servidor disponível em http://localhost:5173/
```

---

### Verificação do código

Comando:

```powershell
npm run lint
```

Resultado:

```text
Nenhum erro encontrado
```

---

### Build de produção

Comando:

```powershell
npm run build
```

Resultado:

```text
Build concluído corretamente
Pasta dist/ gerada
```

---

## Decisões preservadas

Durante esta fase:

- nenhuma integração com a FastAPI foi iniciada;
- CORS não foi configurado;
- nenhuma rota de backend foi alterada;
- nenhuma página completa foi criada antecipadamente;
- nenhuma biblioteca adicional foi instalada;
- nenhum framework de CSS foi utilizado;
- nenhum sistema complexo de componentes foi criado;
- nenhuma animação grande foi adicionada;
- nenhum mockup foi tratado como cópia obrigatória;
- nenhuma funcionalidade fora do planejamento foi adicionada.

---

## Resultado da fase

A aplicação agora possui uma fundação visual e estrutural pronta para receber as páginas reais.

Resultado:

```text
paleta global criada
tipografia global criada
texturas criadas
shell compartilhado criado
top navigation criada
sidebar contextual criada
painel reutilizável criado
relógio criado
responsividade inicial criada
lint concluído
build concluído
```

---

## Próxima fase

O próximo passo será:

```text
Fase 3 — Introdução e Home
```

A implementação seguirá esta ordem:

```text
Introdução
↓
teste
↓
Home
↓
teste
↓
documentação
```

A Introdução substituirá a prévia atual da rota:

```text
/
```

A Home será criada na rota:

```text
/home
```

Serão adicionados progressivamente:

- sequência de inicialização;
- mensagens do sistema;
- botão `UNLOCK ARCHIVE`;
- hero principal;
- System Evolution;
- Featured Records;
- Archive Status;
- Direct Access.

As páginas serão implementadas uma por vez.

---

## Status final

```text
Fase 2 — Base visual
Status: concluída e testada

Próxima etapa:
Fase 3 — Introdução e Home
```