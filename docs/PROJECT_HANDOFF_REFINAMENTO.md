# The AAA Archive — Handoff para a Fase de Refinamento

## Como usar este arquivo no próximo chat

Envie ao novo chat:

```text
1. o ZIP mais recente do projeto;
2. este arquivo PROJECT_HANDOFF_REFINAMENTO.md;
3. o planejamento oficial do frontend;
4. os checkpoints das fases concluídas.
```

O ZIP deve representar exatamente o estado atual do projeto.

Importante:

```text
A revisão da Home proposta na Fase 8.1
AINDA NÃO FOI APLICADA.
```

Portanto, o próximo chat deve começar revisando a Home atual do ZIP e reenviando os arquivos corretos para essa etapa.

---

# 1. Identificação do projeto

Nome:

```text
The AAA Archive
```

Criador:

```text
Kadu Almeida
```

Natureza:

```text
projeto pessoal
+
projeto de portfólio
+
projeto de aprendizado
```

Proposta:

O **The AAA Archive** é um museu digital dedicado à memória, à história e à evolução dos videogames.

O projeto não pretende catalogar todos os jogos existentes.

Ele apresenta uma seleção curada de jogos AAA e single-player considerados importantes por:

- impacto histórico;
- influência;
- inovação;
- relevância artística;
- importância cultural;
- relação pessoal com o criador.

Atmosfera oficial:

```text
museu digital
+
arquivo tecnológico antigo
+
site perdido da internet
+
fliperama depois que todos foram embora
```

---

# 2. Metodologia obrigatória

O desenvolvimento deve continuar seguindo:

```text
planejar
↓
implementar uma etapa pequena
↓
testar
↓
confirmar com Kadu
↓
documentar
↓
só depois avançar
```

Regras didáticas obrigatórias:

- trabalhar uma etapa pequena por vez;
- explicar primeiro o que será feito;
- explicar por que aquilo será feito;
- mostrar quais arquivos serão alterados;
- explicar resumidamente a função de cada arquivo;
- considerar que Kadu ainda está aprendendo React e TypeScript;
- não adicionar complexidade sem necessidade;
- não instalar bibliotecas sem justificar;
- nunca antecipar várias fases ao mesmo tempo;
- sempre testar antes de avançar;
- não presumir que um teste passou sem confirmação de Kadu;
- quando um arquivo precisar ser alterado, enviar o arquivo completo;
- nunca enviar apenas trechos soltos para substituição;
- preservar a arquitetura e a identidade já aprovadas.

Formato preferido por Kadu:

```text
o que estamos fazendo
→ por que estamos fazendo
→ diretório completo
→ ação: criar, substituir ou atualizar
→ arquivo completo
→ teste
→ confirmação
→ próxima etapa
```

Kadu prefere respostas objetivas, mas serenas.

Não é necessário criar respostas enormes quando a etapa for simples.

Sempre mostrar o diretório completo, por exemplo:

```text
frontend/src/pages/HomePage.tsx
```

E indicar claramente:

```text
Ação:
criar
substituir
ou atualizar
```

---

# 3. Stack oficial

Frontend:

```text
React
Vite
TypeScript básico
React Router
CSS personalizado
Fetch API
```

Backend:

```text
Python
FastAPI
Pandas
```

Banco de dados:

```text
PostgreSQL
```

Dashboard:

```text
Streamlit
```

Testes:

```text
pytest
FastAPI TestClient
```

Tecnologias que NÃO devem ser adicionadas:

```text
Next.js
Tailwind
Bootstrap
Axios
Redux
bibliotecas prontas de componentes
bibliotecas grandes de animação
bibliotecas de gráficos sem necessidade
```

---

# 4. Arquitetura oficial

Aplicação web:

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

Fluxo dos dados:

```text
CSV
↓
PostgreSQL
↓
FastAPI
↓
JSON
↓
React
```

Regra essencial:

```text
O React nunca acessa diretamente:
- CSV;
- PostgreSQL;
- módulos Python.
```

Dashboard:

```text
Streamlit
↓
PostgreSQL
```

A Data Room do React é apenas uma prévia analítica.

O dashboard completo continua separado em Streamlit.

---

# 5. Identidade visual

Direção:

```text
escura
íntima
silenciosa
melancólica
nostálgica
tecnológica
retrô
elegante
levemente abandonada
```

