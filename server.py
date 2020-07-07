import socket

UDP_IP = "0.0.0.0"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

x = 0

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:",  data, x
    x += 1