# protocol_server.py
import socket

HOST = '0.0.0.0'
PORT = 13000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))
print(f"Server UDP protocolo en {HOST}:{PORT}")

while True:
    data, addr = sock.recvfrom(4096)
    msg = data.decode()
    print("Paso 1: recibido:", msg, "de", addr)
    # Determinar protocolo según mensaje
    # Se espera msg como "PROTO:<n>:payload"
    try:
        header, payload = msg.split(":", 2)[0:2], msg.split(":",2)[-1]
        # Manejo simplificado:
    except Exception:
        payload = msg

    # Aquí simplificamos: servidor responde con ACK
    sock.sendto(f"ACK:{payload}".encode(), addr)
    # Si el cliente espera confirmación final, el cliente la enviará y servidor la mostrará
