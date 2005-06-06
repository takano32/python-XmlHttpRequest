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





