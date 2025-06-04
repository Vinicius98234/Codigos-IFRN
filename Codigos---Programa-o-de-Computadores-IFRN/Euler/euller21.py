limite = 1000
somatotal = 0

print("Pares de numeros amigos menores que 1000:")

for a in range(2, limite):
    # Calcula soma dos divisores proprios de a
    somadiva = 1  # 1 é divisor para a > 1
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            somadiva += i
            outro_divisor = a // i
            if outro_divisor != i:  # Evita contar quadrados perfeitos duas vezes
                somadiva += outro_divisor
    b = somadiva

    # Verifica se b é amigo de a
    if b > a and b < limite:
        somadivb = 1  # 1 é divisor para b > 1
        for i in range(2, int(b ** 0.5) + 1):
            if b % i == 0:
                somadivb += i
                outro_divisor = b // i
                if outro_divisor != i:
                    somadivb += outro_divisor
        if somadivb == a:
            print(a, "e", b, "sao um par de numeros amigos")
            somatotal += a + b
            print(somatotal)