Elementos visuais:

- preto;
- grafite;
- cinza escuro;
- branco envelhecido;
- bordas finas;
- tipografia monoespaçada;
- painéis;
- scanlines discretas;
- vinheta;
- ruído suave;
- sombras discretas;
- espaços vazios;
- verde discreto para estado estável;
- vermelho discreto para erro.

Regra de idioma:

```text
inglês
→ interface, menus, comandos e títulos técnicos

português
→ conteúdo histórico, editorial e explicativo
```

Regra editorial:

```text
80% informação
20% atmosfera
```

Evitar:

- aparência de loja;
- aparência de wiki;
- visual infantil de arcade;
- excesso de cores;
- excesso de animações;
- excesso de painéis sem função;
- melodrama;
- textos abstratos demais.

---

# 6. Estado geral atual

As estruturas principais do frontend foram concluídas.

```text
Fase 1 — Preparação do React
→ concluída

Fase 2 — Base visual
→ concluída

Fase 3 — Introdução e Home
→ estrutura concluída

Fase 4 — Foundation Collection
→ concluída

Fase 5 — Página individual do jogo
→ concluída

Fase 6 — Awards History
→ concluída

Fase 7 — Data Room
→ concluída

Fase 8 — Refinamento
→ próxima fase
```

A estrutura principal do site está pronta.

A próxima fase não deve reconstruir páginas do zero.

O foco agora é:

```text
revisar
refinar
corrigir
integrar valores ainda estáticos
adicionar imagens
melhorar conteúdo
testar o conjunto completo
```

---

# 7. Rotas atuais

```text
/
→ IntroductionPage

/home
→ HomePage

/foundation
→ FoundationPage

/games/:id
→ GamePage

/awards
→ AwardsPage

/data-room
→ DataRoomPage
```

A navegação superior já possui:

```text
HOME
FOUNDATION
AWARDS
DATA ROOM
```

---

# 8. Fases concluídas

## Fase 1 — Preparação

Concluído:

- React;
- Vite;
- TypeScript;
- React Router;
- estrutura frontend;
- lint;
- build.

Documento:

```text
docs/frontend/frontend_setup_checkpoint.md
```

## Fase 2 — Base visual

Concluído:

- variáveis CSS;
- tipografia;
- fundo;
- scanlines;
- vinheta;
- ArchiveShell;
- TopNavigation;
- ContextSidebar;
- ArchivePanel;
- SystemClock;
- responsividade inicial.

Documento:

```text
docs/frontend/frontend_visual_base_checkpoint.md
```

## Fase 3 — Introdução e Home

Concluído:

- rota `/`;
- rota `/home`;
- sequência da introdução;
- sessionStorage;
- estrutura visual da Home;
- System Evolution;
- Featured Records temporários;
- Archive Status temporário;
- Direct Access temporário.

Documento:

```text
docs/frontend/introduction_home_checkpoint.md
```

Importante:

```text
A Home ainda precisa de revisão.
```

## Fase 4 — Foundation Collection

Concluído:

- carregamento dos 66 jogos;
- busca;
- filtros;
- ordenação;
- estados loading, success, empty e error;
- GameCard;
- rota `/foundation`;
- navegação para a GamePage.

Documento:

```text
docs/frontend/foundation_checkpoint.md
```

## Fase 5 — GamePage

Concluído:

- endpoint individual;
- testes;
- getGameById;
- rota `/games/:id`;
- GameCard clicável;
- loading;
- success;
- not found;
- error;
- hero;
- descrição;
- marcações históricas;
- archive data;
- responsividade inicial.

Documento:

```text
docs/frontend/game_page_checkpoint.md
```

## Fase 6 — Awards History

Concluído:

- rota `/awards`;
- integração com GET /awards;
- Year Index;
- seleção por ano;
- vencedor;
- indicados;
- Foundation Status;
- link para GamePage;
- About the Award;
- estados loading, empty e error;
- responsividade.

Documento:

```text
docs/frontend/awards_history_checkpoint.md
```

## Fase 7 — Data Room

Concluído:

- rota `/data-room`;
- métricas reais;
- jogos por década;
- distribuição por gênero;
- Top 8 desenvolvedoras;
- presença dos vencedores na Foundation;
- link para Streamlit;
- estados loading, empty e error;
- responsividade inicial.

