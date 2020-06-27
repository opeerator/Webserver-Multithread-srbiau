# This is my multithreaded project for OS class at srbiau with Ms.zamani
# Author: Ali Yamini

from threading import Thread 
import socket 
from socketserver import ThreadingMixIn


class CliThread(Thread): 

    def run(self): 
        while True : 
            data = conn.recv(2048) 
            print("Server has got your data: " + data)
            MESSAGE = raw_input("Please give a response from server: (y/n)")
            if MESSAGE == 'n':
                break
            conn.send(MESSAGE)

    def __init__(self,ip,port): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        print "This is a new socket for " + ip + ":" + str(port) 

    # My socket for tcp server
    BUFFER_SIZE = 20
    TCP_IP = '0.0.0.0' 
    TCP_PORT = 2004 
    
    mytcpserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    mytcpserver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    mytcpserver.bind((TCP_IP, TCP_PORT)) 
    threads = [] 

    while True: 
        tcpServer.listen(4) 
        print("Server is waiting for TCP connections...!")
        (conn, (ip,port)) = tcpServer.accept() 
        newthread = ClientThread(ip,port) 
        newthread.start() 
        threads.append(newthread) 
        
    for t in threads: 
    t.join() 