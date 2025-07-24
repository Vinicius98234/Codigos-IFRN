import sys

nomeArqLog = "apache.logs"
try:
    fdLogs = open (nomeArqLog, "r")
    logsHora = {}
    for log in fdLogs:
        inicioTempo = log.find('[')
        FimTempo = log.find(']')
        tempo = log[inicioTempo+1:FimTempo][0:17]
        if tempo in logsHora: 
            logsHora [tempo] += 1
        else:
            logsHora [tempo] = 1
    fdLogs.close()
    print(max (logsHora.items(),key=lambda item:item[1]))
except FileNotFoundError as e:
    print("O arquivo {nomeArqLog} não esta acessivel")
    exit()