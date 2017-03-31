import telegram
TOKEN = '220364559:AAGBb9YoUnjdB_EQTLB91bmM-52-Hbyc4qs'

from telegram.ext import Updater 
from telegram.ext import CommandHandler

updater = Updater(token = TOKEN)
disp = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(bot, update):
	bot.sendMessage(chat_id = update.message.chat_id, text = 'Hello world!')

start_handler = CommandHandler('start', start)
disp.add_handler(start_handler)

updater.start_polling()
print('started')