# Frontend Plan — The AAA Archive

## Objetivo deste documento

Este documento registra o planejamento oficial do front-end do projeto **The AAA Archive**.

Ele reúne as decisões tomadas sobre:

- proposta do site;
- identidade visual;
- experiência desejada;
- páginas;
- navegação;
- conteúdo;
- stack;
- integração com a API;
- imagens;
- responsividade;
- escopo da primeira versão;
- ordem de implementação.

Este arquivo deve servir como referência principal para futuras conversas e etapas do projeto, preservando a proposta já aprovada sem aumentar o escopo desnecessariamente.

---

# 1. Princípios do projeto

## 1.1. Regra principal

O front-end existe para apresentar bem tudo o que já foi construído no **The AAA Archive**.

Ele não deve transformar o projeto em um sistema exageradamente complexo.

A prioridade será:

```text
aproveitar o que já existe
+
criar uma apresentação pública forte
+
preservar a identidade do projeto
+
evitar novas camadas sem necessidade
```

## 1.2. Metodologia de trabalho

O desenvolvimento continuará seguindo a metodologia já utilizada no projeto:

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

Regras didáticas:

- uma etapa por vez;
- explicações simples;
- nenhuma complexidade adicionada sem motivo;
- quando um arquivo de código precisar ser alterado, ele deve ser enviado completo e reescrito, pronto para substituição;
- nenhuma tecnologia ou funcionalidade deve ser adicionada sem explicar antes sua necessidade.

## 1.3. Regra de escopo

Este é um projeto pessoal e de portfólio.

Por isso:

- não será criado um sistema de usuários;
- não haverá autenticação;
- não haverá painel administrativo;
- não haverá upload de imagens;
- não haverá comentários, favoritos ou listas pessoais;
- não haverá infraestrutura complexa;
- não haverá ferramentas novas apenas para “modernizar” o projeto.

O front-end deve valorizar o projeto, não transformá-lo em outra aplicação gigantesca.

---

# 2. Visão do projeto

## 2.1. O que é o The AAA Archive

O **The AAA Archive** é um museu digital dedicado à memória, à história e à evolução dos videogames.

O projeto nasceu da vontade de revisitar jogos marcantes ao longo da vida de seu criador.

Com o tempo, a proposta foi ampliada para incluir também:

- jogos historicamente importantes;
- obras que contribuíram para a evolução do meio;
- jogos não necessariamente jogados pelo criador, mas relevantes para a história;
- registros de premiações;
- uma pequena camada histórica sobre consoles e evolução técnica;
- uma camada analítica de dados.

A aplicação não pretende catalogar todos os jogos existentes.

Ela apresenta uma seleção curada.

## 2.2. Centro do projeto

A hierarquia principal será:

```text
Centro do projeto
→ jogos e história dos videogames

Foundation Collection
→ acervo principal do museu

Awards History
→ contexto histórico complementar

Data Room
→ camada analítica

Busca e filtros
→ ferramentas para explorar o acervo
```

## 2.3. Objetivo da aplicação

A aplicação web deverá:

- apresentar a Foundation Collection;
- contextualizar brevemente a evolução dos videogames;
- mostrar os jogos como obras e registros históricos;
- permitir busca e exploração do acervo;
- apresentar vencedores e indicados de Game of the Year;
- preservar a origem pessoal do projeto;
- demonstrar a arquitetura técnica desenvolvida ao longo do aprendizado.

## 2.4. Público de referência

O projeto é, em primeiro lugar, feito para o próprio criador.

Como referência estética e cultural, ele conversa com:

- público gamer mais nichado;
- pessoas interessadas em jogos single-player;
- admiradores da história dos videogames;
- pessoas que enxergam jogos como obras artísticas e culturais;
- visitantes atraídos por estética retrô, escura e alternativa;
- estudantes ou desenvolvedores interessados na construção técnica do projeto.

O acervo não é guiado apenas pela popularidade atual.

Jogos famosos podem estar presentes, desde que façam sentido dentro da curadoria.

---

# 3. Experiência desejada

## 3.1. Conceito principal

A aplicação deve transmitir a sensação de acessar um arquivo antigo, parcialmente esquecido, ainda funcionando em alguma parte perdida da internet.

A experiência combina:

```text
museu digital
+
arquivo tecnológico antigo
+
site perdido da internet
+
fliperama depois que todos foram embora
```

## 3.2. Atmosfera

A atmosfera deve ser:

