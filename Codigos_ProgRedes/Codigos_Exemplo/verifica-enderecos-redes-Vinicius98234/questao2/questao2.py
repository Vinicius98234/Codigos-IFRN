def convertIP(x):
    lstIP = [int(x) for x in x.split('.')]
    return (lstIP[0] * (256**3)) + (lstIP[1] * (256**2)) + (lstIP[2] * (256**1)) + (lstIP[3] * (256**0))

def validarOct(x):
    qntOct = [int(x) for x in x.split('.')]
    tam = len(qntOct)
    
    # Verifica se tem exatamente 4 octetos
    if tam != 4:
        print("IP não tem 4 octetos")
        return False
    
    # Verifica cada octeto
    for y in range(0, 4):  
        if 0 <= qntOct[y] <= 255:  
            validar = True
        else:
            print(f"O octeto {qntOct[y]} não está no intervalo de 0 a 255")
            validar = False
            break
    
    return validar

def inteiro_para_binario(num):
    "Converte inteiro para 32 bits"
    return f"{num:032b}"

def inteiro_para_ip(num):
    "Converte inteiro de volta para formato IP"
    return f"{(num >> 24) & 0xFF}.{(num >> 16) & 0xFF}.{(num >> 8) & 0xFF}.{num & 0xFF}"

print("Calculadora IP")
ip1 = input("Digite o endereço IP: ")
mask = int(input("Digite a máscara de rede (em bits): "))

if mask < 0 or mask > 32:
    print("Máscara inválida! Deve estar entre 0 e 32 bits")
else:
    if validarOct(ip1):
        ipi = convertIP(ip1)
        host = 32 - mask
        ipl = [int(x) for x in ip1.split('.')]
        ipb = bytes(ipl)
        ipi = int.from_bytes(ipb)
        
        # Cálculos de rede
        net = ipi >> host << host
        bcast = ipi | ((1 << host) - 1)
        gw = net | 1  # Roteador 
        
        # Cálculo do número de hosts 
        num_hosts = (2 ** host) - 1  
        
        print("EM BINÁRIO:")
        print(f"ip:     {inteiro_para_binario(ipi)}")
        print(f"net:    {inteiro_para_binario(net)}")
        print(f"bcast:  {inteiro_para_binario(bcast)}")
        print(f"gw:     {inteiro_para_binario(gw)}")
        print("=" * 40)
        print("EM DECIMAL:")
        print(f"ip:     {inteiro_para_ip(ipi)}")
        print(f"net:    {inteiro_para_ip(net)}")
        print(f"bcast:  {inteiro_para_ip(bcast)}")
        print(f"gw:     {inteiro_para_ip(gw)}")
        print("=" * 40)
        print(f"Número de hosts possíveis (incluindo roteador): {num_hosts}")
        print(f"Endereço do roteador: {inteiro_para_ip(gw)}")
