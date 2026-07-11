-- ==========================================================
-- The AAA Archive
-- Arquivo: schema.sql
--
-- Objetivo:
-- Registrar e recriar a estrutura inicial do banco PostgreSQL
-- usado pelo projeto The AAA Archive.
--
-- Banco de dados:
--   aaa_archive
--
-- Tabelas:
--   games
--   awards
--
-- Autor: Kadu Almeida
-- ==========================================================


-- ==========================================================
-- COMO USAR ESTE ARQUIVO
-- ==========================================================
--
-- Este arquivo deve ficar salvo no projeto em:
--
--   database/schema.sql
--
-- Ele serve como referência oficial da estrutura inicial do banco.
--
-- Em um próximo chat, ou em outro computador, este arquivo ajuda a entender:
--
--   1. qual banco foi criado;
--   2. quais tabelas existem;
--   3. quais colunas cada tabela possui;
--   4. quais tipos de dados foram escolhidos;
--   5. como recriar a estrutura básica do banco.
--
-- IMPORTANTE:
--
-- O comando CREATE DATABASE normalmente deve ser executado enquanto você está
-- conectado ao banco padrão "postgres", e não dentro do próprio aaa_archive.
--
-- Depois de criar o banco aaa_archive, conecte-se nele pelo pgAdmin
-- e execute os comandos de criação das tabelas.
--
-- Ordem recomendada:
--
--   1. Criar o banco aaa_archive;
--   2. Conectar no banco aaa_archive;
--   3. Executar este schema para criar as tabelas games e awards;
--   4. Rodar o script scripts/import_to_postgres.py para importar os CSVs.
--
-- ==========================================================


-- ==========================================================
-- 1. CRIAÇÃO DO BANCO DE DADOS
-- ==========================================================
--
-- Este comando cria o banco principal do projeto.
--
-- Execute este comando apenas se o banco aaa_archive ainda não existir.
--
-- No pgAdmin:
--   - conecte no servidor PostgreSQL;
--   - abra o Query Tool no banco padrão "postgres";
--   - execute o comando abaixo.
--
-- Se você já criou o banco pelo menu visual do pgAdmin, não precisa executar.

-- CREATE DATABASE aaa_archive;


-- ==========================================================
-- 2. CONEXÃO COM O BANCO
-- ==========================================================
--
-- Depois de criar o banco, conecte-se ao banco:
--
--   aaa_archive
--
-- No pgAdmin, clique no banco aaa_archive e abra o Query Tool nele.
--
-- Os comandos abaixo devem ser executados dentro do banco aaa_archive.


-- ==========================================================
-- 3. REMOÇÃO OPCIONAL DAS TABELAS
-- ==========================================================
--
-- Estes comandos apagam as tabelas caso elas já existam.
--
-- ATENÇÃO:
-- Se as tabelas já tiverem dados, esses dados serão apagados.
--
-- Use estes comandos apenas se quiser recriar a estrutura do zero.
--
-- A tabela awards é removida primeiro por organização.
-- A tabela games é removida depois.
--
-- Por segurança, deixamos esses comandos comentados.
-- Para usar, remova os dois traços "--" do início das linhas.

-- DROP TABLE IF EXISTS awards;
-- DROP TABLE IF EXISTS games;


-- ==========================================================
-- 4. TABELA: games
-- ==========================================================
--
-- Esta tabela representa a Foundation Collection.
--
-- Ela foi baseada no arquivo:
--
--   data/games.csv
--
-- Cada linha representa um jogo da coleção principal do The AAA Archive.
--
-- Colunas originais do CSV:
--
--   id
--   nome
--   ano_lancamento
--   genero
--   developer
--   franchise
--   descricao
--   metacritic
--   nota_kadu
--   nota_pavam
--   historico_importante
--   historico_influente
--
-- Observação:
--
-- Nesta primeira versão do PostgreSQL, a tabela games mantém uma estrutura
-- parecida com o CSV.
--
-- Ainda não estamos normalizando em tabelas separadas como:
--
--   developers
--   genres
--   franchises
--
-- Isso foi uma decisão intencional para manter a migração simples,
-- principalmente nesta primeira fase de aprendizado com PostgreSQL.

