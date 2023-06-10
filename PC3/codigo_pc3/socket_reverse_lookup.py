#!/usr/bin/env python

import socket

try :
	result = socket.gethostbyaddr("8.8.8.8")
	print("El nombre del host es:",result[0])
	print("Direccion Ip :")
	for item in result[2]:
		print(" "+item)
except socket.error as e:
	print("Error al resolver la dirección IP:",e)

