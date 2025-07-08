soma = 0
qtdeNum = 0

num = int (input("Digite um número: "))
while num > 0:
    soma += num
    qtdeNum += 1
    num = int (input("Digite um número: "))

if qtdeNum > 0:
    media = soma / qtdeNum
    print (media)