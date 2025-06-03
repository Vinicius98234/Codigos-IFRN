soma = 2 + 3
for n in range(4,2000000):
    ndiv = 0
    for div in range(2,int(n**0.5)+1):
        if n % div == 0:
            ndiv += 1
            break
    if ndiv == 0:
        soma += n
    if n%10000==0:
        print(n)
print(soma)