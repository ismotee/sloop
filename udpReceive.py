import socket
import io

class server:

	list_of_hostnames = []
	connected_hosts = []
	num_hosts = 0

	sock = None	
	port = 5005

	def __init__(self):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind(('localhost',self.port))
		with open("hostnames", "r") as f:
			self.list_of_hostnames = f.read().splitlines()
		self.num_hosts = len(self.list_of_hostnames)

	def waitForConnections(self):
		connections = 0
		print "waiting for connections"
		while connections != self.num_hosts:
			self.sock.listen(1)
			self.conn, self.addr = self.sock.accept()
			connections += 1
			self.connected_hosts.append(socket.gethostbyaddr(self.addr[0])[0])
			print self.connected_hosts[-1], "connected"
			print "waiting for ", str(self.num_hosts - connections), " to connect"
		print "All ready!"

if __name__ == "__main__":
	srv = server()
	srv.waitForConnections()

