# This is my multithreaded project for OS class at srbiau with Ms.zamani
# Author: Ali Yamini

from threading import Thread 
import socket 
from socketserver import ThreadingMixIn


class CliThread(Thread): 

    def __init__(self,ip,port): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        print "[+] New server socket thread started for " + ip + ":" + str(port) 
        
    # My socket for tcp server
    BUFFER_SIZE = 20
    TCP_IP = '0.0.0.0' 
    TCP_PORT = 2004 
    
    mytcpserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    mytcpserver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    mytcpserver.bind((TCP_IP, TCP_PORT)) 
    threads = [] 