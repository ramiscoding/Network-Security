#!/usr/bin/python

import sys
from scapy.all import *

user_input = raw_input("Enter IP address : ")
for i in range(100):
  ip_pkt = IP(dst=user_input)/TCP(sport=i,dport=139,flags="S")
  send(ip_pkt)
  print "TCP connection:%d",i

