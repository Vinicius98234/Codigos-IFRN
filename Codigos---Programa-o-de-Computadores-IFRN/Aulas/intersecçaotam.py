print("Determinar se a intersecção em dois segmentos de reta: ")

# Entrada de dados

ai = int(input("Valor inicial do segmento de reta 1 = "))
af = ai + int(input("Tamanho do segmento de reta 1 = "))
bi = int(input("Valor inicial do segmento de reta 2 = "))
bf = bi + int(input("Tamanho do segmento de reta 2 = "))

# Ordenar Dados

if ai > af:
    af, ai = ai, af
if bi > bf: 
    bf, bi = bi, bf


if af < bi: 
    print("Não houve intersecção")
else: 
    if ai > bf:
        print("Não houve intersecção")
    else:
        print("Houve Intersecção")
