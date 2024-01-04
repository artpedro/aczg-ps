animais = ["O elefante",
           "Os passarinhos",
           "A minhoquinha",
           "Os pinguins",
           "O canguru",
           "O sapinho"]

gestos = ["Braço direito",
          ", braço esquerdo\n",
          "Perna direita",
          ", perna esquerda\n",
          "Balança a cabeça",
          ", dá uma voltinha\n",
          "Dá um pulinho",
          " e abraça o irmão\n"
          ]

estrofes = [
'''
{c1}Erguei as mãos e dai glória a Deus
Erguei as mãos e dai glória a Deus
Erguei as mãos
E cantai como os filhos do Senhor {c2}
''',
'''
{c1}Os animaizinhos subiram de dois em dois
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
E atenção agora, porque
''',
'''
O senhor tem muitos filhos {c1}
Muitos filhos ele tem {c2}
Eu sou um deles, você também {c3}
Louvemos ao senhor
''',
]

comentarios = [
    '(Para não!)\n',
    '(de novo!)',
    '(Até que eu tô em forma)',
    '(muitos filhos)',
    '(Que saudade dessa música)',
    '(Bonita cruz)',
    "(Para não)",
    'Por isso...!\n'
]

primeira_parte = {
    1: {'e':0},
    2: {'e':1,'a':[0,1]},
    3: {'e':1,'c':[0],'a':[2,3]},
    4: {'e':1,'a':[4,5]},
    5: {'e':2},
    6: {'e':0,'c':[7,-1]},
    7: {'e':0,'c':[-1,1]},
    8: {'e':0},
    9: {'e':3}
}

segunda_parte = {4:{2:2},8:{1:3,3:4},12:{2:5},14:{1:6}}

def fstr(estrofe):
    return eval(f"f'{estrofe}'")

def ler_primeira_parte(estrofe=1):
    if estrofe not in range(1,10):
        print('Essa estrófe não existe')
    adicionais = {"a":'',"b":'',"c1":'',"c2":'',"c3":''}
    codigo_estrofe = primeira_parte[estrofe]
    if 'c' in codigo_estrofe:
        n_comentarios = len(codigo_estrofe['c'])
        if n_comentarios:
            for i,com in zip(range(1,n_comentarios+1),codigo_estrofe['c']):
                if com == -1:
                    continue
                adicionais[f'c{i}'] = comentarios[com]
    if 'a' in codigo_estrofe:
        adicionais['a'] = animais[codigo_estrofe['a'][0]]
        adicionais['b'] = animais[codigo_estrofe['a'][1]]
    
    texto = estrofes[codigo_estrofe['e']].format(a=adicionais['a'],b=adicionais['b'], c1 = adicionais['c1'], c2 = adicionais['c2'], c3 = adicionais['c3'])
    print(texto)

def ler_segunda_parte(estrofe=10):
    if estrofe not in range(10,25):
        print("Essa estrófe não existe")
    index = estrofe - 10
    if estrofe%2 == 0:
        adicionais = {'c1':'','c2':'','c3':''}
        if index in segunda_parte.keys():
            for i in segunda_parte[index]:
                adicionais[f"c{i}"] = comentarios[segunda_parte[index][i]]
            texto = estrofes[4].format(c1 = adicionais['c1'], c2 = adicionais['c2'], c3 = adicionais['c3'])
            print(texto)
        else:
            print(estrofes[4].format(c1 = adicionais['c1'], c2 = adicionais['c2'], c3 = adicionais['c3']))
    else:
        texto = [gestos[i] for i in range(index//2+1)]
        print(*texto,sep='')
        
def ler_tudo():
    for i in range(1,10):
        ler_primeira_parte(i)
    for i in range(10,26):
        ler_segunda_parte(i)
while True:
    parcela = input("Você deseja ver toda a música, apenas uma parte ou apenas uma estrófe? (TODA/PARTE1/PARTE2/ESTROFE/SAIR)\n> ")
    if parcela.upper() == 'ESTROFE':
        estrofe = int(input("Qual estrófe? (1-25)\n> "))
        if estrofe < 10:
            ler_primeira_parte(estrofe)
        else:
            ler_segunda_parte(estrofe)
    if parcela.upper() == 'TODA':
        ler_tudo()
    if parcela.upper() == 'PARTE1':
        for i in range(1,10):
            ler_primeira_parte(i)
    if parcela.upper() == 'PARTE2':
        for i in range(10,26):
            ler_segunda_parte(i)
    if parcela.upper() == 'SAIR':
        break