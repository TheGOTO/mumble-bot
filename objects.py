class User:

	name=""
	lastchannel=""
	last_active=""
	event_counter=0
	
	def __init__(self,name,lastchannel,last_active,event_counter): 
		self.event_counter = event_counter 
		self.name=name
		self.lastchannel=lastchannel
		self.last_active=last_active


		
