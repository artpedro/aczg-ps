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

### 3. Hash table:
   - Criar uma hashtable de versos e comentários
   - Codificar a música usando a hash table
   - Reproduzir pelo Reader