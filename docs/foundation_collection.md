# Foundation Collection — The AAA Archive

# Objetivo

A **Foundation Collection** representa o núcleo editorial do **The AAA Archive**.

Ela reúne uma seleção curada de jogos considerados fundamentais para compreender diferentes momentos da evolução da indústria dos videogames, especialmente dentro do recorte de jogos **AAA single-player**.

A coleção serve como base para:

* o dataset `games.csv`;
* a tabela `games` no PostgreSQL;
* os módulos Python;
* a API FastAPI;
* o dashboard Streamlit;
* as análises históricas;
* a futura aplicação web;
* futuras expansões editoriais.

A Foundation Collection não pretende catalogar todos os jogos existentes.

Seu objetivo é preservar uma seleção consistente, historicamente relevante e editorialmente coerente.

---

# Identidade da Coleção

A Foundation Collection representa a primeira coleção oficial do The AAA Archive.

Ela funciona como:

* ponto de partida editorial;
* base histórica do projeto;
* núcleo permanente da aplicação;
* referência para futuras coleções;
* recorte inicial da história dos jogos AAA single-player.

A coleção atual possui:

```text
66 jogos
```

Sua versão oficial é:

```text
Foundation Collection v1.0
```

---

# Filosofia da Coleção

A Foundation Collection não busca reunir apenas:

* jogos com notas altas;
* jogos comercialmente bem-sucedidos;
* vencedores de premiações;
* jogos populares;
* favoritos pessoais.

Seu objetivo é representar diferentes momentos da evolução da indústria.

A seleção considera fatores como:

* inovação tecnológica;
* impacto cultural;
* relevância histórica;
* influência sobre outros jogos;
* reconhecimento crítico;
* importância para uma franquia;
* contribuição para um gênero;
* contribuição para novas mecânicas;
* contribuição narrativa;
* importância editorial para o The AAA Archive.

Cada jogo presente na coleção deve contribuir para contar uma parte da história dos videogames.

---

# Recorte Editorial

O foco principal da coleção está em jogos:

```text
AAA
single-player
historicamente relevantes
```

Alguns jogos podem possuir recursos multijogador, desde que sua importância principal dentro da coleção esteja relacionada à experiência individual, à campanha ou ao impacto histórico de sua proposta principal.

A coleção não busca representar prioritariamente:

* jogos exclusivamente competitivos;
* jogos exclusivamente multiplayer;
* jogos como serviço;
* todos os títulos de uma franquia;
* todas as obras bem avaliadas;
* todos os vencedores de Game of the Year.

---

# Critérios de Inclusão

Um jogo pode integrar a Foundation Collection quando atender a um ou mais dos seguintes critérios:

* representar um marco para a indústria;
* influenciar jogos posteriores;
* influenciar um gênero;
* introduzir ou popularizar mecânicas;
* redefinir padrões técnicos;
* apresentar contribuições narrativas relevantes;
* tornar-se referência dentro de sua franquia;
* possuir reconhecimento crítico consistente;
* possuir impacto cultural;
* representar um momento importante de determinada geração;
* contribuir para a proposta editorial do Archive.

A inclusão depende da análise conjunta desses fatores.

Nenhum critério isolado garante automaticamente a entrada de um jogo.

---

# Critérios que Não Garantem Inclusão

Os seguintes fatores podem contribuir para a análise, mas não garantem entrada automática:

* vendas elevadas;
* popularidade;
* nota do Metacritic;
* indicação a Game of the Year;
* vitória em Game of the Year;
* preferência pessoal;
* importância comercial isolada;
* pertencimento a uma franquia famosa.

A Foundation Collection deve permanecer uma curadoria, e não um ranking ou catálogo automático.

---

# Caráter Permanente

A Foundation Collection v1.0 é considerada a coleção-base permanente do The AAA Archive.

Isso significa que sua composição deve permanecer estável para preservar:

* consistência histórica;
* comparações futuras;
* análises estatísticas;
* identidade editorial;
* evolução documentada do projeto.

