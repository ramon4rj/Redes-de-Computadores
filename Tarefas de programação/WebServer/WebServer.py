# Import socket module and datetime
from socket import *    
from datetime import datetime

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)
serverSocket = socket(AF_INET, SOCK_STREAM)

#define a server
serverName = '192.168.0.105'

# Assign a port number
serverPort = 6789

# Bind the socket to server address and server port
serverSocket.bind((serverName, serverPort))

# Listen to at most 1 connection at a time
serverSocket.listen(1)

# Server should be up and running and listening to the incoming connections
while True:
	print ('Ready to serve...')
	
	# Set up a new connection from the client
	connectionSocket, addr = serverSocket.accept()
	print("Request accepted from {} " .format(addr))
	
	# If an exception occurs during the execution of try clause
	# the rest of the clause is skipped
	# If the exception type matches the word after except
	# the except clause is executed
	try:
		date = datetime.today().strftime("%d/%m/%Y %H:%M:%S")
		# Receives the request message from the client
		message =  connectionSocket.recv(1024)
		print(message)
		# Extract the path of the requested object from the message
		# The path is the second part of HTTP header, identified by [1]
		filename = message.split()[1]
		# Because the extracted path of the HTTP request includes 
		# a character '\', we read the path from the second character 
		f = open(filename[1:])
		# Store the entire contenet of the requested file in a temporary buffer
		outputdata = f.read()
		# Send the HTTP response header line to the connection socket
		connectionSocket.send(b"HTTP/1.1 200 OK\r\n\r\n")
		connectionSocket.send(b"Connection: close\r\n\r\n")
		datestring = str(date)
		connectionSocket.send(b"Date: " + datestring.encode() + b"\r\n\r\n")
		connectionSocket.send(b"Server: MySimpleServer\r\n\r\n")
		connectionSocket.send(b"Last-Modified: Thursday Dec 09 2021 16:06:54\r\n\r\n")
		# Message length 
		length = str(len(outputdata))
		codelength = length.encode()
		connectionSocket.send(b"Content-Length: " + codelength + b"\r\n\r\n")
		connectionSocket.send(b"text/html\r\n\r\n")

		# Send the content of the requested file to the connection socket
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i].encode())
		connectionSocket.send(b"\r\n")
		
		# Close the file
		f.close()
		# Close the client connection socket
		connectionSocket.close()

	except IOError:
		# Send HTTP response message for file not found
		connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
		connectionSocket.send(b"<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n")

		# Close the client connection socket
		connectionSocket.close()
	
serverSocket.close()