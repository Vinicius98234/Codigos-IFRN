import socket
import os
import time
import hashlib

PORT = 20000
PASTA_SERVER = "server"

# Criar pasta do servidor se não existir
if not os.path.exists(PASTA_SERVER):
    os.makedirs(PASTA_SERVER)

def operacao_10_download(conn, nome_arquivo):
    
    caminho = os.path.join(PASTA_SERVER, nome_arquivo)
    
    if os.path.exists(caminho):
        conn.send(b'\x01')
        
        # Obter tamanho
        tamanho = os.path.getsize(caminho)
        conn.send(tamanho.to_bytes(4, byteorder='big'))
        
        # Enviar arquivo
        with open(caminho, "rb") as arquivo:
            enviados = 0
            while enviados < tamanho:
                dados = arquivo.read(1024)
                conn.send(dados)
                enviados += len(dados)
    else:
        conn.send(b'\x00')

def operacao_20_listar(conn):
    try:
        arquivos = []
        for arquivo in os.listdir(PASTA_SERVER):
            caminho = os.path.join(PASTA_SERVER, arquivo)
            if os.path.isfile(caminho):
                tamanho = os.path.getsize(caminho)
                arquivos.append(f'{{"nome": "{arquivo}", "tamanho": {tamanho}}}')
        
        lista_json = "[" + ", ".join(arquivos) + "]"
        lista_bytes = lista_json.encode('utf-8')
        
        conn.send(b'\x01')
        conn.send(len(lista_bytes).to_bytes(4, byteorder='big'))
        conn.send(lista_bytes)
    except:
        conn.send(b'\x00')

def operacao_30_upload(conn, nome_arquivo):
    
    conn.send(b'\x01')
    
    # Receber tamanho
    tam_data = conn.recv(4)
    if len(tam_data) < 4:
        return
    
    tamanho = int.from_bytes(tam_data, byteorder='big')
    
    # Receber arquivo
    caminho = os.path.join(PASTA_SERVER, nome_arquivo)
    recebido = 0
    
    with open(caminho, "wb") as arquivo:
        while recebido < tamanho:
            dados = conn.recv(1024)
            if not dados:
                break
            arquivo.write(dados)
            recebido += len(dados)
    
    # Enviar status final
    if recebido == tamanho:
        conn.send(b'\x01')
    else:
        conn.send(b'\x00')

def operacao_40_download_posicao(conn, nome_arquivo, posicao, hash_cliente):
    """Operação 40: Download a partir de posição COM VERIFICAÇÃO MD5"""
    caminho = os.path.join(PASTA_SERVER, nome_arquivo)
    
    # 1. Verificar se arquivo existe
    if not os.path.exists(caminho):
        conn.send(b'\x0A')  # 10 = arquivo não existe
        print(f"  Arquivo {nome_arquivo} não encontrado")
        return
    
    # 2. CALCULAR MD5 DA PARTE NO SERVIDOR
    try:
        with open(caminho, "rb") as arquivo:
            parte_servidor = arquivo.read(posicao)
            md5_servidor = hashlib.md5(parte_servidor).digest()
    except Exception as e:
        print(f"  Erro ao calcular MD5: {e}")
        conn.send(b'\x00')  # Erro genérico
        return
    
    if hash_cliente == b'\x00' * 16:
        print(f"Cliente enviou hash zerado (primeiro download)")
        # Aceita mesmo com hash zerado (para primeiro download)
    elif hash_cliente != md5_servidor:
        print(f"Hashs diferentes!")
        conn.send(b'\x14')  # 20 = hash não confere
        return
    
    
    conn.send(b'\x01')  # 1 = aceito
    
    # 5. Calcular tamanho 
    tamanho_total = os.path.getsize(caminho)
    tamanho_remanescente = tamanho_total - posicao
    
    
    if posicao > tamanho_total:
        print(f" Posição {posicao} maior que arquivo ({tamanho_total})")
        tamanho_remanescente = 0
    
    print(f"  Tamanho total: {tamanho_total}, Remanescente: {tamanho_remanescente}")
    
    # 6. Enviar tamanho 
    conn.send(tamanho_remanescente.to_bytes(4, 'big'))
    
    # 7. Enviar parte 
    if tamanho_remanescente > 0:
        with open(caminho, "rb") as f:
            f.seek(posicao)  # Pular para a posição
            enviados = 0
            while enviados < tamanho_remanescente:
                dados = f.read(1024)
                conn.send(dados)
                enviados += len(dados)
    
    print(f"Enviados {tamanho_remanescente} bytes")
