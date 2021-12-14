from socket import*

serverName = '192.168.0.105'
serverPort = 8888
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
filename = 'arquivoreq.html'
message = "GET /" + filename + " HTTP/1.1\r\n\r\n"
clientSocket.send(message.encode())

data = 0
while True:
    # Set timeout to receive packet
    clientSocket.settimeout(5)
    modifiedMessage = clientSocket.recv(1024)
    print ('From Server: ', modifiedMessage)
    decoder = modifiedMessage.decode()
    # Receiving parts
    data = decoder
    #clientSocket.close()
    if len(data) ==0:
        break

print(data)

clientSocket.close()