import sys
import telepot
import urllib3
import time
import datetime 
import tools
import cberry
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
import mumble_chat
#sudo apt-get install python3-pil
from PIL import Image
	
bot=None 
token='237430124:AAF9frMQCMB-5K1JmrQNQZs7f5Ervn7-9rE'
chat_id_pbth_group=-176357162

def init():
	global bot
	if bot==None:
		bot = telepot.Bot(token)	


	bot.message_loop({'chat': handle},relax=0.5,timeout=1)


def send_message(msg):
	global bot
#	print(msg)		
	bot.sendMessage(chat_id_pbth_group, msg)
	
 
def handle(msg):
	global bot
	chat_id = msg['chat']['id']
	command = msg['text'] 
	user=msg['chat']['first_name']
    	
	if command == '/time':
		bot.sendMessage(chat_id,str(datetime.datetime.now()))
		return
	elif command == '/info':
		#bot.sendMessage(chat_id, mumble_info())
		return
	if command == '/image':		
		bmp_img=Image.open(cberry.image_file+".bmp")
		bmp_img.save(cberry.image_file+".png","PNG")
		bot.sendPhoto(chat_id, open(cberry.image_file+".png", 'rb'))# open in read byte mode
		return		
	if command == '/help':
		message= "PbtH-Mumble-Help\n"+"/time\n"+"/info\n"+"/image\n"+"/help\n"			
		bot.sendMessage(chat_id,message)		
		return
	
	mumble_chat.send_message(user+":"+command)

		
		
def mumble_info():
	
	mRegistered_users= tools.read_Registered_UsersV2()
	channels= tools.read_channels()
	message =""
	for user in mRegistered_users[1:]:	#ignore first

		channel=channels[user.lastchannel]
		message+=user.name+"@"+channel+"\n"+user.last_active+"\n"	
	
	return message
		
	
#def start():
#	init_bot()
#	global bot
	
#	print ("start telegram_bot")
 
#	while 1:
#		time.sleep(10)

		
"""
fix keyboard

def hide_keyborad():
	global bot	
	markup = ReplyKeyboardHide()
	bot.sendMessage(chat_id_pbth_group, 'connection reset', reply_markup=markup)
"""


