print ("Colocar os numeros em ordem crescente")
a = int(input("Digite o primeiro número = "))
b = int(input("Digite o segundo número = "))
if a != b:
    if a < b:
        print ("Os numeros são ",a,"e",b)
    else :
        print ("Os numeros são ",b,"e" ,a)
else:
    print ("Os dois numeros são iguais a ", a)