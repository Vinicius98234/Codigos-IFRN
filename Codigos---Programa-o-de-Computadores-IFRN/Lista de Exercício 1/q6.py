print ("ICMS a ser recolhido pela empresa na operação.")

i = 0.17
produto = input("Qual o produto: ")
v = int(input("Valor vendido pelo produto = "))
c = int(input("Valor comprado pelo produto = "))
icms = (v - c) * i


print ("O ICMS recolhido pela empresa na operação é de = ", icms)