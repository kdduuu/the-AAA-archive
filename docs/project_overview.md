# Visão Geral do Projeto

## O que é

**The AAA Archive** é um museu digital dedicado à memória, à história e à evolução dos videogames.

A proposta não é catalogar todos os jogos existentes. O projeto preserva uma seleção curada de obras consideradas relevantes por:

- importância histórica;
- influência sobre outros jogos;
- inovação técnica ou de design;
- relevância artística e cultural;
- reconhecimento crítico;
- relação pessoal com o criador.

Apesar do nome, a coleção final não se limita a grandes produções. Ela também inclui clássicos, jogos independentes, experiências narrativas e obras experimentais essenciais para a identidade do arquivo.

## Identidade visual

A direção visual combina:

- museu digital;
- arquivo tecnológico antigo;
- site perdido da internet;
- fliperama depois que todos foram embora.

A interface usa preto, grafite, branco envelhecido, tipografia monoespaçada, bordas técnicas, scanlines discretas e pouco uso de cor.

## Áreas principais

| Área | Função |
| --- | --- |
| Introduction | entrada narrativa e apresentação do sistema |
| Home | visão geral, evolução do meio e acessos principais |
| Foundation Collection | coleção pesquisável dos 105 jogos preservados |
| GamePage | página individual de cada registro |
| Awards History | histórico de vencedores e indicados a Game of the Year |
| Data Room | síntese analítica integrada ao site |
| Streamlit Dashboard | exploração completa dos dados com filtros e gráficos |

## Rotas públicas

```text
/             Introduction
/home         Home
/foundation   Foundation Collection
/games/:id    Registro individual
/awards       Awards History
/data-room    Data Room
```

## Coleção final

A Foundation possui IDs contínuos de `1` a `105`.

Destaques editoriais:

- `Silent Hill 2` e `Silent Hill 2 Remake` são registros separados;
- Silent Hill 2 possui uma descrição especial por ser o registro mais importante para o criador;
- o ranking pessoal da Foundation é:
  1. Silent Hill 2;
  2. The Last of Us;
  3. Life is Strange.

## Estado de produção

- Frontend: `https://the-aaa-archive.vercel.app`
- API: `https://the-aaa-archive-api.onrender.com`
- API Docs: `https://the-aaa-archive-api.onrender.com/docs`
- Dashboard: `https://the-aaa-archive-dashboard.streamlit.app`

A API hospedada no plano gratuito do Render pode levar alguns segundos para responder após um período de inatividade.

## Princípios preservados

- simplicidade antes de complexidade;
- uma responsabilidade clara por camada;
- dados editados nos CSVs e sincronizados com o banco;
- nenhuma credencial no GitHub;
- nenhuma biblioteca adicionada sem necessidade;
- foco em uma experiência consistente e apresentável para portfólio.
