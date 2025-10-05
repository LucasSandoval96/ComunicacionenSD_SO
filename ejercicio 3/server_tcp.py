import socket
import threading

HOST = '0.0.0.0'
PORT = 14000

clients = []  # [(conn, addr, nombre)]

def broadcast(mensaje, origen=None):
    """Envía un mensaje a todos los clientes excepto al origen."""
    for conn, addr, nombre in clients:
        if conn != origen:
            try:
                conn.sendall(mensaje.encode('utf-8'))
            except:
                pass  # ignorar desconectados

def handle_client(conn, addr):
    try:
        nombre = conn.recv(1024).decode('utf-8')
        if not nombre:
            nombre = f"{addr[0]}:{addr[1]}"

        clients.append((conn, addr, nombre))
        print(f"🟢 {nombre} conectado desde {addr}")
        broadcast(f"💬 {nombre} se unió al chat.", conn)

        while True:
            data = conn.recv(1024)
            if not data:
                break
            msg = data.decode('utf-8')
            print(f"[{nombre}] dice: {msg}")
            broadcast(f"[{nombre}] {msg}", conn)
    except Exception as e:
        print(f"⚠️ Error con {addr}: {e}")
    finally:
        print(f"🔴 {nombre} se desconectó")
        conn.close()
        clients.remove((conn, addr, nombre))
        broadcast(f"❌ {nombre} salió del chat.")

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen()
    print(f"🚀 Servidor TCP escuchando en {HOST}:{PORT}")

    try:
        while True:
            conn, addr = sock.accept()
            t = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
            t.start()
    except KeyboardInterrupt:
        print("\nServidor detenido manualmente.")
    finally:
        sock.close()

if __name__ == "__main__":
    main()