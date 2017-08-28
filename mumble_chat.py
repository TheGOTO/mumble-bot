
import sys
sys.path.append('/home/pi/devel/pymumble/')
from pymumble_py3 import mumble, constants 
import telegram


bot=None

def callback(msg):
	
	user=bot.users[msg.actor].get_property("name")
	message=msg.message
	print(user+":"+message)
	telegram.send_message(user+":"+message)
	

def init():
	global bot

	bot=mumble.Mumble("localhost","bot",password='pbth',debug=False,reconnect=True)

	bot.set_application_string("bot")
	bot.callbacks.set_callback(constants.PYMUMBLE_CLBK_TEXTMESSAGERECEIVED, callback)

	bot.start()
	bot.is_ready()
	
	
	channel=bot.channels.find_by_name("Heroes of the Storm")
	channel.move_in()

def send_message(msg):

	for channel in bot.channels.values():
		channel.send_text_message(msg)

