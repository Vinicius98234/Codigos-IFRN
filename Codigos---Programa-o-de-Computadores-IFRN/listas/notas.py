import random

lstNomes = ['Scooby-Doo'       , 'Fred Flintstone', 'Zé Colmeia' , 'Dom Pixote'     , 
            'Muttley'          , 'Binicão'        , 'Tutubarão'  , 'Capitão Caverna', 
            'Formiga Atômica'  , 'Jonny Quest'    , 'Space Ghost', 'Manda-Chuva'    , 
            'Barney Rubble'    , 'Salsicha'       , 'Falcão Azul', 'Batatinha'      , 
            'Penélope Charmosa', 'Pepe Legal'     , 'Catatau'    , 'Dick Vigarista' ]

lstnotas = []

for n in range (len(lstNomes)):
    lstnotas.append([random.randint(0,100) ,random.randint(0,100) ,random.randint(0,100) ])


for pos in range(len(lstNomes)):
    print (lstNomes[pos], lstnotas[pos], end=" ")
    notas = lstnotas[pos]
    nota1 = notas[0]
    nota2 = notas[1]
    soma = nota1 + nota2
    media = soma / 2
    if media >= 60:
        print(f"\033[32mAprovado com média: {media}\033[0m")
    else:
        print(f"\033[31mReprovado com média: {media}\033[0m")
    
        