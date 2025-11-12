import funcoesq2

# Loop principal do programa - fica rodando até o usuário querer sair
while True:
    print("\n=== SISTEMA RAID ===")
    print("1. Inicializar RAID")
    print("2. Carregar RAID existente")
    print("3. Escrever dados")
    print("4. Ler dados")
    print("5. Simular falha de disco")
    print("6. Reconstruir disco")
    print("7. Sair")
        
    opcao = input("Escolha uma opção: ")
        
    if opcao == '1':
        funcoesq2.inicializaRAID()
    elif opcao == '2':
        funcoesq2.obtemRAID()
    elif opcao == '3':
        funcoesq2.escreveRAID()
    elif opcao == '4':
        funcoesq2.leRAID()
    elif opcao == '5':
        funcoesq2.removeDiscoRAID()
    elif opcao == '6':
        funcoesq2.constroiDiscoRAID()
    elif opcao == '7':
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
