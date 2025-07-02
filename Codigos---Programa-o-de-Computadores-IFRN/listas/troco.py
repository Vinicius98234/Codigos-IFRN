print ("Esse programa mostra cédulas de um troco")
produtos = ["laranja", "banana", "abacaxi", "uva", "melancia"]
preco_produto = [2.50, 1.20, 3.00, 4.50, 5.00]

for pos in range(len(produtos)):
    print(produtos[pos], preco_produto[pos])
produto_escolhido = int(input("Escolha o produto (0 a 4): "))
valor_pago = float(input("Quanto você pagou? R$ "))
troco = valor_pago - preco_produto[produto_escolhido]
print(f"Seu troco é de R$ {troco:.2f}")