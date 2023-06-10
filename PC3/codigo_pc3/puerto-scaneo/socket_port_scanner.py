#!/usr/bin/env python

import socket
import sys
from datetime import datetime
import errno

remoteServer    = input("Ingresa un host remoto para escanear: ")
remoteServerIP  = socket.gethostbyname(remoteServer)

print("Ingresa el rango de puertos que te gustaria escanear en la maquina")
startPort    = input("Ingresa un puerto de entrada: ")
endPort    = input("Ingresa a un puerto final: ")

print("Espera, escaneando el host remoto", remoteServerIP)

time_init = datetime.now()

try:
	for port in range(int(startPort),int(endPort)):
		print ("Verificando puerto {} ...".format(port))
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(5)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			print("Puerto {}: 	 Open".format(port))
		else:
			print("Puerto {}: 	 Closed".format(port))
			print("Razon:",errno.errorcode[result])
		sock.close()

except KeyboardInterrupt:
	print("Presiona Ctrl+C")
	sys.exit()
except socket.gaierror:
	print('Nombre del host no es resuelto.  Saliendo')
	sys.exit()
except socket.error:
	print("No se puede conectar al servidor")
	sys.exit()

time_finish = datetime.now()
total =  time_finish - time_init
print('Puerto escaneado completado en: ', total)
