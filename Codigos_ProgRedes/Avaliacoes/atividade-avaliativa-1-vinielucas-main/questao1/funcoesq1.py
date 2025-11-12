import hashlib, time

def findNonce(dataToHash: bytes, bitsToBeZero: int):
    # Marca o tempo inicial para saber quanto tempo demorou
    start_time = time.time()
    nonce = 0  # Começamos a procurar pelo nonce 0
    
    # Vamos testar todos os nonces possíveis de 4 bytes (até 4.294.967.295)
    while nonce <= 0xFFFFFFFF:
        # Prepara os dados: nonce (4 bytes) + dados do usuário
        h = hashlib.sha256()
        h.update(nonce.to_bytes(4, "big") + dataToHash)
        hash_bytes = h.digest()  # Pega o hash em bytes (32 bytes = 256 bits)
        
        # Converte o hash para um número inteiro grande
        hash_int = int.from_bytes(hash_bytes, "big")
        
        # Verifica se os primeiros 'bitsToBeZero' bits são zero
        # Se o número for menor que 2^(256 - bitsToBeZero), os primeiros bits são zero
        if hash_int < (1 << (256 - bitsToBeZero)):
            end_time = time.time()
            elapsed_time = end_time - start_time
            
            # Mostra o hash em formato binário (256 bits)
            hash_binary = format(hash_int, '0256b')
            print(f"nonce: {nonce} hash: {hash_binary}")
            print(f"Tempo total: {elapsed_time:.6f} segundos")
            return nonce, elapsed_time
        
        nonce += 1  # Testa o próximo número
    
    # Se chegou aqui, não encontrou nenhum nonce que funcione
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Nonce não encontrado no range de 4 bytes")
    return -1, elapsed_time