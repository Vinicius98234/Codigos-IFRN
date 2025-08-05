import re  # Necessário para validação, mas é uma biblioteca padrão do Python

banco_de_dados = {}

while True:
    print("\nMenu de Operações:")
    print("a) Cadastrar CPF")
    print("b) Adicionar MAC address a um CPF")
    print("c) Remover um MAC address de um CPF")
    print("d) Remover o CPF")
    print("e) Listar os CPFs cadastrados")
    print("f) Listar os MAC addresses vinculados a um CPF")
    print("g) Salvar o banco de dados em um arquivo")
    print("h) Ler o banco de dados de um arquivo")
    print("i) Sair")
    
    opcao = input("Escolha uma opção: ").lower()
    
    # Validação de CPF
    def validar_cpf(cpf):
        padrao = re.compile(r'^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$')
        if not padrao.match(cpf):
            return False
        
        # Remove caracteres não numéricos
        numeros = [int(digito) for digito in cpf if digito.isdigit()]
        
        if len(numeros) != 11 or len(set(numeros)) == 1:
            return False
        
        # Validação dos dígitos verificadores
        for i in range(9, 11):
            valor = sum((numeros[num] * ((i+1) - num) for num in range(0, i)))
            digito = ((valor * 10) % 11) % 10
            if digito != numeros[i]:
                return False
        
        return True
    
    # Validação de MAC address
    def validar_mac(mac):
        padrao = re.compile(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$')
        return bool(padrao.match(mac))
    
    if opcao == 'a':
        cpf = input("Digite o CPF (formato: 123.456.789-09 ou 12345678909): ")
        if validar_cpf(cpf):
            if cpf not in banco_de_dados:
                banco_de_dados[cpf] = []
                print("CPF cadastrado com sucesso!")
            else:
                print("Este CPF já está cadastrado!")
        else:
            print("CPF inválido!")
    
    elif opcao == 'b':
        cpf = input("Digite o CPF: ")
        if validar_cpf(cpf):
            if cpf in banco_de_dados:
                mac = input("Digite o MAC address (formato: 00:1A:2B:3C:4D:5E ou 00-1A-2B-3C-4D-5E): ")
                if validar_mac(mac):
                    if mac not in banco_de_dados[cpf]:
                        banco_de_dados[cpf].append(mac)
                        print("MAC address adicionado com sucesso!")
                    else:
                        print("Este MAC address já está vinculado a este CPF!")
                else:
                    print("MAC address inválido!")
            else:
                print("CPF não encontrado no banco de dados!")
        else:
            print("CPF inválido!")
    
    elif opcao == 'c':
        cpf = input("Digite o CPF: ")
        if validar_cpf(cpf):
            if cpf in banco_de_dados:
                if banco_de_dados[cpf]:
                    print("MAC addresses vinculados a este CPF:")
                    for i, mac in enumerate(banco_de_dados[cpf], 1):
                        print(f"{i}. {mac}")
                    try:
                        indice = int(input("Digite o número do MAC address a ser removido: ")) - 1
                        if 0 <= indice < len(banco_de_dados[cpf]):
                            mac_removido = banco_de_dados[cpf].pop(indice)
                            print(f"MAC address {mac_removido} removido com sucesso!")
                        else:
                            print("Número inválido!")
                    except ValueError:
                        print("Entrada inválida! Digite um número.")
                else:
                    print("Não há MAC addresses vinculados a este CPF!")
            else:
                print("CPF não encontrado no banco de dados!")
        else:
            print("CPF inválido!")
    
    elif opcao == 'd':
        cpf = input("Digite o CPF a ser removido: ")
        if validar_cpf(cpf):
            if cpf in banco_de_dados:
                if not banco_de_dados[cpf]:
                    del banco_de_dados[cpf]
                    print("CPF removido com sucesso!")
                else:
                    print("Não é possível remover o CPF pois existem MAC addresses vinculados a ele!")
            else:
                print("CPF não encontrado no banco de dados!")
        else:
            print("CPF inválido!")
    
    elif opcao == 'e':
        if banco_de_dados:
            print("CPFs cadastrados:")
            for cpf in banco_de_dados:
                print(f"- {cpf}")
        else:
            print("Nenhum CPF cadastrado no banco de dados!")
    
    elif opcao == 'f':
        cpf = input("Digite o CPF: ")
        if validar_cpf(cpf):
            if cpf in banco_de_dados:
                if banco_de_dados[cpf]:
                    print(f"MAC addresses vinculados ao CPF {cpf}:")
                    for mac in banco_de_dados[cpf]:
                        print(f"- {mac}")
                else:
                    print("Nenhum MAC address vinculado a este CPF!")
            else:
                print("CPF não encontrado no banco de dados!")
        else:
            print("CPF inválido!")
    
    elif opcao == 'g':
        if banco_de_dados:
            nome_arquivo = input("Digite o nome do arquivo para salvar (ex: dados.txt): ")
            try:
                with open(nome_arquivo, 'w') as arquivo:
                    for cpf, macs in banco_de_dados.items():
                        linha = f"{cpf}:{','.join(macs)}\n"
                        arquivo.write(linha)
                print("Banco de dados salvo com sucesso!")
            except IOError:
                print("Erro ao salvar o arquivo!")
        else:
            print("Nenhum dado para salvar!")
    
    elif opcao == 'h':
        nome_arquivo = input("Digite o nome do arquivo para ler (ex: dados.txt): ")
        try:
            with open(nome_arquivo, 'r') as arquivo:
                banco_de_dados = {}
                for linha in arquivo:
                    partes = linha.strip().split(':')
                    if len(partes) == 2:
                        cpf, macs = partes
                        if validar_cpf(cpf):
                            banco_de_dados[cpf] = macs.split(',') if macs else []
                        else:
                            print(f"CPF inválido encontrado no arquivo: {cpf}")
                print("Banco de dados carregado com sucesso!")
        except FileNotFoundError:
            print("Arquivo não encontrado!")
        except IOError:
            print("Erro ao ler o arquivo!")
    
    elif opcao == 'i':
        print("Saindo do programa...")
        break
    
    else:
        print("Opção inválida! Tente novamente.")