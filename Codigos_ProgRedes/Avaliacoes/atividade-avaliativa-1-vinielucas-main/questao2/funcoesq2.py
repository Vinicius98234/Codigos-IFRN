import os

# Variáveis globais do RAID
# (São como "memória" do nosso sistema RAID)
num_discos = 0           # Quantos discos temos no total
tamanho_disco = 0        # Tamanho de cada disco em bytes
tamanho_bloco = 0        # Tamanho de cada bloco em bytes  
pasta_raid = ""          # Onde guardamos os arquivos dos discos
disco_defeituoso = None  # Se algum disco quebrou, guardamos qual é

def inicializaRAID():
    """Função para criar um RAID novo do zero"""
    global num_discos, tamanho_disco, tamanho_bloco, pasta_raid, disco_defeituoso
    
    print("=== INICIALIZAR RAID4 ===")
    # Perguntamos as configurações pro usuário
    num_discos = int(input("Número de discos (mínimo 3): "))
    if num_discos < 3:
        print("Erro: Mínimo 3 discos necessários")
        return
        
    tamanho_disco = int(input("Tamanho de cada disco (bytes): "))
    tamanho_bloco = int(input("Tamanho do bloco (bytes): "))
    pasta_raid = input("Pasta para os arquivos: ")
    
    # Criamos a pasta se não existir
    os.makedirs(pasta_raid, exist_ok=True)
    
    # Criamos um arquivo para cada disco
    for i in range(num_discos):
        with open(f"{pasta_raid}/disco{i}.bin", 'wb') as f:
            f.write(b'\x00' * tamanho_disco)  # Preenche com zeros
    
    # Calculamos a paridade inicial (importante!)
    atualizar_todas_paridades()
    print(f"RAID4 criado: {num_discos-1} discos dados + 1 paridade")

def obtemRAID():
    """Carrega um RAID que já existe"""
    global num_discos, tamanho_disco, tamanho_bloco, pasta_raid
    
    print("=== CARREGAR RAID ===")
    # Pedimos as mesmas informações, mas não criamos arquivos novos
    num_discos = int(input("Número de discos: "))
    tamanho_disco = int(input("Tamanho dos discos: "))
    tamanho_bloco = int(input("Tamanho do bloco: "))
    pasta_raid = input("Pasta dos arquivos: ")
    
    # Verificamos se os arquivos realmente existem
    if not all(os.path.exists(f"{pasta_raid}/disco{i}.bin") for i in range(num_discos)):
        print("Erro: Arquivos RAID não encontrados!")
        return
    
    print("RAID carregado!")

def escreveRAID():
    """Escreve dados em uma posição específica do RAID"""
    global num_discos, tamanho_disco
    
    if num_discos == 0:
        print("Erro: RAID não inicializado!")
        return
        
    # O usuário diz ONDE e O QUE escrever
    posicao = int(input("Posição lógica: "))
    dados = input("Dados: ")
    
    # Calculamos quanto espaço temos disponível
    capacidade = (num_discos - 1) * tamanho_disco
    if posicao < 0 or posicao >= capacidade:
        print(f"Erro: Posição deve estar entre 0 e {capacidade-1}")
        return
    
    # Chamamos a função que faz a escrita de verdade
    escreve_dados_completo(posicao, dados.encode())
    print("Dados escritos!")

def leRAID():
    """Lê dados de uma posição específica do RAID"""
    global num_discos, tamanho_disco
    
    if num_discos == 0:
        print("Erro: RAID não inicializado!")
        return
        
    # O usuário diz ONDE e QUANTO ler
    posicao = int(input("Posição lógica: "))
    quantidade = int(input("Quantidade de bytes: "))
    
    capacidade = (num_discos - 1) * tamanho_disco
    if posicao < 0 or posicao + quantidade > capacidade:
        print(f"Erro: Leitura fora dos limites!")
        return
    
    # Chamamos a função que faz a leitura de verdade
    dados = le_dados_completo(posicao, quantidade)
    print("Dados lidos:", dados.decode())
    return dados

