import requests
from bs4 import BeautifulSoup
import json
import os
        
def extract_comments(verse):
    """
    Recebe um verso e retorna uma tupla com o verso e o comentário, se não houver comentário, retorna None
    """
    start = verse.rfind('(')
    end = verse.rfind(')')
    if start != -1 and end != -1 and start < end:
        phrase = verse[:start].strip()
        comment = verse[start:end+1]
        return phrase, comment
    return None
class Lyrics():
    def __init__(self, url):

        # Faz um request para o site letras.com
        response = requests.get(url)

        # Verifica se o request foi bem sucedido
        if response.status_code == 200:

            # Le o conteudo HTML do site
            soup = BeautifulSoup(response.text, 'html.parser')

            # Procura a div contendo as letras da musica
            lyric_div = soup.find('div', class_='lyric-original')
            self.song_title = soup.find('h1',class_='head-title').get_text()

            if lyric_div:
                
                # Extrai cada paragrafo (estrofe)
                paragraphs = lyric_div.find_all('p')

                # Separa os versos por '\n' e armazena cada estrofe em uma string na lista lyrics_list
                self.full_lyrics = [[verse for verse in paragraph.stripped_strings] for paragraph in paragraphs]
                self.stanza_count = len(self.full_lyrics)

                # Flattening da lista full_lyrics
                self.all_verses = [verse for stanza in self.full_lyrics for verse in stanza]
                self.verse_count = len(self.all_verses)

                print("Letras obtidas com sucesso!")
  
            else:
                raise ValueError("Não foram encontradas letras de música na URL fornecida")
        else:
            raise ValueError(f"Não foi possível acesssar a URL. Status code: {response.status_code}")

    def get_unique_verses(self):
        # Armazena os versos sem redundância   
        unique_verses = list(set(self.all_verses))

        # Armazena os comentários e a contagem em atributos
        self.comments = [i[1] for i in [extract_comments(verse) for verse in unique_verses] if i is not None]
        self.comments_count = len(self.comments)
        
        # Armazena os trechos sem os comentários
        verses_with_comment_removed = [i[0] for i in [extract_comments(verse) for verse in unique_verses] if (i is not None) and (i[0] != "")]
        
        # Armazena os versos unicos sem levar em conta os comentários
        self.unique_verses = list(set([verse for verse in unique_verses+verses_with_comment_removed if "(" not in verse]))                               
        self.unique_verses_count = len(self.unique_verses)
        
        print(f"A música tem {self.unique_verses_count} versos distintos e {self.comments_count} comentários")

    def map_verses(self):
        self.hash_table = {str(index):verse for index,verse in enumerate(self.unique_verses)}
        for index,comment in zip(map(lambda x : str(x),range(-1,-1*(self.comments_count)-1,-1)),self.comments):
            self.hash_table[index] = comment
        self.inverse_hash = {k:str(v) for v,k in self.hash_table.items()}
        self.song_code = []
        for stanza in self.full_lyrics:
            current = []
            for verse in stanza:
                if verse in self.inverse_hash:
                    current.append(self.inverse_hash[verse])       
                elif '(' in verse:
                    for comment in self.comments:
                        if comment in verse:
                            content = extract_comments(verse)
                            if content[0] != '':
                                current.append(self.inverse_hash[content[0]]+self.inverse_hash[comment])
                            else:
                                current.append(self.inverse_hash[comment])
            self.song_code.append(current)
    def write_reduced_song(self, path=os.path.join(".","songs")):
        filename = os.path.join(path,f"{self.song_title.replace(' ','_')}.json")
        with open(filename,'w') as file:
            data = {
                "hash":self.hash_table,
                "code":self.song_code
            }
            json.dump(data,file,indent=0)
        print("Lyrics armazenadas em " + filename)

    def write_full_lyrics(self, path=os.path.join(".","songs")):
        filename = os.path.join(path,f"{self.song_title.replace(' ','_')}.txt")
        with open(filename,'w') as test:
            lyrics = ''
            for i in self.all_verses:
                lyrics += i+"\n"
            test.write(lyrics)

def write_lyrics_from_url(url,path=None,full_lyrics=False):
    lyrics = Lyrics(url)
    lyrics.get_unique_verses()
    lyrics.map_verses()
    if path:
        lyrics.write_reduced_song(path=path)
    else:
        lyrics.write_reduced_song()
    if full_lyrics:
        lyrics.write_full_lyrics()
    return lyrics