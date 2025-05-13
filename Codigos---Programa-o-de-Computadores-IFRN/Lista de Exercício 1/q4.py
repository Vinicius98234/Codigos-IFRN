import math

print("Calculadora da quantidade de meses em relação a um montante por taxa mensal: ")
c = int(input("Diga o valor do Capital = "))
i = int(input("Diga a taxa em porcentagem = "))
m = int(input("Diga o montante = "))

t = math.log(m/c) / math.log(1+i/100)
t = math.ceil(t)

print ("A quantidade de meses em relação ao montante é = ", t , "meses")