Documento:

```text
docs/frontend/data_room_checkpoint.md
```

---

# 9. Estado atual exato

A estrutura principal do frontend foi finalizada.

A próxima fase é:

```text
FASE 8 — REFINAMENTO DO FRONTEND
```

Mas a primeira alteração proposta para essa fase ainda não foi aplicada.

## Pendência imediata

A Home ainda possui acessos antigos ou bloqueados.

O próximo chat deve começar por:

```text
FASE 8.1 — REVISÃO DA HOME
```

Objetivo inicial:

```text
revisar HomePage.tsx
revisar HomePage.css
confirmar estado real no ZIP
ativar os acessos principais
```

Acessos esperados:

```text
ENTER FOUNDATION
→ /foundation

OPEN AWARDS LOG
→ /awards

ENTER DATA ROOM
→ /data-room
```

Importante:

```text
Não confiar nos arquivos de Home enviados no chat anterior.
Eles não foram aplicados por Kadu.
```

O novo chat deve inspecionar os arquivos atuais dentro do ZIP e devolver versões completas e testadas.

---

# 10. Ordem recomendada para o refinamento

## Etapa 8.1 — Revisão da Home

Primeiro:

```text
ler:
frontend/src/pages/HomePage.tsx
frontend/src/pages/HomePage.css
frontend/src/services/api.ts
frontend/src/types/HomeStats.ts
```

Verificar:

- botões Direct Access;
- valores estáticos;
- Featured Records;
- Archive Status;
- links;
- acessibilidade;
- responsividade.

Primeira alteração sugerida:

```text
ativar os três acessos da Home
```

Somente depois da confirmação:

```text
integrar métricas reais da Home
```

Depois:

```text
revisar Featured Records
```

## Etapa 8.2 — Imagens e assets

Ainda existem placeholders em:

```text
Home hero
Featured Records
Foundation hero
GameCards
GamePage
Awards hero
Data Room hero
```

Planejar antes:

```text
frontend/public/assets/
├── games/
├── history/
├── awards/
├── interface/
├── textures/
├── placeholders/
└── hidden/
```

Não adicionar imagens externas aleatórias sem discutir origem, licença, formato e organização.

## Etapa 8.3 — Revisão editorial

Revisar:

- descrições dos jogos;
- importância histórica;
- influência e legado;
- textos ambientais;
- coerência entre inglês e português.

Pendência conhecida:

```text
Silent Hill está na Foundation.
Silent Hill 2 ainda não está.
```

Essa revisão deverá envolver:

```text
games.csv
PostgreSQL
testes
contagens
documentação
```

Não corrigir apenas um jogo isoladamente sem revisar o conjunto.

## Etapa 8.4 — Revisão visual e responsiva

Testar:

- desktop;
- notebook;
- tablet;
- celular;
- textos longos;
- nomes longos;
- painéis vazios;
- navegação por teclado;
- foco visível;
- prefers-reduced-motion.

## Etapa 8.5 — Revisão técnica final

Executar:

```powershell
python -m pytest api/test_main.py -v
```

```powershell
cd frontend
npm run lint
npm run build
```

Também testar:

```text
todas as rotas
todos os links
estados de erro
API desligada
IDs inválidos
responsividade
Streamlit
```

## Etapa 8.6 — Documentação final

Atualizar:

```text
README.md
PROJECT_HANDOFF
checkpoints
estrutura do projeto
comandos
rotas
endpoints
estado final
```

## Etapa 8.7 — Deploy

Somente depois:

```text
publicar PostgreSQL
publicar FastAPI
publicar React
publicar ou configurar Streamlit
trocar URLs locais
testar ambiente publicado
```

---

# 11. Arquivos que o novo chat deve ler primeiro

Ordem recomendada:

```text
1. PROJECT_HANDOFF_REFINAMENTO.md
2. frontend_plan.md
3. ZIP mais recente
4. docs/frontend/introduction_home_checkpoint.md
5. docs/frontend/foundation_checkpoint.md
6. docs/frontend/game_page_checkpoint.md
7. docs/frontend/awards_history_checkpoint.md
8. docs/frontend/data_room_checkpoint.md
9. frontend/src/pages/HomePage.tsx
10. frontend/src/pages/HomePage.css
11. frontend/src/services/api.ts
12. frontend/src/types/HomeStats.ts
13. frontend/src/App.tsx
14. frontend/src/components/TopNavigation.tsx
```

