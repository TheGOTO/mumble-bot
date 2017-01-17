#https://github.com/azlux/pymumble-> PYMUMBLE python library


import os
import subprocess
import time
import cberry
import telegram
import thread 
import tools
import Objects


event_counter=0
last_event_counter=0


# THIS IS THE MAIN ROUTINE --. START OF THE PROGRAM
def main():
		
	global last_event_counter
	global event_counter
	
	one_minute=60000/1000#seconds
	one_second=one_minute/60

	berry =None	
	
	if os.getuid() != 0:
		print("This program is not run as sudo or elevated this it will not work")
		exit()	
		
	thread.start_new_thread(telegram.start,())	
	print("start mumble_bot")

	delay=one_second#init delay

	while True:

		time.sleep(delay);#wait in the release version	

		online_users= read_Online_Users()
		registeredUsers= read_Registered_Users()
			
		one_user_online=False				
		
			

		#check if a user is loged in		
		for user in online_users:		
			#print(user+" "+str(online_users[user]))		
			if online_users[user]%2!=0:
				one_user_online=True

				
		#write to std out or whatsapp
		if  last_event_counter != event_counter and len(online_users)!=0:	#there is a user stat change		
			message=""
			delay=one_minute*5;#wait with the next check 5 minutes		

			#*****************************************************
			#********** telegram part****************************
			#*****************************************************
			
			#iterate over online users			
			for user in online_users:	
				if user in registeredUsers.keys():#user is registered
					#compute message
					if online_users[user] % 2 != 0:						
						message+=user+"\t"+ u'\U00002705'+"\n"#online
					else:						
						message+=user+"\t"+ u'\U0000274C'+"\n"#offline

			if message!="":#a registered user is online
				message="*****************\nPbtH-MumbleV2\n*****************\n"+message#add message to whats app command				
				#print(message.encode("utf-8").expandtabs())				
				telegram.send_message(message.encode("utf-8").expandtabs(16))

			last_event_counter = event_counter;#reset event counter


			#*****************************************************
			#********** c-berry part******************************
			#*****************************************************		
			
			if berry==None:				
				berry=cberry.Cberry()
				berry.turn_screen_on()

			cert_exp=get_cert_validity()
			ip=getIP()			
				
				
			berry.print_on_screen(online_users,ip,cert_exp)#update screen in any case
			
			#write to display
			if(one_user_online==False):#there aren't online users	
				berry.turn_screen_off()
				berry=None
		else:
			delay=one_second#reset delay
				


def get_cert_validity():
#	cert_exp=tools.runCmd("openssl x509 -in /etc/letsencrypt/live/dom.pbth.de/cert.pem -noout -dates | grep 'notAfter'")				
	cert_exp=tools.runCmd("openssl s_client -connect dom.pbth.de:64738 -showcerts </dev/null 2>/dev/null|openssl x509 -dates -noout | grep 'notAfter'")				
	start = cert_exp.find("=")+1
	return cert_exp[start:]#cut first part
			
 #get ip
def getIP():	
	return tools.runCmd('ifconfig eth0 | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1')




 #get all registered users
def read_Registered_Users():   
	mRegistered_users={}
	query= "sudo sqlite3 /var/lib/mumble-server/mumble-server.sqlite 'SELECT name FROM users'"

	p = subprocess.Popen(query, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	for user in p.stdout.readlines():		
		p.wait()		
		user=user[:-1].decode("utf8")#cut \n at the end		
		mRegistered_users=increase_by_one(mRegistered_users,user)		
		

	return mRegistered_users
	
	

 
def read_Online_Users():  
	global event_counter
	event_counter=0#reset event counter
	online_users={}

	server_start_date = tools.runCmd("sqlite3 /var/lib/mumble-server/mumble-server.sqlite 'SELECT msgtime FROM slog WHERE msg LIKE \"%Server listening on%\" ORDER BY msgtime desc LIMIT 1'")
		
	query= "sqlite3 /var/lib/mumble-server/mumble-server.sqlite 'SELECT * FROM slog  WHERE msgtime >=Datetime(\""+server_start_date+"\")' | grep 'Authenticated\\|Connection\\|Rejected'"
	
	p = subprocess.Popen(query, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	for line in p.stdout.readlines():	
			
		p.wait()
		sline=line.decode("utf-8") 
		start = sline.find(":")+1
		stop = sline.find(">")
		if start <0 or stop <0:
			continue	

		substring=sline[start:stop]	
		stop= substring.rfind('(')		
		user=substring[:stop]
		
		if user!="":#user had a disconnect bevore authentication				
			online_users=increase_by_one(online_users,user)			
			event_counter=event_counter+1#update global event counter
		
		
	return online_users

def increase_by_one(dict,key):
	counter=1#default case 
	if key in dict.keys():# key is in dict		
		counter=dict[key]+1;# get the value and increase			
	dict[key]=counter;#update counter
	return dict


if __name__ == '__main__':
    main()



