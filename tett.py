
#deeplink dmis-kbtu
https://m.uber.com/ul/?action=setPickup&client_id=BKWu_B6nDbwDHMDdaJ9WKTN5jVRi8Uxf&pickup[formatted_address]=%D0%90%D1%81%D1%8B%D0%BB%2C%20%D1%83%D0%BB%D0%B8%D1%86%D0%B0%20%D0%A2%D1%83%D1%80%D0%B3%D1%83%D1%82%D0%B0%20%D0%9E%D0%B7%D0%B0%D0%BB%D0%B0%2C%20%D0%90%D0%BB%D0%BC%D0%B0%D1%82%D1%8B%2C%20%D0%9A%D0%B0%D0%B7%D0%B0%D1%85%D1%81%D1%82%D0%B0%D0%BD&pickup[latitude]=43.249957&pickup[longitude]=76.880473&dropoff[formatted_address]=Kazakh-British%20Technical%20University%2C%20Almaty%2C%20Kazakhstan&dropoff[latitude]=43.255184&dropoff[longitude]=76.943138

#deeplink kbtu-dmis
https://m.uber.com/ul/?action=setPickup&client_id=BKWu_B6nDbwDHMDdaJ9WKTN5jVRi8Uxf&pickup[formatted_address]=Kazakh-British%20Technical%20University%2C%20Almaty%2C%20Kazakhstan&pickup[latitude]=43.255184&pickup[longitude]=76.943138&dropoff[formatted_address]=%D0%90%D1%81%D1%8B%D0%BB%2C%20%D1%83%D0%BB%D0%B8%D1%86%D0%B0%20%D0%A2%D1%83%D1%80%D0%B3%D1%83%D1%82%D0%B0%20%D0%9E%D0%B7%D0%B0%D0%BB%D0%B0%2C%20%D0%90%D0%BB%D0%BC%D0%B0%D1%82%D1%8B%2C%20%D0%9A%D0%B0%D0%B7%D0%B0%D1%85%D1%81%D1%82%D0%B0%D0%BD&dropoff[latitude]=43.249957&dropoff[longitude]=76.880473



Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import telegram
>>> TOKEN = '220364559:AAGBb9YoUnjdB_EQTLB91bmM-52-Hbyc4qs'
>>> TOKEN
'220364559:AAGBb9YoUnjdB_EQTLB91bmM-52-Hbyc4qs'
>>> from telegram.ext import Updater
>>> Updater = Updater(token='TOKEN')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python3.5/dist-packages/python_telegram_bot-5.3.0-py3.5.egg/telegram/ext/updater.py", line 87, in __init__
  File "/usr/local/lib/python3.5/dist-packages/python_telegram_bot-5.3.0-py3.5.egg/telegram/bot.py", line 53, in __init__
  File "/usr/local/lib/python3.5/dist-packages/python_telegram_bot-5.3.0-py3.5.egg/telegram/bot.py", line 79, in _validate_token
telegram.error.InvalidToken: Invalid token
>>> Updater = Updater(token=TOKEN)
>>> dispatcher = Updater.dispatcher
>>> import logging
>>> logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


>>> def start(bot, update):
...     bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")
... 

>>> from telegram.ext import CommandHandler
>>> start_handler = CommandHandler('start', start)
>>> dispatcher.add_handler(start_handler)
>>> updater.start_polling()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'updater' is not defined
>>> Updater.start_polling()
<queue.Queue object at 0x7f5d36ee20b8>


>>> def echo(bot, update):
...     bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)
...

>>> from telegram.ext import MessageHandler, Filters
>>> echo_handler = MessageHandler(Filters.text, echo)
>>> dispatcher.add_handler(echo_handler)



>>> def caps(bot, update, args):
...     text_caps = ' '.join(args).upper()
...     bot.sendMessage(chat_id=update.message.chat_id, text=text_caps)
... 

>>> caps_handler = CommandHandler('caps', caps, pass_args=True)
>>> dispatcher.add_handler(caps_handler)





>>> 2017-03-10 13:58:04,151 - telegram.ext.dispatcher - WARNING - A TelegramError was raised while processing the Update.
2017-03-10 14:00:59,946 - urllib3.connectionpool - WARNING - Retrying (Retry(total=2, connect=None, read=None, redirect=None)) after connection broken by 'ReadTimeoutError("HTTPSConnectionPool(host='api.telegram.org', port=443): Read timed out. (read timeout=15.0)",)': /bot220364559:AAGBb9YoUnjdB_EQTLB91bmM-52-Hbyc4qs/getUpdates
dispdispatcher.add_handler(caps_handler
KeyboardInterrupt
>>> 


KeyboardInterrupt
>>> updater.stop()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'updater' is not defined
>>> Updater.stop()
>>> exit()
