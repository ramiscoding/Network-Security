#!/usr/bin/python

import sys
from scapy.all import *

user_input = raw_input("Enter IP address : ")
ip_pkt = IP(dst=user_input,ttl=(1,25),id=RandShort())/TCP(flags=0x2)
ans_reply,unans_reply = sr(ip_pkt)

for snd,rcv in ans_reply:
  print snd.ttl, rcv.src, isinstance(rcv.payload, TCP)


