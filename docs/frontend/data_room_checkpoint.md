# Data Room Checkpoint — The AAA Archive

## Objetivo deste documento

Este documento registra a conclusão da **Fase 7 — Data Room** do front-end do projeto **The AAA Archive**.

A Data Room funciona como uma prévia analítica integrada ao site React. Ela apresenta métricas e visualizações resumidas, enquanto o dashboard completo continua separado em Streamlit.

A metodologia utilizada permaneceu:

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

## Estado atual

```text
Fase 7 — Data Room
Status: concluída, integrada e testada
```

Rota:

```text
/data-room
```

A área pode ser acessada pelo item `DATA ROOM` da navegação superior.

---

## Responsabilidade da Data Room

A divisão atual é:

```text
React
→ prévia analítica pública
→ métricas essenciais
→ gráficos resumidos
→ acesso ao dashboard

Streamlit
→ dashboard analítico completo
→ filtros
→ tabelas
→ visualizações detalhadas
```

O React não substitui o Streamlit.

---

## Arquivos principais

```text
frontend/src/pages/DataRoomPage.tsx
frontend/src/pages/DataRoomPage.css
frontend/src/types/HomeStats.ts
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

O React não acessa diretamente:

```text
CSV
PostgreSQL
módulos Python
```

---

## Endpoints utilizados

```text
GET /stats/home
GET /games
GET /awards
GET /awards/foundation/winners
```

### GET /stats/home

Fornece métricas gerais, como:

```text
total de jogos
total de desenvolvedoras
total de franquias
total de gêneros
```

### GET /games

É utilizado para:

```text
período da Foundation
distribuição por década
distribuição por gênero
ranking de desenvolvedoras
```

### GET /awards

É utilizado para:

```text
total de registros
período das premiações
total de edições
total de vencedores
```

### GET /awards/foundation/winners

É utilizado para comparar:

```text
vencedores confirmados na Foundation
vencedores fora da Foundation
porcentagem de presença
```

---

## Estados da página

A Data Room representa:

```text
loading
success
empty
error
```

O status visual do hero pode apresentar:

```text
retrieving
stable
empty
unavailable
```

Erros técnicos internos não são exibidos diretamente ao visitante.

---

## Archive Metrics

O painel apresenta dados reais:

```text
Foundation Records
Awards Logs
Archive Period
Awards Period
```

Também utiliza informações complementares:

```text
developers
genres
award editions
winners
```

---

## Foundation Data

### Registros por década

Os anos dos jogos são agrupados pelo React.

Exemplo:

```text
2018
→ década de 2010
```

A página:

```text
ignora registros sem ano
agrupa por década
conta os registros
ordena cronologicamente
calcula barras proporcionais
```

### Registros por gênero

A página:

```text
ignora gêneros vazios
agrupa nomes iguais
conta os registros
ordena por quantidade
apresenta barras horizontais
```

Todos os gêneros presentes nos registros carregados podem ser representados.

### Desenvolvedoras com mais registros

A página cria um ranking com as oito desenvolvedoras mais recorrentes.

Regras:

```text
ignorar valores vazios
contar registros
ordenar da maior presença para a menor
usar ordem alfabética em empates
mostrar apenas o Top 8
```

A lista completa continua disponível no Streamlit.

---

## Awards Data

O painel compara os vencedores de Game of the Year.

Categorias:

```text
CONFIRMED IN FOUNDATION
OUTSIDE FOUNDATION
```

Também é calculada a porcentagem de vencedores preservados na Foundation Collection.

A visualização utiliza barras horizontais proporcionais.

---

## Dashboard Streamlit

O painel `OPEN DASHBOARD` possui um link externo para:

```text
http://localhost:8501
```

O link abre em outra aba.

Durante o desenvolvimento local, o dashboard deve ser iniciado com:

```powershell
python -m streamlit run dashboard/app.py
```

O React e o Streamlit permanecem como aplicações separadas.

---

## System Information

A página apresenta a arquitetura técnica:

```text
DATA SOURCE
→ PostgreSQL

PROCESSING
→ Python / Pandas

API LAYER
→ FastAPI

FRONTEND
→ React / TypeScript

DASHBOARD
→ Streamlit
```

---

## Navegação contextual

A barra lateral apresenta:

```text
ARCHIVE METRICS
FOUNDATION DATA
AWARDS DATA
OPEN DASHBOARD
SYSTEM INFORMATION
```

Cada item direciona para uma seção da mesma página.

---

## Responsividade e acessibilidade

A implementação possui:

```text
layout adaptável
gráficos reorganizados em telas menores
links reais
foco visível
aria-live para estados assíncronos
respeito ao prefers-reduced-motion
```

A responsividade inicial foi implementada e deve continuar sendo revisada durante os testes finais do projeto.

---

## Testes realizados

Foram confirmados no navegador:

```text
rota /data-room
item DATA ROOM ativo
métricas reais
gráfico por década
distribuição por gênero
ranking de desenvolvedoras
gráfico de vencedores
link do Streamlit
navegação lateral
```

Verificações técnicas realizadas durante as etapas:

```powershell
npm run lint
npm run build
```

Resultados:

```text
lint concluído sem erros
build de produção concluído corretamente
```

---

## Limites preservados

Não foram adicionados:

```text
biblioteca de gráficos
novo framework
acesso direto ao PostgreSQL
filtros avançados no React
tabelas analíticas completas
duplicação do dashboard Streamlit
```

As visualizações foram construídas com React e CSS personalizados.

---

## Estado final da Fase 7

```text
rota /data-room
→ concluída

navegação superior
→ concluída

métricas reais
→ concluídas

gráfico por década
→ concluído

distribuição por gênero
→ concluída

Top 8 desenvolvedoras
→ concluído

presença dos vencedores na Foundation
→ concluída

acesso ao Streamlit
→ concluído

estados da requisição
→ concluídos

responsividade inicial
→ implementada

lint
→ aprovado

build
→ aprovado

documentação
→ concluída
```

---

## Próxima fase

A próxima etapa será revisar a **Home** e seus acessos.

Prioridades:

```text
verificar valores estáticos
integrar métricas reais quando necessário
ativar acessos ainda bloqueados
preservar o visual aprovado
testar antes de avançar
```