from scapy.all import *
import sys
SEQ_NUM_LEN = 5

def print_packet(p):
	pl = str(p[UDP].payload)
	print p.sprintf("\n%IP.src%:%UDP.sport% -> %IP.dst%:%UDP.dport%")
	print "data:",pl

sniff(filter="udp and host 127.0.0.1",prn=print_packet)