def removeDiscoRAID():
    """Simula que um disco quebrou - deletamos o arquivo"""
    global num_discos, pasta_raid, disco_defeituoso
    
    if num_discos == 0:
        print("Erro: RAID não inicializado!")
        return
        
    disco = int(input("Disco a remover (0 a {}): ".format(num_discos - 2)))
    
    if disco < 0 or disco >= num_discos - 1:
        print("Erro: Disco inválido!")
        return
        
    # Deletamos o arquivo do disco (simula que quebrou)
    arquivo = f"{pasta_raid}/disco{disco}.bin"
    if os.path.exists(arquivo):
        os.remove(arquivo)
        disco_defeituoso = disco  # Lembramos qual disco quebrou
        print(f"Disco {disco} removido (simulando falha)!")
    else:
        print("Arquivo do disco não encontrado!")

def constroiDiscoRAID():
    """Recupera um disco que estava quebrado"""
    global num_discos, tamanho_disco, tamanho_bloco, pasta_raid, disco_defeituoso
    
    if disco_defeituoso is None:
        print("Nenhum disco defeituoso!")
        return
    
    # Primeiro criamos o arquivo vazio do disco
    with open(f"{pasta_raid}/disco{disco_defeituoso}.bin", 'wb') as f:
        f.write(b'\x00' * tamanho_disco)
    
    # Para cada bloco do disco, recuperamos os dados usando XOR
    num_stripes = tamanho_disco // tamanho_bloco
    for stripe in range(num_stripes):
        dados = recuperar_bloco_stripe(disco_defeituoso, stripe)
        with open(f"{pasta_raid}/disco{disco_defeituoso}.bin", 'r+b') as f:
            f.seek(stripe * tamanho_bloco)
            f.write(dados)
    
    disco_defeituoso = None  # Disco não está mais quebrado!
    print("Disco reconstruído!")

def calcular_posicao(posicao_logica):
    """Mágica do RAID: converte posição lógica em disco/stripe/offset"""
    global num_discos, tamanho_bloco
    
    num_discos_dados = num_discos - 1  # Descontamos o disco de paridade
    
    # Cálculos para descobrir onde estão os dados:
    bloco_logico = posicao_logica // tamanho_bloco           # Qual bloco lógico?
    stripe = bloco_logico // num_discos_datos               # Em qual stripe?
    disco = bloco_logico % num_discos_datos                 # Em qual disco?
    offset = posicao_logica % tamanho_bloco                 # Em qual posição do bloco?
    
    return disco, stripe, offset

def escreve_dados_completo(posicao, dados):
    """Escreve dados que podem cruzar vários blocos/discos"""
    global tamanho_bloco, pasta_raid, disco_defeituoso
    
    bytes_escritos = 0
    dados_restantes = len(dados)
    
    # Enquanto ainda tiver dados para escrever
    while dados_restantes > 0:
        # Descobrimos onde escrever o próximo pedaço
        disco, stripe, offset = calcular_posicao(posicao + bytes_escritos)
        
        # Calculamos quantos bytes cabem neste bloco
        bytes_no_bloco = min(tamanho_bloco - offset, dados_restantes)
        dados_atuais = dados[bytes_escritos:bytes_escritos + bytes_no_bloco]
        
        # Se o disco não está quebrado, escrevemos nele
        if disco != disco_defeituoso:
            with open(f"{pasta_raid}/disco{disco}.bin", 'r+b') as f:
                f.seek(stripe * tamanho_bloco + offset)  # Vai pra posição certa
                f.write(dados_atuais)                    # Escreve os dados
        
        # Atualizamos a paridade deste stripe (IMPORTANTE!)
        atualizar_paridade_stripe(stripe)
        bytes_escritos += bytes_no_bloco
        dados_restantes -= bytes_no_bloco