Não é necessário reanalisar todo o backend antes da primeira revisão da Home.

O ZIP deve ser usado para confirmar o estado real.

---

# 12. Comandos locais

Backend:

```powershell
fastapi dev api/main.py
```

FastAPI:

```text
http://127.0.0.1:8000
```

Documentação:

```text
http://127.0.0.1:8000/docs
```

Frontend:

```powershell
cd frontend
npm run dev
```

React:

```text
http://localhost:5173
```

Lint:

```powershell
npm run lint
```

Build:

```powershell
npm run build
```

Testes backend:

```powershell
python -m pytest api/test_main.py -v
```

Streamlit:

```powershell
python -m streamlit run dashboard/app.py
```

Streamlit:

```text
http://localhost:8501
```

---

# 13. Regras para o próximo assistente

O próximo assistente deve:

- ler este handoff antes de propor mudanças;
- inspecionar o ZIP;
- não reiniciar o planejamento;
- não trocar a stack;
- não reescrever páginas do zero;
- não criar componentes sem necessidade;
- não instalar bibliotecas;
- não alterar vários arquivos quando poucos bastam;
- devolver arquivos completos;
- sempre mostrar o diretório completo;
- indicar se a ação é criar, substituir ou atualizar;
- explicar o que está sendo feito;
- explicar por que está sendo feito;
- explicar resumidamente a função de cada arquivo;
- testar lint e build antes de enviar;
- pedir confirmação do teste no navegador;
- avançar somente após a confirmação;
- preservar a estética;
- preservar os endpoints;
- preservar os testes existentes;
- manter o projeto simples;
- tratar o ZIP mais recente como fonte final.

---

# 14. Mensagem pronta para abrir o próximo chat

Copie e cole:

```text
Olá! Quero continuar o desenvolvimento do meu projeto The AAA Archive.

A estrutura principal do frontend já foi concluída e agora estamos entrando na fase de refinamento.

Estou enviando:

1. o ZIP mais recente do projeto;
2. o arquivo PROJECT_HANDOFF_REFINAMENTO.md;
3. o planejamento oficial do frontend;
4. os checkpoints das fases concluídas.

Leia primeiro o PROJECT_HANDOFF_REFINAMENTO.md e depois inspecione o ZIP antes de propor mudanças.

Regras obrigatórias:

- uma etapa pequena por vez;
- explique primeiro o que vamos fazer e por quê;
- sou iniciante em React e TypeScript;
- sempre mostre o diretório completo;
- diga se devo criar, substituir ou atualizar o arquivo;
- envie arquivos completos, nunca apenas trechos;
- teste lint e build antes de avançar;
- não presuma que o teste no navegador passou;
- não instale bibliotecas sem necessidade;
- preserve React + Vite + TypeScript básico + React Router + CSS + Fetch API;
- preserve React → FastAPI → PostgreSQL;
- não use Next.js, Tailwind, Bootstrap, Axios ou Redux;
- não reinicie o projeto do zero;
- mantenha respostas objetivas, mas didáticas e serenas.

Estado atual:

- Foundation concluída;
- GamePage concluída;
- Awards concluída;
- Data Room concluída;
- estrutura principal do site concluída;
- fase atual: refinamento.

Importante:

Eu NÃO apliquei a última revisão da Home enviada no chat anterior.

Portanto, comece inspecionando:

frontend/src/pages/HomePage.tsx
frontend/src/pages/HomePage.css

e me envie novamente a primeira revisão da Home, começando pelos acessos:

ENTER FOUNDATION → /foundation
OPEN AWARDS LOG → /awards
ENTER DATA ROOM → /data-room

Não avance para métricas, Featured Records ou imagens antes de eu testar e confirmar essa primeira etapa.
```

---

# 15. Estado final deste handoff

```text
estrutura principal do frontend
→ concluída

Foundation
→ concluída

GamePage
→ concluída

Awards History
→ concluída

Data Room
→ concluída

Home
→ estrutura existente, mas revisão pendente

fase atual
→ refinamento

próxima etapa exata
→ revisar e ativar os acessos da Home
```