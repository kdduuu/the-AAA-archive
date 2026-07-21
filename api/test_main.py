"""
===========================================================
The AAA Archive
Arquivo: test_main.py

Objetivo:
Testar os endpoints principais da API do The AAA Archive.

Esses testes verificam se:
- a API está respondendo corretamente;
- os dados retornados fazem sentido;
- a API utiliza PostgreSQL como fonte principal;
- um jogo individual pode ser localizado pelo ID;
- um ID inexistente retorna o status 404 esperado.

Nesta fase, a API não lê mais diretamente os CSVs.

Arquitetura:

    api/main.py
        ↓
    scripts/database.py
        ↓
    PostgreSQL

Autor: Kadu Almeida
===========================================================
"""


# ==========================================================
# IMPORTAÇÃO E CONFIGURAÇÃO DOS AVISOS
# ==========================================================

import warnings


"""
O FastAPI/Starlette pode mostrar um aviso interno relacionado
ao TestClient:

    StarletteDeprecationWarning

Esse aviso não significa que nossa API está quebrada.

O filtro precisa ser configurado antes da importação do
TestClient, pois o aviso acontece durante essa importação.
"""

warnings.filterwarnings(
    "ignore",
    message=(
        r"Using `httpx` with "
        r"`starlette\.testclient` is deprecated.*"
    ),
)


# ==========================================================
# IMPORTAÇÃO DOS MÓDULOS DA API
# ==========================================================

from fastapi.testclient import TestClient

from main import app


# ==========================================================
# CLIENTE DE TESTE
# ==========================================================

"""
O TestClient permite testar a API sem precisar iniciar
manualmente o servidor da FastAPI.

Em vez de abrir:

    fastapi dev api/main.py

o teste realiza requisições internas como:

    client.get("/games")

Isso permite validar automaticamente os endpoints.
"""

client = TestClient(app)


# ==========================================================
# TESTE — ENDPOINT INICIAL
# ==========================================================

def testar_endpoint_inicial():
    """
    Testa se o endpoint inicial da API está funcionando.

    A API deve informar:
    - status online;
    - versão 0.2.0;
    - fonte de dados PostgreSQL.
    """

    resposta = client.get("/")

    assert resposta.status_code == 200

    dados = resposta.json()

    assert (
        dados["mensagem"]
        == "The AAA Archive API está funcionando"
    )

    assert dados["status"] == "online"
    assert dados["versao"] == "0.2.0"
    assert dados["fonte_dados"] == "PostgreSQL"


# ==========================================================
# TESTES — GAMES
# ==========================================================

def testar_listar_games():
    """
    Testa se o endpoint /games retorna uma lista de jogos.

    Como a tabela games possui atualmente 66 registros,
    esperamos receber 66 jogos.
    """

    resposta = client.get("/games")

    assert resposta.status_code == 200

    dados = resposta.json()

    assert isinstance(dados, list)
    assert len(dados) == 66

    assert "id" in dados[0]
    assert "nome" in dados[0]
    assert "ano_lancamento" in dados[0]
    assert "genero" in dados[0]
    assert "developer" in dados[0]
    assert "franchise" in dados[0]


def testar_game_por_id():
    """
    Testa o endpoint responsável por buscar um único jogo.

    Endpoint:

        GET /games/{game_id}

    Utilizamos o registro de ID 1 e esperamos receber
    Final Fantasy VII.
    """

    resposta = client.get("/games/1")

    assert resposta.status_code == 200

    dados = resposta.json()

    """
    Diferentemente de GET /games, este endpoint deve retornar
    um único objeto, e não uma lista.
    """

    assert isinstance(dados, dict)

    assert dados["id"] == 1
    assert dados["nome"] == "Final Fantasy VII"

    assert "ano_lancamento" in dados
    assert "genero" in dados
    assert "developer" in dados
    assert "franchise" in dados
    assert "descricao" in dados
    assert "metacritic" in dados
    assert "nota_kadu" in dados
    assert "nota_pavam" in dados
    assert "historico_importante" in dados
    assert "historico_influente" in dados


def testar_game_por_id_inexistente():
    """
    Testa a resposta da API quando o ID não existe.

    Utilizamos o ID 999, que não pertence à Foundation
    Collection atual.

    Resultado esperado:
    - status 404;
    - mensagem amigável.
    """

    resposta = client.get("/games/999")

    assert resposta.status_code == 404

    dados = resposta.json()

    assert (
        dados["detail"]
        == "Jogo não encontrado na Foundation Collection."
    )


