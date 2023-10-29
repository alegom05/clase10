import socket
import time

SOCK_BUFFER = 1024


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5001)

    print(f"Conectando al servidor {server_address[0]}:{server_address[1]}")
    sock.connect(server_address)
    try:
        print("¿Qué desea hacer?")
        print("1. Ingresar paciente")
        print("2. Descargar pacientes")
        rpta=input( )
        if rpta=="1":
            sock.send(("rellenar").encode()) 
            while(1):
                print("Ingrese datos del paciente:")
                nombre=input("\nIngrese Nombre(s): ")
                apellido=input("\nIngrese Apellido(s): ")
                peso=input("\nIngrese peso: ")
                talla=input("\nIngrese talla: ")
                edad=input("\nIngrese edad: ")
                
                while(1):
                    seguro1=input("\n¿Cuenta con seguro? (s/n): ")            
                    if seguro1=="s":
                        seguro="True"
                        break
                    elif seguro1=="n":
                        seguro="False"
                        break
                    else:
                        print("No tipeo bien")
                        break
                sock.send(("\n"+nombre+","+apellido+","+peso+","+talla+","+edad+","+seguro).encode())
                a=(+nombre+","+apellido+","+peso+","+talla+","+edad+","+seguro)
                print(a)
        elif rpta=="2":
            sock.send(("descargar").encode()) 
            while(1):
                 
        else:
            print("Tipeo mal")
        
    except:KeyboardInterrupt