import sl_settings
import os

import time
from time import sleep
from omxplayer.player import OMXPlayer
from dynamic_ip import dynamic_ip

def error (id):
	error = {
		1: "no sloop.config found. Run sloop-setup first.",
		
	}
	print "error:", error.get(id, "no reason")

if __name__ == "__main__":

#loading settings from setup.config
	settings = sl_settings.Settings()
	if not settings.load():
		error(1)

	ip_setup = dynamic_ip()
	ip_setup.set(settings.get("ip_address"))
	
	plr = OMXPlayer(settings.get("file_name"))

	if settings.get("ismaster") == "True":
		if ip_setup.waitForConnections(settings.get("num_clients")):
			ip_setup.sendStartSignal()
	else:
		ip_setup.connectToServer()
		ip_setup.waitForStartSignal()
		print "this function is not ready yet"
		### TODO: error check 
	#loop_time = plr.duration() - float(settings.get("load_time"))
	plr.play()
	
	while True:
		if settings.get("ismaster") == "False":
			ip_setup.waitForStartSignal()
			plr.set_position(0)
		elif settings.get("ismaster") == "True":
			sleep(plr.duration() - 1.0)
			#sleep(6)
			ip_setup.sendStartSignal()
			plr.set_position(0)

	ip_setup.closeConnection()

	#plr.stop()

	ip_setup.setOldIp()
