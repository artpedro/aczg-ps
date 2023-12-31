import requests
from bs4 import BeautifulSoup

class Lyrics():
    def __init__(self, url):

        # Faz um request para o site letras.com
        response = requests.get(url)

        # Verifica se o request foi bem sucedido
        if response.status_code == 200:

            # Le o conteudo HTML do site
            self.soup = BeautifulSoup(response.text, 'html.parser')

            # Procura a div contendo as letras da musica
            lyric_div = self.soup.find('div', class_='lyric-original')

            if lyric_div:
                # Extrai cada paragrafo (estrofe)
                paragraphs = lyric_div.find_all('p')

                # Separa os versos por '\n' e armazena cada estrofe em uma string na lista lyrics_list
                self.full_lyrics = [[verse for verse in paragraph.stripped_strings] for paragraph in paragraphs]
                self.stanza_count = len(self.full_lyrics)

                # Compacta full_lyrics
                self.all_verses = [verse for stanza in self.full_lyrics for verse in stanza]
                self.verse_count = len(self.all_verses)

                print("Letras obtidas com sucesso!")
  
            else:
                raise ValueError("Não foram encontradas letras de música na URL fornecida")
        else:
            raise ValueError(f"Não foi possível acesssar a URL. Status code: {response.status_code}")
    def get_unique_verses(self):
        
        self.unique_verses = list(set(self.all_verses))
        self.unique_verses_count = len(self.unique_verses)

        print(f"A música tem {self.unique_verses_count} versos distintos")
        print(self.unique_verses)
        for a_verse in range(self.unique_verses_count):
            for b_verse in range(a_verse + 1, self.unique_verses_count):
                # print(f"Pair: {self.unique_verses[a_verse]}, {self.unique_verses[b_verse]}")
                pass

    def map_verses(self):
        pass

url = 'https://www.letras.mus.br/padre-marcelo-rossi/47896/'

lyrics = Lyrics(url)

if lyrics:
    lyrics.get_unique_verses()