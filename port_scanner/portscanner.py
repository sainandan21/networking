#Which is going to allow us to find open ports in servers, computers, printers.
#we are going to use multithreading to make this port scanner as fast as possible
#so we are going to run multiple threads so we can scan hundreds of
#of ports per second

#WHy to scan open port
#open port is especially an unnecessarily open port might be a secuirty gap
#we always wana find security gaps either in our own networks to make sure that our
#network is secure enough or if we have bad intentions and we are hacking

#Port scanning is an illegal activity until and unless you have a permission

# If a port is open, then attacker or hacker can easily attack that open port.
# Import necessary libraries
import socket
import threading
from queue import Queue

# Define the target (in this case, it's a local host, which is typically 127.0.0.1)
target = '127.0.0.1'

# Create a queue to store ports to be scanned and an empty list to store open ports
queue = Queue()
open_ports = []

# Define a function to check if a specific port is open
def portscan(port):
    try:
        # Create a socket object and try to connect to the target on the specified port
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True  # If the connection is successful, the port is open
    except:
        return False  # If the connection fails, the port is closed

# Example usage of the portscan function
print(portscan(80))  # It checks if port 80 is open

# Define a function to fill the queue with a list of ports to be scanned
def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

# Define a worker function that checks ports from the queue
def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("Port {} is open".format(port))
            open_ports.append(port)

# Create a list of ports to be scanned (in this case, ports from 1 to 1023)
port_list = range(1, 1024)

# Fill the queue with the list of ports
fill_queue(port_list)

# Create a list of threads for parallel port scanning
thread_list = []

# Start 10 worker threads to scan ports in parallel
for t in range(10):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

# Wait for all threads to complete
for thread in thread_list:
    thread.join()

# Print the list of open ports
print("Open ports are: ", open_ports)
