import subprocess
import socket
from time import sleep

class dynamic_ip:

	old_ip = "0.0.0.0"
	current_ip = "0.0.0.0"
	client_ips = []

	HOST = ''
	PORT = 50007
	conn = ''
	addr = ''
	s = None

	def __init__(self):
		self.old_ip = subprocess.check_output(["./get_ip.sh"])
		self.old_ip = self.old_ip.strip()
		self.current_ip = self.old_ip
		
		self.HOST = ''
		self.PORT = 50007
		self.conn = ''
		self.addr = ''

	def set (self, ip_address):

		if ip_address == self.current_ip:
			return True

		answer = subprocess.check_output(["./is_ip_reserved.sh", str(ip_address)])
		if not answer:
			subprocess.call(["./set_ip.sh", str(ip_address)])
			self.current_ip = str(ip_address)
			return True
		else:
			return False

	def setOldIp (self):
		subprocess.call(["./set_ip.sh", self.old_ip])
		self.current_ip = self.old_ip

### functions for sloop player only:

	def waitForConnections (self, num_clients):

		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.bind((self.HOST,self.PORT))
		connected = 0
		
		print "waiting for", num_clients, "to connect"

		while connected != int(num_clients):
			
			self.s.listen(1)
			self.conn, self.addr = self.s.accept()
			connected += 1
			self.client_ips.append(self.conn)
			print self.addr, "connected"

			self.conn = ''
			self.addr = ''	

		print "All ready!"

		return True

	def sendStartSignal (self):
		if len(self.client_ips) == 0:
			return True
		else:
			for ip in self.client_ips:
				print "sending signal"
				ip.sendall("1")

	def connectToServer (self):
		self.HOST = self.current_ip
		self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.s.connect((self.HOST,self.PORT))
		self.s.sendall("ready")
		
	def waitForStartSignal(self):
		self.data = self.s.recv(1024)
		
		if repr(self.data) == "1":
			self.data = ''
			return True
		else:
			self.data = ''
			return False

	def closeConnection (self):
		self.s.close()
