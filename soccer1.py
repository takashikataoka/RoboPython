from socket import *
import sys


HOST = 'localhost'
ADRESS = "127.0.0.1"
PORT = 53020

s =socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
s.bind((HOST, PORT))

while True:
    msg = raw_input("> ")
    s.sendto(msg, (ADDRESS, PORT))
    if msg == ".":
        break

s.close()
sys.exit()
