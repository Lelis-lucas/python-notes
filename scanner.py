#!/bin/python3

import sys
import socket
from datetime import datetime

#Define our target/definir nosso alvo
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #sys.argv[1] == bash: $1 /Translate hostname to IPv4
else: 
	print('Invalid amount of arguments.')
	print('Syntax: python3 scanner.py <ip>')
	
#ADD A PRETTY BANNER/ADICIONAR BANNER
print('-' * 50)
print('Scanning target: ' + target)
print('Time Started: ' + str(datetime.now()))
print('-' * 50)

try:
	for port in range(1, 10000): #THREATING IS BETTER FOR MEMORY ENERGY
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1) #IF THE SCANNER CAN'T CONNECT THE PORT, WAIT 1 SECOND AND PASS TO OTHER PORT.
		result = s.connect_ex((target, port)) #returns a error indicator
		#print('Checking port {}'.format(port))
		if result == 0:
			print('Port {} is open'.format(port))
		s.close()
			
except KeyboardInterrupt:
	print('\nExiting program')
	sys.exit()
	
except spcket.gaierror:
	print('Couldnt connect to server.')
	sys.exit()
	
