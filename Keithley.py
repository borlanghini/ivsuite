import sys
import visa

class K2400Series():
	
	"""Keithley 2400 instrument class. """
	RQS = (1<<11)
	SRQ = (1<<12)
	TIMO = (1<<14)

	def __init__(self, address = 24):
		self.address = address
		self.myOS = sys.platform.lower()  #define OS
		
		if self.myOS.startswith('win'):
			#using the windows VISA library from NI as backend
			rm = visa.ResourceManager()
		elif self.myOS.startswith('linux'):
			#using the new backend pyvisa-py in linux announced in 
			# http://python-in-the-lab.blogspot.it/2014/10/communicating-with-instruments-using.html
			#and as pyvisa-py relies on linux-gpib for GPIB it allows me to use only pyvisa to control
			rm = visa.ResourceManager('@py')
			
		self.ctrl = rm.open_resource("GPIB::{0:d}".format(self.address))
		
	def write(self, string):
		self.ctrl.write(string)
		
	def read(self):
		return self.ctrl.read()
		
	def wait_for_srq(self, wait_timeout = 25000):
		self.ctrl.wait_for_srq(wait_timeout)
		
	def gpib_ask(self):
		return self.ctrl.query_ascii_values(":trace:data?")
	
	def reset(self):
		""" Resets the instrument. """
		self.ctrl.write(":syst:pres; *RST; *CLS") # reset equipment
		self.ctrl.write(":sens:func:conc off")  # Turn off concurrent functions
		self.ctrl.write(":trace:feed:cont never") 
		
	def outputoff(self):
		self.ctrl.write(":OUTP OFF")
		
	def outputon(self):
		self.ctrl.write(":OUTP ON")
		
		
