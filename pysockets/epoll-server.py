#!/usr/bin/python
# http://www.codexon.com/posts/debunking-the-erlang-and-haskell-hype-for-servers

import select
import socket
 
EPOLLIN = select.EPOLLIN
EPOLLOUT = select.EPOLLOUT
 
epoll = select.epoll(60000)
connections = {}
 
class Server(object):
    def __init__(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.setblocking(0)
        sock.bind(('', 8050))
        sock.listen(60000)
        self.socket = sock
 
        fileno = sock.fileno()
        connections[fileno] = self
        epoll.register(fileno, EPOLLIN)
 
    def onInput(self):
        sock, address = self.socket.accept()
        Client(sock)
 
class Client(object):
    input  = ''
    output = "HTTP/1.0 200 OK\r\nContent-Length: 5\r\n\r\nPong!\r\n"
 
    def __init__(self, sock):
        sock.setblocking(0)
        fileno = sock.fileno()
        epoll.register(fileno, EPOLLIN|EPOLLOUT)
        connections[fileno] = self
        self.socket = sock
 
    def onInput(self):
        newdata = self.socket.recv(1024)
        if len(newdata) is 0:
            self.close()
        self.input += newdata
 
    def onOutput(self):
        sent = self.socket.send(self.output)
        self.output = self.output[sent:]
        if len(self.output) is 0:
            self.close()
 
    def close(self):
        fileno = self.socket.fileno()
        del connections[fileno]
        epoll.unregister(fileno)
        self.socket.close()
 
Server()
 
while 1:
    for fd, event in epoll.poll():
        if event & EPOLLIN:
            connections[fd].onInput()
 
        if event & EPOLLOUT:
            connections[fd].onOutput()
