print("Maior sequência de Collatz - Problema 14")

# n = int(input("Numero qualquer para descobrir a maior sequencia = "))

x = 1
maiortam = 0
geradormaior = 0
while x < 1000000:
    n = x
    tam = 1
    while n > 1:
        if n % 2 == 0:
            n = n // 2
            
        else: 
            n = 3 * n + 1
        tam += 1
    # print("A cadeia do", x, "tem", tam, "elementos")
    if tam > maiortam:
        maiortam = tam
        geradormaior = x
    x += 1
print("FIM - O maior tamanho é: ", maiortam, "na sequência do", geradormaior)


