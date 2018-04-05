
import mumble_bot
import cberry
import time

last_event_counter=0

def main():

	global last_event_counter
	berry =None	
	
	while True:
	
	
		online_users= mumble_bot.read_Online_Users()# set  event_counter
		registeredUsers= mumble_bot.read_Registered_Users()
		
		one_user_online=False	

		#check if a user is loged in		
		for user in online_users:
			
			#print(user+" "+str(online_users[user]))		
			if online_users[user].event_counter%2!=0:
				one_user_online=True
	
		if  last_event_counter != mumble_bot.event_counter and len(online_users)!=0:	#there is a user stat change	


			last_event_counter = mumble_bot.event_counter;#reset event counter
			#*****************************************************
			#********** c-berry part******************************
			#*****************************************************		
			
			
			if berry==None:							
				berry=cberry.Cberry()
				berry.turn_screen_on()
				cert_exp=mumble_bot.get_cert_validity()
				ip=mumble_bot.getIP()			
			
	
			berry.print_on_screen(online_users,ip,cert_exp)#update screen in any case
			
			#write to display
			if(one_user_online==False):#there aren't online users	
				berry.turn_screen_off()
				berry=None
	
		time.sleep(1)

		
if __name__ == '__main__':
    main()