- escura;
- íntima;
- silenciosa;
- melancólica;
- nostálgica;
- tecnológica;
- retrô;
- elegante;
- levemente abandonada.

A nostalgia não deve ser infantil ou cartunesca.

A ideia não é um arcade cheio de cores e personagens.

A ideia é:

> um fliperama depois que todos foram embora.

## 3.3. Relação com o projeto seemilyplay

O projeto será fortemente inspirado na estética do **seemilyplay**, principalmente em:

- paleta escura;
- bordas finas;
- tipografia de sistema;
- painéis;
- espaços vazios;
- mensagens ambientais;
- aparência de interface antiga;
- contraste entre tecnologia e memória.

Porém, o The AAA Archive não será uma cópia.

A diferença conceitual será:

```text
seemilyplay
→ navegador pessoal encontrado

The AAA Archive
→ sistema de preservação de videogames encontrado
  dentro de um museu ou fliperama abandonado
```

O novo projeto poderá reutilizar o DNA visual, mas não deve repetir exatamente:

- a janela de navegador central;
- o menu File / Edit / View;
- a mesma composição;
- o mesmo fluxo de páginas;
- as mesmas divisões internas.

---

# 4. Identidade visual

## 4.1. Direção oficial

A direção visual aprovada é representada pelos mockups conceituais criados para:

- Introdução;
- Home;
- Foundation Collection;
- Página individual do jogo;
- Awards History;
- Data Room.

Essas imagens devem ser tratadas como referência visual oficial juntamente com este documento.

## 4.2. Paleta

A base será formada por:

- preto;
- grafite;
- cinza muito escuro;
- cinza metálico;
- branco envelhecido;
- pequenos acentos funcionais.

Cores de destaque serão raras.

Possíveis usos:

- verde discreto para estado estável;
- vermelho discreto para falha ou registro não confirmado;
- pequenos destaques em hover;
- item ativo de navegação.

## 4.3. Contraste

O contraste será controlado.

A profundidade virá principalmente de diferentes tons de preto e cinza, e não de muitas cores.

Exemplo conceitual:

```text
fundo geral
→ quase preto

painéis
→ grafite muito escuro

cabeçalhos
→ um tom levemente mais claro

bordas
→ cinza discreto

texto principal
→ branco envelhecido
```

## 4.4. Tipografia

A interface deve utilizar tipografias com aparência:

- monoespaçada;
- de sistema;
- terminal;
- internet antiga;
- técnica, mas elegante.

Títulos:

- caixa alta;
- espaçamento entre letras;
- grande presença visual.

Textos editoriais:

- legíveis;
- linhas curtas;
- tamanho confortável.

## 4.5. Texturas e efeitos

A interface pode utilizar com moderação:

- scanlines;
- ruído suave;
- granulação;
- vinheta;
- sombras discretas;
- brilho mínimo;
- cursor piscando;
- pequenas animações de revelação.

O efeito deve enriquecer a experiência, nunca prejudicar a leitura.

## 4.6. Minimalismo

O minimalismo não significa esvaziar o site.

A referência continua sendo a riqueza visual dos mockups.

A regra será:

```text
organização
+
hierarquia
+
espaçamento
+
ausência de poluição
```

Painéis, informações de sistema, imagens e detalhes continuarão presentes.

---

# 5. Idioma

## 5.1. Mistura controlada

O site utilizará uma mistura controlada de inglês e português.

A regra será:

```text
inglês
→ interface, menus, comandos e títulos técnicos

português
→ conteúdo histórico, editorial e explicativo
```

## 5.2. Exemplos em inglês

- HOME
- FOUNDATION
- AWARDS
- DATA ROOM
- SYSTEM EVOLUTION
- ARCHIVE STATUS
- UNLOCK ARCHIVE
- HISTORICAL IMPORTANCE
- INFLUENCE & LEGACY
- ARCHIVE METADATA

## 5.3. Exemplos em português

- textos sobre a história dos consoles;
- explicações sobre jogos;
- curadoria;
- importância histórica;
- relação emocional e cultural;
- creator.log.

## 5.4. Contraste de voz

```text
a máquina fala em inglês
+
o arquivista fala em português
```

---

# 6. Voz editorial

## 6.1. Mistura controlada

A voz editorial será uma mistura entre:

- informação histórica;
- clareza;
- escrita simples;
- pequenas frases poéticas.

Proporção aproximada:

```text
80% informação
20% atmosfera
```

## 6.2. Regra editorial

O conteúdo deve:

