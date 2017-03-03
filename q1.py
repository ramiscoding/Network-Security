#!/usr/bin/python

import sys
from scapy.all import *

user_input = raw_input("Enter IP address : ")
ip_pkt = IP(dst=user_input)
tcp_pkt = TCP(dport=[80,53])
#l2_pkt = Ether()/ip_pkt
My_pkts = [p for p in ip_pkt]
del My_pkts[0]
del My_pkts[-1]
#print My_pkts
for p in My_pkts:
  final_pkt = p/tcp_pkt
  final_pkt.show()
