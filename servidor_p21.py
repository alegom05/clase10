import socket

SOCK_BUFFER = 1024

if __name__ == '__main__':

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('0.0.0.0', 5001)

    print(f"Iniciando servidor en: {server_address[0]}:{server_address[1]}")
    sock.bind(server_address)

    sock.listen(1)
    print("Esperando conexiones...")

    conn, client_address = sock.accept()
    señal=conn.recv(1024).decode()

    if señal=="rellenar":
        while True:
                text=open('pacientes.csv',"a")
                dato=conn.recv(1024).decode()
                print(dato)
                text=open('pacientes.csv',"a")
                text.write(dato)
            #finally:
                #conn.close()
                #print("Cerrando la conexion")
    elif señal=="descargar":
        packet=open('pacientes.csv',"r").read().split('\n')
        cantEnvios=len(packet)
        sock.send(str(cantEnvios).encode())
            for i in range(cantEnvios):
                sock.send(packet[i].encode())
                #descarga el archivo
        
