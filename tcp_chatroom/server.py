# We are going to set up a server and multiple clients and these clients can then connect to the server
# Which works as a chat room and each client can send messages to the  server with nickname
# all other clients can see messages and they can respond back.
# Import necessary libraries
import threading
import socket

# Define the host and port to listen on (localhost and port 55455)
host = '127.0.0.1'  # Local host
port = 55455

# Create a socket object and bind it to the host and port
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()  # Listen for incoming connections

# Create lists to store connected clients and their nicknames
clients = []
nicknames = []

# Function to broadcast a message to all connected clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Function to handle messages from a single client
def handle(client):
    while True:
        try:
            # Receive a message from the client
            message = client.recv(1024)
            # Broadcast the message to all clients
            broadcast(message)
        except:
            # If an error occurs (e.g., client disconnects), remove the client and their nickname
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            # Broadcast a message indicating that the client has left the chat
            broadcast(f'{nickname} left the chat'.encode('ascii'))
            break

# Function to accept and manage incoming client connections
def receive():
    while True:
        # Accept a new client connection and get the client's address
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        # Prompt the client to provide a nickname
        client.send("NICK".encode("ascii"))
        nickname = client.recv(1024).decode("ascii")
        nicknames.append(nickname)
        clients.append(client)
        print(f"Nickname of the client is {nickname}")

        # Broadcast a message indicating that the client has joined the chat
        broadcast(f"{nickname} joined the chat".encode("ascii"))

        # Send a welcome message to the client
        client.send("Connected to the server".encode("ascii"))

        # Start a thread to handle the client's messages
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

# Start receiving and handling client connections
print("Server is listening")
receive()


