
class User:
	
	name=""
	event_counter=0
	last_event=""

	def __init__(self, name,event_counter, last_event):
		self.event_counter = event_counter
		self.last_event = last_event
		self.name=name

	def __str__(self):
		return self.name+" "+self.last_event+" "+str(self.event_counter)
