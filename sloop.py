#!/usr/bin/python
from sl_settings import Settings
from sl_net import sl_net
import time
#from omxplayer.player import OMXPlayer

settings = Settings("settings")
net = sl_net()
#plr = OMXPlayer(settings.Get('path'),["--blank","--no-osd"])

#yhdistetaan
# serveri
settings.tell()
if settings.Get('master'):
	net.wait_for_clients(settings.Get('num_clients'),5005)
#clientti
else:
	net.connect_as_client(settings.Get('master_name'),5005)

#eka kierros
if settings.Get('master'):
	net.send('start')
	print('plr.play()')
else:
	msg = net.receive()
	if(msg == 'start'):
		print('plr.play()')

while True:
	try:
		if settings.Get('master'):
			#time.sleep(plr.duration()-1.5)
			time.sleep(10)			
			net.send('restart')
			print('plr.set_position(0)')
		else:
			msg = net.receive()
			if(msg == 'restart'):
				print('plr.set_position(0)')

	except KeyboardInterrupt:
		print "interrupted!"
		net.close()
		#plr.stop()
		#plr.quit()
		break
			
