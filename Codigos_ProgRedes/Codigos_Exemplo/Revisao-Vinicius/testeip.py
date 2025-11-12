# Coloque aqui o código de resposta aa questao 1

ip1 = input ("Digite o primeiro endereço IP: ")
ip2 = input ("Digite o segundo endereço IP: ")
mask = int(input ("Digite o tamanho da máscara de rede (em bits): "))

def convertIP(x):
    lstIP = [int(x) for x in x.split('.')]
    return (lstIP[0] * (256**3)) + (lstIP[1] * (256**2)) + (lstIP[2] * (256**1)) + (lstIP[3] * (256**0))

ip1 = convertIP(ip1)
ip2 = convertIP(ip2)
bitsHost = 32 - mask

net1 = ip1 >> bitsHost
net2 = ip2 >> bitsHost

if net1 == net2:
    print ("Redes iguais!!")
else:
    print ("Redes diferentes!!")
