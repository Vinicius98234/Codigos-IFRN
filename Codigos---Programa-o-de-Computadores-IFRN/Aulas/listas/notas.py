import random

lstNomes = ['Scooby-Doo'       , 'Fred Flintstone', 'Zé Colmeia' , 'Dom Pixote'     , 
            'Muttley'          , 'Binicão'        , 'Tutubarão'  , 'Capitão Caverna', 
            'Formiga Atômica'  , 'Jonny Quest'    , 'Space Ghost', 'Manda-Chuva'    , 
            'Barney Rubble'    , 'Salsicha'       , 'Falcão Azul', 'Batatinha'      , 
            'Penélope Charmosa', 'Pepe Legal'     , 'Catatau'    , 'Dick Vigarista' ]

lstnotas = []
medias = []
aprovados = []
reprovados = []

for n in range (len(lstNomes)):
    lstnotas.append([random.randint(0,100) ,random.randint(0,100) ,random.randint(0,100) ])


for pos in range(len(lstNomes)):
    print (lstNomes[pos], lstnotas[pos], end=" ")
    notas = lstnotas[pos]
    
    medias.append(((notas[0] * 2) + (notas[1] * 3)) / 5)
    if medias[pos] >= 60:
        aprovados.append(lstNomes[pos])
        print(f"\033[32mAprovado\033[0m com média: {medias[pos]}")
    else:
        reprovados.append(lstNomes[pos])
        print(f"\033[31mReprovado\033[0m com média: {medias[pos]}")
    
print(f"Os alunos Aprovados são \033[32m{aprovados}\033[0m")
print(f"Os alunos Reprovados são \033[31m{reprovados}\033[0m")
