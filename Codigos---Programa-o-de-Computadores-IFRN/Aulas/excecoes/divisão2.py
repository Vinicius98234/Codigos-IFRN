while True:
    try:
        num = int(input("Digite um numerador = "))
        den = int(input("Digite o denominador = "))
        print (num/den)
        break
    except ValueError as e1:
        print("Erro na digitação!!!")
    except ZeroDivisionError as e2:
        print("Erro na divisão por zero!!!")
