n = int(input("Qual numero você quer o fatorial: "))
m = int(input("digite um numero inteiro e positivo: "))

fatorial = 1
contador = 1

while contador <= n:
    fatorial *= contador
    contador += 1
    
for x in range(n + 1, m ):   
    if fatorial % x == 0:
        print(x, "é um Jaime de", n)
