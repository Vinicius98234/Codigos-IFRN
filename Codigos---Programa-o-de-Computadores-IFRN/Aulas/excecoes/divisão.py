while True:
    try:
        num = int(input("Digite um numerador = "))
        den = int(input("Digite o denominador = "))
        print (num/den)
        break
    except:
        print("Erro na digitação!!!")

