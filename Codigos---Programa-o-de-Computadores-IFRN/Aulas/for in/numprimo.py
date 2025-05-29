print("Diga o número primo")
num = int(input("Diga o número = "))
ndiv = 0

for a in range(1,num // 2 + 1):
    if num % a == 0:
        ndiv += 1 

if ndiv == 1:
    print(num, "É primo")
else:
    print(num, "Não é primo")

    
        
            