numero = int(input("Digite um número maior que 0 = "))
lista = []

while numero > 0:
    lista += [numero]
    numero = int(input("Digite um número maior que 0 = "))

tamanho = 0
for _ in lista:
    tamanho += 1
print(f"A lista tem {tamanho} elementos")

numexiste = int(input("Digite um número para ver se ele existe = "))
primocorr = -1
numocorrenc = 0
pos = 0
for num in lista: 
    if num == numexiste:
        numocorrenc += 1
        if numocorrenc == 1:
            primocorr = pos
    pos += 1
    
print (f"Existem {numocorrenc} ocorrências de {numexiste} na lista")
if numocorrenc > 0:
    print(f"A primeira ocorrência está no índice {primocorr}.")

menor = lista [0]
for numero in lista:
    if numero < menor:
        menor = numero
print(f"O menor número da lista é {menor}.")

maior = lista[0]
for numero in lista:
    if numero > maior:
        maior = numero
print(f"O maior número da lista é {maior}")

soma = 0
for numero in lista:
    soma += numero
print(f"A soma dos números da lista é {soma}")

