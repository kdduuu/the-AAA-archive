"""
===========================================================
The AAA Archive
Arquivo: main.py

Objetivo:
Criar a primeira versão da API do The AAA Archive.

Nesta fase inicial, a API terá apenas um endpoint simples
para testar se o servidor está funcionando.

Autor: Kadu Almeida
===========================================================
"""

# ==========================================================
# IMPORTAÇÃO DOS MÓDULOS
# ==========================================================

from fastapi import FastAPI


# ==========================================================
# CRIAÇÃO DA APLICAÇÃO
# ==========================================================

app = FastAPI(
    title="The AAA Archive API",
    description="API para consultar dados do projeto The AAA Archive.",
    version="0.1.0"
)


# ==========================================================
# ENDPOINT INICIAL
# ==========================================================

@app.get("/")
def read_root():
    """
    Endpoint inicial da API.

    Endpoint:
        GET /

    Objetivo:
        Verificar se a API está funcionando corretamente.

    Returns:
        dict: mensagem simples confirmando que a API está ativa.
    """

    return {
        "mensagem": "The AAA Archive API está funcionando",
        "status": "online",
        "versao": "0.1.0"
    }