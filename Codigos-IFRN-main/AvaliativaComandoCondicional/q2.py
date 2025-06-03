# Pega a nota final do estudante 
print ("Calcular Nota Final: ")
n1 = float(input("Nota do Primeiro Bimestre: "))
n2 = float(input("Nota do Segundo Bimestre: "))

media = ((2*n1) + (3*n2)) / 5 # Calcula a média

if media < 20: # Se a média for menor que 20, exibe que o aluno foi reprovado
    print ("Reprovado! Com média: ", media) 
else:
    if 20 <= media < 60: # Se a média for maior ou igual que 20 e menor que 60 o aluno vai para prova final
        print ("Você vai para prova final!!! Com média: ", media)
        naf = float(input("Nota da avaliação final: ")) 
        mdf = (media + naf) / 2 # Calcula a média final da avaliação final
        if mdf < 60: # Se a média final for abaixo de 60 vai ser reprovado
            print("Você foi reprovado! Com média final: ", mdf)
        else: # Se não, aprovado!
            print("Aprovado!!! Com média: ", mdf)
    else: # Se tudo isso não acontecer e sua média for acima de 60 você foi aprovado
        print("Você foi aprovado! Com média: ", media)




