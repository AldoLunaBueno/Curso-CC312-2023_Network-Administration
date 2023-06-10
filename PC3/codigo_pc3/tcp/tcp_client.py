#!/usr/bin/python
 
import socket

host="127.0.0.1"
port = 9998

try:
	mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	mysocket.connect((host, port))
	print('Conectado al host '+str(host)+' en puerto: '+str(port))
	message = mysocket.recv(1024)
	print("Mensaje recibido desde el servidor", message)
	while True:
		message = input("Ingresa un mensaje > ")
		mysocket.send(bytes(message.encode('utf-8')))
		if message== "quitar":
			break
except socket.errno as error:
	print("Error socket ", error)
finally:
	mysocket.close()