CREATE TABLE IF NOT EXISTS games (
    -- id vem do próprio games.csv.
    -- Como cada jogo já possui um id no dataset, usamos INTEGER PRIMARY KEY.
    id INTEGER PRIMARY KEY,

    -- Nome do jogo.
    -- NOT NULL significa que esse campo não pode ficar vazio.
    nome VARCHAR(200) NOT NULL,

    -- Ano de lançamento do jogo.
    ano_lancamento INTEGER,

    -- Gênero principal usado no dataset.
    genero VARCHAR(100),

    -- Desenvolvedora do jogo.
    developer VARCHAR(150),

    -- Franquia à qual o jogo pertence.
    franchise VARCHAR(150),

    -- Descrição editorial do jogo.
    -- TEXT é usado porque o texto pode ser maior.
    descricao TEXT,

    -- Nota Metacritic.
    metacritic INTEGER,

    -- Nota pessoal do Kadu.
    -- NUMERIC(3, 1) permite valores como 9.5 ou 10.0.
    nota_kadu NUMERIC(3, 1),

    -- Nota pessoal do Pavam.
    nota_pavam NUMERIC(3, 1),

    -- Indica se o jogo é historicamente importante.
    historico_importante BOOLEAN,

    -- Indica se o jogo é historicamente influente.
    historico_influente BOOLEAN
);


-- ==========================================================
-- 5. TABELA: awards
-- ==========================================================
--
-- Esta tabela representa a Awards History.
--
-- Ela foi baseada no arquivo:
--
--   data/awards.csv
--
-- Cada linha representa um jogo indicado ou vencedor em uma edição
-- de premiação de Game of the Year.
--
-- Colunas originais do CSV:
--
--   ano
--   premiacao
--   jogo
--   status
--
-- Observação:
--
-- O arquivo awards.csv não possui uma coluna id.
--
-- Por isso, no PostgreSQL criamos uma coluna id automática com SERIAL.
--
-- SERIAL significa que o próprio PostgreSQL gera o número do id
-- automaticamente a cada novo registro.
--
-- Exemplo:
--
--   primeiro registro  -> id 1
--   segundo registro   -> id 2
--   terceiro registro  -> id 3

CREATE TABLE IF NOT EXISTS awards (
    -- id automático criado pelo PostgreSQL.
    id SERIAL PRIMARY KEY,

    -- Ano da premiação.
    ano INTEGER,

    -- Nome da premiação.
    --
    -- Exemplos:
    --   Spike Video Game Awards
    --   VGX
    --   The Game Awards
    premiacao VARCHAR(150),

    -- Nome do jogo indicado ou vencedor.
    jogo VARCHAR(200),

    -- Status do jogo naquela edição.
    --
    -- Exemplos:
    --   Vencedor
    --   Indicado
    status VARCHAR(50)
);


-- ==========================================================
-- 6. CONSULTAS DE CONFERÊNCIA
-- ==========================================================
--
-- Depois de criar as tabelas, você pode executar este comando
-- para conferir se elas existem no schema public.
--
-- Resultado esperado:
--
--   awards
--   games

SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
ORDER BY table_name;


-- ==========================================================
-- 7. CONSULTAS ÚTEIS APÓS IMPORTAR OS CSVs
-- ==========================================================
--
-- Depois de rodar:
--
--   python scripts/import_to_postgres.py
--
-- use estas consultas para conferir se os dados entraram corretamente.
--
-- Resultado esperado atual:
--
--   games  -> 66 registros
--   awards -> 127 registros
--
-- Estes comandos estão comentados para não rodarem automaticamente
-- junto com a criação das tabelas.
--
-- Para usar algum deles, remova os dois traços "--" do início.


-- ----------------------------------------------------------
-- Contar registros da tabela games
-- ----------------------------------------------------------

-- SELECT COUNT(*) FROM games;


-- ----------------------------------------------------------
-- Contar registros da tabela awards
-- ----------------------------------------------------------

-- SELECT COUNT(*) FROM awards;


-- ----------------------------------------------------------
-- Visualizar os 10 primeiros jogos
-- ----------------------------------------------------------

-- SELECT *
-- FROM games
-- LIMIT 10;


-- ----------------------------------------------------------
-- Visualizar os 10 primeiros registros de awards
-- ----------------------------------------------------------

-- SELECT *
-- FROM awards
-- LIMIT 10;


-- ----------------------------------------------------------
-- Consultar jogos por desenvolvedora
-- ----------------------------------------------------------

