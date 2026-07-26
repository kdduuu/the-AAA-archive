# Backend e Dashboard

## FastAPI

Arquivo principal:

```text
api/main.py
```

A API é somente de leitura. Ela carrega DataFrames do PostgreSQL, reutiliza os módulos de `scripts/` e converte os resultados para JSON.

### Endpoints

```text
GET /
GET /games
GET /games/search?term={term}
GET /games/developer/{developer}
GET /games/genre/{genre}
GET /games/franchise/{franchise}
GET /games/year/{year}
GET /games/decade/{decade}
GET /games/historical
GET /games/influential
GET /games/{game_id}
GET /stats/home
GET /awards
GET /awards/winners
GET /awards/foundation/winners
GET /awards/foundation/nominees
GET /awards/foundation/outside
GET /awards/{year}
```

A documentação interativa fica disponível em `/docs`.

### Respostas e erros

- listas vazias são retornadas quando uma busca ou filtro não encontra jogos;
- jogo inexistente retorna HTTP 404;
- valores vazios do Pandas são convertidos para `null` em JSON;
- falhas de banco são tratadas pela API como erro do servidor.

## Módulos Python

| Arquivo | Responsabilidade |
| --- | --- |
| `scripts/database.py` | configuração, conexão e leitura do PostgreSQL |
| `scripts/import_to_postgres.py` | validação e importação dos CSVs |
| `scripts/load_data.py` | leitura direta dos CSVs para testes e operações editoriais |
| `scripts/search.py` | busca textual |
| `scripts/filters.py` | filtros da Foundation |
| `scripts/site_statistics.py` | métricas e distribuições |
| `scripts/awards.py` | consultas e comparação entre Awards e Foundation |

A lógica deve permanecer nesses módulos quando puder ser reutilizada pela API ou pelo dashboard.

## Banco de dados

A conexão é centralizada por `scripts/database.py`.

Funções principais:

- `obter_configuracao_banco()`;
- `conectar_postgres()`;
- `executar_select()`;
- `carregar_games_do_banco()`;
- `carregar_awards_do_banco()`;
- funções de contagem.

A aplicação usa variáveis de ambiente e nunca grava credenciais diretamente no código.

## Streamlit

Arquivo principal:

```text
dashboard/app.py
```

Funções auxiliares:

```text
dashboard/dashboard_helpers.py
```

O dashboard consulta o PostgreSQL diretamente, sem passar pela FastAPI. Isso é intencional: ele reutiliza a camada Python e mantém a análise separada do site principal.

### Recursos

- busca textual;
- filtros por gênero, desenvolvedora, ano e franquia;
- métricas reativas;
- gráficos por década, gênero e desenvolvedora;
- destaques históricos e influentes;
- tabela da Foundation;
- consulta de Awards por ano;
- comparação entre Awards e Foundation;
- cache com `st.cache_data`.

## Execução local

Na raiz do projeto:

```powershell
fastapi dev api/main.py
```

API Docs:

```text
http://127.0.0.1:8000/docs
```

Dashboard:

```powershell
streamlit run dashboard/app.py
```

Endereço padrão:

```text
http://localhost:8501
```

## Testes

Principais comandos:

```powershell
python scripts/test_database.py
python -m pytest api/test_main.py -v
python scripts/test_filters.py
python scripts/test_search.py
python scripts/test_site_statistics.py
python scripts/test_awards.py
```

Resultados esperados do banco:

```text
games: 105
awards: 127
```

Os testes não devem exigir nomes fixos de banco, usuário ou host, pois o projeto funciona tanto localmente quanto no Neon.
