import sys
import telepot
import telepot.api
import urllib3
import time
import datetime 
import tools
import cberry
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply

	
bot=None 
token='237430124:AAF9frMQCMB-5K1JmrQNQZs7f5Ervn7-9rE'
chat_id_pbth_group=-176357162

def init_bot():
	global bot
	if bot==None:
		bot = telepot.Bot(token)	


"""
fix keyboard
"""
def hide_keyborad():
	init_bot()
	global bot	
	markup = ReplyKeyboardHide()
	bot.sendMessage(chat_id_pbth_group, 'connection reset', reply_markup=markup)

def send_message(message):
	init_bot()
	global bot
		
	bot.sendMessage(chat_id_pbth_group, message)
	
 
def handle(msg):
	chat_id = msg['chat']['id']
	command = msg['text'] 
    	
	if command == '/time':
		bot.sendMessage(chat_id,str(datetime.datetime.now()))
		return
	elif command == '/info':
		bot.sendMessage(chat_id, mumble_info())
		return
	if command == '/image':
		bot.sendPhoto(chat_id, open(cberry.bmp_file, 'rb'))
		return
		
	if command == '/help':
		message= "PbtH-Mumble-Help\n"+"/time\n"+"/info\n"+"/image\n"+"/help\n"			
		bot.sendMessage(chat_id,message)		
		return
		
		
def mumble_info():
	
	mRegistered_users= tools.read_Registered_UsersV2()
	channels= tools.read_channels()
	message =""
	for user in mRegistered_users[1:]:	#ignore first

		channel=channels[user.lastchannel]
		message+=user.name+"@"+channel+"\n"+user.last_active+"\n"	
	
	return message
		
	
def start():
	init_bot()
	global bot
	
	bot.message_loop(handle)
	print ("start telegram_bot")
 
	while 1:
		time.sleep(10)

		
	


