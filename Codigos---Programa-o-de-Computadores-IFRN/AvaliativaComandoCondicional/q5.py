print("Programa que calcula o valor a ser pago no estacionamento com base no tempo de permanência.")  

permanencia = int(input("Quanto tempo em minutos seu carro passou no estacionamento? "))  

horas = permanencia // 60  # Horas completas  
minutos = permanencia % 60  # Minutos excedentes  

# Se houver minutos excedentes, conta +1 hora  
if minutos > 0:  
    horas += 1  

# Definição das tarifas  
tarifa1 = 8   # R$/hora (primeiras 2 horas)  
tarifa2 = 5   # R$/hora (3ª e 4ª horas)  
tarifa3 = 3   # R$/hora (5ª à 12ª horas)  
tarifa_fixa = 30  # Fixo após 12 horas  

# Cálculo do valor  
if horas <= 2:  
    valor_pago = horas * tarifa1  
elif horas <= 4:  
    valor_pago = (2 * tarifa1) + ((horas - 2) * tarifa2)  
elif horas < 12:  
    valor_pago = (2 * tarifa1) + (2 * tarifa2) + ((horas - 4) * tarifa3)  
else:  
    valor_pago = tarifa_fixa  

# Exibição do resultado (sem str(), sem f-string, sem .format())  
print("Você passou", permanencia, "minutos (", horas, "horas) no estacionamento.")  
print("O valor a ser pago é de R$", valor_pago, ".00")  