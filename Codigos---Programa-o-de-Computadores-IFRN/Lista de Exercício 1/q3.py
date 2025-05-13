print("Calculador do montante gerado pelo capital: ")
c = int(input("Diga o valor do Capital = "))
i = int(input("Diga a taxa em porcentagem = "))
t = int(input("Diga o tempo em meses = "))

montante = c * (1 + i/100)**t
print ("O valor do montante é =", montante)
