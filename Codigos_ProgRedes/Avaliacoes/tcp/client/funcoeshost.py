import socket
import hashlib

HOST = '192.168.1.5'
PORT = 20000

def menu():
    print("\n=== FILE SERVER TCP ===")
    print("1. Download de arquivo")
    print("2. Listar arquivos")
    print("3. Upload de arquivo")
    print("4. Download a partir de posição")
    print("5. Download múltiplo")
    print("6. Sair")
    return input("Escolha: ")

def download_arquivo():
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10.0)
    
    try:
        sock.connect((HOST, PORT))
    except Exception as e:
        print(f"Erro ao conectar: {e}")
        return
    
    nome_arq = input("Nome do arquivo para download: ")
    
    # Enviar operação (10)
    sock.send(b'\x0A')
    
    # Enviar tamanho do nome (4 bytes big endian)
    tam_nome = len(nome_arq)
    sock.send(tam_nome.to_bytes(4, byteorder='big'))
    
    # Enviar nome do arquivo
    sock.send(nome_arq.encode('utf-8'))
    
    # Receber status (1 byte)
    resposta_data = sock.recv(1)
    if not resposta_data:
        print("Sem resposta do servidor")
        sock.close()
        return
    
    resposta = resposta_data[0]
    
    if resposta == 1:
        print("Arquivo encontrado")
        
        # Receber tamanho do arquivo (4 bytes)
        tamanho_data = sock.recv(4)
        if len(tamanho_data) < 4:
            print("Erro ao receber tamanho")
            sock.close()
            return
        
        tamanho_arquivo = int.from_bytes(tamanho_data, byteorder='big')
        print(f"Tamanho do arquivo: {tamanho_arquivo} bytes")
        
        # Receber conteúdo
        recebido = 0
        with open(nome_arq, "wb") as arquivo:
            while recebido < tamanho_arquivo:
                dados = sock.recv(1024)
                if not dados:
                    break
                arquivo.write(dados)
                recebido += len(dados)
                print(f"Recebidos {recebido}/{tamanho_arquivo} bytes")
        
        print(f"Arquivo '{nome_arq}' salvo com sucesso!")
    else:
        print("Arquivo não encontrado no servidor")
    
    sock.close()

def listar_arquivos():
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10.0)
    
    try:
        sock.connect((HOST, PORT))
    except Exception as e:
        print(f"Erro ao conectar: {e}")
        return
    
    # Enviar operação (20)
    sock.send(b'\x14')
    
    # Receber status
    status_data = sock.recv(1)
    if not status_data:
        print("Sem resposta")
        sock.close()
        return
    
    status = status_data[0]
    
    if status == 1:
        # Receber tamanho da listagem
        tam_data = sock.recv(4)
        if len(tam_data) < 4:
            print("Erro ao receber tamanho da listagem")
            sock.close()
            return
        
        tam_lista = int.from_bytes(tam_data, byteorder='big')
        
        # Receber JSON
        lista_bytes = b''
        while len(lista_bytes) < tam_lista:
            dados = sock.recv(1024)
            if not dados:
                break
            lista_bytes += dados
        
        # Simples impressão - sem import json
        lista_str = lista_bytes.decode('utf-8')
        print("\n=== ARQUIVOS DISPONÍVEIS ===")
        print(lista_str)
        print("============================\n")
    else:
        print("Erro ao listar arquivos")
    
    sock.close()

def upload_arquivo():
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10.0)
    
    try:
        sock.connect((HOST, PORT))
    except Exception as e:
        print(f"Erro ao conectar: {e}")
        return
    
    nome_arq = input("Nome do arquivo para upload: ")
    
    # Tentar abrir arquivo local
    try:
        with open(nome_arq, "rb") as arquivo:
            conteudo = arquivo.read()
        tam_arquivo = len(conteudo)
    except:
        print("Arquivo não encontrado localmente")
        sock.close()
        return
    
    # Enviar operação (30)
    sock.send(b'\x1E')
    
    # Enviar tamanho do nome
    tam_nome = len(nome_arq)
    sock.send(tam_nome.to_bytes(4, byteorder='big'))
    
    # Enviar nome do arquivo
    sock.send(nome_arq.encode('utf-8'))
    
    # Receber status inicial
    status_data = sock.recv(1)
    if not status_data:
        print("Sem resposta")
        sock.close()
        return
    
    status = status_data[0]
    
    if status == 1:
        # Enviar tamanho do arquivo
        sock.send(tam_arquivo.to_bytes(4, byteorder='big'))
        
        # Enviar conteúdo
        enviados = 0
        while enviados < tam_arquivo:
            bloco = conteudo[enviados:enviados + 1024]
            sock.send(bloco)
            enviados += len(bloco)
            print(f"Enviados {enviados}/{tam_arquivo} bytes")
        
        # Receber status final
        status_final_data = sock.recv(1)
        if status_final_data and status_final_data[0] == 1:
            print("Upload realizado com sucesso!")
        else:
            print("Erro no upload")
    else:
        print("Servidor recusou o upload")
    
    sock.close()

