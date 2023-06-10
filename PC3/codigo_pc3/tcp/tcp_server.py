#!/usr/bin/python

import socket
import threading

SERVER_IP   = "127.0.0.1"
SERVER_PORT = 9998

#  family = Internet, type = stream socket means TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((SERVER_IP,SERVER_PORT))

server.listen(5)

print("[*] Servido escuchando en  %s:%d" % (SERVER_IP,SERVER_PORT))

client,addr = server.accept()

client.send("Soy el servidor aceptando conexiones...".encode())

print("[*] Conexion aceptada desde: %s:%d" % (addr[0],addr[1]))

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print("[*] Solicitud pedida : %s desde el cliente %s" , request, client_socket.getpeername())
    client_socket.send(bytes("ACK","utf-8"))

while True:
    handle_client(client)
    
client_socket.close()
server.close()
