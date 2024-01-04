import lyrics_reducer
import os
import json
from colorama import Back, Style

def print_name():
    print(Style.BRIGHT + Back.LIGHTGREEN_EX + 'LyricsReader:'+ Back.RESET + Style.RESET_ALL ,end=' ')

def read_all(code,hash_table):
    print("\n")
    for stanza in code:
        for verse in stanza:
            both = verse.split('-')
            if both[0] != "" and len(both) == 2:
                print(hash_table[both[0]]+' '+hash_table['-' + both[1]])
            else:
                print(hash_table[verse])
        print("\n")

def read_verse(code,hash_table,index):
    print('\n')
    all_verses = [verse for stanza in code for verse in stanza]
    both = all_verses[index].split('-')
    if both[0] != "" and len(both) == 2:
        print(hash_table[both[0]]+' '+hash_table['-' + both[1]])
    else:
        print(hash_table[all_verses[index]])
    print("\n")

def read_stanza(code, hash_table, index):
    print("\n")
    for verse in code[index]:
        both = verse.split('-')
        if both[0] != "" and len(both) == 2:
            print(hash_table[both[0]]+' '+hash_table['-' + both[1]])
        else:
            print(hash_table[verse])
    print("\n")

def reader(obj=None,name=None):
    while True:
        if obj:
            song_hash = obj.hash_table
            song_code = obj.song_code
            all_verses_count = obj.verse_count
        if name:
            path = os.path.join(".","songs",name)
            with open(path,'r') as song:
                info = json.load(song)
                song_hash = info['hash']
                song_code = info['code']
                all_verses_count = len([verse for verse in [stanza for stanza in song_code]])
        print_name()
        choice = input("Do you wanna read the full lyrics, a verse or a stanza?" +Style.DIM + " (FULL/VERSE/STANZA/QUIT)" + Style.RESET_ALL + "\n")
        if choice.upper() == 'FULL':
            read_all(song_code,song_hash)
        if choice.upper() == 'VERSE':
            print_name()
            index = int(input('Which verse?\n'))
            if index <= all_verses_count:
                read_verse(song_code, song_hash, index)
            else:
                print("Invalid verse")
        if choice.upper() == 'STANZA':
            print_name()
            index = int(input('Which stanza?\n'))
            if index <= len(song_code):
                read_stanza(song_code, song_hash, index)
            else:
                print('Invalid stanza')
        if choice.upper() == 'QUIT':
            break

if __name__ == '__main__':

    print(Style.BRIGHT+'''
    ╔════════════════════════════════════════════════════════════════════╗
    ║ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪  ║
    ║ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪         Lyrics Reader       ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪  ║
    ║ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪  ║
    ╚════════════════════════════════════════════════════════════════════╝
    '''+Style.RESET_ALL
    )
    
    while True:
        print_name()
        choice = input('You want to read a song from the URL or from Songs folder?' + Style.DIM +' (URL/FOLDER/QUIT)' + Style.RESET_ALL + '\n')
        if choice.upper() == 'URL':
            print_name()
            url = input("Input your URL: ")
            try:
                lyrics = lyrics_reducer.write_lyrics_from_url(url)
            except:
                raise(ValueError("Invalid URL"))
            reader(obj = lyrics)
        elif choice.upper() == 'FOLDER':
            path = os.path.join(".","songs","")
            songs = {index:name for index,name in enumerate(os.listdir(path))}
            print(songs)
            print()
            print([str(index)+f" - {name[:len(name)-5]}" for index,name in enumerate(os.listdir(path))])
            print()
            print_name()
            number = int(input("What song do you want?\n"))
            if int(number) in songs:
                reader(name=songs[number])
            else:
                print_name()
                print('Invalid Song')
        elif choice.upper() == "QUIT":
            print_name()
            print('Ok, bye!')
            break
    