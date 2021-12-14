from socket import *

# Message to send
msg = '\r\nI love computer networks!'.encode()
endmsg = '\r\n.\r\n'.encode()

# Choose a mail server (e.g. Google mail server) and call it mailserver
#mailserver = 'mail.smtp2go.com'
mailserver = 'smtp.gmail.com'

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)

# Port number may change according to the mail server   587
clientSocket.connect((mailserver, 25))
recv = clientSocket.recv(1024)
print (recv)
if recv[:3] != '220':
	print ('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO gmail.com\r\n'.encode()
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
recv1 = recv1.decode()
print("From recv1: ")
print (recv1)
if recv1[:3] != '250':
	print ('250 reply not received from server.')
	
# Send MAIL FROM command and print server response.
mailfrom = 'MAIL FROM: <alice@gmail.com>\r\n'.encode()
clientSocket.send(mailfrom)
recv2 = clientSocket.recv(1024)
recv2 = recv2.decode()
print("From recv2: ")
print (recv2)
if recv2[:3] != '250':
	print ('250 reply not received from server.')

# Send RCPT TO command and print server response. 
rcptto = 'RCPT TO: <bob@yahoo.com>\r\n'.encode()
clientSocket.send(rcptto)
recv3 = clientSocket.recv(1024)
recv3 = recv3.decode()
print("From recv3: ")
print (recv3)
if recv3[:3] != '250':
	print ('250 reply not received from server.')

# Send DATA command and print server response. 
data = 'DATA\r\n'.encode()
clientSocket.send(data)
recv4 = clientSocket.recv(1024)
recv4 = recv4.decode()
print("From recv4: ")
print (recv4)
if recv4[:3] != '354':
	print ('354 reply not received from server.')

# Send message data.
clientSocket.send(b'SUBJECT: Greeting To you!\r\n')
clientSocket.send(b'test again')
clientSocket.send(msg)

# Message ends with a single period.
clientSocket.send(endmsg)
recv5 = clientSocket.recv(1024)
recv5 = recv5.decode()
print("From recv5: ")
print (recv5)
if recv5[:3] != '250':
	print ('250 reply not received from server.')

# Send QUIT command and get server response.
quitcommand = 'QUIT\r\n'
quitcommandcode = quitcommand.encode()
clientSocket.send(quitcommandcode)
recv6 = clientSocket.recv(1024)
recv6 = recv6.decode()
print("From recv6: ")
print (recv6)
if recv6[:3] != '221':
	print ('221 reply not received from server.')

clientSocket.close()
