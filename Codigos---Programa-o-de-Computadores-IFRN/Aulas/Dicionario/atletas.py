import requests, json

try:
    dados = requests.get("https://api.cartola.globo.com/atletas/mercado").text
    atletas = json.loads(dados)["atletas"]
    posicoes = json.loads(dados)["posicoes"]
    
    """for atleta in atletas:
        if atleta["clube_id"] == 263: # Botafogo/RJ
            print (f"{atleta['apelido']} -> {atleta['nome']}")"""
    
    saopaulo = filter (lambda x: x['clube_id'] == 276, atletas)

    saopaulo_ordenado = sorted(saopaulo, key=lambda x: x['preco_num'], reverse=True)
    for atleta in saopaulo_ordenado:
        posicoes_id = str(atleta['posicao_id'])
        nome_posicao = posicoes[posicoes_id]['nome']
        preco_ordenado = f"{atleta['preco_num']:.2f}"
        print("\n")
        print (f"Apelido: {atleta['apelido']} \n Nome: {atleta['nome']} \n Posição: {nome_posicao} \n Valor: C$ {preco_ordenado}")
except json.decoder.JSONDecodeError as e:
    print ("Erro na conversão de JSON para dicionario")