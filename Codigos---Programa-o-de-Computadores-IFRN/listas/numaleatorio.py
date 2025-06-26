import random

n = int(input("Digite um número N = "))

l = []

for i in range (100):
    l.append(random.randint(-n , n))
pares = list(filter(lambda x : (x % 2== 0) and (x >= 0) , l))
print(pares)    