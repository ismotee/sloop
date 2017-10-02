from sl_settings import Settings
import os

if __name__ == "__main__":
	settings = Settings("settings")
	
	ismaster = raw_input("Server or Client (s/C): ")
	if ismaster == 's':
		settings.Set('master', True)
		settings.Set('master_name', "localhost")
		num_clients = raw_input("how many clients: ")
		if int(num_clients):
			settings.Set('num_clients',num_clients)
	else:
		settings.Set('num_clients','0')
		settings.Set('master', False)
		mastername = raw_input("define server hostname: ")
		if not mastername:
			settings.Set('master_name', "sloopServer")
		else:
			settings.Set('master_name', mastername)

	settings.tell()
