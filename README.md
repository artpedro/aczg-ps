# LyricsReducer

## Guia para implementação

### 1. Criar um parser para extrair estrofes de uma música a partir de uma URL:
   - Armazenar em uma lista chamada 'full_song';
   - Cada estrofe será uma lista contendo cada verso em ordem.

### 2. Verificar versos únicos:
   + **Variáveis:**
     - `full_song`: List[List[str]]
         - Exemplo: `full_song[1][2]` = verso 3 da estrofe 2
     - `unique_verses`: List[str]

### 3. Verificar extensões ou parcelas de versos únicos:
   - Criar uma função que recebe duas strings (a, b) e compara o número de palavras em cada uma:
       - Se houver discrepância, verificar, palavra por palavra, se a é uma extensão de b ou uma parcela
    - Aplicar essa função em cada par de versos

### 4. Verificar versos do mesmo tamanho diferentes por uma palavra
   - Criar uma função que recebe duas strings (a, b) com a mesma quantidade de palavras (deve ser checado)
       - Checar, palavra por palavra, se as duas strings se diferem por somente uma palavra (devolver True)
    - Criar uma segunda função que verifica a posição e as palavras que se diferem (devolve uma tupla `(posição, list(palavras))`)
