import socket
import time
import math

UDP_IP = "127.0.0.1"
UDP_PORT = 12321
PACKET_SIZE = 100
SEQ_NUM_LEN = 4
MESSAGE = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit.\n Aenean commodo ligula eget dolor. Aenean massa. \nCum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.\n Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim.\n Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu.\n In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo.\n Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi.\n Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus.\n Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet.\n Etiam ultricies nisi vel augue.Curabitur ullamcorper ultricies nisi.Nam eget dui. Etiam rhoncus."

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
data_size = (PACKET_SIZE - SEQ_NUM_LEN - 1)
packets_len = int(math.ceil(len(MESSAGE) / float(data_size)))
packets = [("{0:0"+str(SEQ_NUM_LEN)+"d}").format(packets_len - (i//data_size)-1) + "#" + MESSAGE[i:i+(data_size)] for i in range(0, len(MESSAGE), data_size)]
while True:
	print "\nclient starts sending the message to server"
	for p in packets:
		sock.sendto(p, (UDP_IP , UDP_PORT))
		print "\nclient sent packet no." ,int(p[:SEQ_NUM_LEN])
		time.sleep(1)
	print "\nclient finished to send the message to server."
	print "\nclient waits to receive message lines back from server"
	for i in range(len(MESSAGE.split('\n'))):
		data,addr = sock.recvfrom(10000)
		print "\nclient received line:", data
	print "\nclient received all data lines from server"
 	print "\nclient waits 3 seconds..."
	time.sleep(3)