Alterações na coleção-base devem ser excepcionais.

Um jogo só deverá ser removido ou substituído caso seja identificado:

* erro factual;
* duplicação;
* incompatibilidade grave com o recorte;
* problema estrutural no dataset;
* decisão editorial formalmente documentada.

Mudanças desse tipo deverão gerar uma nova versão do documento.

---

# Fonte Editorial e Fonte Operacional

A Foundation Collection possui duas representações.

## Fonte Editorial

```text
data/games.csv
```

O CSV é utilizado como:

* base original;
* fonte de edição manual;
* referência editorial;
* entrada para o processo de importação;
* histórico simples da coleção.

---

## Fonte Operacional

```text
PostgreSQL
└── public.games
```

A tabela `games` é utilizada por:

* API;
* dashboard;
* camada Python de banco;
* testes de integração;
* futura aplicação web.

---

# Fluxo dos Dados

```text
Foundation Collection
↓
data/games.csv
↓
scripts/import_to_postgres.py
↓
PostgreSQL
↓
scripts/database.py
↓
API e Dashboard
```

A composição oficial da coleção deve permanecer sincronizada entre:

```text
games.csv
tabela games
este documento
```

---

# Estrutura dos Dados

Cada jogo da Foundation Collection possui os seguintes campos:

```text
id
nome
ano_lancamento
genero
developer
franchise
descricao
metacritic
nota_kadu
nota_pavam
historico_importante
historico_influente
```

As regras técnicas de cada campo são documentadas em:

```text
docs/data_dictionary.md
```

---

# Organização da Coleção

A coleção está dividida em blocos históricos.

Essa divisão facilita:

* leitura;
* documentação;
* análise por períodos;
* visualização da evolução da indústria;
* comparação entre gerações.

Os blocos representam períodos de lançamento, mas a ordem interna dos jogos segue a organização editorial atual do dataset e não precisa funcionar como uma cronologia exata dentro de cada grupo.

---

# Relação com a Awards History

A Awards History faz parte do The AAA Archive, mas permanece independente da Foundation Collection.

Isso significa que:

* um jogo pode estar na Foundation Collection sem ter sido indicado a Game of the Year;
* um jogo pode vencer Game of the Year sem estar na Foundation Collection;
* um indicado pode não fazer parte da coleção;
* premiações não controlam a curadoria editorial.

As bases são relacionadas por:

```text
awards.jogo
games.nome
```

Esse relacionamento já é utilizado pelo sistema para identificar:

* vencedores presentes na Foundation Collection;
* indicados presentes na Foundation Collection;
* jogos da Awards History fora da coleção;
* diferenças entre reconhecimento institucional e curadoria editorial.

---

# Foundation Collection v1.0

## Década de 1990

1. Final Fantasy VII
2. Resident Evil 2
3. Metal Gear Solid
4. The Legend of Zelda: Ocarina of Time
5. Silent Hill

Total do período:

```text
5 jogos
```

---

## 2000–2004

1. Deus Ex
2. Halo: Combat Evolved
3. Max Payne
4. GTA: Vice City
5. Prince of Persia: The Sands of Time
6. GTA: San Andreas
7. Halo 2
8. Metal Gear Solid 3: Snake Eater
9. Resident Evil 4
10. Half-Life 2

Total do período:

```text
10 jogos
```

---

## 2005–2009

1. God of War
2. Shadow of the Colossus
3. Black
4. Need for Speed: Most Wanted
5. The Elder Scrolls IV: Oblivion
6. Gears of War
7. Call of Duty 4: Modern Warfare
8. BioShock
9. Mass Effect
10. Dead Space
11. Fallout 3
12. Assassin's Creed II
13. Batman: Arkham Asylum
14. Demon's Souls
15. Uncharted 2: Among Thieves

Total do período:

```text
15 jogos
```

---

## 2010–2014