def operacao_50_download_multiplo(conn, mascara):
    
    # Lista simples de arquivos
    arquivos = []
    for arquivo in os.listdir(PASTA_SERVER):
        caminho_completo = os.path.join(PASTA_SERVER, arquivo)
        if os.path.isfile(caminho_completo):
            # Verificação simples da máscara
            if "*" in mascara:
                if mascara == "*" or mascara == "*.*":
                    arquivos.append(arquivo)
                elif mascara.startswith("*."):
                    extensao = mascara[1:]  # .txt
                    if arquivo.endswith(extensao):
                        arquivos.append(arquivo)
                elif mascara.endswith("*"):
                    prefixo = mascara[:-1]
                    if arquivo.startswith(prefixo):
                        arquivos.append(arquivo)
            elif arquivo == mascara:
                arquivos.append(arquivo)
    
    if not arquivos:
        conn.send(b'\x00')
        return
    
    conn.send(b'\x01')
    
    # Número de arquivos
    conn.send(len(arquivos).to_bytes(4, 'big'))
    
    # Enviar cada arquivo
    for nome_arquivo in arquivos:
        caminho = os.path.join(PASTA_SERVER, nome_arquivo)
        
        if not os.path.exists(caminho):
            continue
            
        tamanho = os.path.getsize(caminho)
        
        # 1. Enviar tamanho do NOME
        conn.send(len(nome_arquivo).to_bytes(4, 'big'))
        
        time.sleep(0.01)
        
        # 2. Enviar NOME do arquivo
        conn.send(nome_arquivo.encode())
    
        time.sleep(0.01)
        
        # 3. Enviar tamanho do CONTEÚDO
        conn.send(tamanho.to_bytes(4, 'big'))
        
        time.sleep(0.01)
        
        # 4. Enviar CONTEÚDO do arquivo
        with open(caminho, "rb") as f:
            enviados = 0
            while enviados < tamanho:
                dados = f.read(1024)
                conn.send(dados)
                enviados += len(dados)
        
        # Pausa entre arquivos
        time.sleep(0.02)

def handle_cliente(conn, addr):
    print(f"Conexão de {addr}")
    conn.settimeout(30.0)
    
    try:
        op_data = conn.recv(1)
        if not op_data:
            conn.close()
            return
        
        operacao = op_data[0]
        
        if operacao == 10:  # Download
            tam_nome_data = conn.recv(4)
            tam_nome = int.from_bytes(tam_nome_data, 'big')
            nome_arquivo = conn.recv(tam_nome).decode()
            operacao_10_download(conn, nome_arquivo)
            
        elif operacao == 20:  # Listar
            operacao_20_listar(conn)
            
        elif operacao == 30:  # Upload
            tam_nome_data = conn.recv(4)
            tam_nome = int.from_bytes(tam_nome_data, 'big')
            nome_arquivo = conn.recv(tam_nome).decode()
            operacao_30_upload(conn, nome_arquivo)
            
        elif operacao == 40:  # Download por posição
            tam_nome_data = conn.recv(4)
            tam_nome = int.from_bytes(tam_nome_data, 'big')
            nome_arquivo = conn.recv(tam_nome).decode()
            
            posicao_data = conn.recv(4)
            posicao = int.from_bytes(posicao_data, 'big')
            
            hash_data = conn.recv(16)
            
            operacao_40_download_posicao(conn, nome_arquivo, posicao, hash_data)
            
        elif operacao == 50:  # Download múltiplo
            tam_mascara_data = conn.recv(4)
            tam_mascara = int.from_bytes(tam_mascara_data, 'big')
            mascara = conn.recv(tam_mascara).decode()
            
            operacao_50_download_multiplo(conn, mascara)
            
    except:
        print(f"Erro com {addr}")
    finally:
        conn.close()