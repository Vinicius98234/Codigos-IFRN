import random

palavras = ("Abacate", "Lima", "Abacaxi", "limao")
segredo = palavras [random.randint(0,len(palavras)-1)]
segredo = segredo.upper()
visivel = "_" * len(segredo)
tentativas = 0

while visivel != segredo:
    if tentativas <= 4:
        print("TERMO")
        print("Você tem apenas 4 tentativas!")
        print (visivel)
        letra = input("Diga uma letra: ")
        letra = letra.upper()
        if len(letra) == 1:
            for l in visivel:
                if l == letra:
                    print("Você já disse essa letra!")
                    print("Tente novamente!")
                    break
            else:
                novovisual = ""
                for pos in range(len(segredo)):
                    if letra == segredo[pos]:
                        novovisual += segredo[pos]
                    else:
                        novovisual += visivel[pos]
                visivel = novovisual
                tentativas += 1
        else:
            print("Digite uma letra somente!!")
            print("Tente novamente!")
    else:
        print("Acabou o numero de chances")
        print("Você tem mais uma chace de acertar a palavra de uma vez!")

        final = input("Palavra que você suspeita que é = ")
        final = final.upper()
        if final == segredo:
            print("Você acertou a chance de ouro!")
            break
        else:
            print("Você errou! A palavra era:", segredo)
            break
else:
    print("Você achou a palavra ela era:", segredo)
