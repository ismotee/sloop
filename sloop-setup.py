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

def info (key):
	print key , "set to", settings.get(key)

def isInt (trans):
	try:
		int(float(trans))
		return True
	except:
		return False

def toInt (trans):
	return int(float(trans))

def videoTest(file_name):
	try:
		start_time = time.time()
		plr = OMXPlayer(file_name)
		plr.stop()
		return time.time() - start_time
	except:
		print "could not load file", file_name	
		return -1
		# use -1 for error handling

if __name__ == "__main__":
	settings = sl_settings.Settings()
	if not settings.load():
		print "no config file. Loading defaults."


## Ask Client or Server
	ismaster = raw_input("Server/Client? [s/C] ")

	if ismaster == 's':
### if server, ask number of clients
		settings.set("ismaster", True)

		num_clients = raw_input("number of clients: ")
		
		if isInt(num_clients):
			int_clients = toInt(num_clients)
			settings.set("num_clients", int_clients)
		else:
			print "answer is not a number. Setting default."
			settings.set("num_clients", 0)
	else:
		settings.set("ismaster", False)

	info ("ismaster")
	info ("num_clients")
	

### find video
	path = raw_input("path and name of the video file: ")
	
	if os.path.isfile(path):
### video test
		load_time = videoTest(path)
		if load_time != -1:
			settings.set("file_name", path)
			settings.set("load_time", load_time)
		else:
			print "could not open a media file"

	else:
		print "File not found. Setting path to latest file."

	info("file_name")
	info("load_time")

# TODO: Setup connection
# set ip address
# handle stderr when is_ip_reserved says no 
	ip_setup = dynamic_ip()
	ip_setup.set("192.168.2.200") # using this address to access to the same address family
	if settings.get("ismaster") == "True":
		while not ip_setup.set("192.168.2.100"):
			print "ip_address reserved. Change other devices to client"
			sleep(1)
		settings.set("ip_address", "192.168.2.100")
	elif settings.get("ismaster") == "False":
		i = 101
		while not ip_setup.set("192.168.2." + str(i)):
			i = i + 1
			if i > 254:
				print "couldn't find network."
				break;
		else:
			settings.set("ip_address", "192.168.2."+str(i))

	info("ip_address")
# TODO: Ask if user wants setup program to start on startup
	print "setup is now complete"
	ip_setup.setOldIp()
	settings.save()
