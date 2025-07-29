import matplotlib as plt
import sys


nomeArqLog = "apache.logs"
try:
    fdLogs = open (nomeArqLog, "r")
    logsDia = {}
    for log in fdLogs:
        inicioTempo = log.find('[')
        FimTempo = log.find(']')
        tempo = log[inicioTempo+1:FimTempo][0:17]
        if tempo in logsDia:
            logsDia[tempo] += 1
        else:
            logsDia[tempo] = 1
        
    logsDia = dict(sorted(logsDia.items(), key=lambda x:x[0]))

    plt.title("Logs apache por dia")
    plt.bar (logsDia.keys(), logsDia.values())
    plt.show
    fdLogs.close()
    
except FileNotFoundError as e:
    print("O arquivo {nomeArqLog} não esta acessivel")
    exit()