#wrapper for python-telegram-bot
# https://github.com/python-telegram-bot/python-telegram-bot

import sys
import urllib3
import time
import datetime 
import subprocess   
import logging
import telegram_private
import subprocess   
import cberry
import tools

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

	
updater=None 

default_chat_id=telegram_private.chat_id_goto
log=None




def init(mode='debug'):
	global updater
	global default_chat_id
	global log
	if updater==None:		
		updater = Updater(telegram_private.token,use_context=True)	
	else:
		return
		
	logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
	
	#logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.DEBUG)
	
	log = logging.getLogger(__name__)
	
		
	if mode == "release":
		default_chat_id=telegram_private.chat_id_pbth_group
		log.setLevel(logging.ERROR)
	else:		
		log.setLevel(logging.DEBUG)
		log.debug('hi from the debug logger!')

	log.debug("chat id= "+str(default_chat_id))	


	 # Get the dispatcher to register handlers
	dp = updater.dispatcher

	
	dp.add_handler(CommandHandler("help", help))
	dp.add_handler(CommandHandler("traffic", traffic))
	dp.add_handler(CommandHandler("current_time", current_time))
	dp.add_handler(CommandHandler("mumble_info", mumble_info))
	dp.add_handler(CommandHandler("mumble_image", mumble_image))
	dp.add_handler(CommandHandler("uptime", uptime))
	dp.add_handler(CommandHandler("who", who))
		
	
	dp.add_error_handler(error)
	#dp.add_handler(MessageHandler(Filters.text, echo))
	
	# Start the Bot
	updater.start_polling()#starts a new thread		

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
	#updater.idle()
	


def echo(update,context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)
	
	
def current_time(update,context):		
		update.message.reply_text(str(datetime.datetime.now()))
		
def mumble_info(update,context):		
		update.message.reply_text(_mumble_info())
		
def mumble_image(update,context):	
		chat_id = update.message.chat_id
		subprocess.check_output("convert "+cberry.image_file+".bmp "+cberry.image_file+".jpg", shell=True)
		send_image(cberry.image_file+".jpg",chat_id)# open in read byte mode				
		
def uptime(update,context):			
		direct_output = subprocess.check_output('uptime', shell=True)
		update.message.reply_text(direct_output.decode("utf-8"))		
		
def who(update,context):	
		direct_output = subprocess.check_output('who', shell=True)
		update.message.reply_text(direct_output.decode("utf-8"))
	
def traffic(update,context):

		chat_id = update.message.chat_id

		subprocess.check_output('vnstati -i eth0 -h -o /home/pi/devel/mumble-bot/img/vnstat_hourly.png', shell=True)
		#subprocess.check_output('vnstati -i wlan0 -d -o /home/pi/devel/mumble-bot/img/vnstat_daily.png', shell=True)
		subprocess.check_output('vnstati -i eth0 -m -o /home/pi/devel/mumble-bot/img/vnstat_monthly.png', shell=True)
		subprocess.check_output('vnstati -i eth0 -t -o /home/pi/devel/mumble-bot/img/vnstat_top10.png', shell=True)
		subprocess.check_output('vnstati -i eth0 -s -o /home/pi/devel/mumble-bot/img/vnstat_summary.png', shell=True)
		
		
		send_image("/home/pi/devel/mumble-bot/img/vnstat_summary.png",chat_id)# open in read byte mode
		#send_image("/home/pi/devel/mumble-bot/img/vnstat_daily.png",chat_id)# open in read byte mode
		send_image("/home/pi/devel/mumble-bot/img/vnstat_monthly.png",chat_id)# open in read byte mode
		send_image("/home/pi/devel/mumble-bot/img/vnstat_hourly.png",chat_id)# open in read byte mode
		send_image("/home/pi/devel/mumble-bot/img/vnstat_top10.png",chat_id)# open in read byte mode		
		
	
def help(update,context):	
		message= ("PbtH-Mumble-Help\n"
		+"/current_time\n show server time\n"
		+"/uptime\n server up time\n"
		+"/who\n who is logged in\n"		
		+"/traffic\n show current traffic\n"
		+"/mumble_info\n advanced mumble info's\n"
		+"/mumble_image\n show mumble screen\n"
		+"/help\n show this help\n")	
		
		
		update.message.reply_text(message)


def error(update, context):
    """Log Errors caused by Updates."""
    log.error('Update "%s" caused error "%s"', context,context.error)
	
	
def send_message(p_msg,p_chat_id=0):	
	
	if not p_chat_id:#set to default
		p_chat_id=default_chat_id
	
	updater.bot.send_message(p_chat_id, p_msg.decode("utf-8") )
	
	
def send_image(path,chat_id=0):
	
	log.debug("sending now")	
	
	if not chat_id:#set to default
		chat_id=default_chat_id
	
	file=open(path, 'rb')# open in read byte mode
	
	log.debug(file)
	
	#call_with_timeout(send_image_thread,(chat_id,file))	
	updater.bot.sendPhoto(chat_id,file)
	
	
	file.close()
	
	log.debug("photo send")
	
	
def _mumble_info():
	
	mRegistered_users= tools.read_Registered_UsersV2()
	channels= tools.read_channels()
	message =""
	for user in mRegistered_users[1:]:	#ignore first

		channel=channels[user.lastchannel]
		message+=user.name+"@"+channel+"\n"+user.last_active+"\n"	
	
	return message
	
	

	

	
	
	
	

		