- informar primeiro;
- emocionar depois;
- evitar exagero;
- evitar melodrama;
- evitar frases abstratas sem conteúdo;
- evitar apresentar a coleção como uma lista definitiva dos “melhores jogos da história”.

## 6.3. Exemplo

```text
HISTORICAL IMPORTANCE

Silent Hill 2 colocou culpa, luto e memória no centro de uma
experiência de terror psicológico. Sua narrativa influenciou
jogos que passaram a tratar o horror de forma mais íntima.

Algumas cidades desaparecem quando desligamos o console.
Silent Hill continua esperando.
```

## 6.4. Regra que resume a voz

> O arquivo informa com clareza, mas às vezes se lembra de que está preservando memórias.

---

# 7. Estrutura oficial do site

A primeira versão terá sete áreas:

```text
1. Introdução
2. Home
3. Foundation Collection
4. Página individual do jogo
5. Awards History
6. Data Room
7. creator.log
```

Estrutura geral:

```text
Introdução
↓
Home
├── Foundation Collection
│   └── Registro individual do jogo
├── Awards History
├── Data Room
└── creator.log oculto
```

---

# 8. Introdução

## 8.1. Função

A introdução será a porta de entrada do arquivo.

Ela deve parecer uma sequência curta de restauração e desbloqueio de sistema.

## 8.2. Fluxo aprovado

```text
signal detected...
↓
restoring archive node...
↓
database integrity verified...
↓
access granted
↓
[ UNLOCK ARCHIVE ]
```

## 8.3. Conteúdo aprovado

```text
THE AAA ARCHIVE
digital preservation system

> signal detected...
> restoring archive node...
> database integrity verified...
> foundation records: 66
> awards logs: 127
> access level: visitor

ACCESS GRANTED

[ UNLOCK ARCHIVE ]

the past is not gone. it is archived.
```

## 8.4. Comportamento

- as mensagens aparecem progressivamente;
- a sequência deve durar poucos segundos;
- o botão aparece ao final;
- a introdução pode ser pulada;
- ela não deve reaparecer a cada navegação;
- ela não deve depender da API para funcionar.

---

# 9. Home

## 9.1. Função

A Home será o hall principal do museu.

Ela deve:

- apresentar a proposta;
- criar a atmosfera;
- contextualizar a história dos videogames;
- apresentar registros em destaque;
- conduzir para as áreas principais.

## 9.2. Estrutura aprovada

A Home terá:

- hero principal;
- System Evolution;
- Featured Records;
- Archive Status;
- Direct Access;
- rodapé com frase ambiental;
- creator.log escondido em algum detalhe.

## 9.3. Hero principal

O hero terá:

- título THE AAA ARCHIVE;
- pequeno texto editorial;
- imagem ampla de fliperama abandonado ou ambiente de arquivo;
- estado do sistema.

Texto conceitual aprovado:

```text
Preservamos o que o tempo esquece.
Fragmentos de código, arte e som —
memórias de mundos antes jogados.
É aqui que eles continuam.
```

Status:

```text
> archive integrity: stable
```

## 9.4. System Evolution

A Home terá uma área curta sobre a evolução dos videogames.

O foco será:

```text
consoles
+
evolução gráfica
+
processamento
+
mudanças na forma de jogar
+
jogos e personagens emblemáticos
```

A seção será resumida e fácil de absorver.

Divisão inicial:

### Early Systems / Arcades

- arcades;
- Pong;
- Space Invaders;
- Atari 2600;
- popularização dos videogames dentro de casa.

### 8 & 16-Bit Era

- NES;
- Master System;
- Mega Drive;
- Super Nintendo;
- sprites mais detalhados;
- trilhas maiores;
- fortalecimento das franquias.

Ícones e personagens possíveis:

- Mario;
- Sonic;
- Donkey Kong;
- Link;
- Samus;
- Mega Man.

### 3D Transition

- PlayStation;
- Nintendo 64;
- Sega Saturn;
- gráficos poligonais;
- câmeras 3D;
- CDs;
- mundos maiores.

Jogos e símbolos possíveis:

- Super Mario 64;
- Final Fantasy VII;
- Metal Gear Solid;
- Resident Evil;
- Crash Bandicoot;
- Ocarina of Time.

### Sixth Generation

- PlayStation 2;
- Dreamcast;
- GameCube;
- Xbox;
- modelos mais detalhados;
- narrativas mais maduras;
- consolidação de experiências cinematográficas.

### HD Era

