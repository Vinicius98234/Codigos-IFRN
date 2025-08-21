print ("Colocar os numeros em ordem crescente")
a = int(input("Digite o primeiro número = "))
b = int(input("Digite o segundo número = "))
c = int(input("Digite o terceiro número = "))

if (a != b and a != c) or (b != a and b != c) or (c != a and c != b):
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


    if (a and b) < (maior):
        if a > b:
            print(b , a, maior)
# TENTANDO AINDA
else: 
    print("Os números são iguais")