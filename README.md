# UDP SOCKET PING

### **OVERVIEW**

This project involves implementing a simple Internet Ping server in Python and creating a corresponding client. The functionality provided by these programs is similar to that of standard ping programs available in modern operating systems. However, these programs use a simpler protocol, UDP (User Datagram Protocol), instead of the standard ICMP (Internet Control Message Protocol) to communicate with each other. The ping protocol allows a client machine to send a data packet to a remote machine and have the remote machine return the data unchanged (an action known as echoing). Among other uses, the ping protocol allows hosts to determine round-trip times to other machines.

### **PACKET LOSS**

UDP provides applications with an unreliable transport service. Messages can be lost in the network due to router queue overflow, faulty hardware, or other reasons. Since packet loss is rare or even non-existent in typical campus networks, this example server injects artificial loss to simulate the effects of network packet loss. The server creates a random integer variable that determines whether a particular input packet is lost or not.

### **EXECUTION**

Terminal for SERVER

`python3 udpping_server.py`

Terminal for CLIENT

`python3 udpping_client.py localhost 12000`

#### **AUTHOR**

- Giovane Hashinokuti Iwamoto - Computer Science student at UFMS - Brazil - MS

I am always open to receiving constructive criticism and suggestions for improvement in my developed code. I believe that feedback is an essential part of the learning and growth process, and I am eager to learn from others and make my code the best it can be. Whether it's a minor tweak or a major overhaul, I am willing to consider all suggestions and implement the changes that will benefit my code and its users.
