print ("Colocar 3 números em ordem crescente")
a = int(input("Digite o primeiro número = "))
b = int(input("Digite o segundo número = "))
c = int(input("Digite o terceiro número = "))
menorvalor = a
if b < menorvalor:
    menorvalor = b
if c < menorvalor:
    menorvalor = c
maiorvalor = a
if b > maiorvalor:
    maiorvalor = b
if c > maiorvalor:
    maiorvalor = c
valormedio = menorvalor<maiorvalor




print ("Os numeros em ordem são ", menorvalor,valormedio,maiorvalor )        