-- SELECT *
-- FROM games
-- WHERE developer = 'Capcom';


-- ----------------------------------------------------------
-- Consultar jogos por ano de lançamento
-- ----------------------------------------------------------

-- SELECT *
-- FROM games
-- WHERE ano_lancamento = 2018;


-- ----------------------------------------------------------
-- Consultar jogos de uma franquia
-- ----------------------------------------------------------

-- SELECT *
-- FROM games
-- WHERE franchise = 'Resident Evil';


-- ----------------------------------------------------------
-- Consultar jogos historicamente importantes
-- ----------------------------------------------------------

-- SELECT *
-- FROM games
-- WHERE historico_importante = TRUE;


-- ----------------------------------------------------------
-- Consultar jogos historicamente influentes
-- ----------------------------------------------------------

-- SELECT *
-- FROM games
-- WHERE historico_influente = TRUE;


-- ----------------------------------------------------------
-- Consultar vencedores ou indicados de um ano específico
-- ----------------------------------------------------------

-- SELECT *
-- FROM awards
-- WHERE ano = 2018;


-- ----------------------------------------------------------
-- Consultar apenas vencedores
-- ----------------------------------------------------------

-- SELECT *
-- FROM awards
-- WHERE status = 'Vencedor';


-- ----------------------------------------------------------
-- Contar jogos por gênero
-- ----------------------------------------------------------

-- SELECT genero, COUNT(*) AS total
-- FROM games
-- GROUP BY genero
-- ORDER BY total DESC;


-- ----------------------------------------------------------
-- Contar jogos por desenvolvedora
-- ----------------------------------------------------------

-- SELECT developer, COUNT(*) AS total
-- FROM games
-- GROUP BY developer
-- ORDER BY total DESC;


-- ----------------------------------------------------------
-- Contar jogos por década
-- ----------------------------------------------------------
--
-- Aqui usamos uma conta simples:
--
--   ano_lancamento / 10
--
-- Depois multiplicamos por 10 para chegar na década.
--
-- Exemplo:
--   2005 vira 2000
--   2018 vira 2010

-- SELECT
--     (ano_lancamento / 10) * 10 AS decada,
--     COUNT(*) AS total
-- FROM games
-- GROUP BY decada
-- ORDER BY decada;


-- ==========================================================
-- 8. FLUXO ATUAL DO BANCO NO PROJETO
-- ==========================================================
--
-- O fluxo atual da fase PostgreSQL é:
--
--   data/games.csv
--   data/awards.csv
--          ↓
--   scripts/import_to_postgres.py
--          ↓
--   PostgreSQL
--          ↓
--   tabelas games e awards
--
-- Para ler dados do banco pelo Python:
--
--   PostgreSQL
--          ↓
--   scripts/database.py
--          ↓
--   DataFrames Pandas
--
-- Arquivos relacionados:
--
--   scripts/import_to_postgres.py
--     Importa os CSVs para o PostgreSQL.
--
--   scripts/database.py
--     Lê dados do PostgreSQL e retorna DataFrames.
--
--   scripts/test_database.py
--     Testa se o Python consegue ler corretamente as tabelas do banco.
--
-- ==========================================================


-- ==========================================================
-- 9. STATUS DA ESTRUTURA
-- ==========================================================
--
-- Banco:
--   aaa_archive
--
-- Schema:
--   public
--
-- Tabelas:
--   games
--   awards
--
-- Fonte inicial dos dados:
--   data/games.csv
--   data/awards.csv
--
-- Quantidade esperada após importação:
--   games: 66 registros
--   awards: 127 registros
--
-- Integrações concluídas:
--
--   1. conexão com o PostgreSQL configurada por meio do arquivo .env;
--   2. API FastAPI adaptada para ler dados do PostgreSQL;
--   3. dashboard Streamlit adaptado para ler dados do PostgreSQL.
--
-- Possíveis evoluções futuras:
--
--   1. avaliar a criação de uma relação entre games e awards
--      somente quando a aplicação web demonstrar essa necessidade;
--   2. avaliar a normalização do banco apenas se a estrutura atual
--      deixar de atender às necessidades reais do projeto;
--   3. criar tabelas separadas para developers, genres e franchises
--      somente se houver benefício claro para consultas e manutenção;
--   4. criar novas tabelas ou relacionamentos apenas após planejamento,
--      implementação, testes e documentação.
--
-- ==========================================================