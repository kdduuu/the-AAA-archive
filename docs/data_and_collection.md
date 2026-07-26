# Dados e Coleções

## Fontes editoriais

```text
data/games.csv
→ Foundation Collection

data/awards.csv
→ Awards History
```

A edição dos dados deve acontecer nos CSVs. Depois, o importador sincroniza o PostgreSQL.

## Foundation Collection

Estado atual:

- **105 jogos**;
- IDs contínuos de `1` a `105`;
- período de 1991 a 2025;
- 105 descrições editoriais;
- 100 Metascores preenchidos;
- 5 Metascores intencionalmente vazios.

### Estrutura de `games.csv`

| Campo | Tipo | Regra principal |
| --- | --- | --- |
| `id` | inteiro | identificador único e estável |
| `nome` | texto | nome usado no site e na API |
| `ano_lancamento` | inteiro | ano do lançamento original do registro |
| `genero` | texto | gênero principal |
| `developer` | texto | desenvolvedora principal |
| `franchise` | texto | franquia ou propriedade relacionada |
| `descricao` | texto | resumo editorial curto em português |
| `metacritic` | inteiro ou vazio | Metascore conforme a regra editorial |
| `nota_kadu` | decimal ou vazio | avaliação pessoal opcional |
| `nota_pavam` | decimal ou vazio | avaliação pessoal opcional |
| `historico_importante` | booleano ou vazio | marca de importância histórica |
| `historico_influente` | booleano ou vazio | marca de influência e legado |

### Regra do Metacritic

Usar o maior Metascore entre as plataformas do lançamento original daquele registro.

Não usar notas de relançamentos posteriores, remasters ou versões que não correspondam ao registro catalogado. Um remake incluído como jogo próprio usa a nota de seu próprio lançamento.

O campo pode ficar vazio quando não existe um Metascore compatível com essa regra.

Registros atualmente sem nota:

- The Legend of Zelda: A Link to the Past;
- Chrono Trigger;
- DOOM (1993);
- Cry of Fear;
- P.T.

### Descrições

As descrições devem:

- ter aproximadamente duas frases;
- apresentar importância e identidade do jogo;
- evitar formato de wiki;
- evitar sinopses extensas;
- manter tom editorial e informativo.

Silent Hill 2 possui uma descrição ampliada e pessoal por ser o registro central do criador.

## Awards History

Estado atual:

- **127 registros**;
- **23 edições**;
- período de 2003 a 2025;
- premiações: Spike Video Game Awards, VGX e The Game Awards.

### Estrutura de `awards.csv`

| Campo | Tipo | Regra principal |
| --- | --- | --- |
| `ano` | inteiro | ano da edição |
| `premiacao` | texto | nome oficial da premiação |
| `jogo` | texto | vencedor ou indicado |
| `status` | texto | `Vencedor` ou `Indicado` |

Cada edição possui um vencedor e seus indicados.

### Relação com a Foundation

A base de Awards é independente da Foundation. Um jogo premiado não entra automaticamente na coleção.

A comparação normaliza diferenças conhecidas de nomes, incluindo:

- `GTA` e `Grand Theft Auto`;
- `The Walking Dead` e `The Walking Dead: Season One`.

No estado atual, **19 de 23 vencedores** estão na Foundation, aproximadamente **83%**.

## PostgreSQL

Tabelas operacionais:

```sql
CREATE TABLE games (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(200) NOT NULL,
    ano_lancamento INTEGER,
    genero VARCHAR(100),
    developer VARCHAR(150),
    franchise VARCHAR(150),
    descricao TEXT,
    metacritic INTEGER,
    nota_kadu NUMERIC(3, 1),
    nota_pavam NUMERIC(3, 1),
    historico_importante BOOLEAN,
    historico_influente BOOLEAN
);

CREATE TABLE awards (
    id SERIAL PRIMARY KEY,
    ano INTEGER,
    premiacao VARCHAR(150),
    jogo VARCHAR(200),
    status VARCHAR(50)
);
```

O `id` de Awards é técnico e gerado pelo PostgreSQL.

## Assets dos jogos

Padrão principal:

```text
frontend/public/assets/games/{id}/cover.webp
```

Existe um `cover.webp` para cada ID de `1` a `105`. A mesma imagem é usada no GameCard e na GamePage.

Não existe `hero.webp` separado para os registros.

Assets exclusivos da Home:

```text
frontend/public/assets/games/1/featured.webp
frontend/public/assets/games/3/featured.webp
frontend/public/assets/games/14/featured.webp
frontend/public/assets/games/41/featured.webp
```

Eles representam Final Fantasy VII, Metal Gear Solid, Resident Evil 4 e The Last of Us.

## Atualização dos dados

1. editar `data/games.csv` ou `data/awards.csv`;
2. validar nomes e colunas;
3. executar:

```powershell
python scripts/import_to_postgres.py
```

4. conferir:

```powershell
python scripts/test_database.py
```

5. testar API, frontend e dashboard;
6. enviar as alterações ao GitHub.

O importador limpa e recarrega as duas tabelas. Portanto, o CSV completo precisa permanecer consistente antes da execução.
