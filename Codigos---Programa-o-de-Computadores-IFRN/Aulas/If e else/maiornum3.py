print("Codigo para saber qual número maior: ")
a = int(input("Digite um número qualquer: "))
b = int(input("Digite um número qualquer: "))
c = int(input("Digite um número qualquer: "))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f"O menor número é {menor} e o maior número é {maior}")