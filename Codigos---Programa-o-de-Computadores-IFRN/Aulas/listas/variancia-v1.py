soma = 0
qtdeNum = 0

nums = []
num = int (input("Digite um número: "))
while num > 0:
    soma += num 
    qtdeNum += 1
    nums.append(num)
    num = int (input("Digite um número: "))

if qtdeNum > 0:
    media = soma / qtdeNum
    soma = 0
    for num in nums:
        soma += (num - media) ** 2
    variancia = soma / qtdeNum
    print(f"A variancia é {variancia}")
    