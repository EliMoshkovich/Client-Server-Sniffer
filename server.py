import socket
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 12321
SEQ_NUM_LEN = 4
msg = ""
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

print "server started to listen on port " , UDP_PORT
while True:
	msg=""
	data, addr = sock.recvfrom(100) 
	print "server starts to recive data from ", addr[0], ":" , addr[1]
	print "\nserver received packet no.", int(data[:SEQ_NUM_LEN])
	msg+=data[SEQ_NUM_LEN+1:]
	while int(data[:SEQ_NUM_LEN]):
		data, addr = sock.recvfrom(100) 
		msg+=data[SEQ_NUM_LEN+1:]
		print "\nserver received packet no.", int(data[:SEQ_NUM_LEN])
	print "\nserver starts to echo the data lines back"
	for m in msg.split('\n'):
		sock.sendto(m, addr)
		print "\nserver echoed",m
		time.sleep(1)

