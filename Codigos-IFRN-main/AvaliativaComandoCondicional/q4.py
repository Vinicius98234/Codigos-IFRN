dia_inicio = int(input("Digite o dia inicial: "))
mes_inicio = int(input("De qual mês: "))

if mes_inicio == 1:
    total_inicio = 334 + dia_inicio
if mes_inicio == 2:
    total_inicio = 304 + dia_inicio
if mes_inicio == 3:
    total_inicio = 273 + dia_inicio
if mes_inicio == 4:
    total_inicio = 243 + dia_inicio
if mes_inicio == 5:
    total_inicio = 212 + dia_inicio
if mes_inicio == 6:
    total_inicio = 181 + dia_inicio
if mes_inicio == 7:
    total_inicio = 151 + dia_inicio
if mes_inicio == 8:
    total_inicio = 120 + dia_inicio
if mes_inicio == 9:
    total_inicio = 90 + dia_inicio
if mes_inicio == 10:
    total_inicio = 59 + dia_inicio
if mes_inicio == 11:
    total_inicio = 31 + dia_inicio
if mes_inicio == 12:
    total_inicio = dia_inicio

dia_fim = int(input("Digite o dia final: "))
mes_fim = int(input("De qual mês: "))

if mes_fim == 1:
    total_fim = 334 + dia_fim
if mes_fim == 2:
    total_fim = 304 + dia_fim
if mes_fim == 3:
    total_fim = 273 + dia_fim
if mes_fim == 4:
    total_fim = 243 + dia_fim
if mes_fim == 5:
    total_fim = 212 + dia_fim
if mes_fim == 6:
    total_fim = 181 + dia_fim
if mes_fim == 7:
    total_fim = 151 + dia_fim
if mes_fim == 8:
    total_fim = 120 + dia_fim
if mes_fim == 9:
    total_fim = 90 + dia_fim
if mes_fim == 10:
    total_fim = 59 + dia_fim
if mes_fim == 11:
    total_fim = 31 + dia_fim
if mes_fim == 12:
    total_fim = dia_fim

print("Passaram-se", abs(total_fim - total_inicio), "dias, entre", dia_inicio, "do", mes_inicio, "até", dia_fim, "do", mes_fim)