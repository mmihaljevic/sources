#!/usr/bin/python

__author__= 'Melita Mihaljevic'
__date__= '2011'

# uses pywurfl module http://pypi.python.org/pypi/pywurfl
#
# usage: python mobile_devices_engine.py <arguments>
#
# possible arguments:
# (1)  um <model_name> <file_name>   - find all userAgent for given model
# (2)  devOS <device_os> <file_name> - find devices that run specific OS
# (3)  generate <file_name>          - generate UA data
# (4)  detect <user_agent>           - detect device based on userAgent

from wurfl import devices
from  pywurfl.algorithms import TwoStepAnalysis
import sys

class UAManager:
	
	def __init__(self):
		""""""
		pass	

	def findAllUAforModel(self,model_name,filename=None):
		uA_list = []
		for device in devices.devids.values():
			if device.model_name.lower() == unicode(model_name).lower():
				uA_list.append(device.devua)
		
		if(filename):
			with open(filename, "w") as f:
				for user_agent in uA_list:
					f.write((user_agent + "\n").encode("utf-8"))

		else:
			for user_agent in uA_list:
				print user_agent

	def findDeviceDataforOS(self,device_os,filename=None):
		uA_list = []
		for device in devices.devids.values():
			if device.device_os.lower() == unicode(device_os).lower():
				uA_list.append([device.brand_name,device.model_name,device.devua])

		if(filename):
			with open(filename, "w") as f:
			  for device_data in uA_list:
				dev_data = device_os + "$" + device_data[1] + "$" + device_data[2] + "\n"
				f.write(dev_data.encode("utf-8"))
		
		else:
			for device_data in uA_list:
				print device_os + "$" + device_data[1] + "$" + device_data[2]

	def generateUAListWithAndroid(self,filename):
		brand = ""
		device_DF = []
		for device in devices.devids.values():
			if device.device_os.lower() == u"android":
				brand = "Android"
			else:
				brand = device.brand_name
			device_data = brand + "$" + device.model_name + "$" + device.devua + "\n"
			device_DF.append(device_data)
		
		with open(filename, "w") as f:
			for device_data in device_DF:
				f.write(device_data.encode("utf-8"))	

	def detectMobileByUA(self,user_agent):
		search_algorithm = TwoStepAnalysis(devices)
		device = devices.select_ua(unicode(user_agent), search=search_algorithm)
	
		print device

user_manager = UAManager()
file_name = None 
if len(sys.argv)<2:
	print "wrong parms"
	sys.exit(-1)

if sys.argv[1] == "um":
	model_name = sys.argv[2]
	if len(sys.argv) == 4:
		file_name = sys.argv[3]
	user_manager.findAllUAforModel(model_name,file_name)

elif sys.argv[1] == "devOS":
	device_os = sys.argv[2]
	if len(sys.argv) == 4:
		file_name = sys.argv[3]
	user_manager.findDeviceDataforOS(device_os, file_name)

elif sys.argv[1] == "generate":
	file_name = sys.argv[2]
	user_maneger.generateUAListWithAndroid(file_name)

elif sys.argv[1] == "detect":
	user_agent = sys.argv[2]
	user_manager.detectMobileByUA(user_agent)

else:
	print "could not recognise action"
	sys.exit(-1)

