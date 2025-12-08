from funcoeshost import *

while True:
    opcao = menu()
        
    if opcao == '1':
        download_arquivo()
    elif opcao == '2':
        listar_arquivos()
    elif opcao == '3':
        upload_arquivo()
    elif opcao == '4':
        download_por_posicao()
    elif opcao == '5':
        download_multiplo_por_mascara()
    elif opcao == '6':
        print("Saindo...")
        break
    else:
        print("Opção inválida!")