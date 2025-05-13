print ("Calculadora de IMC")

altura = float(input("Informe sua Altura(m): "))

peso = float(input("Informe seu Peso(kg): "))

imc = (peso) / ((altura/100)**2)

print ("Seu IMC é: ", round(imc,1))

if imc > 40:
    print("Obesidade Extrema")
    print("Obesidade Grau 3")
else:
    if  30 < imc < 40:
        print("Obesidade")
        print("Obesidade Grau 2")
        
    else:
        if 25 < imc < 30:
            print("Sobrepeso")
            print("Obesidade Grau 1")
        else:
            if 18.5 < imc < 25:
                print("Peso Normal")
                print("Obesidade Grau 0")
            else:
                print("Magreza")
                print("Obesidade Grau 0")