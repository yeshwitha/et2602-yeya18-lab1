import socket
import sys
from _thread import *
import select 
import re 

if len(sys.argv)!=2:
    print("entry format = ./chatserver ip:port ")
    sys.exit()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Info = (sys.argv[1])
a=Info.split(':')
IP_addr=str(a[0])
port=int(a[1])

server.bind((IP_addr,port))
server.listen(100)
print('Hello my name is Jarvis, Welcome to the chat server')
print('Waiting for connections')
clients=[]
clients.append(server)

def broadcasting(message,connection,nick1):
    for sockets in clients:
        if sockets!= server:
            try:
                sockets.sendall(message.encode('utf-8'))
            except KeyboardInterrupt:
                    clients.remove(sockets)
                    break 


while True:
    conn,addr=server.accept()
    #accepts incoming connections 
    conn.sendall('Hello 1'.encode('utf-8'))
    clients.append(conn)
    print(addr[0]+" has connected")
    


conn.close()
server.close()  