import socket

HOST = '10.25.3.43'
PORT = 20000  

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


nome_arq = input("Nome arquivo = ")
tam_nome = len(nome_arq)
tam_nome_byte = tam_nome.to_bytes(1, byteorder='big')
nome_arq_encoded = nome_arq.encode('utf-8')

udp_socket.sendto(tam_nome_byte, (HOST, PORT))
udp_socket.sendto(nome_arq_encoded, (HOST, PORT))

print("Solicitação enviada")

resposta_data, _ = udp_socket.recvfrom(1)
resposta = resposta_data[0]
if resposta == 1:
    print(f"Resposta do servidor: {resposta} ")
   
    # Receber tamanho do arquivo (4 bytes)
    tamanho_data, _ = udp_socket.recvfrom(4)
    tamanho_arquivo = int.from_bytes(tamanho_data, byteorder='big')

    print(f"Tamanho do arquivo: {tamanho_arquivo} bytes")
   
    
    recebido = 0
    with open(nome_arq, "wb") as arquivo:
        while recebido < tamanho_arquivo:
            dados, _ = udp_socket.recvfrom(4096)
            arquivo.write(dados)
            recebido += len(dados)
            print(f"Recebidos {recebido}/{tamanho_arquivo} bytes")
    
    print(f"Arquivo '{nome_arq}' salvo com sucesso! ({recebido} bytes recebidos)")
else:
    print(f"Resposta do servidor: {resposta} (arquivo não encontrado)")

udp_socket.close()