def le_dados_completo(posicao, quantidade):
    """Lê dados que podem estar em vários blocos/discos"""
    global tamanho_bloco, pasta_raid, disco_defeituoso
    
    dados_lidos = bytearray()  # Onde vamos juntar tudo
    bytes_lidos = 0
    
    # Enquanto não ler tudo que foi pedido
    while bytes_lidos < quantidade:
        # Descobrimos onde ler o próximo pedaço
        disco, stripe, offset = calcular_posicao(posicao + bytes_lidos)
        
        # Calculamos quantos bytes podemos ler deste bloco
        bytes_a_ler = min(tamanho_bloco - offset, quantidade - bytes_lidos)
        
        # Se o disco está quebrado, recuperamos os dados via XOR
        if disco == disco_defeituoso:
            bloco_recuperado = recuperar_bloco_stripe(disco, stripe)
            dados_bloco = bloco_recuperado[offset:offset + bytes_a_ler]
        else:
            # Senão, lemos normalmente do disco
            with open(f"{pasta_raid}/disco{disco}.bin", 'rb') as f:
                f.seek(stripe * tamanho_bloco + offset)
                dados_bloco = f.read(bytes_a_ler)
        
        # Juntamos os dados lidos
        dados_lidos.extend(dados_bloco)
        bytes_lidos += bytes_a_ler
    
    return bytes(dados_lidos)

def atualizar_paridade_stripe(stripe):
    """Recalcula a paridade de um stripe específico"""
    global num_discos, tamanho_bloco, pasta_raid, disco_defeituoso
    
    disco_paridade = num_discos - 1  # Último disco é sempre a paridade
    paridade = bytearray(tamanho_bloco)  # Começa com zeros
    
    # Para cada disco de dados...
    for disco in range(num_discos - 1):
        if disco == disco_defeituoso:
            # Se o disco quebrou, recuperamos os dados primeiro
            dados = recuperar_bloco_stripe(disco, stripe)
        else:
            # Senão, lemos normalmente
            with open(f"{pasta_raid}/disco{disco}.bin", 'rb') as f:
                f.seek(stripe * tamanho_bloco)
                dados = f.read(tamanho_bloco)
        
        # Fazemos XOR byte a byte com a paridade
        for i in range(tamanho_bloco):
            paridade[i] ^= dados[i]  # XOR: 0^0=0, 0^1=1, 1^0=1, 1^1=0
    
    # Escrevemos a paridade calculada no disco de paridade
    with open(f"{pasta_raid}/disco{disco_paridade}.bin", 'r+b') as f:
        f.seek(stripe * tamanho_bloco)
        f.write(paridade)

def atualizar_todas_paridades():
    """Calcula paridade para todos os stripes (usado na inicialização)"""
    global num_discos, tamanho_disco, tamanho_bloco, pasta_raid
    
    disco_paridade = num_discos - 1
    num_stripes = tamanho_disco // tamanho_bloco
    
    # Para cada stripe...
    for stripe in range(num_stripes):
        paridade = bytearray(tamanho_bloco)
        
        # Para cada disco de dados...
        for disco in range(num_discos - 1):
            with open(f"{pasta_raid}/disco{disco}.bin", 'rb') as f:
                f.seek(stripe * tamanho_bloco)
                dados = f.read(tamanho_bloco)
            
            # XOR byte a byte
            for i in range(tamanho_bloco):
                paridade[i] ^= dados[i]
        
        # Escreve a paridade
        with open(f"{pasta_raid}/disco{disco_paridade}.bin", 'r+b') as f:
            f.seek(stripe * tamanho_bloco)
            f.write(paridade)

def recuperar_bloco_stripe(disco_perdido, stripe):
    """Mágica do RAID: recupera dados de disco quebrado usando XOR"""
    global num_discos, tamanho_bloco, pasta_raid
    
    bloco_recuperado = bytearray(tamanho_bloco)  # Onde vamos reconstruir
    disco_paridade = num_discos - 1
    
    # Primeiro lemos a paridade deste stripe
    with open(f"{pasta_raid}/disco{disco_paridade}.bin", 'rb') as f:
        f.seek(stripe * tamanho_bloco)
        paridade = f.read(tamanho_bloco)
    
    # Para cada disco que NÃO está quebrado...
    for disco in range(num_discos - 1):
        if disco != disco_perdido:
            with open(f"{pasta_raid}/disco{disco}.bin", 'rb') as f:
                f.seek(stripe * tamanho_bloco)
                dados_disco = f.read(tamanho_bloco)
            
            # Fazemos XOR com os dados bons
            for i in range(tamanho_bloco):
                bloco_recuperado[i] ^= dados_disco[i]
    
    # Finalmente, fazemos XOR com a paridade para recuperar os dados perdidos
    for i in range(tamanho_bloco):
        bloco_recuperado[i] ^= paridade[i]
    
    return bloco_recuperado
