import socket
import os
import time
HOST = ""
PORT = 50000
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_socket.bind((HOST,PORT))
tcp_socket.listen(5)
print("Escutando todos os ips na porta 20000...")    

PASTA_SERVER = "server"
while True:
    con,cliente = tcp_socket.accept()
    print(f"Conecetado por: {cliente}")
    while True:
        # Receber tamanho do nome do arquivo
        tam_nome_data = con.recv(1)
        tam_nome = int.from_bytes(tam_nome_data, byteorder='big')
        print(f"Tamanho do nome do arquivo: {tam_nome} bytes")

        # Receber nome do arquivo
        nome_arqu_data = con.recv(tam_nome)
        nome_arqu = nome_arqu_data.decode('utf-8')
        

        caminho_arquivo = os.path.join(PASTA_SERVER, nome_arqu)
        if os.path.exists(caminho_arquivo):
            resposta = b"\x01"  # Arquivo existe
            print("Arquivo encontrado")
            con.send(resposta)

            # Obter tamanho do arquivo
            tamanho_arquivo = os.path.getsize(caminho_arquivo)
            print(f"Tamanho do arquivo: {tamanho_arquivo} bytes")

            # Enviar tamanho do arquivo em 4 bytes
            tamanho_bytes = tamanho_arquivo.to_bytes(4, byteorder='big')
            con.send(tamanho_bytes)
    
            # Enviar conteúdo do arquivo
            with open(caminho_arquivo, "rb") as arquivo:
                enviados = 0
                while enviados < tamanho_arquivo:
                    dados = arquivo.read(4096)
                    con.send(dados)
                    enviados += len(dados)
                    time.sleep(0.1)

                print(f"Conteúdo do arquivo enviado ({enviados} bytes)")
            break
        else:
            resposta = b"\x00"  # Arquivo não existe
            print("Arquivo não encontrado")
            con.send(resposta)
            break
    print(f"Finaliando conexão do cliente {cliente}")
    con.close()