- Xbox 360;
- PlayStation 3;
- Nintendo Wii;
- alta definição;
- física e iluminação avançadas;
- serviços online;
- controles de movimento.

### Modern Systems

- PlayStation 4;
- Xbox One;
- Nintendo Switch;
- PlayStation 5;
- Xbox Series;
- mundos mais complexos;
- carregamentos rápidos;
- maior fidelidade visual.

## 9.5. Featured Records

A Home mostrará poucos jogos em destaque.

Exemplo aprovado:

- Super Mario 64;
- Metal Gear Solid;
- Silent Hill 2;
- The Last of Us.

Cada entrada terá:

- pequena imagem;
- título;
- ano;
- desenvolvedora;
- frase editorial curta.

## 9.6. Archive Status

Painel com métricas reais e simples:

- Foundation Records: 66;
- Awards Logs: 127;
- Archive Period: 1993—2025;
- Node Status: Stable.

## 9.7. Direct Access

Acessos principais:

```text
[ ENTER FOUNDATION ]
[ OPEN AWARDS LOG ]
[ ENTER DATA ROOM ]
```

---

# 10. Foundation Collection

## 10.1. Função

A Foundation Collection será o acervo principal do museu.

## 10.2. Estrutura

A página terá:

- header da coleção;
- imagem atmosférica;
- barra de pesquisa;
- filtros;
- ordenação;
- grid de jogos;
- navegação lateral contextual.

## 10.3. Navegação lateral

```text
ALL RECORDS
SEARCH ARCHIVE
DECADES
YEARS
GENRES
DEVELOPERS
FRANCHISES
```

## 10.4. Search Terminal

```text
SEARCH TERMINAL

Search by title, developer, franchise, or keyword...

[ EXECUTE ]
```

## 10.5. Filtros

Filtros simples:

- década;
- ano;
- gênero;
- desenvolvedora;
- franquia.

Não será criado um sistema complexo de combinações avançadas.

## 10.6. Ordenação

Opções iniciais:

- ano mais recente;
- ano mais antigo;
- nome.

## 10.7. Cards

Cada card mostrará:

- imagem;
- ano;
- título;
- desenvolvedora;
- plataforma, quando fizer sentido.

Informações mais detalhadas ficarão na página individual.

## 10.8. Tratamento visual das imagens

```text
estado normal
→ escura e desaturada

hover
→ aumenta contraste
→ parte da cor retorna

registro aberto
→ imagem mais visível
```

## 10.9. Estado sem resultado

```text
NO RECORDS FOUND

Nenhum registro corresponde aos termos consultados.

[ CLEAR SEARCH ]
```

## 10.10. Limites

Não entra na primeira versão:

- paginação complexa;
- carregamento infinito;
- combinação de muitos filtros;
- múltiplos modos avançados;
- sistema de favoritos.

---

# 11. Página individual do jogo

## 11.1. Função

A página individual deve parecer uma ficha preservada dentro do museu.

Não deve parecer uma wiki ou loja.

## 11.2. Estrutura

- breadcrumb;
- título;
- ano;
- desenvolvedora;
- plataforma;
- gênero;
- franquia;
- imagem hero;
- descrição editorial;
- importância histórica;
- influência e legado;
- dados do arquivo;
- contexto da era;
- relação com premiações, quando existir;
- notas pessoais de forma discreta.

## 11.3. Navegação lateral

```text
RECORD OVERVIEW
HISTORICAL NOTES
ARCHIVE DATA
ERA CONTEXT
RELATED RECORDS
```

## 11.4. Painéis principais

```text
EDITORIAL DESCRIPTION
HISTORICAL IMPORTANCE
INFLUENCE & LEGACY
ARCHIVE METADATA
ERA CONTEXT
```

## 11.5. Notas pessoais

As notas continuarão disponíveis, mas discretas.

Exemplo:

```text
ARCHIVE DATA

Metacritic ........ 89
Kadu .............. 10.0
Pavam ............. —
```

A possível remoção de `nota_pavam` será discutida futuramente.

Nenhuma alteração deve ser feita agora.

## 11.6. Campos vazios

```text
campo vazio
→ não exibir
```

## 11.7. Limites

Não entra na primeira versão:

- galeria grande;
- carrosséis excessivos;
- dezenas de abas;
- recomendações automáticas;
- grande lista de premiações;
- conteúdo longo demais.

---

# 12. Awards History

## 12.1. Função

A Awards History será um registro histórico dos vencedores e indicados de Game of the Year.

## 12.2. Atmosfera

