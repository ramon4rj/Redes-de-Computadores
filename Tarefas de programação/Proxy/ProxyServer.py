from socket import *

# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(('192.168.0.105', 8888))
tcpSerSock.listen(100)

while 1:
	# Strat receiving data from the client
	print ('Ready to serve...')
	tcpCliSock, addr = tcpSerSock.accept()
	print ('Received a connection from: {}' .format(addr))
	message = tcpCliSock.recv(1024).decode()
	#decodemessage = message.decode()
	print("Message: ")
	print (message)
	# Extract the filename from the given message
	print (message.split()[1])
	filename = message.split()[1].partition("/")[2]
	# And print its name
	print("File name: ")
	print (filename)
	fileExist = "false"
	filetouse = "/" + filename
	#filetouse = filename
	print("File to use: ")
	print (filetouse)
	try:
		# Check wether the file exist in the cache
		f = open(filetouse[1:], "r")                      
		outputdata = f.readlines()               
		fileExist = "true"
		# ProxyServer finds a cache hit and generates a response message
		tcpCliSock.send(b"HTTP/1.1 200 OK\r\n")
		tcpCliSock.send(b"Content-Type:text/html\r\n")
		print(len(outputdata))
		print(outputdata)
		for i in range(0, len(outputdata)):
			print('a')
			tcpCliSock.send(outputdata[i].encode())
			print ('Read from cache')     
	# Error handling for file not found in cache
	except IOError:    # Got to finish from here from below
		if fileExist == "false":
		# Create a socket on the proxyserver
			c = socket(AF_INET, SOCK_STREAM)            
			hostn = filename.replace("www.","",1)
			print("Host n: ")   
			print (hostn)
			try:
				# Connect to the socket to port 80
				# This is where it was supossed to connect using the browser, since its not the case it will conect to the IP adressed to the WebServer.py
				c.connect(('192.168.0.105', 6789))
				print('chegou aqui 1')
				# Create a temporary file on this socket and ask port 80 for the file requested by the client
				#fileobj = c.makefile()
				fileobj = "GET /" + filename + " HTTP/1.1\r\n\r\n"
				print("chegou aqui 2")
				#fileobj.write("GET "+"http://" + filename + " HTTP/1.1\n\n")
				
				#fileobj.write("GET /" + filename + "HTTP/1.1\r\n\r\n")
				print('fileobj: ')
				print(fileobj)
				#message_from_server = fileobj.readlines()
				
				#c.send(message_from_server.encode())
				c.send(fileobj)
				
				# Set timeout to server response
				#c.settimeout(5)

				rcvmessage = c.recv(1024)
				print('chegou aqui 3')
				#print(rcvmessage)
				
				# Read the response into buffer
				#buff = fileobj.readlines()
				#buff = rcvmessage.decode()
				print("Buff: ")
				buff = rcvmessage
				#print(buff)
				# Create a new file in the cache for the requested file. Also send the response in the buffer to client socket and the corresponding file in the cache
				tmpFile = open('filenamecopy.html',"wb")

				#tmpFile = open("./" + filename ,"wb")

				#sendfile = tmpFile.readlines()
				
				for line in buff():
					tmpFile.write(line)
					#tmpFile.close()
					tcpCliSock.send(line)

				tcpCliSock.send('\r\n')
				# Close file to commit changes
				tmpFile.close()
				#if len(buff) == 0:
				#	break
			except:
				print ("Illegal request")                                               
		else:
			# HTTP response message for file not found
			tcpCliSock.send(b"HTTP/1.0 404 sendErrorErrorError\r\n")                             
			tcpCliSock.send(b"Content-Type:text/html\r\n")
			tcpCliSock.send(b"\r\n")
	# Close the client and the server sockets    
	tcpCliSock.close() 
tcpSerSock.close()
