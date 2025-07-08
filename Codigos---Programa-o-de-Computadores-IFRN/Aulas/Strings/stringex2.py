# V1
s = "Vinicius"
count = 0
l = input("Digite uma letra: ")
for i in s:
    if i == l:
        count += 1
if count > 0:
    print(l, "existe em", s)
else:
    print(l, "não existem em", s) 

# V2
existe = False
s = "Vinicius"
l = int("Digite uma letra: ")
for i in s:
    if i == l:
        existe = True
if existe:
    print(l, "existe em", s)
else:
    print(l, "não existem em", s) 

# V3 - Usando while
existe = False
s = "Vinicius"
l = int("Digite uma letra: ")
pos = 0
while pos < len(s):
    if s[pos] == l:
        existe = True
    pos += 1
if existe:
    print(l, "existe em", s)
else:
    print(l, "não existem em", s) 

# V4 - Ultima posição da letra
    achouem = -1
existe = False
s = "Vinicius"
l = input("Digite uma letra: ")
pos = 0
while (pos < len(s)) and (achouem == -1):
    if s[pos] == l:
        existe = True
        achouem = pos
    pos += 1
if existe:
    print("a ultima ocorrencia de", l, "está em", pos)
else:
    print(l, "não existem em", s) 
