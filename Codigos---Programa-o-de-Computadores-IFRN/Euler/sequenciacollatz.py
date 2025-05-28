print("Maior sequência de Collatz - Problema 14")

# n = int(input("Numero qualquer para descobrir a maior sequencia = "))

x = 1
while x < 10:
    n = x
    print(n)
    while n > 1:
        if n % 2 == 0:
            n = n // 2
            
        else: 
            n = 3 * n + 1
        print("->", n, end ="")
    print()
    x += 1
print("FIM")


