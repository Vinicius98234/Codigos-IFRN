# Coloque aqui o código de resposta aa questao 1

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
    
    

ip1 = input ("Digite o primeiro endereço IP: ")
ip2 = input ("Digite o segundo endereço IP: ")
mask = int(input ("Digite o tamanho da máscara de rede (em bits): "))

if mask < 0 or mask > 32:
    print("Máscara inválida! Deve estar entre 0 e 32 bits")
else:
    # Valida os IPs
    if validarOct(ip1) and validarOct(ip2):
        ip1_convertido = convertIP(ip1)
        ip2_convertido = convertIP(ip2)
        bitsHost = 32 - mask

        net1 = ip1_convertido >> bitsHost
        net2 = ip2_convertido >> bitsHost

        if net1 == net2:
            print("Redes iguais!!")
        else:
            print("Redes diferentes!!")
    else:
        print("Digite um IPV4 válido")
