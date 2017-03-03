#!/usr/bin/python

import sys
from scapy.all import *

user_input = raw_input("Enter IP address : ")
icmp_pkt = IP(dst=user_input)/ICMP()
icmp_pkt.show()
reply = sr(icmp_pkt)
print reply