A sensação deve ser:

```text
a cerimônia já terminou
↓
as pessoas foram embora
↓
restaram apenas os registros
```

## 12.3. Apresentação

A página será principalmente tipográfica.

Imagens:

- poucas;
- escuras;
- atmosféricas;
- nunca em uma grade barulhenta.

## 12.4. Navegação lateral

```text
ALL YEARS
WINNERS
2003—2009
2010—2019
2020—2025
FOUNDATION MATCHES
```

## 12.5. Ano inicial

A página abrirá em:

```text
2003
```

A ideia é começar a história pelo primeiro registro.

## 12.6. Estrutura

- hero da seção;
- Year Index;
- Selected Year;
- vencedor;
- indicados;
- Foundation Status;
- About the Award;
- rodapé.

## 12.7. Registro do ano

Exemplo:

```text
SELECTED YEAR

2003

Spike Video Game Awards
GAME OF THE YEAR

VENCEDOR
...

INDICADOS
...
```

## 12.8. Foundation Status

Painel mostrando se o vencedor está na Foundation Collection.

Estados possíveis:

- CONFIRMED;
- NOT ARCHIVED;
- NOT CONFIRMED.

Quando houver relação:

```text
[ VIEW FOUNDATION RECORD ]
```

## 12.9. About the Award

Texto curto sobre:

- Spike Video Game Awards;
- VGX;
- The Game Awards.

Não será uma história completa das cerimônias.

## 12.10. Limites

Não entra:

- todas as categorias;
- vídeos;
- discursos;
- rankings de vencedores;
- votação;
- análise extensa.

---

# 13. Data Room

## 13.1. Função

A Data Room será a sala técnica do museu.

```text
nas outras páginas
→ os jogos são lembrados como obras

na Data Room
→ os jogos são observados como dados
```

## 13.2. Estrutura

A Data Room será uma mistura de:

- métricas simples;
- poucos gráficos integrados;
- acesso ao dashboard Streamlit completo.

## 13.3. Navegação lateral

```text
ARCHIVE METRICS
FOUNDATION DATA
AWARDS DATA
OPEN DASHBOARD
SYSTEM INFORMATION
```

## 13.4. Archive Metrics

- Foundation Records: 66;
- Awards Logs: 127;
- Archive Period: 1993—2025;
- Awards Period: 2003—2025.

## 13.5. Gráficos

Poucos gráficos:

- jogos por década;
- distribuição por gênero;
- desenvolvedoras com mais registros.

Eles devem seguir o visual do site:

- fundo escuro;
- escala de cinza;
- linhas finas;
- quase nenhuma cor;
- sem aparência corporativa.

## 13.6. Dashboard completo

```text
[ OPEN ANALYTICAL DASHBOARD ]
```

O botão abrirá o Streamlit em outra aba.

O front-end não irá reconstruir todo o dashboard.

## 13.7. System Information

```text
Data Source ........ PostgreSQL
Processing ......... Python / Pandas
API Layer .......... FastAPI
Dashboard .......... Streamlit
Status ............. Online
```

## 13.8. Limites

A Data Room não deve virar um segundo sistema.

Ela é apenas uma prévia analítica.

---

# 14. creator.log

## 14.1. Função

O creator.log será a área escondida equivalente a uma página “Sobre”.

## 14.2. Conteúdo

- origem do projeto;
- motivação;
- visão do arquivo;
- critério da Foundation Collection;
- tecnologias;
- autoria;
- repositório.

## 14.3. Tom

Mais íntimo e autoral.

Exemplo conceitual:

```text
Este arquivo começou como uma tentativa de lembrar.

Alguns dos jogos registrados aqui fizeram parte da minha vida.
Outros chegaram antes de mim, mas ajudaram a construir tudo
o que encontrei quando comecei a jogar.

O objetivo nunca foi guardar todos eles.
Apenas aqueles que ainda parecem emitir algum sinal.
```

## 14.4. Descoberta

Não aparecerá no menu principal.

Pode ser acessado por:

- número da versão;
- node ID;
- texto do rodapé;
- pequeno arquivo escondido.

---

# 15. Easter eggs

## 15.1. Regra

Os easter eggs serão:

- opcionais;
- pequenos;
- simples;
- recompensas para curiosidade;
- nunca obrigatórios para navegar.

## 15.2. Possibilidades

- clicar em ARCHIVE NODE ONLINE;
- pequenos arquivos ocultos;
- mensagens raras;
- frases escondidas;
- alterações discretas;
- creator.log;
- referências a jogos da coleção;
- horários ou datas estranhas.

