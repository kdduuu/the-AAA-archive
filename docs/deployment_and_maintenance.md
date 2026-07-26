# Deploy e Manutenção

## Serviços de produção

| Camada | Plataforma | Endereço |
| --- | --- | --- |
| Frontend | Vercel | `https://the-aaa-archive.vercel.app` |
| API | Render | `https://the-aaa-archive-api.onrender.com` |
| API Docs | Render/FastAPI | `https://the-aaa-archive-api.onrender.com/docs` |
| Banco | Neon PostgreSQL | configurado por variáveis de ambiente |
| Dashboard | Streamlit Community Cloud | `https://the-aaa-archive-dashboard.streamlit.app` |

## Variáveis de ambiente

### Backend local e Render

```env
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=
POSTGRES_PORT=5432
CORS_ALLOWED_ORIGINS=http://localhost:5173,https://the-aaa-archive.vercel.app
```

O `.env` real não deve ser enviado ao GitHub. O `.env.example` contém apenas o modelo.

### Frontend na Vercel

```env
VITE_API_URL=https://the-aaa-archive-api.onrender.com
VITE_STREAMLIT_URL=https://the-aaa-archive-dashboard.streamlit.app
```

Variáveis do Vite são incorporadas durante o build. Após alterar qualquer `VITE_*`, é necessário criar um novo deployment.

### Streamlit Secrets

```toml
POSTGRES_DB = "..."
POSTGRES_USER = "..."
POSTGRES_PASSWORD = "..."
POSTGRES_HOST = "..."
POSTGRES_PORT = "5432"
```

Os Secrets ficam no painel do Streamlit e não devem ser adicionados ao repositório.

## Deploy do frontend

Configuração da Vercel:

```text
Root Directory: frontend
Framework: Vite
Build Command: npm run build
Output Directory: dist
Install Command: npm install
```

O arquivo `frontend/vercel.json` contém a regra de SPA:

```json
{
  "rewrites": [
    {
      "source": "/(.*)",
      "destination": "/index.html"
    }
  ]
}
```

Pushes na branch `main` geram novos deployments automaticamente.

## Deploy da API

Configuração do Render:

```text
Build Command:
pip install -r requirements.txt

Start Command:
python -m uvicorn api.main:app --host 0.0.0.0 --port $PORT
```

O plano gratuito pode suspender o serviço por inatividade. A primeira requisição após esse período pode ser mais lenta.

## Deploy do dashboard

Configuração do Streamlit:

```text
Repository: kdduuu/the-AAA-archive
Branch: main
Main file: dashboard/app.py
```

As credenciais do Neon são configuradas em `Manage app → Settings → Secrets`.

## Fluxo de manutenção

### Alteração de código

1. modificar o arquivo local;
2. executar os testes relacionados;
3. verificar `git status`;
4. criar commit;
5. enviar para `main`;
6. acompanhar Vercel, Render ou Streamlit;
7. validar o serviço publicado.

### Alteração da Foundation ou Awards

1. editar o CSV correspondente;
2. manter IDs e nomes consistentes;
3. executar o importador contra o banco correto;
4. rodar os testes do banco e da API;
5. verificar o site e o dashboard;
6. enviar CSV e código ao GitHub.

### Nova imagem

Salvar como:

```text
frontend/public/assets/games/{id}/cover.webp
```

Não criar um segundo asset de hero para a GamePage.

## Validação antes de um release

```powershell
python scripts/test_database.py
python -m pytest api/test_main.py -v

cd frontend
npm run lint
npm run build
```

Verificar no site:

- `/`;
- `/home`;
- `/foundation`;
- registros individuais;
- `/games/999`;
- `/awards`;
- `/data-room`;
- busca, filtros e ordenação;
- imagens;
- navegação mobile;
- abertura do Streamlit.

## Problemas comuns

### Site abre, mas os dados não carregam

- confirmar se a API do Render está `Live`;
- aguardar a inicialização da instância gratuita;
- abrir `/docs` e testar um endpoint;
- conferir `VITE_API_URL` e CORS.

### Data Room abre `localhost:8501`

- corrigir `VITE_STREAMLIT_URL` na Vercel;
- fazer novo redeploy sem reutilizar o build antigo;
- atualizar o navegador sem cache.

### Streamlit não conecta ao banco

- conferir os Secrets;
- confirmar que as tabelas existem no Neon;
- testar as mesmas credenciais localmente sem compartilhá-las.

### Erro `relation does not exist`

Criar as tabelas usando `database/schema.sql` antes de importar os CSVs.

## Segurança

- nunca compartilhar connection strings ou senhas;
- redefinir imediatamente qualquer credencial exposta;
- manter `.env` no `.gitignore`;
- usar `.env.example` apenas como modelo;
- não salvar Secrets em arquivos versionados.
