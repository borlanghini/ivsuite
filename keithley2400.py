import visa

class K2400Series():
	
	"""Keithley 2400 instrument class. """
	RQS = (1<<11)
	SRQ = (1<<12)
	TIMO = (1<<14)

	def __init__(self, address = 24):
		rm = visa.ResourceManager()
		self.ctrl = rm.open_resource("GPIB:: %" % address)
		
	def write(self, string):
		self.ctrl.write(string)
		
	def wait_for_srq(self, wait_timeout = 25000):
		self.ctrl.wait_for_srq(wait_timeout)
		
	def gpib_ask(self):
		return self.ctrl.query_ascii_values(":trace:data?")
	
	def reset(self):
		""" Resets the instrument. """
		self.ctrl.write(":syst:pres; *RST; *CLS") # reset equipment
		self.ctrl.write(":sens:func:conc off")  # Turn off concurrent functions
		self.ctrl.write(":trace:feed:cont never") 
		
