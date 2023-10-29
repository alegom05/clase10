import socket
import csv

host = '127.0.0.1'
port = 5001
SOCK_BUFFER= 1024

if __name__ == '__main__':
   
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (host, port)

        print(f"Iniciando servidor en: {server_address[0]}:{server_address[1]}")
        server_socket.bind((host, port))

        server_socket.listen(5)
        print("Esperando conexiones...")

#def guardar_datos(c1: str) -> None:
    #with open("datos.csv", "a") as f:
        #f.write(f"{c1}\n")

#def promedio(datos):
        #edades=[int(line.split(',')[1]) for line in datos[1:] if len(line.split(',')) > 1]
        #return sum(edades)/(len(datos)-1)

#def contar(datos,x):
        #datos_x= [(line.split(',')[1]) for line in datos[1:] if len(line.split(',')) > 1]
        #return datos_x.count(x)

def promedio2(archivo):
    suma = 0
    contador = 0
    
    with open(archivo, 'r', encoding='utf-8') as f:
        next(f)  # Saltar la primera línea con los parámetros
        for fila in f:
            elementos = fila.strip().split(',')
            if len(elementos) > 1:
                valor = float(elementos[1])
                suma += valor
                contador += 1
    
    if contador == 0:
        return 0
    
    promedio = suma / contador
    return promedio


def contar2(archivo, letra):
    # Abre el archivo CSV "datos.csv" en modo lectura
    with open(archivo, "r", encoding='utf-8') as f:
        # Crea un lector CSV
        f = csv.reader(f)
        next(f)  # Saltar la primera fila con los parámetros
        # Inicializa un contador para contar la cantidad de veces que se repite la letra
        contador = 0
        # Itera sobre las filas del archivo CSV
        for fila in f:
            # Comprueba si la segunda columna de la fila (índice 1) contiene la letra deseada
            if len(fila) >= 2 and letra in fila[2]:
                contador += 1
    return contador

while True:
        conn, server_address = server_socket.accept()#sock.accept
        try:
                rpt=conn.recv(SOCK_BUFFER)
                rpt=rpt.decode('utf-8')
                cont="datos.csv"

                match rpt:
                        case "a":#promedio de edades
                                rpta= promedio2(cont) 
                                print(rpta)
                        case "b":#num de pacientes enfermos
                                rpta= contar2(cont,"e")
                                print(rpta)
                        case "c":#num de pacientes sanos
                                rpta= contar2(cont,"s")
                                print(rpta)
                        case _:
                                rpta= "No definido"
                print(rpta)
                conn.sendall(str(rpta).encode('utf-8'))
        except ConnectionResetError:
                break

server_socket.close()

        