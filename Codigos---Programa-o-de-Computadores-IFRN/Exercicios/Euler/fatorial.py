fatorial = int(input("Qual numero você quer o fatorial: "))

resultado = 1
contador = 1
while contador <= fatorial:
    resultado *= contador
    contador += 1

print (resultado)