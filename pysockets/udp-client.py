#!/usr/bin/env python

import socket
import time

# send to multicast by selecting multicast addr
addr="ohm:7777"
addr="schrute:7777"
addr="239.239.239.7:7777"

(host,port)=addr.split(':')
port=int(port)

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 12)

x=0
while True:
    x+=1
    msg = "hello tbs %d"%(x)
    print msg,host,port
    sock.sendto(msg,(host,port))
    time.sleep(1)
