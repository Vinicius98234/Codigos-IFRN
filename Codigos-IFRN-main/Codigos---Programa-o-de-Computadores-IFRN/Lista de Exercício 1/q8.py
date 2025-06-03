print("       Calcular volume do cilindro           ")
print(" Formula para calcular volume do cilindro é: ")
print("                 V=π⋅r2⋅h                     ")

r = float(input("Informe o raio do cilindro = "))
h = float(input("Informe a altura do cilindro = "))
pi = 3.14

base = pi * (r**2)

volcilindro = base * h

print("O volume do cilindro é ", round(volcilindro, 2), "cm³")