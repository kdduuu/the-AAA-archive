# API Checkpoint — The AAA Archive

## Estado Atual

A primeira versão da API do **The AAA Archive** está funcionando.

A API foi criada com **FastAPI** e atualmente reutiliza os módulos já existentes do backend.

Ela ainda utiliza os arquivos CSV como fonte de dados:

```text
data/games.csv
data/awards.csv
```

---

## Objetivo da API

A API funciona como uma ponte entre os dados do projeto e futuras interfaces, como:

* website;
* dashboard;
* outras aplicações;
* consultas externas.

Nesta fase, a API apenas lê dados e retorna respostas em JSON.

Ela ainda não cadastra, edita ou remove informações.

---

## Estrutura Atual

```text
api/
  main.py
  test_main.py
```

O arquivo `main.py` contém os endpoints da API.

O arquivo `test_main.py` contém os testes dos endpoints principais.

---

## Endpoints Atuais

### Endpoint inicial

```text
GET /
```

Verifica se a API está online.

---

## Jogos

```text
GET /games
```

Retorna todos os jogos da Foundation Collection.

```text
GET /games/search?term=zelda
```

Pesquisa jogos por nome, gênero, desenvolvedora, franquia ou descrição.

```text
GET /games/developer/{developer}
```

Retorna jogos de uma desenvolvedora específica.

```text
GET /games/genre/{genre}
```

Retorna jogos de um gênero específico.

```text
GET /games/year/{year}
```

Retorna jogos lançados em um ano específico.

---

## Estatísticas

```text
GET /stats/home
```

Retorna estatísticas gerais da Foundation Collection para a futura Home do site.

Exemplos de dados retornados:

* total de jogos;
* total de desenvolvedoras;
* total de franquias;
* total de gêneros;
* jogos por gênero;
* jogos por década.

---

## Awards

```text
GET /awards
```

Retorna todos os registros da Awards History.

```text
GET /awards/winners
```

Retorna todos os vencedores de Game of the Year.

```text
GET /awards/{year}
```

Retorna vencedor e indicados de um ano específico.

```text
GET /awards/foundation/winners
```

Retorna vencedores de Game of the Year que também estão na Foundation Collection.

```text
GET /awards/foundation/nominees
```

Retorna indicados a Game of the Year que também estão na Foundation Collection.

```text
GET /awards/foundation/outside
```

Retorna jogos presentes na Awards History, mas ausentes da Foundation Collection.

---

## Módulos Reutilizados

A API reutiliza os seguintes módulos:

```text
load_data.py
filters.py
search.py
site_statistics.py
awards.py
```

Isso evita duplicação de lógica.

A API não recria filtros, buscas ou estatísticas. Ela apenas chama funções que já existem.

---

## Testes

A API possui testes próprios em:

```text
api/test_main.py
```

Além disso, o projeto mantém os testes dos módulos principais:

```text
scripts/test_filters.py
scripts/test_search.py
scripts/test_site_statistics.py
scripts/test_awards.py
```

Comando para rodar todos os testes:

```bash
python scripts/test_filters.py
python scripts/test_search.py
python scripts/test_site_statistics.py
python scripts/test_awards.py
python api/test_main.py
```

---

## O Que a API Ainda Não Faz

Nesta fase, a API ainda não possui:

* banco de dados PostgreSQL;
* cadastro de novos jogos;
* edição de dados;
* exclusão de dados;
* autenticação;
* login;
* painel administrativo;
* separação em routers.

Essas funcionalidades podem ser consideradas futuramente.

---

## Próximo Passo Recomendado

A API atual está funcional e testada.

O próximo passo recomendado é manter a API como está por enquanto e avançar para uma das próximas fases:

```text
1. Streamlit Dashboard
2. Refatoração da API com routers
3. PostgreSQL
```

A recomendação atual é seguir para o **Streamlit Dashboard**, pois ele permitirá visualizar os dados do projeto com gráficos e tabelas sem aumentar demais a complexidade da API.
