# udp_server.py
import socket

HOST = '0.0.0.0'  # escuchar todas las interfaces
PORT = 12000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))
print(f"UDP server escuchando en {HOST}:{PORT}")

try:
    while True:
        data, addr = sock.recvfrom(4096)
        msg = data.decode('utf-8', errors='replace')
        print(f"Recibido de {addr}: {msg}")
        reply = f"OK: {msg}"
        sock.sendto(reply.encode('utf-8'), addr)
except KeyboardInterrupt:
    print("Servidor detenido")
finally:
    sock.close()
