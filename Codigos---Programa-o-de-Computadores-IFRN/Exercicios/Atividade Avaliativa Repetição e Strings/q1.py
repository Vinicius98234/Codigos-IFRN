import re  # Necessário para validação, mas é uma biblioteca padrão do Python
import json
import funcoesq1
banco_de_dados = {}

# while True:
#     print("\nMenu de Operações:")
#     print("a) Cadastrar CPF")
#     print("b) Adicionar MAC address a um CPF")
#     print("c) Remover um MAC address de um CPF")
#     print("d) Remover o CPF")
#     print("e) Listar os CPFs cadastrados")
#     print("f) Listar os MAC addresses vinculados a um CPF")
#     print("g) Salvar o banco de dados em um arquivo")
#     print("h) Ler o banco de dados de um arquivo")
#     print("i) Sair")
    
#     opcao = input("Escolha uma opção: ").lower()
    
    # Validação de CPF

cpf = input("Digite seu CPF: ")
print ("CPF é valido: ", funcoesq1.cpf_valido(cpf))
        
