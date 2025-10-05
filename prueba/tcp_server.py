# tcp_server.py
import socket
import threading
from utils_tcp import recv_msg, send_msg

HOST = '0.0.0.0'
PORT = 14000

def handle_client(conn, addr):
    print("Conexión desde", addr)
    try:
        while True:
            msg = recv_msg(conn)
            if msg is None:
                break
            text = msg.decode('utf-8', errors='replace')
            print("Recibido desde:", text)
            # responder
            resp = f"Echo: {text}".encode()
            send_msg(conn, resp)
    finally:
        conn.close()
        print("Desconectado", addr)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen()
print("TCP server escuchando en", HOST, PORT)

try:
    while True:
        conn, addr = sock.accept()
        t = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
        t.start()
except KeyboardInterrupt:
    print("Servidor TCP detenido")
finally:
    sock.close()
