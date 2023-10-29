import socket
import time

SOCK_BUFFER = 1024


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5001)

    sock.connect(server_address)

    a=input("Ingrese una letra ")

    sock.sendall(a.encode('utf-8'))

    rpta = sock.recv(SOCK_BUFFER)
    rpta = rpta.decode('utf-8')
    print(rpta)

    print(f"Respuesta: {rpta}")