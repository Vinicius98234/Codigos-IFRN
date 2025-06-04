maiorcombinacao = 0 
maiorp = 0
for p in range (1, 1001):
    combat = 0
    for a in range (1, p // 3 + 1 ):
        for b in range (a, p+1-a):
            c = p - (a+b)
            if c > 0:
                a2 = a * a
                b2 = b * b
                c2 = c * c
                if(a2 + b2) == c2:
                    print("para",p, "=",a, b, c)
                    combat += 1
                elif (a2 + b2) > c2:
                    break
    if combat > maiorcombinacao:
        maiorcombinacao = combat
        maiorp = p
print(maiorp,maiorcombinacao)