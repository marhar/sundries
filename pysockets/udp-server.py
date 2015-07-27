#!/usr/bin/env python
"""
sample code for a udp receiver.
works with multicast if specified with a multicast address
"""

import sys
import socket
import struct

def ismulticast(mreq):
    """is this address a multicast address?"""
    # -- yes if bits 0-3 are 1110
    return ord(mreq[0]) & 0xf0 == 0xe0

def main():

    bufsz=4096
    addr=sys.argv[1] # e.g.  tbs:7777,schrute:7777,239.239.239.7:7777,:7777

    (host,port)=addr.split(':')
    port=int(port)

    mreq=struct.pack("4sl",socket.inet_aton(socket.gethostbyname(host)),
                               socket.INADDR_ANY)
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    if ismulticast(mreq):
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    sock.bind(('',port))

    while True:
        (msg,sender)=sock.recvfrom(bufsz)
        print sender,msg
        # you can reply to sender if you like
        #s.sendto("hello",sender)

main()
