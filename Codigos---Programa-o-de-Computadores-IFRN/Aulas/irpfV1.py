print("Calcular o imposto a pagar e o salário líquido: ")

bruto = float(input("Digite seu salário bruto = "))


if bruto >= 4664.68:
    imposto = (bruto * 0.275) - 908.73
else:
    if 3571.06 <= bruto <= 4664.68:
        imposto = (bruto * 0.225) - 675.49
    else:
        if 2826.66 <= bruto <= 3571.05:
            imposto = (bruto * 0.15) - 394.16
        else:
            if 2428.80 <= bruto <= 2826.65:
                imposto = (bruto * 0.075) - 182.16
            else:
                imposto = (bruto * 0) - 0
                print("Você está insento de imposto")

# Se por um numero 2428.805 como bruto o comando da erro por causa dos valores que foram editados no irpfV2.py

liquido = bruto - imposto
print("O imposto a ser pago vai ser de ", imposto, "e o seu salário liquido é de: ", liquido)
