num = int(input("Digite um número = "))
try:
    numInteiro = int(num)
except:
    print("Você digitou um número errado, supondo 0.")
    numInteiro = 0
dobro =  2 * numInteiro
print(f"O dobro de {numInteiro} é {dobro}")