import socket 

host = socket.gethostname() 
port = 2004
BUFFER_SIZE = 2000 
MESSAGE = raw_input("Please type something or just quit")
 
secondclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
secondclient.connect((host, port))

while MESSAGE != 'quit':
    secondclient.send(MESSAGE)     
    data = secondclient.recv(BUFFER_SIZE)
    print "second client got the data:", data
    MESSAGE = raw_input("first client: Please type something or just quit:")


tcpClientB.close() 