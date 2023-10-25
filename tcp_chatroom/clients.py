# Import necessary libraries
import threading
import socket

# Create a socket object and connect to the server at localhost and port 55455
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55455))

# Ask the user to choose a nickname
nickname = input("Choose a nickname: ")

# Function to receive and display messages from the server
def receive():
    while True:
        try:
            # Receive a message from the server
            message = client.recv(1024).decode('ascii')
            # Check if the message is a special "NICK" message
            if message == "NICK":
                pass  # Ignore this message
            else:
                # Display the received message
                print(message)
        except:
            print("An error occurred")
            client.close()
            break

# Function to input and send messages to the server
def write():
    while True:
        # Prompt the user to input a message
        message = f'{nickname}: {input("")}'
        # Send the message to the server
        client.send(message.encode("ascii"))

# Start a thread to receive messages from the server
receive_thread = threading.Thread(target=receive)
receive_thread.start()

# Start a thread to input and send messages to the server
write_thread = threading.Thread(target=write)
write_thread.start()
