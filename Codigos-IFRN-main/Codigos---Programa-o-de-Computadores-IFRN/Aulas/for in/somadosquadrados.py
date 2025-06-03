somaq = 0
qsoma = 0
for x in range(0,101):
    somaq += x ** 2
    qsoma += x

diferenca = somaq - qsoma

print("A diferença é", diferenca)