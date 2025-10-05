# tcp_client.py
import socket
from utils_tcp import send_msg, recv_msg

SERVER = ('127.0.0.1', 14000)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(SERVER)

try:
    while True:
        txt = input("Mensaje (ENTER para salir): ")
        if not txt:
            break
        send_msg(sock, txt.encode('utf-8'))
        resp = recv_msg(sock)
        if resp is None:
            print("Conexión cerrada por el servidor")
            break
        print("Respuesta:", resp.decode())
finally:
    sock.close()
