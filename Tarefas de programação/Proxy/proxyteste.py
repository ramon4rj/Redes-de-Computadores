from socket import *


# Define port
proxyPort = 8888
# Create a server socket, bind it to the port and start listening
proxySocket = socket(AF_INET, SOCK_STREAM)
proxySocket.bind(('192.168.0.105', proxyPort))
proxySocket.listen(100)
print("Listening on port {}" .format(proxyPort))

while True:
    # Strat receiving data from the client
    print('Ready to serve...')
    connectionSocket, address = proxySocket.accept()
    print("Request accepted from: {}..." .format(address))
    data = connectionSocket.recv(1024).decode()
    print("Received sentence: {}" .format(data))
    datacode = data.encode()


    # Send forward to WebServer port: 6789
    serverName = '192.168.0.105'
    serverPort = 6789
    print("Connecting to server on port {}" .format(serverPort))

    # Create a socket to request file from the WebServer
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    clientSocket.send(datacode)
    print('datacode: ')
    print(datacode)

    # Receives the messages from the WebServer
    serverReply = clientSocket.recv(1024)
    print("Server Reply: {}" .format(serverReply.decode()))
    print(serverReply.decode())
    #clientSocket.close()


    # Forward back to Client
    connectionSocket.send(serverReply)
    connectionSocket.close()