1. Red Dead Redemption
2. Fallout: New Vegas
3. Mass Effect 2
4. Portal 2
5. The Elder Scrolls V: Skyrim
6. Dark Souls
7. Batman: Arkham City
8. Far Cry 3
9. BioShock Infinite
10. Tomb Raider
11. The Last of Us
12. Grand Theft Auto V

Total do período:

```text
12 jogos
```

---

## 2015–2019

1. Bloodborne
2. The Witcher 3: Wild Hunt
3. Ori and the Blind Forest
4. DOOM
5. Uncharted 4: A Thief's End
6. The Last Guardian
7. Horizon Zero Dawn
8. NieR: Automata
9. Persona 5
10. The Legend of Zelda: Breath of the Wild
11. God of War
12. Marvel's Spider-Man
13. Red Dead Redemption 2
14. Sekiro: Shadows Die Twice
15. Control
16. Quantum Break
17. Death Stranding

Total do período:

```text
17 jogos
```

---

## 2020–Atualidade

1. Ghost of Tsushima
2. The Last of Us Part II
3. Elden Ring
4. Alan Wake 2
5. Baldur's Gate 3
6. Astro Bot
7. Black Myth: Wukong

Total do período:

```text
7 jogos
```

---

# Resumo da Coleção

| Período         | Quantidade |
| --------------- | ---------: |
| Década de 1990  |          5 |
| 2000–2004       |         10 |
| 2005–2009       |         15 |
| 2010–2014       |         12 |
| 2015–2019       |         17 |
| 2020–Atualidade |          7 |
| **Total**       |     **66** |

---

# Classificações Editoriais

Além de pertencer à Foundation Collection, um jogo pode futuramente receber classificações editoriais adicionais.

## Historicamente Importante

Campo:

```text
historico_importante
```

Indica que o jogo representa um marco relevante para a indústria, para uma geração, para uma franquia ou para a cultura dos videogames.

---

## Historicamente Influente

Campo:

```text
historico_influente
```

Indica que o jogo influenciou diretamente:

* outros jogos;
* gêneros;
* mecânicas;
* sistemas;
* estruturas narrativas;
* decisões de design;
* tendências da indústria.

---

## Diferença entre as Classificações

Um jogo pode ser:

* importante e influente;
* importante, mas não diretamente influente;
* influente, mas menos central culturalmente;
* ainda não classificado.

Esses campos não alteram a presença do jogo na Foundation Collection.

Eles adicionam novas camadas de análise editorial.

---

# Conteúdo Editorial Pendente

A lista de jogos está definida, mas parte do conteúdo editorial ainda está em desenvolvimento.

Campos que podem permanecer vazios:

```text
descricao
metacritic
nota_kadu
nota_pavam
historico_importante
historico_influente
```

O preenchimento gradual desses campos não modifica a composição da coleção.

Ele apenas enriquece as informações disponíveis sobre cada jogo.

---

# Expansion Collections

A Foundation Collection permanecerá preservada como a coleção-base.

Novos jogos poderão ser organizados futuramente em:

```text
Expansion Collections
```

Possíveis exemplos:

```text
Expansion Collection 2027
Expansion Collection 2028
```

Uma Expansion Collection poderá incluir:

* jogos lançados após o congelamento da coleção-base;
* títulos reconsiderados editorialmente;
* novos recortes históricos;
* jogos que ganharam relevância com o passar do tempo;
* expansões temáticas.

---

# Relação entre Foundation e Expansion Collections

As Expansion Collections não devem alterar silenciosamente a Foundation Collection.

A separação permite:

* preservar a versão original;
* analisar o crescimento do Archive;
* comparar períodos;
* registrar decisões editoriais;
* evitar mudanças retroativas constantes.

A futura aplicação poderá apresentar:

```text
Foundation Collection
Expansion Collections
Todas as coleções
```

A estrutura técnica das Expansion Collections ainda não foi definida.

---

# Processo para Novas Inclusões

Antes de incluir um jogo em uma futura coleção, deve-se registrar:

