# Echo client program
import socket

HOST = 'localhost'    # The remote host
PORT = 7070              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.send("""
<imc>
<login id="mino01" domain="example.com" pass="mino01"/>
</imc>\0
""")

data = s.recv(1024)

s.close()
print 'Received', repr(data)



class SimpleClient():
  def __init__(self, host, port):
    self.host = host
	 self.port = port
	 self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  def connect():
	 self.socket.connect(self.host, self.port)

  def send(message):
    sock = self.socket
    sock.send(message)
	 data = list()
	 while( ch = sock.recv(1)):
	   data.append(ch)
	 return "".join(data)

  def close():
    self.socket.close()



