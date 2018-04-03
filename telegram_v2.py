#wrapper for python-telegram-bot
# https://github.com/python-telegram-bot/python-telegram-bot

import sys
import urllib3
import time
import datetime 
import subprocess   
import logging


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

	
updater=None 
token='237430124:AAF9frMQCMB-5K1JmrQNQZs7f5Ervn7-9rE'
chat_id_pbth_group=-176357162
chat_id_goto=263478717
default_chat_id=chat_id_goto
log=None


def test(bot, update):
    """Send a message when the command /test is issued."""
    update.message.reply_text('Hi!')


def echo(bot, update):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    log.error('Update "%s" caused error "%s"', update, error)

def init(mode='debug'):
	global updater
	global default_chat_id
	global log
	if updater==None:		
		updater = Updater(token)	
	else:
		return
		
	logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
	log = logging.getLogger(__name__)
	
		
	if mode == "release":
		default_chat_id=chat_id_pbth_group
		log.setLevel(logging.ERROR)
	else:		
		log.setLevel(logging.DEBUG)
		log.debug('hi from the debug logger!')

	log.debug("chat id= "+str(default_chat_id))	


	 # Get the dispatcher to register handlers
	dp = updater.dispatcher

	dp.add_handler(CommandHandler("test", test))
	dp.add_error_handler(error)
	dp.add_handler(MessageHandler(Filters.text, echo))
	
	# Start the Bot
	
	updater.start_polling()#starts a new thread

    	# Run the bot until you press Ctrl-C or the process receives SIGINT,
    	# SIGTERM or SIGABRT. This should be used most of the time, since
    	# start_polling() is non-blocking and will stop the bot gracefully.
	#updater.idle()


	
def send_message(p_msg,p_chat_id=0):

	init()	
	
	if not p_chat_id:#set to default
		p_chat_id=default_chat_id
	
	updater.bot.send_message(p_chat_id, p_msg)
	
	

	

	
	
	
	

		


