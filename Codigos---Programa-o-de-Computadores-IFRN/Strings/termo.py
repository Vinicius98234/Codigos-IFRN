import random
palavras = ("Abacate", "Lima", "Abacaxi")
segredo = palavras [random.randint(0,len(palavras)-1)]
segredo = segredo.lower()
visivel = "_" * len(segredo)

while visivel != segredo:
    print (visivel)
    letra = input("Diga uma letra: ")
    novavisual = ""
    for pos in range(len(segredo)):
        if letra == segredo[pos]:
            novavisual += segredo[pos]
        else:
            novavisual += visivel[pos]
    visivel = novavisual
else:
    print("Você achou a palavra ela era:", segredo)
