import sys
import telepot
import urllib3
import time
import datetime 
import tools
import cberry
from telepot.loop import MessageLoop
#from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
import mumble_chat
import subprocess   
#sudo apt-get install python3-pil
from PIL import Image
	
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

	#print (default_chat_id)
	
	
		
	#bot.message_loop({'chat': handle},relax=0.5,timeout=1)
	
	MessageLoop(bot, {'chat': handle}).run_as_thread()


def send_message(msg):
	global bot
#	print(msg)		
	bot.sendMessage(default_chat_id, msg)
	
 
def handle(msg):
	global bot
	chat_id = msg['chat']['id']
	command = msg['text'] 
	user=msg['chat']['first_name']
	
	if command == '/current_time':
		bot.sendMessage(chat_id,str(datetime.datetime.now()))
		return
	elif command == '/mumble_info':
		bot.sendMessage(chat_id, mumble_info())
		return
	elif command == '/mumble_image':	#!!!not working at all!!! bot hangs completely :fixed:
		bmp_img=Image.open(cberry.image_file+".bmp")		
		bmp_img.save(cberry.image_file+".jpg","JPEG") 		
		ret=bot.sendPhoto(chat_id, open(cberry.image_file+".jpg", 'rb'))# open in read byte mode		
		return				
	elif command == '/uptime':	
		direct_output = subprocess.check_output('uptime', shell=True)
		bot.sendMessage(chat_id, direct_output)
		
	elif command == '/who':	
		direct_output = subprocess.check_output('who', shell=True)
		bot.sendMessage(chat_id, direct_output)
	
	elif command == '/wifi':	
		direct_output = subprocess.check_output('iwconfig wlan0 | grep "Bit \| Quality"', shell=True)
		
		bot.sendMessage(chat_id, direct_output)
		
	elif command == '/traffic':	
		subprocess.check_output('vnstati -i wlan0 -h -o /home/pi/devel/mumble-bot/img/vnstat_hourly.png', shell=True)
		#subprocess.check_output('vnstati -i wlan0 -d -o /home/pi/devel/mumble-bot/img/vnstat_daily.png', shell=True)
		subprocess.check_output('vnstati -i wlan0 -m -o /home/pi/devel/mumble-bot/img/vnstat_monthly.png', shell=True)
		subprocess.check_output('vnstati -i wlan0 -t -o /home/pi/devel/mumble-bot/img/vnstat_top10.png', shell=True)
		subprocess.check_output('vnstati -i wlan0 -s -o /home/pi/devel/mumble-bot/img/vnstat_summary.png', shell=True)
		
		
		bot.sendPhoto(chat_id, open("/home/pi/devel/mumble-bot/img/vnstat_summary.png", 'rb'))# open in read byte mode
		#bot.sendPhoto(chat_id, open("/home/pi/devel/mumble-bot/img/vnstat_daily.png", 'rb'))# open in read byte mode
		bot.sendPhoto(chat_id, open("/home/pi/devel/mumble-bot/img/vnstat_monthly.png", 'rb'))# open in read byte mode
		bot.sendPhoto(chat_id, open("/home/pi/devel/mumble-bot/img/vnstat_hourly.png", 'rb'))# open in read byte mode
		bot.sendPhoto(chat_id, open("/home/pi/devel/mumble-bot/img/vnstat_top10.png", 'rb'))# open in read byte mode
		
		 

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
		#message= "PbtH-Mumble-Help\n"+"/time\n"+"/info\n"+"/help\n"			
		bot.sendMessage(chat_id,message)		
		return
	
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


