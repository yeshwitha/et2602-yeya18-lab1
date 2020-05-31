import socket
import sys
from _thread import *
import select 
import re 

if len(sys.argv)!=2:
    print("entry format = ./chatserver ip:port ")
    sys.exit()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
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


def clientthread(conn,addr):
    while True:
        
        try:
            nick=conn.recv(2048).decode('utf-8')
            nick1=nick.strip('NICK ')
            regex = re.compile('[@!#$%^&*()?/|}{~:]')
            
            if(regex.search(nick1) == None) and len(nick1)<=12 and 'NICK ' in nick :
                conn.sendall('OK'.encode('utf-8'))
                break
            elif len(nick1) or regex.search(nick1) != None:
                conn.sendall('ERR malformed nick name'.encode('utf-8'))
            else:
                conn.close()
                print(addr[0]+" has disconnected")
                clients.remove(conn)
                del clients[conn]
                break
        except :
                break

        

    while True:
        try:
            if conn in clients:
                message = conn.recv(2048).decode('utf-8')
                message1=message.strip('MSG ')
                #print(len(message1))
            
                if not message:
                    conn.close()
                    print(addr[0]+" has disconnected")
                    clients.remove(conn)
                    break 

                else 'MSG ' not in message:
                    conn.sendall('ERROR malformed message'.encode('utf-8'))
                

        except KeyboardInterrupt:
            conn.close()
            break
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