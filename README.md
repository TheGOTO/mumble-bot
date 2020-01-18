# mumble-bot
a mumble/telegram bot in python

The purpus of this bot is to inform a group of people about the online and offline Mumble users.

Features:
* send a telegram message to a group in case a mumble user is online
* show the status of the mumble users on a screen 

Used Hardware
* c-berry http://www.admatec.de/pdfs/C-Berry_0.pdf
* Raspberry PI v3

Used Software
* python 3


how to use the bot:
create a file "telegram_private.py" and add the following params

token / telegram api token
chat_id_pbth_group / id of the chat group for the release version of the bot
chat_id_goto / id of the chat group for the debug version of the bot

start the bot:
python3 mumble_bot.py --release
#we assume a user "telegram" to execute  mumble_bot.py 

python3 cberry_bot.py
#cberry need root permission

