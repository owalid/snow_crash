'''
	Simple socket server using threads
'''

import socket
import sys
import time
import os

HOST = ''
PORT = 6969

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.bind((HOST, PORT))
except socket.error as msg:
	sys.exit()
	

s.listen(1)

while 1:
	conn, addr = s.accept()
	os.remove('/tmp/lol')
	os.symlink('/home/user/level10/token', '/tmp/lol')
	while True:
			data = conn.recv(1000)
			if data == b'':
				print('finish')
				break
			print(data)
	
s.close()