def testar_pesquisar_games():
    """
    Testa se a busca textual da API funciona.

    Pesquisamos por "zelda" e esperamos encontrar algum jogo
    com Zelda no nome.
    """

    resposta = client.get(
        "/games/search?term=zelda",
    )

    assert resposta.status_code == 200

    dados = resposta.json()

    assert isinstance(dados, list)
    assert len(dados) > 0

    nomes = [
        jogo["nome"]
        for jogo in dados
    ]

    assert any(
        "Zelda" in nome
        for nome in nomes
    )


def testar_games_por_developer():
    """
    Testa o filtro de jogos por desenvolvedora.

    Exemplo utilizado:
        Capcom
    """

    resposta = client.get(
        "/games/developer/Capcom",
    )

    assert resposta.status_code == 200

    dados = resposta.json()

    assert isinstance(dados, list)
    assert len(dados) > 0

    assert all(
        jogo["developer"] == "Capcom"
        for jogo in dados
    )


def testar_games_por_genero():
    """
    Testa o filtro de jogos por gênero.

    Exemplo utilizado:
        Survival Horror
    """

    resposta = client.get(
        "/games/genre/Survival%20Horror",
    )

    assert resposta.status_code == 200

    dados = resposta.json()

    assert isinstance(dados, list)
    assert len(dados) > 0

    assert all(
        jogo["genero"] == "Survival Horror"
        for jogo in dados
    )


def testar_games_por_franquia():
    """
    Testa o filtro de jogos por franquia.

    Exemplo utilizado:
        Resident Evil
    """

    resposta = client.get(
        "/games/franchise/Resident%20Evil",
    )

    assert resposta.status_code == 200

    dados = resposta.json()

    assert isinstance(dados, list)
    assert len(dados) > 0

    assert all(
        jogo["franchise"] == "Resident Evil"
        for jogo in dados
    )


def testar_games_por_ano():
    """
    Testa o filtro de jogos por ano.

    Exemplo utilizado:
        2018
    """

    resposta = client.get(
        "/games/year/2018",
    )

    assert resposta.status_code == 200

    dados = resposta.json()

    assert isinstance(dados, list)
    assert len(dados) > 0

    assert all(
        jogo["ano_lancamento"] == 2018
        for jogo in dados
    )


def testar_games_por_decada():
    """
    Testa o filtro de jogos por década.

    Exemplo utilizado:
        2000

    Todos os jogos retornados precisam ter sido lançados
    entre 2000 e 2009.
    """

    resposta = client.get(
        "/games/decade/2000",
    )

    assert resposta.status_code == 200

    dados = resposta.json()

    assert isinstance(dados, list)
    assert len(dados) > 0

    assert all(
        2000
        <= jogo["ano_lancamento"]
        <= 2009
        for jogo in dados
    )


def testar_games_historicos():
    """
    Testa o endpoint de jogos historicamente importantes.
    """

    resposta = client.get(
        "/games/historical",
    )

    assert resposta.status_code == 200

    dados = resposta.json()

    assert isinstance(dados, list)

    if len(dados) > 0:
        assert "nome" in dados[0]

        assert (
            "historico_importante"
            in dados[0]
        )

        assert all(
            jogo["historico_importante"] is True
            for jogo in dados
        )


def testar_games_influentes():
    """
    Testa o endpoint de jogos historicamente influentes.
    """

    resposta = client.get(
        "/games/influential",
    )

    assert resposta.status_code == 200

    dados = resposta.json()

    assert isinstance(dados, list)

    if len(dados) > 0:
        assert "nome" in dados[0]

        assert (
            "historico_influente"
            in dados[0]
        )

        assert all(
            jogo["historico_influente"] is True
            for jogo in dados
        )


# ==========================================================
# TESTE — ESTATÍSTICAS
# ==========================================================

def testar_estatisticas_home():
    """
    Testa se o endpoint /stats/home retorna estatísticas
    gerais da Foundation Collection.
    """

    resposta = client.get(
        "/stats/home",
    )

    assert resposta.status_code == 200

    dados = resposta.json()

    assert isinstance(dados, dict)

    assert "total_jogos" in dados
    assert "total_developers" in dados
    assert "total_franquias" in dados
    assert "total_generos" in dados

    assert dados["total_jogos"] == 66
    assert dados["total_developers"] > 0
    assert dados["total_franquias"] > 0
    assert dados["total_generos"] > 0


