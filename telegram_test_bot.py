import sys
import telepot
from telepot.delegate import per_chat_id, create_open


class MessageCounter(telepot.helper.ChatHandler):
    def __init__(self, seed_tuple, timeout):
        super(MessageCounter, self).__init__(seed_tuple, timeout)
        self._count = 0

    def on_chat_message(self, msg):

	command = msg['text'].strip().lower()

	if command == '/start':
		print("start")

	if command == '/help':
		print("help")

	if command == '/info':

        	self._count += 1
	        self.sender.sendMessage(self._count)
		print("hello")



TOKEN = "237430124:AAF9frMQCMB-5K1JmrQNQZs7f5Ervn7-9rE"


bot = telepot.DelegatorBot(TOKEN, [
	(per_chat_id(), create_open(MessageCounter, timeout=10)),
])
bot.message_loop(run_forever='Listening ...')
