import sys, time
from socket import *

timeout = 1 # in second
 
#Assign server
serverName = '192.168.0.105'

# Create UDP client socket
# Note the use of SOCK_DGRAM for UDP datagram packet
clientsocket = socket(AF_INET, SOCK_DGRAM)
# Set socket timeout as 1 second
clientsocket.settimeout(timeout) 
# Sequence number of the ping message
ptime = 0  

# Ping for 10 times
while ptime < 10: 
    ptime += 1
    # Format the message to be sent
    data = "Ping " + str(ptime) + " " + time.asctime()
    databytes = bytes(data, 'utf-8')
    # Send the UDP packet with the ping message
    clientsocket.sendto(databytes, (serverName, 12000))
    RTTa = time.time()*1000  # seconds to ms
    
    try:
        print(' ')
	# Receive the server response
        message, address = clientsocket.recvfrom(1024)
        modifiedMessage = message.decode()
        RTTb = time.time()*1000  #seconds to ms
	# Display the server response as an output
        print ("Reply from '{}': {}" .format(address[0], modifiedMessage))
	# Round trip time is the difference between sent and received time
        print ("RTT: " + str(RTTb - RTTa))

    except:
        # Server does not response
	# Assume the packet is lost
        print ("Request timed out.")
        ptime += 1
        continue

# Close the client socket
clientsocket.close()
 
