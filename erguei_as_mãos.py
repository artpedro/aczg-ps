from lyrics_reducer import Lyrics

song = Lyrics(url="https://www.letras.mus.br/padre-marcelo-rossi/47896/")

animais = ["O elefante",
           "Os passarinhos",
           "A minhoquinha",
           "Os pinguins",
           "O canguru",
           "O sapinho"]

gestos = ["Braço direito",
          "braço esquerdo",
          "Perna direita",
          "perna esquerda",
          "Balança a cabeça",
          "dá uma voltinha",
          "Dá um pulinho",
          "e abraça o irmão"
          ]
a,b,c1,c2,c3 = '','','','',''

estrofes = [
f'''Erguei as mãos e dai glória a Deus
Erguei as mãos e dai glória a Deus
Erguei as mãos
E cantai como os filhos do Senhor {c1}
''',
f'''
{c1}
Os animaizinhos subiram de dois em dois
Os animaizinhos subiram de dois em dois
{a}
E {b}, como os filhos do Senhor
''',
'''
Deus disse a Noé: Constrói uma arca
Deus disse a Noé: Constrói uma arca
Que seja feita
De madeira para os filhos do Senhor
''',
'''
Por isso...!
''',
'''
E atenção agora, porque
''',
f'''
O senhor tem muitos filhos {c1}
Muitos filhos ele tem {c2}
Eu sou um deles, você também {c3}
Louvemos ao senhor
''',
]

comentarios = [
    '(Para não!)',
    '(de novo!)',
    '(Até que eu tô em forma)',
    '(muitos filhos)',
    '(Que saudade dessa música)',
    '(Bonita cruz)'
    '(Para não)'
]