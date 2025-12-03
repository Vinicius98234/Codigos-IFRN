import socket

HOST = '10.25.3.43'
PORT = 50000  

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.connect((HOST,PORT))

nome_arq = input("Nome arquivo = ")
tam_nome = len(nome_arq)
tam_nome_byte = tam_nome.to_bytes(1, byteorder='big')
nome_arq_encoded = nome_arq.encode('utf-8')

tcp_socket.send(tam_nome_byte)
tcp_socket.send(nome_arq_encoded)

print("Solicitação enviada")

resposta_data = tcp_socket.recv(1)
resposta = resposta_data[0]
if resposta == 1:
    print(f"Resposta do servidor: {resposta} ")
   
    # Receber tamanho do arquivo (4 bytes)
    tamanho_data = tcp_socket.recv(4)
    tamanho_arquivo = int.from_bytes(tamanho_data, byteorder='big')

    print(f"Tamanho do arquivo: {tamanho_arquivo} bytes")
   
    
    recebido = 0
    with open(nome_arq, "wb") as arquivo:
        while recebido < tamanho_arquivo:
            dados = tcp_socket.recv(4096)
            arquivo.write(dados)
            recebido += len(dados)
            print(f"Recebidos {recebido}/{tamanho_arquivo} bytes")
    
    print(f"Arquivo '{nome_arq}' salvo com sucesso! ({recebido} bytes recebidos)")
else:
    print(f"Resposta do servidor: {resposta} (arquivo não encontrado)")

tcp_socket.close()