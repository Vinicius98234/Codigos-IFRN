# Recebe o número do usuário
numero = int(input("Digite um número de até quatro algarismos (0 a 9999): "))

# Verifica se o número é válido
if numero < 0 or numero >= 10000:
    print("Numero só pode ser positivo e ter apenas 4 algarismos")
else:
    # Extrai cada algarismo separadamente
    milhar = numero // 1000
    centena = (numero % 1000) // 100
    dezena = (numero % 100) // 10
    unidade = numero % 10

    # Calcula a soma
    soma = milhar + centena + dezena + unidade

    # Exibe o resultado
    print("A soma dos algarismos de ",numero, "é" ,soma)
