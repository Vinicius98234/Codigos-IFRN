num = int(input("Digite um número para saber se ele é palíndromo = "))
numfinal = num
n = 0
while num > 0:
    algarismo = num % 10
    num = num // 10
    n = 10 * n + algarismo
    
if n == numfinal:
    print(n, "é um palíndromo!")
else:
    print(n, "não é um palíndromo!")