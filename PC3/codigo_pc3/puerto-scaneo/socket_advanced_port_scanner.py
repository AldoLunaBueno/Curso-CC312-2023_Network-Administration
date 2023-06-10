#!/usr/bin/python

import optparse
from socket import *
from threading import *

def socketScan(host, port):
	try:
		socket_connect = socket(AF_INET, SOCK_STREAM)
		socket_connect.settimeout(5)
		result = socket_connect.connect((host, port))
		print('[+] %d/tcp open' % port)
	except Exception as exception:
		print('[-] %d/tcp closed' % port)
		print('[-] Razon:%s' % str(exception))
	finally:
		socket_connect.close()	

def portScanning(host, ports):
	try:
		ip = gethostbyname(host)
		print('[+] Scan Resultados para: ' + ip)
	except:
		print("[-] No se puede resolver '%s': host no conocido" %host)
		return

	for port in ports:
		t = Thread(target=socketScan,args=(ip,int(port)))
		t.start()

def main():
	parser = optparse.OptionParser('socket_portScan '+ '-H <Host> -P <Puerto>')
	parser.add_option('-H', dest='host', type='string', help='Especificar host')
	parser.add_option('-P', dest='port', type='string', help='Especificar puerto[s] separado por coma')

	(options, args) = parser.parse_args()

	host = options.host
	ports = str(options.port).split(',')

	if (host == None) | (ports[0] == None):
		print(parser.usage)
		exit(0)

	portScanning(host, ports)


if __name__ == '__main__':
	main()
