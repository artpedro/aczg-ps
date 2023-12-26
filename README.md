Objetivos:
    - Criar um parser para extrair de um url cada estrofe da música e armazenar em uma lista 'full_song', cada estrofe será uma lista com cada verso em ordem
    - Verificar quais são os versos únicos
        + variaveis:
            - full_song: [["verse","verse"], ["verse","verse"]]
                full_song[1][2] = verso 3 da estrofe 2
            - unique_verses: [[verse]]
    - Verificar quais dos versos únicos são extensões ou parcelas de outros versos
        - Criando uma função que recebe duas strings (a, b) e compara o número de palavras em cada,
        e se houver discrepância, verifica, palavra por palavra, se a é uma extensão de b ou uma parcela
    
    - Verificar quais dos versos possuem o mesmo tamanho, mas diferem em uma palavra de outro
        - Criando uma função que recebe duas strings (a, b) com a mesma quantidade de palavras (deve ser checado) que
        checa, palavra por palavra, se as duas strings se diferem por somente uma palavra (devolve True)
        - Criando uma segunda função que verifica a posição e as palavras que se diferem (devolve uma tupla (posição, list(palavras)))
         