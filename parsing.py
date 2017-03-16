
import requests

import telegram
from bs4 import BeautifulSoup

cars_l = []
gear_type = 'механика'
cars_p = []

TOKEN = '220364559:AAGBb9YoUnjdB_EQTLB91bmM-52-Hbyc4qs'

from telegram.ext import Updater, CommandHandler, MessageHandler

updater = Updater(token = TOKEN)
disp = updater.dispatcher

def start(bot, update):
	bot.sendMessage(chat_id = update.message.chat_id, text = 'Hello world!')

start_handler = CommandHandler('start', start)
disp.add_handler(start_handler)

def cars(bot, update):
	global gear_type
	global cars_l, cars_p
	response = requests.get("http://newauto.kz/?gear_type={}".format(gear_type) )
	html = response.text
	soup = BeautifulSoup(html, 'html.parser')

	car_title = soup.find_all('span', class_='car-item-title')
	for car in car_title:
		cars_l.append(str(car.get_text()[1:-1]) )

	car_price = soup.find_all('span', class_='car-item-price')
	for pr in car_price:
		cars_p.append(str(pr.get_text()[1:-1]) )

	print("cars ready!")
	print(cars_l[0])

	print('\ncars:\n'+cars_l[0] + ' :: ' + cars_p[0][1:-2])
	ind=0
	for car1 in cars_l:
		print(car1+" : : "+cars_p[ind][1:12])
		bot.sendMessage(chat_id = update.message.chat_id, text = car1+" : : "+cars_p[ind][1:12])
		ind+=1

car_handler = CommandHandler('cars',cars)
disp.add_handler(car_handler)

def quit(bot, update):
	updater.stop()

def echo(bot, update):
	bot.sendMessage(chat_id = update.message.chat_id, text = update.message.text)

def gear_mechanics(bot, update):
	global gear_type
	gear_type = "механика"
	bot.sendMessage(chat_id = update.message.chat_id, text = 'changed to mechanics')


gear_mechanics_handler = CommandHandler('mechanics', gear_mechanics)
disp.add_handler(gear_mechanics_handler)

def gear_automatics(bot, update):
	global gear_type
	gear_type = "автомат"
	bot.sendMessage(chat_id = update.message.chat_id, text = 'changed to automatics')


gear_automatics_handler = CommandHandler('automatics', gear_automatics)
disp.add_handler(gear_automatics_handler)


from telegram.ext import Filters

echo_handler = MessageHandler(Filters.text, echo)
disp.add_handler(echo_handler)


quit_handler = CommandHandler('quit', quit)
disp.add_handler(quit_handler)

print("is started")
updater.start_polling()