print("Programa que leia o número de minutos que um veículo permaneceu no estacionamento e exiba o valor a ser pago pelo responsável.") #Exibe o que o programa faz

permanencia = int(input("Quanto tempo em minutos seu carro passou no estacionamento? "))
horas = permanencia/60

tarifa1 = 8 #Tarifa das primeira 2 horas
tarifa2 = 5 #Tarifa de 3 as 4 horas
tarifa3 = 3 #Tarifa de 4 as 12 horas
tarifafix = 30 # Tarifa fixa a partir das 12 horas

if horas <= 2: 
    valpago = tarifa1 * horas  # Tarifa 1 * a quantidade de horas
    print("Você passou", permanencia, "minutos no estacionamento. O valor a ser pago é de R$", valpago)
else:
    if horas <= 4:
        valpago = (2 * tarifa1) + ((horas-2) * tarifa2) # valor pago pelas duas primeiras horas e soma com as ultimas horas
        print("Você passou", permanencia, "minutos no estacionamento. O valor a ser pago é de R$", valpago)
    else:
        if horas < 12:
            valpago = (2 * tarifa1) + (2 * tarifa2) + ((horas - 4) * tarifa3) # valor pago pelas duas primeiras horas e a soma entre as 3 e 4 horas e o resto das horas até 12 horas
            print("Você passou", permanencia, "minutos no estacionamento. O valor a ser pago é de R$", valpago)
        else:
            valpago = tarifafix # Valor fixo a partir das 12 horas
            print("Você passou", permanencia, "minutos no estacionamento, que é equivalente a mais de 12 horas, então, O valor a ser pago é de R$", valpago)
    
    

