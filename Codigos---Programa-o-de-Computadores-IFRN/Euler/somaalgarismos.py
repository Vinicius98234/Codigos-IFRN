print("Somar os algarismos de um numero qualquer")

num = int(input("Digite um numero: "))
soma = 0

while num > 0:
    soma += num % 10
    num = num // 10

print("A soma dos algarismos é igual a: ",soma)