import socket 

# A simple TCP client for the first user

host = socket.gethostname() 
port = 2004
BUFFER_SIZE = 2000 
MESSAGE = raw_input("Please type something or just quit") 
 
firstclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
firstclient.connect((host, port))

while MESSAGE != 'quit':
    firstclient.send(MESSAGE)     
    data = firstclient.recv(BUFFER_SIZE)
    print "second client got the data:", data
    MESSAGE = raw_input("first client: Please type something or just quit:")

firstclient.close()