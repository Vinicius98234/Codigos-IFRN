with open ("apache.logs", "r") as fdHMS:
    contador = {}
    for log in fdHMS:
        sepreq = log.split()[3]
        data = sepreq.split(":")[0]
        hora = data[1]
        minuto = data [2]
        contador[sepreq] = contador.get(data, 0) + 1

    