## 15.3. Prioridade

Primeiro o site deve funcionar.

Easter eggs serão adicionados somente depois.

---

# 16. Navegação

## 16.1. Navegação híbrida

A navegação oficial será:

```text
topo
→ áreas principais

lateral
→ opções internas da seção atual
```

## 16.2. Top navigation

```text
HOME
FOUNDATION
AWARDS
DATA ROOM
```

creator.log não aparece.

## 16.3. Side navigation

A lateral muda conforme a página.

Exemplos:

### Home

```text
ARCHIVE OVERVIEW
SYSTEM EVOLUTION
FEATURED RECORDS
COLLECTION ACCESS
```

### Foundation

```text
ALL RECORDS
SEARCH ARCHIVE
DECADES
YEARS
GENRES
DEVELOPERS
FRANCHISES
```

### Awards

```text
ALL YEARS
WINNERS
2003—2009
2010—2019
2020—2025
FOUNDATION MATCHES
```

### Data Room

```text
ARCHIVE METRICS
FOUNDATION DATA
AWARDS DATA
OPEN DASHBOARD
SYSTEM INFORMATION
```

---

# 17. Stack oficial

## 17.1. Stack aprovada

```text
React para web
+
Vite
+
TypeScript básico
+
React Router
+
CSS personalizado
+
Fetch API
```

## 17.2. Papel de cada tecnologia

```text
React
→ componentes e comportamento

Vite
→ ambiente de desenvolvimento e build

TypeScript
→ tipos básicos e segurança dos dados

React Router
→ rotas e páginas

CSS
→ identidade visual

Fetch API
→ comunicação com a FastAPI
```

## 17.3. O que não será usado

```text
React Native
Next.js
Tailwind
Bootstrap
Redux
Axios
bibliotecas prontas de componentes
bibliotecas grandes de animação
```

## 17.4. TypeScript

O TypeScript será usado apenas no necessário:

- tipos dos jogos;
- tipos de premiações;
- props;
- respostas da API;
- campos opcionais.

Sem recursos avançados desnecessários.

---

# 18. Arquitetura geral

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

Dashboard:

```text
Data Room
↓
Streamlit
↓
PostgreSQL
```

O React nunca acessará o banco diretamente.

---

# 19. Rotas planejadas

```text
/
→ introdução

/home
→ hall principal

/foundation
→ coleção

/games/:id
→ página individual

/awards
→ premiações

/data-room
→ análises

/creator-log
→ arquivo oculto
```

A rota exata pode ser ajustada na implementação, mas essa é a organização aprovada.

---

# 20. Integração com a FastAPI

## 20.1. Serviço central

Chamadas de API não devem ficar espalhadas pelos componentes.

Estrutura prevista:

```text
src/
└── services/
    └── api.ts
```

Funções conceituais:

```text
getGames()
searchGames(term)
getGamesByDecade(decade)
getGamesByYear(year)
getGamesByGenre(genre)
getGamesByDeveloper(developer)
getGamesByFranchise(franchise)
getGameById(id)
getAwardsByYear(year)
getHomeStats()
```

## 20.2. Endpoints atuais

### Home / Data Room

```text
GET /stats/home
```

### Foundation

```text
GET /games
GET /games/search
GET /games/developer/{developer}
GET /games/genre/{genre}
GET /games/franchise/{franchise}
GET /games/year/{year}
GET /games/decade/{decade}
```

### Awards

```text
GET /awards
GET /awards/winners
GET /awards/{year}
GET /awards/foundation/winners
GET /awards/foundation/nominees
GET /awards/foundation/outside
```

## 20.3. Novo endpoint necessário

A página individual provavelmente exigirá:

```text
GET /games/{id}
```

Esse endpoint só será criado quando a implementação da página individual começar.

Não será criado antecipadamente.

## 20.4. CORS

CORS será configurado somente quando o React fizer a primeira comunicação real com a FastAPI.

Não será adicionado antes.

---

# 21. Estados da interface

## 21.1. Estados principais

```text
LOADING
SUCCESS
EMPTY
ERROR
```

## 21.2. Loading

Exemplo:

```text
RETRIEVING RECORDS...

> connecting to archive node
> requesting foundation collection
> awaiting response
```

## 21.3. Empty

```text
NO RECORDS FOUND

Nenhum registro corresponde aos termos consultados.
```

## 21.4. Error

