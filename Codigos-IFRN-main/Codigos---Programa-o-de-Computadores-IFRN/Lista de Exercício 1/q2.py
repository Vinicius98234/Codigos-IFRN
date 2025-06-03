print ("Calculadora das Raizes de uma Equação de Segundo Grau")

a = int(input("Informe o valor de a = "))
if a != 0:
    b = int(input("Informe o valor de b = "))
    c = int(input("Informe o valor de c = "))

    delta = b**2-4*a*c
    print(f"Valor de Delta Δ = {delta}")
    if delta > 0:
        x1 = (-b + delta ** (1/2)) / (2 * a)
        x2 = (-b - delta ** (1/2)) / (2 * a)
        if x1 == x2:
            print ("A unica raiz é: ", x1)
        else:
            print("As Raízes são: ", x1, x2)
    else:
        print ("Não existe raízes reais!!")
else:
    print("Não é uma equação do 2º Grau!!!")


