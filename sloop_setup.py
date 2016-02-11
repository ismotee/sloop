#!/usr/bin/env python
#settings container class
import sl_settings
#for everything
import os
#for videotest
import time
from time import sleep
from omxplayer.player import OMXPlayer
#interface for setting up ip address
from dynamic_ip import dynamic_ip

class sloop_setup:
	def info (self, key):
		print key , "set to", self.settings.get(key)

	def isInt (self,trans):
		try:
			int(float(trans))
			return True
		except:
			return False

	def toInt (self, trans):
		return int(float(trans))

	def videoTest(self, file_name):
		try:
			start_time = time.time()
			plr = OMXPlayer(file_name)
			plr.stop()
			return time.time() - start_time
		except:
			print "could not load file", file_name	
			return -1
			# use -1 for error handling

	def __init__(self):
		self.settings = sl_settings.Settings()
		if not self.settings.load():
			print "no config file. Loading defaults."


## Ask Client or Server
		ismaster = raw_input("Server/Client? [s/C] ")

		if ismaster == 's':
### if server, ask number of clients
			self.settings.set("ismaster", True)

			num_clients = raw_input("number of clients: ")
		
			if self.isInt(num_clients):
				int_clients = self.toInt(num_clients)
				self.settings.set("num_clients", int_clients)
			else:
				print "answer is not a number. Setting default."
				self.settings.set("num_clients", 0)
		else:
			self.settings.set("ismaster", False)

		self.info ("ismaster")
		self.info ("num_clients")
	

### find video
		path = raw_input("path and name of the video file: ")
	
		if os.path.isfile(path):
### video test
			load_time = self.videoTest(path)
			if load_time != -1:
				self.settings.set("file_name", path)
				self.settings.set("load_time", load_time)
			else:
				print "could not open a media file"

		else:
			print "File not found. Setting path to latest file."

		self.info("file_name")
		self.info("load_time")

# TODO: Setup connection
# set ip address
# handle stderr when is_ip_reserved says no 
		ip_setup = dynamic_ip()
		ip_setup.set("192.168.2.200") # using this address to access to the same address family
		if self.settings.get("ismaster") == "True":
			while not ip_setup.set("192.168.2.100"):
				print "ip_address reserved. Change other devices to client"
				sleep(1)
			self.settings.set("ip_address", "192.168.2.100")
		elif self.settings.get("ismaster") == "False":
			i = 101
			while not ip_setup.set("192.168.2." + str(i)):
				i = i + 1
				if i > 254:
					print "couldn't find network."
					break;
			else:
				self.settings.set("ip_address", "192.168.2."+str(i))	

		self.info("ip_address")
# TODO: Ask if user wants setup program to start on startup
		print "setup is now complete"
		ip_setup.setOldIp()
		self.settings.save()
