import socket
import sys
from _thread import *
import select 
import re 

if len(sys.argv)!=3:
    print("entry format = ./chatclient ip:port nickname")
    sys.exit()
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
Info = (sys.argv[1])
a=Info.split(':')
IP_addr=str(a[0])
port=int(a[1])
nick=str(sys.argv[2])
server.connect((IP_addr, port))
message1=server.recv(2048).decode('utf-8')
print(message1)

nick = 'NICK ' + nick
print('NICK '+nick.encode('utf-8'))
server.sendall(nick.encode('utf-8'))
ok_msg=server.recv(2048).decode('utf-8')
print(ok_msg)
if ok_msg == "OK":
    pass
elif ok_msg == "ERR malformed nick name":
    print('do not enter nick name with special characters,limit to 12 chars')
    print('sorry you are disconnected try again with valid nickname')
    sys.exit()



server.close() #closing the connection