import os
import pickle

class Settings:
	# name, master/slave, number of clients, ipaddress, video path, load time 
	def __init__(self):
		self.SETTINGS_LIST = ['noname','False','0','192.168.2.200','video/test.mov','0.0'];
		

	def load(self):
		if os.path.isfile("/home/pi/sloop/sloop.config"):
			f = open("/home/pi/sloop/sloop.config", 'rb')
			self.SETTINGS_LIST = pickle.load(f)
			f.close()
			return True
		else:
			return False

	def save(self):
		f = open("/home/pi/sloop/sloop.config", 'wb')
		#turnicate()
		#f.writelines(self.SETTINGS_LIST)
		pickle.dump(self.SETTINGS_LIST, f)
		f.close()

	def set (self, property, value):
		if property == "NAME" or property == "name":
			self.SETTINGS_LIST[0] = str(value)
			#self.SEETINGS_LIST.remove(1)
		elif property == "ISMASTER" or property == "ismaster":
			self.SETTINGS_LIST[1] = str(value)
			#self.SETTINGS_LIST.remove(2)
		elif property == "NUM_CLIENTS" or property == "num_clients":
			self.SETTINGS_LIST[2] = str(value)
		elif property == "IP_ADDRESS" or property == "ip_address":
			self.SETTINGS_LIST[3] = str(value)
		elif property == "FILE_NAME" or property == "file_name":
			self.SETTINGS_LIST[4] = str(value)
		elif property == "LOAD_TIME" or property == "load_time":
			self.SETTINGS_LIST[5] = str(value)
		else:
			print "invalid property name"

	def get (self, property):
		if property == "NAME" or property == "name":
			return self.SETTINGS_LIST[0]
		elif property == "ISMASTER" or property == "ismaster":
			return self.SETTINGS_LIST[1]
		elif property == "NUM_CLIENTS" or property == "num_clients":
			return self.SETTINGS_LIST[2]
		elif property == "IP_ADDRESS" or property == "ip_address":
			return self.SETTINGS_LIST[3]
		elif property == "FILE_NAME" or property == "file_name":
			return self.SETTINGS_LIST[4]
		elif property == "LOAD_TIME" or property == "load_time":
			return self.SETTINGS_LIST[5]
		else:
			print "invalid property name"

