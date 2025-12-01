import socket
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", 20000))
sock.settimeout(30.0)  
PASTA_SERVER = "server"

while True:
    print("Escutando todos os ips na porta 20000...")
   
    # Receber tamanho do nome do arquivo
    tam_nome_data, src = sock.recvfrom(1)
    tam_nome = int.from_bytes(tam_nome_data, byteorder='big')
    print(f"Tamanho do nome do arquivo: {tam_nome} bytes")

    # Receber nome do arquivo
    nome_arqu_data, src = sock.recvfrom(tam_nome)
    nome_arqu = nome_arqu_data.decode('utf-8')
    print(f"Recebido de {src}: {nome_arqu}")

    caminho_arquivo = os.path.join(PASTA_SERVER, nome_arqu)
    if os.path.exists(caminho_arquivo):
        resposta = b"\x01"  # Arquivo existe
        print("Arquivo encontrado")
        sock.sendto(resposta, src)

        # Obter tamanho do arquivo
        tamanho_arquivo = os.path.getsize(caminho_arquivo)
        print(f"Tamanho do arquivo: {tamanho_arquivo} bytes")

        # Enviar tamanho do arquivo em 4 bytes
        tamanho_bytes = tamanho_arquivo.to_bytes(4, byteorder='big')
        sock.sendto(tamanho_bytes, src)
   
        # Enviar conteúdo do arquivo
        with open(caminho_arquivo, "rb") as arquivo:
            enviados = 0
            while enviados < tamanho_arquivo:
                dados = arquivo.read(4096)
                sock.sendto(dados, src)
                enviados += len(dados)

            print(f"Conteúdo do arquivo enviado ({enviados} bytes)")
    else:
        resposta = b"\x00"  # Arquivo não existe
        print("Arquivo não encontrado")
        sock.sendto(resposta, src)