```text
ARCHIVE NODE UNAVAILABLE

Não foi possível estabelecer conexão com o servidor de dados.

[ RETRY CONNECTION ]
```

## 21.5. Regras

- nunca mostrar erro técnico cru;
- não usar loaders coloridos;
- refazer somente a consulta necessária;
- uma falha parcial não deve derrubar a página inteira;
- a introdução continua funcionando mesmo sem API.

---

# 22. Responsividade

## 22.1. Estratégia

```text
desktop
→ experiência completa

tablet
→ painéis reorganizados

mobile
→ interface adaptada, não apenas encolhida
```

## 22.2. Desktop-first

A construção começa no desktop porque os mockups foram aprovados nesse formato.

Cada página seguirá:

```text
desktop
↓
tablet
↓
mobile
↓
teste
↓
próxima página
```

## 22.3. Top navigation no mobile

```text
THE AAA ARCHIVE        [ MENU ]
```

O menu abrirá como painel escuro.

## 22.4. Side navigation no mobile

A lateral vira botão contextual.

Exemplo:

```text
[ COLLECTION INDEX ]
```

## 22.5. Home no mobile

Ordem sugerida:

```text
hero
↓
Direct Access
↓
Featured Records
↓
System Evolution
↓
Archive Status
```

## 22.6. Foundation no mobile

- uma ou duas colunas;
- filtros recolhíveis;
- busca em linha própria;
- cards legíveis;
- hover não será necessário.

## 22.7. Página individual no mobile

```text
título
↓
dados principais
↓
imagem
↓
descrição
↓
importância
↓
influência
↓
dados do arquivo
↓
Awards
```

## 22.8. Awards no mobile

O índice pode virar:

```text
SELECT YEAR
[ 2003 ▼ ]
```

## 22.9. Data Room no mobile

Cada gráfico ocupará uma linha.

---

# 23. Imagens e assets

## 23.1. Estrutura

```text
frontend/
└── public/
    └── assets/
        ├── games/
        ├── history/
        ├── awards/
        ├── interface/
        ├── textures/
        ├── placeholders/
        └── hidden/
```

## 23.2. Jogos

Organização por ID:

```text
games/
├── 1/
│   ├── cover.webp
│   └── hero.webp
├── 2/
│   ├── cover.webp
│   └── hero.webp
```

Isso evita problemas com nomes repetidos, como God of War.

## 23.3. Funções

```text
cover.webp
→ Foundation e listas

hero.webp
→ página individual e destaques
```

## 23.4. Featured Records

Reutiliza `hero.webp` inicialmente.

`featured.webp` será opcional.

## 23.5. System Evolution

```text
history/
├── early-systems.webp
├── eight-sixteen-bit.webp
├── three-d-transition.webp
├── sixth-generation.webp
├── hd-era.webp
└── modern-systems.webp
```

## 23.6. Awards

Poucas imagens.

A página será majoritariamente tipográfica.

## 23.7. Formatos

```text
WebP
→ capas, screenshots e artes

SVG
→ ícones e elementos simples

PNG
→ apenas quando transparência for necessária
```

## 23.8. Placeholders

```text
game-cover.webp
game-hero.webp
image-unavailable.webp
```

## 23.9. Tratamento visual

O escurecimento e a desaturação serão feitos com CSS.

Não serão salvas várias versões da mesma imagem.

## 23.10. Fontes das imagens

Será criado futuramente:

```text
docs/image_sources.md
```

O arquivo registrará origem e observações dos materiais usados.

---

# 24. Organização inicial do front-end

Estrutura conceitual:

```text
frontend/
├── public/
│   └── assets/
├── src/
│   ├── components/
│   ├── pages/
│   ├── services/
│   ├── styles/
│   ├── types/
│   └── main.tsx
├── index.html
├── package.json
├── tsconfig.json
└── vite.config.ts
```

Essa estrutura pode ser ajustada durante a criação.

Não deve ser fragmentada além do necessário.

---

# 25. Componentes conceituais

Possíveis componentes:

```text
TopNavigation
ContextSidebar
ArchivePanel
SystemStatus
GameCard
SearchTerminal
LoadingPanel
ErrorPanel
YearIndex
FoundationStatus
```

Eles serão criados apenas quando realmente forem reutilizados.

Não será criado um sistema complexo de componentes antecipadamente.

---

# 26. Deploy

## 26.1. Regra

Deploy não é prioridade agora.

Primeiro tudo deve funcionar localmente.

## 26.2. Ambiente local

