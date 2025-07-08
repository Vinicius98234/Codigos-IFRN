print ("Esse programa mostra cédulas de um troco")
produtos = ["Hambúrguer","Pizza","Refrigerante","Batata Frita","Salada","Suco Natural","Sorvete"]

preco_produto = [15.00, 30.00,5.00,10.00, 12.00,8.00,7.00]


for pos in range(len(produtos)):
    print(produtos[pos], preco_produto[pos])
produto_escolhido = int(input("Escolha o produto (0 a 6): "))
valor_pago = float(input("Quanto você pagou? R$ "))
troco = valor_pago - preco_produto[produto_escolhido]
print(f"Seu troco é de R$ {troco:.2f}")
