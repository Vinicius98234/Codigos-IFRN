dia_inicio = int(input("Digite o dia inicial: "))
mes_inicio = int(input("De qual mês: "))

# Verificação básica de data válida
if mes_inicio < 1 or mes_inicio > 12 or dia_inicio < 1 or dia_inicio > 31:
    print("Data inicial inválida!")
    exit()

# Calcula o total de dias desde o início do ano até a data inicial
total_inicio = 0
if mes_inicio > 1:
    total_inicio += 31  # Janeiro
if mes_inicio > 2:
    total_inicio += 28  # Fevereiro (considerando ano não bissexto)
if mes_inicio > 3:
    total_inicio += 31  # Março
if mes_inicio > 4:
    total_inicio += 30  # Abril
if mes_inicio > 5:
    total_inicio += 31  # Maio
if mes_inicio > 6:
    total_inicio += 30  # Junho
if mes_inicio > 7:
    total_inicio += 31  # Julho
if mes_inicio > 8:
    total_inicio += 31  # Agosto
if mes_inicio > 9:
    total_inicio += 30  # Setembro
if mes_inicio > 10:
    total_inicio += 31  # Outubro
if mes_inicio > 11:
    total_inicio += 30  # Novembro
total_inicio += dia_inicio

dia_fim = int(input("Digite o dia final: "))
mes_fim = int(input("De qual mês: "))

# Verificação básica de data válida
if mes_fim < 1 or mes_fim > 12 or dia_fim < 1 or dia_fim > 31:
    print("Data final inválida!")
    exit()

# Calcula o total de dias desde o início do ano até a data final
total_fim = 0
if mes_fim > 1:
    total_fim += 31  # Janeiro
if mes_fim > 2:
    total_fim += 28  # Fevereiro (considerando ano não bissexto)
if mes_fim > 3:
    total_fim += 31  # Março
if mes_fim > 4:
    total_fim += 30  # Abril
if mes_fim > 5:
    total_fim += 31  # Maio
if mes_fim > 6:
    total_fim += 30  # Junho
if mes_fim > 7:
    total_fim += 31  # Julho
if mes_fim > 8:
    total_fim += 31  # Agosto
if mes_fim > 9:
    total_fim += 30  # Setembro
if mes_fim > 10:
    total_fim += 31  # Outubro
if mes_fim > 11:
    total_fim += 30  # Novembro
total_fim += dia_fim

diferenca = total_fim - total_inicio

if diferenca < 0:
    print("A data final deve ser posterior à data inicial!")
else:
    print("Passaram-se", diferenca, "dias, entre", dia_inicio, "do", mes_inicio, "até", dia_fim, "do", mes_fim)