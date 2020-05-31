import socket
import sys
from _thread import *
import select 
import re 

if len(sys.argv)!=3:
    print("entry format = ./chatclient ip:port nickname")
    sys.exit()
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Info = (sys.argv[1])
a=Info.split(':')
IP_addr=str(a[0])
port=int(a[1])
nick=str(sys.argv[2])
message1=server.recv(2048).decode('utf-8')
print(message1)
nick = 'NICK ' + nick
print('NICK '+nick.encode('utf-8'))
server.sendall(nick.encode('utf-8'))
ok_msg=server.recv(2048).decode('utf-8')
print(ok_msg)

server.close() #closing the connection