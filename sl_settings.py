from __future__ import print_function
import os
class Settings:

	settings = {'master':False,'num_clients':2, 'master_name':'', 'path':'videos/video'}
	fileName = ''

	def __init__(self,file): #reading settings from a file in constructor
		if os.path.isfile(file):
			with open(file, "r") as f:
				lines = f.read().splitlines()
				if(len(lines) == 3):
					self.settings['master'] = lines[0]
					self.settings['num_clients'] = lines[1]
					self.settings['master_name'] = lines[2]
					self.settings['path'] =  lines[3]
			self.fileName = file


	def tell(self):
		print (self.settings)

	def Get(self, key):
		return self.settings[key]

	def Set(self,key, value):
		self.settings[key] = value

	def save(self):
		with open(self.fileName,"w") as f:
			print(str(self.settings['master']), file=f) 
			print(str(self.settings['master_name']), file=f)
			print(str(self.settings['num_clients']), file=f)
			print(str(self.settings['path']), file=f) 

