print("Calcular o maior fator primo de um número: ")
n = int(input("Numero para descobrir seu maior fator primo = "))
fatorprimo = 2 
maiorfator = -1

while n > 1:
    if n % fatorprimo == 0:
        n = n // fatorprimo
        if fatorprimo > maiorfator:
            maiorfator = fatorprimo
    else:
        fatorprimo += 1
    print(fatorprimo)
print("O maior fator é",maiorfator)

        

   
    
