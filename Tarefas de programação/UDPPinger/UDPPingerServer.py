#UDPPingerServer
import random
import socket
from socket import *

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP addres and port number to socket
serverSocket.bind(('127.0.0.1', 12000))

while True:
    print("Running...")
    # Generate random number in the range of 0 to 10
    rand = random.randint(0, 10)
    # Receive the client packet along with the addres it is coming from
    message, addres = serverSocket.recvfrom(1024)
    # Capitalize the message from the client 
    message = message.upper()
    # If rand is less than 4, we consider the packet lost and not respond
    if rand < 4:
        continue
    # Otherwise, the server responds
    serverSocket.sendto(message, addres)

