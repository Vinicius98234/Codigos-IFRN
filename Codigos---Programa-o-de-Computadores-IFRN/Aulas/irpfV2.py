print("Calcular o imposto a pagar e o salário líquido: ")

bruto = float(input("Digite seu salário bruto = "))
bruto = round(bruto, 2)

if bruto >= 4664.68:
    imposto = (bruto * 0.275) - 908.73
else:
    if bruto <= 4664.68:
        imposto = (bruto * 0.225) - 675.49
    else:
        if bruto <= 3571.05:
            imposto = (bruto * 0.15) - 394.16
        else:
            if bruto <= 2826.65:
                imposto = (bruto * 0.075) - 182.16
            else:
                imposto = (bruto * 0) - 0
                print("Você está insento de imposto")

liquido = bruto - imposto
print("O imposto a ser pago vai ser de ", imposto, "e o seu salário liquido é de: ", liquido)
