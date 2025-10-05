# protocol_client.py
import socket
import sys
import time

SERVER = ('127.0.0.1', 13000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 0))  # puerto efímero local
mode = int(sys.argv[1]) if len(sys.argv) > 1 else 2
payload = "Hello"

if mode == 2:
    # 2 vías: petición -> respuesta
    sock.sendto(payload.encode(), SERVER)
    data, _ = sock.recvfrom(4096)
    print("Respuesta:", data.decode())

elif mode == 3:
    # 3 vías: petición -> ack -> confirmación final
    sock.sendto(payload.encode(), SERVER)
    data, _ = sock.recvfrom(4096)
    print("Paso 2 (ack):", data.decode())
    # Envía confirmación final
    sock.sendto(("FINAL:"+payload).encode(), SERVER)
    print("Enviada confirmación final.")

elif mode == 4:
    # 4 vías ejemplo (simulamos handshake adicional)
    sock.sendto(("SYN:"+payload).encode(), SERVER)
    synack, _ = sock.recvfrom(4096)
    print("Recibido:", synack.decode())
    sock.sendto(("ACK:"+payload).encode(), SERVER)
    final, _ = sock.recvfrom(4096)
    print("Paso final del servidor:", final.decode())

sock.close()
