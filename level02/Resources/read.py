from scapy.all import *

scapy_cap = rdpcap('level02.pcap')
i = 0
for packet in scapy_cap:
	if type(packet[TCP].payload) == scapy.packet.Raw:
		try:
			print(i, ':', packet[TCP].payload.load.decode())
		except:
			print(i, ':', packet[TCP].payload.load)
	i += 1