def download_por_posicao():
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10.0)
    
    try:
        sock.connect((HOST, PORT))
    except:
        print("Erro ao conectar")
        return
    
    nome_arq = input("Nome do arquivo: ")
    posicao_str = input("Posição inicial (0): ") or "0"
    posicao = int(posicao_str)
    
    # CALCULAR MD5 DA PARTE EXISTENTE (se existir)
    hash_md5 = b'\x00' * 16  # Padrão: hash zerado
    
    try:
        # Tentar abrir arquivo local para calcular MD5
        with open(nome_arq, "rb") as f:
            # Ler até a posição especificada
            parte_existente = f.read(posicao)
            if parte_existente:  # Se tem algo para calcular
                md5_calc = hashlib.md5(parte_existente)
                hash_md5 = md5_calc.digest()  # 16 bytes reais
                print(f"MD5 calculado da parte existente ({len(parte_existente)} bytes)")
    except FileNotFoundError:
        print("Arquivo não existe localmente - começando do zero")
        hash_md5 = b'\x00' * 16
    except Exception as e:
        print(f"Erro ao calcular MD5: {e}")
        hash_md5 = b'\x00' * 16
    
    # Enviar operação (40)
    sock.send(b'\x28')
    
    # Enviar tamanho do nome
    sock.send(len(nome_arq).to_bytes(4, 'big'))
    
    # Enviar nome
    sock.send(nome_arq.encode())
    
    # Enviar posição
    sock.send(posicao.to_bytes(4, 'big'))
    
    # Enviar MD5 REAL (16 bytes)
    sock.send(hash_md5)
    
    # Receber status
    status = sock.recv(1)[0]
    
    if status == 1:
        print("Iniciando download...")
        
        # Receber tamanho remanescente
        tamanho_data = sock.recv(4)
        if len(tamanho_data) < 4:
            print("Erro ao receber tamanho")
            sock.close()
            return
        
        tamanho_remanescente = int.from_bytes(tamanho_data, 'big')
        print(f"Faltam {tamanho_remanescente} bytes")
        
        # Receber arquivo (append se já existir)
        modo = "ab" if posicao > 0 else "wb"
        with open(nome_arq, modo) as f:
            recebido = 0
            while recebido < tamanho_remanescente:
                dados = sock.recv(1024)
                if not dados:
                    break
                f.write(dados)
                recebido += len(dados)
                print(f"Recebidos {recebido}/{tamanho_remanescente} bytes")
        
        
        print("Download concluído")
        
    elif status == 10:
        print(" Arquivo não existe no servidor")
    elif status == 20:
        print("Hash não confere!")
        print("A parte que você tem é diferente da do servidor")
    else:
        print(f" Erro não identificado (código: {status})")
    
    sock.close()

def download_multiplo_por_mascara():
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10.0)
    
    try:
        sock.connect((HOST, PORT))
    except:
        print("Erro ao conectar")
        return
    
    mascara = input("Máscara (ex: *.txt): ")
    
    # Enviar operação (50)
    sock.send(b'\x32')
    
    # Enviar tamanho da máscara
    sock.send(len(mascara).to_bytes(4, 'big'))
    
    # Enviar máscara
    sock.send(mascara.encode())
    
    # Receber status
    status = sock.recv(1)[0]
    
    if status == 1:
        # Receber número de arquivos
        num = int.from_bytes(sock.recv(4), 'big')
        print(f"{num} arquivo(s) encontrado(s)")
        
        for _ in range(num):
            # Receber tamanho do nome
            tam_nome = int.from_bytes(sock.recv(4), 'big')
            
            # Receber nome
            nome = sock.recv(tam_nome).decode()
            
            # Receber tamanho
            tamanho = int.from_bytes(sock.recv(4), 'big')
            
            # Receber arquivo
            with open(nome, "wb") as f:
                recebido = 0
                while recebido < tamanho:
                    dados = sock.recv(1024)
                    f.write(dados)
                    recebido += len(dados)
            
            print(f"  - {nome} ({tamanho} bytes)")
    else:
        print("Nenhum arquivo encontrado")
    
    sock.close()