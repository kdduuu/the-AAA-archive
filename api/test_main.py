"""
===========================================================
The AAA Archive
Arquivo: test_main.py

Objetivo:
Testar os endpoints principais da API do The AAA Archive.

Esses testes verificam se a API está respondendo corretamente
e se os dados retornados fazem sentido.

Autor: Kadu Almeida
===========================================================
"""

# ==========================================================
# IMPORTAÇÃO DOS MÓDULOS
# ==========================================================

from fastapi.testclient import TestClient

from main import app


# ==========================================================
# CLIENTE DE TESTE
# ==========================================================

client = TestClient(app)


# ==========================================================
# TESTE - ENDPOINT INICIAL
# ==========================================================

def testar_endpoint_inicial():
    """
    Testa se o endpoint inicial da API está funcionando.
    """

    resposta = client.get("/")

    assert resposta.status_code == 200

    dados = resposta.json()

    assert dados["status"] == "online"
    assert dados["versao"] == "0.1.0"


# ==========================================================
# TESTE - GAMES
# ==========================================================

def testar_listar_games():
    """
    Testa se o endpoint /games retorna uma lista de jogos.
    """

    resposta = client.get("/games")

    assert resposta.status_code == 200

    dados = resposta.json()

    assert isinstance(dados, list)
    assert len(dados) > 0

    assert "nome" in dados[0]
    assert "ano_lancamento" in dados[0]


def testar_pesquisar_games():
    """
    Testa se a busca textual da API funciona.
    """

    resposta = client.get("/games/search?term=zelda")

    assert resposta.status_code == 200

    dados = resposta.json()

    assert isinstance(dados, list)
    assert len(dados) > 0

    nomes = [jogo["nome"] for jogo in dados]

    assert any("Zelda" in nome for nome in nomes)


def testar_games_por_developer():
    """
    Testa o filtro de jogos por desenvolvedora.
    """

    resposta = client.get("/games/developer/Capcom")

    assert resposta.status_code == 200

    dados = resposta.json()

    assert isinstance(dados, list)
    assert len(dados) > 0

    assert all(jogo["developer"] == "Capcom" for jogo in dados)


def testar_games_por_genero():
    """
    Testa o filtro de jogos por gênero.
    """

    resposta = client.get("/games/genre/Survival%20Horror")

    assert resposta.status_code == 200

    dados = resposta.json()

    assert isinstance(dados, list)
    assert len(dados) > 0

    assert all(jogo["genero"] == "Survival Horror" for jogo in dados)


def testar_games_por_ano():
    """
    Testa o filtro de jogos por ano.
    """

    resposta = client.get("/games/year/2018")

    assert resposta.status_code == 200

    dados = resposta.json()

    assert isinstance(dados, list)
    assert len(dados) > 0

    assert all(jogo["ano_lancamento"] == 2018 for jogo in dados)


def testar_games_historicos():
    """
    Testa o endpoint de jogos historicamente importantes.
    """

    resposta = client.get("/games/historical")

    assert resposta.status_code == 200

    dados = resposta.json()

    assert isinstance(dados, list)

    if len(dados) > 0:
        assert "nome" in dados[0]
        assert "historico_importante" in dados[0]


def testar_games_influentes():
    """
    Testa o endpoint de jogos historicamente influentes.
    """

    resposta = client.get("/games/influential")

    assert resposta.status_code == 200

    dados = resposta.json()

    assert isinstance(dados, list)

    if len(dados) > 0:
        assert "nome" in dados[0]
        assert "historico_influente" in dados[0]


# ==========================================================
# TESTE - ESTATÍSTICAS
# ==========================================================

def testar_estatisticas_home():
    """
    Testa se o endpoint /stats/home retorna estatísticas gerais.
    """

    resposta = client.get("/stats/home")

    assert resposta.status_code == 200

    dados = resposta.json()

    assert isinstance(dados, dict)

    assert "total_jogos" in dados
    assert "total_developers" in dados
    assert "total_franquias" in dados
    assert "total_generos" in dados

    assert dados["total_jogos"] > 0


# ==========================================================
# TESTE - AWARDS
# ==========================================================

def testar_listar_awards():
    """
    Testa se o endpoint /awards retorna registros de premiações.
    """

    resposta = client.get("/awards")

    assert resposta.status_code == 200

    dados = resposta.json()

    assert isinstance(dados, list)
    assert len(dados) > 0

    assert "ano" in dados[0]
    assert "premiacao" in dados[0]
    assert "jogo" in dados[0]
    assert "status" in dados[0]


def testar_awards_vencedores():
    """
    Testa se o endpoint /awards/winners retorna vencedores.
    """

    resposta = client.get("/awards/winners")

    assert resposta.status_code == 200

    dados = resposta.json()

    assert isinstance(dados, list)
    assert len(dados) > 0

    assert all(item["status"] == "Vencedor" for item in dados)


def testar_awards_por_ano():
    """
    Testa se o endpoint /awards/2018 retorna a edição de 2018.
    """

    resposta = client.get("/awards/2018")

    assert resposta.status_code == 200

    dados = resposta.json()

    assert isinstance(dados, list)
    assert len(dados) > 0

    jogos = [item["jogo"] for item in dados]

    assert "God of War" in jogos
    assert "Red Dead Redemption 2" in jogos


def testar_awards_vencedores_na_foundation():
    """
    Testa vencedores do Awards que estão na Foundation Collection.
    """

    resposta = client.get("/awards/foundation/winners")

    assert resposta.status_code == 200

    dados = resposta.json()

    assert isinstance(dados, list)
    assert len(dados) > 0

    jogos = [item["jogo"] for item in dados]

    assert "God of War" in jogos
    assert "Elden Ring" in jogos


def testar_awards_indicados_na_foundation():
    """
    Testa indicados do Awards que estão na Foundation Collection.
    """

    resposta = client.get("/awards/foundation/nominees")

    assert resposta.status_code == 200

    dados = resposta.json()

    assert isinstance(dados, list)
    assert len(dados) > 0

    jogos = [item["jogo"] for item in dados]

    assert "Red Dead Redemption 2" in jogos
    assert "The Last of Us" in jogos


def testar_awards_fora_da_foundation():
    """
    Testa jogos do Awards que ainda não estão na Foundation Collection.
    """

    resposta = client.get("/awards/foundation/outside")

    assert resposta.status_code == 200

    dados = resposta.json()

    assert isinstance(dados, list)
    assert len(dados) > 0

    jogos = [item["jogo"] for item in dados]

    assert "Madden NFL 2004" in jogos
    assert "God of War" not in jogos


# ==========================================================
# EXECUÇÃO DOS TESTES
# ==========================================================

if __name__ == "__main__":
    """
    Executa todos os testes da API manualmente.

    Se nenhum erro aparecer no terminal,
    significa que todos os endpoints testados passaram.
    """

    testar_endpoint_inicial()

    testar_listar_games()
    testar_pesquisar_games()
    testar_games_por_developer()
    testar_games_por_genero()
    testar_games_por_ano()
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