```text
React
→ localhost:5173

FastAPI
→ localhost:8000

PostgreSQL
→ localhost:5432

Streamlit
→ localhost:8501
```

## 26.3. Custo

A primeira versão pública deve possuir uma opção com custo mensal de R$ 0.

Nenhum serviço pago deve ser obrigatório.

As condições dos planos gratuitos devem ser verificadas novamente apenas quando o deploy começar.

## 26.4. Simplicidade

O deploy não deve virar uma nova fase gigantesca.

A escolha final das plataformas será feita no final, com foco em:

- custo zero;
- pouca configuração;
- manutenção simples;
- funcionamento suficiente para portfólio.

---

# 27. Escopo real da primeira versão

## 27.1. O que entra

- introdução;
- Home;
- Foundation;
- página individual;
- Awards;
- Data Room simples;
- creator.log;
- busca e filtros básicos;
- responsividade;
- integração com a API;
- poucos easter eggs;
- identidade visual completa.

## 27.2. O que não entra

- autenticação;
- usuários;
- comentários;
- favoritos;
- listas pessoais;
- painel administrativo;
- uploads;
- CMS;
- sistema de cadastro;
- Redux;
- Next.js;
- Tailwind;
- Axios;
- testes de front-end excessivamente complexos;
- múltiplas galerias por jogo;
- infraestrutura cara;
- recursos criados apenas para aumentar o projeto.

---

# 28. Roadmap de implementação

## Fase 1 — Preparação

- criar o projeto React;
- configurar Vite;
- configurar TypeScript básico;
- instalar React Router;
- criar a pasta `frontend/`.

## Fase 2 — Base visual

- criar variáveis de cores;
- definir tipografia;
- criar fundo e texturas;
- criar layout global;
- criar top navigation;
- criar contextual sidebar;
- criar painéis reutilizáveis.

## Fase 3 — Introdução e Home

- implementar introdução;
- criar sequência de mensagens;
- criar botão UNLOCK ARCHIVE;
- implementar Home;
- criar System Evolution;
- criar Featured Records;
- criar Archive Status;
- criar Direct Access.

## Fase 4 — Foundation

- conectar à API;
- carregar os 66 jogos;
- criar GameCard;
- criar busca;
- criar filtros simples;
- criar ordenação;
- tratar loading, empty e error.

## Fase 5 — Página individual

- criar `GET /games/{id}`;
- testar o endpoint;
- criar a rota;
- implementar página individual;
- ocultar campos vazios;
- exibir notas discretamente.

## Fase 6 — Awards

- abrir em 2003;
- criar Year Index;
- carregar vencedor e indicados;
- criar Foundation Status;
- criar About the Award.

## Fase 7 — Data Room

- carregar métricas;
- criar poucos gráficos;
- criar System Information;
- criar botão para Streamlit.

## Fase 8 — Responsividade e easter eggs

- adaptar desktop;
- adaptar tablet;
- adaptar mobile;
- criar creator.log;
- adicionar pequenos easter eggs.

## Fase 9 — Revisão

- revisar visual;
- revisar textos;
- testar rotas;
- testar API;
- testar erros;
- documentar.

## Fase 10 — Deploy

- verificar opções gratuitas atuais;
- publicar banco e API;
- publicar front-end;
- publicar dashboard;
- configurar CORS;
- testar produção.

---

# 29. Regra final de implementação

```text
O front-end existe para apresentar bem
o projeto que já foi construído.

Ele não precisa provar todas as possibilidades
do desenvolvimento web.
```

Toda decisão futura deve respeitar:

```text
identidade
+
clareza
+
escopo controlado
+
uma etapa por vez
```

---

# 30. Resumo final

O **The AAA Archive** será:

```text
um museu digital sobre videogames
+
um arquivo perdido da internet
+
um sistema de preservação antigo
+
uma coleção pessoal e histórica
+
uma experiência escura, íntima e nostálgica
```

A direção visual será:

```text
preto e grafite
+
bordas finas
+
tipografia de sistema
+
imagens desaturadas
+
painéis
+
scanlines discretas
+
muito cuidado com a atmosfera
```

A direção técnica será:

```text
React
+
Vite
+
TypeScript básico
+
React Router
+
CSS personalizado
+
Fetch API
```

A arquitetura continuará:

```text
React
↓
FastAPI
↓
PostgreSQL
```

Com:

```text
Data Room
↓
Streamlit
```

Este documento deve ser tratado como a referência oficial para a implementação do front-end do **The AAA Archive**.