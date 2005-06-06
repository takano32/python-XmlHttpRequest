#! /usr/bin/env python
# Echo client program
import socket

class SimpleClient:
  def __init__(self, host, port):
    self.host = host
    self.port = port
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  def connect(self):
    opt = (self.host, self.port)
    self.socket.connect(opt)

  def send(self, message):
    self.socket.send(message)

  def recv(self):
    data = list()
    ch = self.socket.recv(1)
    while( ch != "\x01" and ch != "\x00"):
      data.append(ch)
      ch = self.socket.recv(1)
    return "".join(data)

  def close(self):
    self.socket.close()


client = SimpleClient('localhost', 7070)
client.connect()
print 'Received'
client.send("""
<imc>
<login id="mino01" domain="example.com" pass="mino01"/>
</imc>\0
""")
print client.recv()
client.send("secound step")
print client.recv()


