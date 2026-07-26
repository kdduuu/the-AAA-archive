# Documentação — The AAA Archive

Esta pasta reúne a documentação final e enxuta do projeto.

Os antigos arquivos de planejamento, handoff e checkpoints foram removidos porque descreviam etapas já concluídas, repetiam informações ou registravam estados desatualizados. A documentação atual explica somente o produto final, sua arquitetura, seus dados e sua manutenção.

## Estado atual

- projeto publicado e funcional;
- Foundation Collection com **105 jogos**;
- Awards History com **127 registros** entre 2003 e 2025;
- frontend em React/Vite;
- API em FastAPI;
- PostgreSQL hospedado no Neon;
- dashboard em Streamlit;
- navegação desktop e mobile concluída.

## Índice

| Arquivo | Conteúdo |
| --- | --- |
| [`project_overview.md`](project_overview.md) | proposta, identidade, escopo e páginas do projeto |
| [`architecture.md`](architecture.md) | arquitetura, stack e responsabilidades das camadas |
| [`data_and_collection.md`](data_and_collection.md) | Foundation, Awards, regras editoriais e assets |
| [`frontend.md`](frontend.md) | rotas, páginas, componentes e comportamento da interface |
| [`backend_and_dashboard.md`](backend_and_dashboard.md) | API, módulos Python, banco e Streamlit |
| [`deployment_and_maintenance.md`](deployment_and_maintenance.md) | ambientes, comandos, deploy e manutenção |

## Fonte de verdade

Em caso de diferença entre documentação e implementação, considere esta ordem:

1. código presente no repositório;
2. `data/games.csv` e `data/awards.csv`;
3. banco PostgreSQL sincronizado;
4. documentação desta pasta.

Os CSVs são a fonte editorial. O PostgreSQL é a fonte operacional usada pela API e pelo dashboard.

## Documentos antigos substituídos

Esta estrutura substitui todos os arquivos anteriores de:

- `*_plan.md`;
- `*_checkpoint.md`;
- handoffs de refinamento;
- planos antigos do frontend;
- dicionários extensos e repetitivos;
- documentos que descreviam o frontend ou o deploy como etapas futuras.

Esses arquivos não precisam permanecer na pasta final.
