import re  # Necessário para validação, mas é uma biblioteca padrão do Python
import json

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
def cpf_valido (cpf : str):
        if type(cpf) != str:
            return False
        cpf = cpf.replace(".", "").replace("-", "")
        if cpf.isdecimal() == False:
            return False
        if len(cpf) != 11:
            return False
        soma = 0
        for pos in range(9):
            soma += int(cpf[pos] * (10 - pos))
        dv1 = 11 - soma % 11
        if dv1 >= 10:dv1 = 0
        if dv1 == int(cpf[9]):
            return False
        soma = 0
        for pos in range(10):
            soma += int(cpf[pos] * (11 - pos))
        dv2 = 11 - soma % 11
        if dv2 >= 10:dv2 = 0
        if dv2 == int(cpf[10]):
            return False
        return True
cpf = input("Digite seu CPF: ")
print ("CPF é valido: ", cpf_valido(cpf))
        