# ==========================================================
# TESTES — AWARDS
# ==========================================================

def testar_listar_awards():
    """
    Testa se o endpoint /awards retorna os registros de
    premiações.

    Como a tabela possui atualmente 127 registros,
    esperamos receber 127 itens.

    A coluna id do PostgreSQL é removida da resposta para
    preservar o formato anteriormente utilizado pela API.
    """

    resposta = client.get(
        "/awards",
    )

    assert resposta.status_code == 200

    dados = resposta.json()

    assert isinstance(dados, list)
    assert len(dados) == 127

    assert "ano" in dados[0]
    assert "premiacao" in dados[0]
    assert "jogo" in dados[0]
    assert "status" in dados[0]

    assert "id" not in dados[0]


def testar_awards_vencedores():
    """
    Testa se /awards/winners retorna apenas vencedores.
    """

    resposta = client.get(
        "/awards/winners",
    )

    assert resposta.status_code == 200

    dados = resposta.json()

    assert isinstance(dados, list)
    assert len(dados) > 0

    assert all(
        item["status"] == "Vencedor"
        for item in dados
    )


def testar_awards_por_ano():
    """
    Testa se /awards/2018 retorna a edição de 2018.

    Esperamos encontrar:
    - God of War;
    - Red Dead Redemption 2.
    """

    resposta = client.get(
        "/awards/2018",
    )

    assert resposta.status_code == 200

    dados = resposta.json()

    assert isinstance(dados, list)
    assert len(dados) > 0

    assert all(
        item["ano"] == 2018
        for item in dados
    )

    jogos = [
        item["jogo"]
        for item in dados
    ]

    assert "God of War" in jogos
    assert "Red Dead Redemption 2" in jogos


def testar_awards_vencedores_na_foundation():
    """
    Testa os vencedores do Awards que também estão
    presentes na Foundation Collection.
    """

    resposta = client.get(
        "/awards/foundation/winners",
    )

    assert resposta.status_code == 200

    dados = resposta.json()

    assert isinstance(dados, list)
    assert len(dados) > 0

    jogos = [
        item["jogo"]
        for item in dados
    ]

    assert "God of War" in jogos
    assert "Elden Ring" in jogos


def testar_awards_indicados_na_foundation():
    """
    Testa os indicados do Awards que estão presentes
    na Foundation Collection.
    """

    resposta = client.get(
        "/awards/foundation/nominees",
    )

    assert resposta.status_code == 200

    dados = resposta.json()

    assert isinstance(dados, list)
    assert len(dados) > 0

    jogos = [
        item["jogo"]
        for item in dados
    ]

    assert "Red Dead Redemption 2" in jogos
    assert "The Last of Us" in jogos


def testar_awards_fora_da_foundation():
    """
    Testa jogos do Awards que ainda não pertencem à
    Foundation Collection.

    God of War está na Foundation e não deve aparecer.

    Madden NFL 2004 não está na Foundation e deve aparecer.
    """

    resposta = client.get(
        "/awards/foundation/outside",
    )

    assert resposta.status_code == 200

    dados = resposta.json()

    assert isinstance(dados, list)
    assert len(dados) > 0

    jogos = [
        item["jogo"]
        for item in dados
    ]

    assert "Madden NFL 2004" in jogos
    assert "God of War" not in jogos


# ==========================================================
# EXECUÇÃO MANUAL DOS TESTES
# ==========================================================

if __name__ == "__main__":
    """
    Executa todos os testes da API manualmente.

    Essa parte não é necessária quando utilizamos pytest,
    mas permite executar diretamente:

        python api/test_main.py
    """

    testar_endpoint_inicial()

    testar_listar_games()
    testar_game_por_id()
    testar_game_por_id_inexistente()
    testar_pesquisar_games()
    testar_games_por_developer()
    testar_games_por_genero()
    testar_games_por_franquia()
    testar_games_por_ano()
    testar_games_por_decada()
    testar_games_historicos()
    testar_games_influentes()

    testar_estatisticas_home()

    testar_listar_awards()
    testar_awards_vencedores()
    testar_awards_por_ano()
    testar_awards_vencedores_na_foundation()
    testar_awards_indicados_na_foundation()
    testar_awards_fora_da_foundation()

    print("=" * 60)
    print("TODOS OS TESTES DA API PASSARAM!")
    print("=" * 60)