print("Codigo para saber qual número maior: ")
n1 = int(input("Digite um número qualquer: "))
n2 = int(input("Digite um número qualquer: "))
n3 = int(input("Digite um número qualquer: "))

if n1 > n2 and n1 > n3:
    print(f"{n1} é o maior número: ")
else:
    if n2 > n1 and n2 > n3:
        print(f"{n2} é o maior número: ")
    else:
        print(f"{n3} é o maior número: ")

if n1 < n2 and n1 < n3:
    print(f"{n1} é o menor número: ")
else:
    if n2 < n1 and n2 < n3:
        print(f"{n2} é o menor número: ")
    else:
        print(f"{n3} é o menor número: ")