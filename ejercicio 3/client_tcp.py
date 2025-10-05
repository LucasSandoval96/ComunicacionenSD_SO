import socket
import threading

SERVER_IP =  '192.168.0.21' # ⚠️ cambiar por la IP del servidor si está en otra PC
PORT = 14000

def recibir(sock):
    """Hilo para recibir mensajes del servidor."""
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print("\n" + data.decode('utf-8'))
        except:
            print("Conexión cerrada por el servidor.")
            break

def main():
    nombre = input("Tu nombre: ")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((SERVER_IP, PORT))
    sock.sendall(nombre.encode('utf-8'))

    threading.Thread(target=recibir, args=(sock,), daemon=True).start()

    print("💬 Escribí mensajes (ENTER para enviar, 'salir' para desconectarte)\n")

    try:
        while True:
            msg = input()
            if msg.lower() == "salir":
                break
            sock.sendall(msg.encode('utf-8'))
    except KeyboardInterrupt:
        pass
    finally:
        sock.close()
        print("Desconectado del chat.")

if __name__ == "__main__":
    main()