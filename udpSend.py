import socket

udpHostname = "127.0.0.1"
udpPort = 5005
message = "Hello,World!"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((udpHostname,udpPort))
