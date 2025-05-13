print ("Esse programa mostra cédulas de um troco")
preco_produto = int(input("Quanto é o produto?"))
valor_pago = int(input("Quanto você pagou?"))
troco = int(valor_pago - preco_produto)

if valor_pago > preco_produto:
    print("Seu troco é de R$", troco)
else:
    print("Você não pagou o valor necessário para o produto")
    exit()

notas200 = troco//200
troco = troco % 200

notas100 = troco//100
troco = troco % 100

notas50 = troco//50
troco = troco % 50

notas20 = troco//20
troco = troco % 20

notas10 = troco//10
troco = troco % 10

notas5 = troco//5
troco = troco % 5

notas2 = troco//2
troco = troco % 2

moedas1 = troco//1
troco = troco % 1

print("Total de cedulas do troco:")

print(f"{notas200} nota(s) de R$ 200,00")
print(f"{notas100} nota(s) de R$ 100,00")
print(f"{notas50} nota(s) de R$ 50,00")
print(f"{notas20} nota(s) de R$ 20,00")
print(f"{notas10} nota(s) de R$ 10,00")
print(f"{notas5} nota(s) de R$ 5,00")
print(f"{notas2} nota(s) de R$ 2,00")
print(f"{moedas1} moeda(s) de R$ 1,00")

