import sys
import telepot
import urllib3
import time
import datetime 
import tools
import cberry
from telepot.loop import MessageLoop
import mumble_chat
import subprocess   
import logging
import multiprocessing

	
bot=None 
token='237430124:AAF9frMQCMB-5K1JmrQNQZs7f5Ervn7-9rE'
chat_id_pbth_group=-176357162
chat_id_goto=263478717
default_chat_id=0

def init(mode):
	global bot
	global default_chat_id
	if bot==None:
		bot = telepot.Bot(token)	
		
	if mode == "release":
		default_chat_id=chat_id_pbth_group
	else:
		default_chat_id=chat_id_goto
		logging.getLogger().setLevel(logging.DEBUG)
		logging.debug('hi from the logger!')

	logging.debug(default_chat_id)	
	
	MessageLoop(bot, {'chat': handle}).run_as_thread()


def send_message(msg,chat_id=0):
	if not chat_id:#set to default
		chat_id=default_chat_id

	logging.debug(msg)		
	bot.sendMessage(chat_id, msg)
	
def send_image_thread(chat_id,file):
	bot.sendPhoto(chat_id,file)
	
def send_image(path,chat_id=0):
	
	logging.debug("sending now")	
	
	if not chat_id:#set to default
		chat_id=default_chat_id
	
	file=open(path, 'rb')# open in read byte mode
	
	logging.debug(file)
	
	
	#**********send with time out**************************
	p = multiprocessing.Process(target=send_image_thread,args= (chat_id,file))
	p.start()

    # Wait for 5 seconds or until process finishes
	p.join(5)

    # If thread is still active
	if p.is_alive():
		logging.error("running... let's kill telegram sending...")

        # Terminate
		p.terminate()
		p.join()	
	#**********send with time out**************************
	
	
	file.close()
	
	logging.debug("photo send")
	
 
def handle(msg):	
	chat_id = msg['chat']['id']
	command = msg['text'] 
	user=msg['chat']['first_name']
		
	logger = logging.getLogger()
	logger.setLevel(level=logging.DEBUG)
	
	logging.debug(msg)
	
	
	if command == '/current_time':
		send_message(str(datetime.datetime.now()),chat_id)
		
	elif command == '/mumble_info':
		send_message(mumble_info(),chat_id)
		
	elif command == '/mumble_image':	#!!!not working at all!!! bot hangs completely :fixed:		
		subprocess.check_output("convert "+cberry.image_file+".bmp "+cberry.image_file+".jpg", shell=True)
		send_image(cberry.image_file+".jpg",chat_id)# open in read byte mode				
		
	elif command == '/uptime':	
		direct_output = subprocess.check_output('uptime', shell=True)
		send_message(direct_output,chat_id)
		
	elif command == '/who':	
		direct_output = subprocess.check_output('who', shell=True)
		send_message(direct_output,chat_id)
	
	elif command == '/wifi':	
		direct_output = subprocess.check_output('iwconfig wlan0 | grep "Bit \| Quality"', shell=True)
		
		send_message(direct_output,chat_id,)
		
	elif command == '/traffic':	
		subprocess.check_output('vnstati -i wlan0 -h -o /home/pi/devel/mumble-bot/img/vnstat_hourly.png', shell=True)
		#subprocess.check_output('vnstati -i wlan0 -d -o /home/pi/devel/mumble-bot/img/vnstat_daily.png', shell=True)
		subprocess.check_output('vnstati -i wlan0 -m -o /home/pi/devel/mumble-bot/img/vnstat_monthly.png', shell=True)
		subprocess.check_output('vnstati -i wlan0 -t -o /home/pi/devel/mumble-bot/img/vnstat_top10.png', shell=True)
		subprocess.check_output('vnstati -i wlan0 -s -o /home/pi/devel/mumble-bot/img/vnstat_summary.png', shell=True)
		
		
		send_image("/home/pi/devel/mumble-bot/img/vnstat_summary.png",chat_id)# open in read byte mode
		#send_image("/home/pi/devel/mumble-bot/img/vnstat_daily.png",chat_id)# open in read byte mode
		send_image("/home/pi/devel/mumble-bot/img/vnstat_monthly.png",chat_id)# open in read byte mode
		send_image("/home/pi/devel/mumble-bot/img/vnstat_hourly.png",chat_id)# open in read byte mode
		send_image("/home/pi/devel/mumble-bot/img/vnstat_top10.png",chat_id)# open in read byte mode
		
		 

	elif command == '/help':
		message= ("PbtH-Mumble-Help\n"
		+"/current_time\n show server time\n"
		+"/uptime\n server up time\n"
		+"/who\n who is logged in\n"
		+"/wifi\n show wi-fi status\n"
		+"/traffic\n show current traffic\n"
		+"/mumble_info\n advanced mumble info's\n"
		+"/mumble_image\n show mumble screen\n"
		+"/help\n show this help\n")	
		
		send_message(message,chat_id)		
		
	else:
		logging.debug(command)
		#mumble_chat.send_message(user+":"+command)
		
		
def mumble_info():
	
	mRegistered_users= tools.read_Registered_UsersV2()
	channels= tools.read_channels()
	message =""
	for user in mRegistered_users[1:]:	#ignore first

		channel=channels[user.lastchannel]
		message+=user.name+"@"+channel+"\n"+user.last_active+"\n"	
	
	return message
		
	


		
"""
fix keyboard

def hide_keyborad():
	global bot	
	markup = ReplyKeyboardHide()
	bot.sendMessage(chat_id_pbth_group, 'connection reset', reply_markup=markup)
"""


