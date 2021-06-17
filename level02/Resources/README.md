- on crée un script qui print la data de tout les paquets
```
from scapy.all import *

scapy_cap = rdpcap('level02.pcap')
for packet in scapy_cap:
	if type(packet[TCP].payload) == scapy.packet.Raw:
		print(packet[TCP].payload.load.decode())
```
- Le retour
```
42 : Password: 
44 : f
46 : t
48 : _
50 : w
52 : a
54 : n
56 : d
58 : r
60 : <DEL> 
62 : <DEL> 
64 : <DEL> 
66 : N
68 : D
70 : R
72 : e
74 : l
76 : <DEL>
78 : L
80 : 0
82 : L
```
- password: `ft_waNDReL0L`
- flag: `kooda2puivaav1idi4f57q8iq`
