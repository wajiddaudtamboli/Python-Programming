#1 Client.Py
'''
import socket
s=socket.socket()
host=socket.gethostname()
port=6000
s.connect((host,port))
print(s.recv(1024))
s.send(b"Hello This is client")

s.close()
'''
#2 server.Py

import socket
s=socket.socket()
host=socket.gethostname()
port=6000
s.bind((host,port))
s.listen(5)
c,addr=s.accept()
c.send(b"Hello This is server")
print(s.recv(1024))

s.close()
