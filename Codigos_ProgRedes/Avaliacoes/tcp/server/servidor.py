import socket
from funcoeserver import *

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("", PORT))
sock.listen(5)
    
print(f"Servidor TCP escutando em porta {PORT}")
print(f"Pasta do servidor: {PASTA_SERVER}")
    
try:
    while True:
        conn, addr = sock.accept()
        handle_cliente(conn, addr)
except KeyboardInterrupt:
    print("\nServidor encerrado.")
except Exception as e:
    print(f"Erro: {e}")
finally:
    sock.close()
