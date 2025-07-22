
fdlogs = open ("apache.logs", "r")
ips = set()
for log in fdlogs:
    ip = log.split()[0]
    ips.add(ip)
fdlogs.close()

with open("ips.txt", "w") as fdips:
    for ip in ips:
        fdips.write(ip+"\n")
