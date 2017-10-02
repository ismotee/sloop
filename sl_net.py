import socket
import time

class sl_net:


	def __init__(self):
		self.connected = False
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.conn = None
		self.connections = []
		self.addr = None
		self.server = False
		self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	def send(self, msg):

		if self.server and self.connected:
			for connection in self.connections:
				connection.sendall(msg)
		elif self.connected:
			self.sock.sendall(msg)
		else: 
			print("not connected")
	
	def connect_as_client(self, address,port):
	# connection loop
		while not self.connected:
		    try:
				self.sock.connect((address,port))
				self.connected = True
		    except:	
				print 'Waiting for the server'
				time.sleep(2)

	def wait_for_clients(self, num_clients,port):
		self.sock.bind(('',port))
		self.server = True
		num_connections  = 0
		print 'Waiting for connections'
		while num_connections != num_clients:
			self.sock.listen(5)
			num_connections += 1
			self.conn, self.addr = self.sock.accept()
			self.connections.append(self.conn)
			print socket.gethostbyaddr(self.addr[0])[0], " connected!"
			print "waiting for ", str(num_clients - num_connections), " to connect"
		print "all ready!"
		self.connected = True

	def receive(self):

		if self.server:
			data = ''
			while data == '' or data == 0:
				data = self.conn.recv(16)
			return data
		else:
			data = ''
			while data == '' or data == 0:
				data = self.sock.recv(16)
			return data

	def close(self):
		if not self.server:
			self.sock.close()
		else:
			self.conn.close()
			self.sock.close()