1. Nome do jogo.
2. Ano de lançamento.
3. Desenvolvedora.
4. Franquia.
5. Gênero principal.
6. Motivo da inclusão.
7. Relevância histórica.
8. Influência.
9. Relação com o recorte editorial.
10. Coleção à qual ele pertencerá.

A decisão não deve ser tomada apenas para aumentar a quantidade de jogos.

---

# Processo para Alterar a Foundation Collection

Uma alteração na coleção-base deverá seguir:

```text
Identificar necessidade
↓
Revisar critérios editoriais
↓
Comparar com games.csv
↓
Documentar justificativa
↓
Atualizar este documento
↓
Atualizar data_dictionary.md, se necessário
↓
Atualizar games.csv
↓
Importar para PostgreSQL
↓
Executar testes
↓
Criar nova versão
↓
Registrar em commit
```

---

# Uso no Backend

A Foundation Collection é utilizada pelos módulos:

```text
load_data.py
filters.py
search.py
site_statistics.py
database.py
import_to_postgres.py
```

Esses módulos permitem:

* carregar os dados;
* filtrar jogos;
* pesquisar;
* gerar estatísticas;
* importar para o banco;
* consultar o PostgreSQL.

---

# Uso na API

A Foundation Collection alimenta endpoints como:

```text
GET /games
GET /games/search
GET /games/developer/{developer}
GET /games/genre/{genre}
GET /games/franchise/{franchise}
GET /games/year/{year}
GET /games/decade/{decade}
GET /games/historical
GET /games/influential
GET /stats/home
```

---

# Uso no Dashboard

A coleção é utilizada para apresentar:

* total de jogos;
* total de desenvolvedoras;
* total de franquias;
* total de gêneros;
* jogos por década;
* jogos por gênero;
* jogos por desenvolvedora;
* filtros;
* busca textual;
* tabelas;
* recorte editorial.

---

# Uso Futuro na Aplicação Web

A Foundation Collection deverá alimentar áreas como:

* Home;
* Archive;
* páginas individuais dos jogos;
* filtros;
* busca;
* destaques editoriais;
* linha do tempo;
* relações entre jogos;
* comparações com premiações.

A aplicação web deverá consumir esses dados preferencialmente por meio da API.

---

# Princípios da Curadoria

Toda evolução editorial deve preservar:

* relevância histórica;
* coerência com o recorte;
* qualidade acima de quantidade;
* separação entre gosto pessoal e importância histórica;
* independência em relação às premiações;
* documentação das decisões;
* estabilidade da coleção-base;
* crescimento controlado.

---

# O que a Foundation Collection Não É

A coleção não é:

* ranking dos melhores jogos;
* lista dos jogos favoritos de Kadu;
* lista completa de jogos AAA;
* lista completa de jogos single-player;
* reprodução dos vencedores de Game of the Year;
* ranking do Metacritic;
* catálogo comercial;
* lista definitiva e universal da história dos videogames.

Ela representa a visão editorial do The AAA Archive.

---

# Estado Atual

```text
Foundation Collection definida ✅
66 jogos catalogados ✅
games.csv estruturado ✅
Tabela games criada ✅
Dados importados para PostgreSQL ✅
API integrada ✅
Dashboard integrado ✅
Comparação com Awards History implementada ✅
Campos editoriais em preenchimento ⏳
```

---

# Versionamento

**Versão do documento:** 2.0

**Versão da coleção:** Foundation Collection v1.0

**Quantidade:** 66 jogos

**Status:** Coleção-base congelada

Esta versão atualiza o documento para representar:

* a integração com PostgreSQL;
* o uso pela API;
* o uso pelo dashboard;
* a relação atual com a Awards History;
* a quantidade oficial de registros;
* as regras para futuras Expansion Collections.

---

# Status Oficial

A Foundation Collection representa oficialmente a coleção permanente inicial do The AAA Archive.

Sua composição atual deve permanecer preservada como referência editorial para todas as futuras expansões do projeto.
