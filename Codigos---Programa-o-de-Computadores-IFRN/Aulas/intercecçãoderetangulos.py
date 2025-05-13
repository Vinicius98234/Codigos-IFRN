print ("Intersecção entre dois retangulos num plano cartesiano: ")

print("Diga as informações do quadrado 1:")
x01 = int(input("X do retangulo 1 = "))
y01 = int(input("Y do retangulo 1 = "))
lx1 = int(input("Largura do retangulo 1 = "))
hy1 = int(input("Altura do retangulo 1  = "))

xdoquadrado1 = x01 + lx1 
ydoquadrado1 = y01 + hy1

print("Agora diga as informações do retangulo 2:")
x02 = int(input("X do retangulo 2 = "))
y02 = int(input("Y do retangulo 2 = "))
lx2 = int(input("Largura do retangulo 2 = "))
hy2 = int(input("Altura do retangulo 2  = "))

xdoquadrado2 = x02 + lx2
ydoquadrado2 = y02 + hy2

if (xdoquadrado2 < x01) or (x02 > xdoquadrado1):
    intersX = False
else:
    intersX = True
if (ydoquadrado2 < y01) or (y02 > ydoquadrado1):
    intersY = False
else:
    intersY = True

if intersX and intersY:
    print ("Houve intersecção")
else:
    print("Sem intersecção")



# if  xdoquadrado1 < x02: 
#     print("Não houve intersecção")
# else: 
#     if xdoquadrado2 < x01:
#         print("Não houve intersecção")
#     else:
#         if ydoquadrado1 < y02:
#             print("Não houve intersecção")
#         else:
#             if ydoquadrado2 < y01:
#                 print("Não houve intersecção")
#             else:
#                 print("Houve intersecção")