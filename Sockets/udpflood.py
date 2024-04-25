import socket 
import random
import time
import sys

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #Creamos un socket
bytes=random._urandom(1024) #Creamos un paquete
dur=1 #Tiempo de la prueba
ip=r'140.0.24.49' #ÏP destino
port=8000 #Puerto destino
sent = int(0)
timeout = time.time()+dur 

while 1 == 1: 
    try:
        if time.time()>timeout:         #Salida por timeout
            sys.exit()
    except KeyboardInterrupt:           #Salida por interrupción de teclado
        sys.exit()
    else:
        sock.sendto(bytes,(ip,port))
        print(f"Enviado {sent} la cantidad de paquetes a {ip} en el puerto {port}.")
        sent= sent + 1
    