import socket

mi_socket = socket.socket()
mi_socket.bind( ('localhost', 8000) ) #Se establece la conexión
mi_socket.listen(5)   #Se define la cantidad de solicitudes que puede esperar en cola

while True:
    conexion, addr = mi_socket.accept()
    print("Nueva conexion establecida!")
    print(addr)

    #Para que el servidor muestre lo que está enviando el cliente.
    peticion = conexion.recv(1024)
    print(peticion)

    #Mensaje desde el servidor.
    conexion.send("Hola, te saludo desde el servidor!".encode())
    conexion.close() #Cerramos la conexion y seguimos a la escucha.