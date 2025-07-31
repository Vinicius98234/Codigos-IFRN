import random

# Cores
VERDE = '\033[32m'   # Posição correta
AMARELO = '\033[33m' # Letra existe mas posição errada
VERMELHO = '\033[31m'# Letra não existe
RESET = '\033[0m'    # Resetar cor

print("DUETO\n")

palavras = ["pleno", "risco", "claro", "trago", "forte", "vento", "chave", "basta", "nuvem", "saiba", 
            "lente", "mente", "copos", "brisa", "tocar"] # Palavras aleatórias 

# Selecionar palavras secretas
indice1 = random.randint(0, len(palavras)-1)
palavra1 = palavras[indice1].upper()

indice2 = random.randint(0, len(palavras)-1)
palavra2 = palavras[indice2].upper()
while palavra1 == palavra2:
    indice2 = random.randint(0, len(palavras)-1)
    palavra2 = palavras[indice2].upper()

tentativas = 0
acertou_palavra1 = False  # Aqui já inicia dizendo que ainda não acertou as palavras
acertou_palavra2 = False
letras_fora1 = []
letras_fora2 = []

while tentativas < 7 and not (acertou_palavra1 and acertou_palavra2):  # Enquanto as tentativas forem menores que 7 e não tiver acertado as palavras continua rodando
    tentativa = input(f"Tentativa {tentativas+1}/7: ").upper() # Aqui é a tentativa
    
    if len(tentativa) != 5: # Se a tentativa tiver menos ou mais de 5 letras n roda
        print("Palavra deve ter 5 letras!")
        continue
    
    # Preparar visualização para cada palavra secreta usando listas
    resultado1 = []
    resultado2 = []
    
    for i in range(5): # Percorre todas as letras da tentativa
        letra = tentativa[i]
        
        # Verifica se acertou a palavra ou a posição de alguma letra da palavra 1
        if not acertou_palavra1:
            if letra == palavra1[i]:
                resultado1.append(f"{VERDE}{letra}{RESET}")
            elif letra in palavra1:
                resultado1.append(f"{AMARELO}{letra}{RESET}")
            else:
                resultado1.append(f"{VERMELHO}{letra}{RESET}")
                letras_fora1.append(letra)
        else:
            resultado1.append(letra)
        
        # Verifica se acertou a palavra ou a posição de alguma letra da palavra 2
        if not acertou_palavra2:
            if letra == palavra2[i]:
                resultado2.append(f"{VERDE}{letra}{RESET}")
            elif letra in palavra2:
                resultado2.append(f"{AMARELO}{letra}{RESET}")
            else:
                resultado2.append(f"{VERMELHO}{letra}{RESET}")
                letras_fora2.append(letra)
        else:
            resultado2.append(letra)
    
    # Exibe as duas palavras lado a lado parecido com o jogo termo 
    print('\n' + ' '.join(tentativa))
    print(' '.join(resultado1), '   ', ' '.join(resultado2))
    
    # Mostrar letras que não estão em cada palavra
    if not acertou_palavra1:
        print(f"Letras fora da 1ª: {' '.join(sorted(letras_fora1))}")
    if not acertou_palavra2:
        print(f"Letras fora da 2ª: {' '.join(sorted(letras_fora2))}")
    
    # Verifica se acertou alguma das palavras ou ambas
    if not acertou_palavra1 and tentativa == palavra1:
        acertou_palavra1 = True
        print(f"\n✅ Acertou a 1ª palavra: {palavra1}")
    
    if not acertou_palavra2 and tentativa == palavra2:
        acertou_palavra2 = True
        print(f"\n✅ Acertou a 2ª palavra: {palavra2}")
    
    if acertou_palavra1 and acertou_palavra2:  
        print("\n Parabéns! Você acertou ambas as palavras!")
        break
    
    tentativas += 1

if not (acertou_palavra1 and acertou_palavra2): # Se acabar o numero de tentativas e n acertar nenhuma das palavras ai acaba o jogo
    print(f"\nFim de jogo! As palavras eram: {palavra1} e {palavra2}")