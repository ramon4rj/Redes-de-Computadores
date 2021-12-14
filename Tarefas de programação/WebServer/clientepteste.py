from socket import*

serverName = '127.0.0.1'
serverPort = 6789
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
    decoder = modifiedMessage.decode()
    print ('From Server: ', decoder)
    #decoder = modifiedMessage.decode()
    # Receiving parts
    data = decoder
    #clientSocket.close()
    if len(data) ==0:
        break

print(data)

clientSocket.close()