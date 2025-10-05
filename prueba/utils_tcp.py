# utils_tcp.py
import socket
import struct

def send_msg(sock: socket.socket, data: bytes):
    # Prependimos 4 bytes (big-endian) con la longitud
    length = struct.pack('!I', len(data))
    sock.sendall(length + data)

def recv_msg(sock: socket.socket):
    # Leer exactamente 4 bytes para la longitud
    raw_len = recvall(sock, 4)
    if not raw_len:
        return None
    length = struct.unpack('!I', raw_len)[0]
    # Leer el mensaje completo
    return recvall(sock, length)

def recvall(sock: socket.socket, n: int):
    data = b''
    while len(data) < n:
        chunk = sock.recv(n - len(data))
        if not chunk:
            return None
        data += chunk
    return data
