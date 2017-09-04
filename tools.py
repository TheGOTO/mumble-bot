 

import subprocess
import objects
 
 #call a cmd
def runCmd(cmd):
	ret=""
	
	p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	for line in p.stdout.readlines():		
		p.wait()
		ret+=line.decode("utf-8")
	
	return ret[:-1]#cut \n
	
	
 #get all registered users
def read_Registered_UsersV2():   
	mRegistered_users=[]
	query= "sqlite3 /var/lib/mumble-server/mumble-server.sqlite 'SELECT name, lastchannel,last_active FROM users'"

	p = subprocess.Popen(query, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	for line in p.stdout.readlines():		
		p.wait()	
		line=line[:-1]#cut \n at the end	
		
		
		line_array= str.split(line.decode('utf-8'),'|')#decode byte to str
		
		new_user = objects.User(line_array[0],line_array[1],line_array[2],0)
		
		mRegistered_users.append(new_user)		

	return mRegistered_users

def read_channels():   
	channels={}
	query= "sqlite3 /var/lib/mumble-server/mumble-server.sqlite 'SELECT channel_id,name FROM channels'"

	p = subprocess.Popen(query, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	for line in p.stdout.readlines():		
		p.wait()	
		line=line[:-1]#cut \n at the end		
		line_array= str.split(line.decode('utf-8'),'|')#decode byte to string
		channels[line_array[0]]=line_array[1]

	return channels
