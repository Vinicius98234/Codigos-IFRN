import random

# Sorteia o número secreto
nsecreto = random.randint(1, 100)

limiteinf = 1
limitesup = 100

print("Tente adivinhar o número entre 1 e 100. Você tem 4 tentativas!")

# Primeira tentativa
print("Tentativa 1 - Digite um número entre", limiteinf, "e", limitesup)
palpite = int(input(": "))
if palpite == nsecreto:
    print("Parabéns! Você acertou na primeira tentativa!")
else:
    if palpite < nsecreto:
        limiteinf = palpite + 1
        print("O número é maior.")
    else:
        limitesup = palpite - 1
        print("O número é menor.")
    
    # Segunda tentativa
    print("Tentativa 2 - Digite um número entre", limiteinf, "e", limitesup)
    palpite = int(input(": "))
    if palpite == nsecreto:
        print("Parabéns! Você acertou na segunda tentativa!")
    else:
        if palpite < nsecreto:
            limiteinf = palpite + 1
            print("O número é maior.")
        else:
            limitesup = palpite - 1
            print("O número é menor.")
        
        # Terceira tentativa
        print("Tentativa 3 - Digite um número entre", limiteinf, "e", limitesup)
        palpite = int(input(": "))
        if palpite == nsecreto:
            print("Parabéns! Você acertou na terceira tentativa!")
        else:
            if palpite < nsecreto:
                limiteinf = palpite + 1
                print("O número é maior.")
            else:
                limitesup = palpite - 1
                print("O número é menor.")
            
            # Quarta tentativa
            print("Tentativa 4 - Digite um número entre", limiteinf, "e", limitesup)
            palpite = int(input(": "))
            if palpite == nsecreto:
                print("Parabéns! Você acertou na quarta tentativa!")
            else:
                print("Suas tentativas acabaram! O número era", nsecreto)