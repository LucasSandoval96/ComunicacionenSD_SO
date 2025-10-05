# udp_client.py
import socket

SERVER = ('127.0.0.1', 12000)  # cambiar a IP del server
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    while True:
        msg = input("Mensaje (ENTER para salir): ")
        if not msg:
            break
        sock.sendto(msg.encode('utf-8'), SERVER)
        data, _ = sock.recvfrom(4096)
        print("Respuesta:", data.decode('utf-8'))
finally:
    sock.close()
