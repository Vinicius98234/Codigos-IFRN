while True:
    try:
        num = input("Digite um número = ")
        numInteiro = int(num)
        break
    except:
        print("Erro na digitação!!!")

dobro =  2 * numInteiro
print(f"O dobro de {numInteiro} é {dobro}")