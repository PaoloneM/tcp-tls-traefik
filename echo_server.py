# Echo server program
import socket
import os
from _thread import *

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
thread_count = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
print('Waiting for a Connection..')
s.listen(5)

def threaded_client(conn, addr):

  print('Connected by ', addr)
  
  while 1:
    data = conn.recv(1024)
    if not data: break
    conn.sendall(data)
    
  print('Closing connection')
  conn.close()

while True:
    Client, address = s.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, address))
    thread_count += 1
    print('Thread Number: ' + str(thread_count))
    
s.close()