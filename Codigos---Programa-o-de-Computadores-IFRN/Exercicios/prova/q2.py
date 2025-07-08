n = int(input("Qual numero você quer o fatorial: "))
m = int(input("digite um numero inteiro e positivo: "))

fatorial = 1
contador = 1

while contador <= n:
    fatorial *= contador
    contador += 1
    
if fatorial % m == 0:
    print(m, "é um Jaime de", n)
