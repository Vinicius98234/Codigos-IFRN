numero = 10
div = 0
somadiv = 0
for n in range (1, numero):
    if numero % n == 0:
        div += 1
        somadiv += div
        print(div)
print(somadiv)