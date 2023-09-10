import sys, time
from socket import *

# Get the server hostname and port as command line arguments
argv = sys.argv                      
host = argv[1]
port = argv[2]
timeout = 1 # in second

# Create UDP client socket
# Note the use of SOCK_DGRAM for UDP datagram packet
client_socket = socket(AF_INET,SOCK_DGRAM)

# Set socket timeout as 1 second
client_socket.settimeout(1.0)

# Command line argument is a string, change the port into integer
port = int(port)  

# Sequence number of the ping message
seqNum = 0  

# Ping for 10 times
while seqNum < 10: 
	seqNum += 1
	# Format the message to be sent
	data = "Ping " + str(seqNum) + " " + time.asctime()
    
	try:
	# Sent time
		RTTs = time.time()  #time in seconds
	
	# Send the UDP packet with the ping message
		address = (host, port)
		message = data.encode('utf-8')

		client_socket.sendto(message, address)

	# Receive the server response
		response, address = client_socket.recvfrom(2048)
	
	# Received time
		RTTr = time.time()
	
	# Display the server response as an output
		print("✅ REPLY FROM " + address[0] + ": " + response.decode())       
	
	# Round trip time is the difference between sent and received time
		RTT = RTTr - RTTs
		print("⏱️ RTT: {:.6f} SECONDS".format(RTT))

	except:
		# Server does not respond
	        # Assume the packet is lost
		print ("❌ REQUEST", seqNum,"TIMED OUT.")
		continue

# Close the client socket
client_socket.close()




