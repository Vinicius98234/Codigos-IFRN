from funcoesq1 import findNonce
import csv

# Tabela conforme a questão
tabela = [
    {"text": "Esse é fácil", "bits": 8},
    {"text": "Esse é fácil", "bits": 10},
    {"text": "Esse é fácil", "bits": 15},
    {"text": "Texto maior muda o tempo?", "bits": 8},
    {"text": "Texto maior muda o tempo?", "bits": 10},
    {"text": "Texto maior muda o tempo?", "bits": 15},
    {"text": "É possível calcular esse?", "bits": 18},
    {"text": "É possível calcular esse?", "bits": 19},
    {"text": "É possível calcular esse?", "bits": 20},
]

resultados = []

print("Iniciando cálculo de nonces...")
print("=" * 50)

for item in tabela:
    texto_a_validar = item["text"]
    bits_in_zero = item["bits"]

    # Converter texto para bytes
    data_bytes = texto_a_validar.encode('utf-8')

    print(f"Calculando: '{texto_a_validar}' com {bits_in_zero} bits zero")
    
    nonce_encontrado, tempo_decorrido = findNonce(data_bytes, bits_in_zero)
    
    print(f"Nonce: {nonce_encontrado} em {tempo_decorrido:.6f} segundos")
    print("-" * 30)

    resultados.append([texto_a_validar, bits_in_zero, nonce_encontrado, tempo_decorrido])

# Salvar em CSV
nome_arq_csv = "tabela_preenchida.csv"

with open(nome_arq_csv, 'w', newline='', encoding='utf-8') as arquivocsv:
    escritor_csv = csv.writer(arquivocsv)
    
    # Cabeçalho
    escritor_csv.writerow(["Texto a validar", "Bits em zero", "Nonce", "Tempo (em s)"])
    
    # Dados
    for linha in resultados:
        # Formatar tempo com 6 casas decimais
        texto, bits, nonce, tempo = linha
        escritor_csv.writerow([texto, bits, nonce, f"{tempo:.6f}"])

print(f"\nProcesso concluído! Resultados salvos em '{nome_arq_csv}'")
