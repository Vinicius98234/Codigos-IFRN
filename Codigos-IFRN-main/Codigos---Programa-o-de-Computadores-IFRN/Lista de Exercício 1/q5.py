print ("calculadora do saldo da conta")

c = int(input("Informe o capital inicial = "))
d = int(input("Informe o deposito mensal = "))
i = int(input("Informe a taxa de juros mensal = "))
n = int(input("Informe a quantidade de meses = "))
taxa = 1+i/100

saldo = (c * (taxa)**n) + (d * ((taxa)**n - (taxa)) / (i/100))
print ("Seu saldo é =", round(saldo, 2))

# 1000
#d=500
#i=2
#n = 80
# saldo = 101.261,42