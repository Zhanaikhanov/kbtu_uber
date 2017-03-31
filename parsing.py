from telegram.ext import Filters

import requests, time, json

import telegram
from bs4 import BeautifulSoup

cars_l = []
gear_type = 'механика'
cars_p = []

TOKEN = '220364559:AAGBb9YoUnjdB_EQTLB91bmM-52-Hbyc4qs'

from telegram.ext import Updater, CommandHandler, MessageHandler

updater = Updater(token = TOKEN)
disp = updater.dispatcher

##########################################################################################3
import http.server
import socketserver
from http import client
import requests
import json
import os
data_file = open('data.txt' , 'r')
auth_code = ''
start_lat=43.2551839
start_lon=76.9431379
end_lat=43.2389054 
end_lon=76.8261563
num = 0
access_token=''
client_id="Q0sTmuz3e_dOA_y6rAq71oLVaoJYPsoI"
client_secret="Fb1W_6uWbr5CLjFYcSmmTEsxeK9I0XImR-QkR17A"
redirect_url="http://localhost:4444"
product_id=""
accept_lang='en_EN'
choose = []
response_taxi = []

##########################################################################################3

def sign_in():
	PORT = 4444
	class Handler(http.server.BaseHTTPRequestHandler):
		def do_GET(self):
			self.send_response(200)
			self.send_header("Content-type","text/html")
			self.end_headers()
			self.wfile.write(b"""
				<!DOCTYPE html>
				<html>
				<head>
				    <title>Kbtu_uber</title>
				</head>
				<body>
					<p>get back to the console !</p>
				</body>
				</html>
				""")
			path1 = str(self.path)
			if 'code' in path1:				
				global auth_code
				auth_code = path1[60:]
				state = path1[8:path1.index("code")-1]
				
		
	try:	
		httpd = socketserver.TCPServer(('localhost', 4444), Handler)

		print("at port :",PORT)
		print("EXIT")
		os.system("firefox --private-window https://auth.uber.com/login/?next_url=https%3A%2F%2Flogin.uber.com%2Foauth%2Fv2%2Fauthorize%3Fclient_id%3DQ0sTmuz3e_dOA_y6rAq71oLVaoJYPsoI%26response_type%3Dcode&state=2UmVBhhyM7pUhfVGQI_PSBluHwe0EQUmJBwk3z-6syY%3D")
		httpd.handle_request()
	except:
		httpd = socketserver.TCPServer(('localhost', 4441), Handler)

		print("at port :",PORT)
		print("EXIT")
		os.system("firefox --private-window https://auth.uber.com/login/?next_url=https%3A%2F%2Flogin.uber.com%2Foauth%2Fv2%2Fauthorize%3Fclient_id%3DQ0sTmuz3e_dOA_y6rAq71oLVaoJYPsoI%26response_type%3Dcode&state=2UmVBhhyM7pUhfVGQI_PSBluHwe0EQUmJBwk3z-6syY%3D")
		httpd.handle_request()
one = CommandHandler('sign_in', sign_in)
disp.add_handler(one)


##########################################################################################3

def to_see_the_Uber_products_available(bot, update):
	header = {
		"Authorization":"Token nP6AFQcEjxivyOtuuoMd__Tv5MgB3FrBmF94MYcD",
		"Content-type":"aplication/json",
		"Accept-Language":"en_EN"	
			}

	response = requests.get('https://api.uber.com/v1.2/products?latitude=37.7752315&longitude=-122.418075',
							headers=header)
	response = response.text
	products_1 = json.loads(response).get("products")
	print("\n")
	i_1 = 1 
	for i in products_1:

		bot.sendMessage(chat_id = update.message.chat_id, text ="[ "+ str(i_1) +" ]"+"description :"+ i["description"] + "\n\t\t\t\t\t" + "capacity :" + str(i["capacity"]) )
		i_1 += 1


two = CommandHandler('to_see_the_Uber_products_available', to_see_the_Uber_products_available)
disp.add_handler(two)	
##########################################################################################3

def exchange_to_access_token(bot, update):
	global auth_code, access_token
	header = {
		'Content-Type':'application/x-www-form-urlencoded'
			}

	body = {
		'client_id':'Q0sTmuz3e_dOA_y6rAq71oLVaoJYPsoI',
     	'client_secret':'Fb1W_6uWbr5CLjFYcSmmTEsxeK9I0XImR-QkR17A',
        'grant_type':'authorization_code',
        'redirect_uri':'http://localhost:4444',
        'code':auth_code
		}

	response = requests.post('https://login.uber.com/oauth/v2/token',data = body
							,headers=header)

	response = json.loads(response.text)
	access_token = response.get("access_token")
	#bot.sendMessage(chat_id = update.message.chat_id, text ='\n'+access_token+'\n')
three = CommandHandler('exchange_to_access_token', exchange_to_access_token)
disp.add_handler(three)	
##########################################################################################3

def about_user(bot, update):
	header = {
		"Authorization":"Bearer {}".format(access_token),
		"Content-Type":"application/json",
        "Accept-Language":"en_EN" 
		}

	response = requests.get('https://api.uber.com/v1.2/me'
							,headers=header)

	response = json.loads(response.text)
	try:
		f_name = response.get("first_name")
		l_name = response.get("last_name")

		bot.sendMessage(chat_id = update.message.chat_id, text =" Hello "+f_name+" "+l_name+"!")

		bot.sendMessage(chat_id = update.message.chat_id, text =" your promo code is ---->: "+response.get("promo_code"))

		bot.sendMessage(chat_id = update.message.chat_id, text ="      your email is ---->: "+response.get("email"))

	except:
		bot.sendMessage(chat_id = update.message.chat_id, text ="error 4")
four = CommandHandler('about_user', about_user)
disp.add_handler(four)	

##########################################################################################3

def Get_a_list_of_products_available(bot, update):
	header = {
        "Authorization":" Bearer {}".format(access_token),
        "Content-Type":"application/json",
        "Accept-Language":" en_EN"
		}     
	try:
		response = requests.get('https://api.uber.com/v1.2/products?latitude={}&longitude={}'.format(start_lat, start_lon)
							,headers=header)
		response = json.loads(response.text).get("products")
		i_1 = 1
		global choose
		for i in response:

			bot.sendMessage(chat_id = update.message.chat_id, text ="[ "+ str(i_1) +" ]"+" description :"+i["description"]+" / "+i["short_description"])

			bot.sendMessage(chat_id = update.message.chat_id, text ="[ "+ str(i_1) +" ]"+" PRODUCT_ID : "+i["product_id"])

			bot.sendMessage(chat_id = update.message.chat_id, text ="[ "+ str(i_1) +" ]"+" product group: "+i["product_group"])

			choose.append(i)
			i_1+=1
	except:
		bot.sendMessage(chat_id = update.message.chat_id, text ="error 5")
five = CommandHandler('Get_a_list_of_products_available', Get_a_list_of_products_available)
disp.add_handler(five)	

##########################################################################################3

def get_request_estimate(bot, update):
	global choose,start_lat,start_lon,end_lat,end_lat, num, response_taxi
	bot.sendMessage(chat_id = update.chat_id, text ="Take taxi")
	sleep(5)
	print(num)
	print("Your taxi is :",1)
	header = {
		"Authorization":" Bearer {}".format(access_token) ,
     	"Content-Type": "application/json",
		}
	data1 = {
		"product_id":choose[1]["product_id"] ,
      	"start_latitude": str(start_lat),
       	"start_longitude": str(start_lon),	
        "end_latitude": str(end_lat),
	    "end_longitude": str(end_lon),
	    "seat_count": "2"
        }

	try:
		response = requests.post("https://api.uber.com/v1.2/requests/estimate"
							,data = json.dumps(data1),headers=header)
		response = json.loads(response.text)
		bot.sendMessage(chat_id = update.message.chat_id, text ="<-----Your choice----->")	
		bot.sendMessage(chat_id = update.message.chat_id, text ="|Display: "+response["fare"]["display"])

		bot.sendMessage(chat_id = update.message.chat_id, text ="|distance_unit: "+response["trip"]["distance_unit"])

		bot.sendMessage(chat_id = update.message.chat_id, text ="|duration_estimate: "+str(response["trip"]["duration_estimate"]) )

		bot.sendMessage(chat_id = update.message.chat_id, text ="|distance_estimate: "+str(response["trip"]["distance_estimate"]) )

		bot.sendMessage(chat_id = update.message.chat_id, text ="|pick up estimate: "+str(response["pickup_estimate"]) )

		response_taxi.append(response)
	except:
		bot.sendMessage(chat_id = update.message.chat_id, text ="error 6")
six = CommandHandler('get_request_estimate', get_request_estimate)
disp.add_handler(six)	

##########################################################################################3

def ride_requests(bot, update):

	global choose,start_lat,start_lon,end_lat,end_lat,num,response_taxi
	header = {
		"Authorization":" Bearer {}".format(access_token) ,
     	"Content-Type": "application/json",
		}
	data1 = {
		"product_id":choose[num]["product_id"] ,
      	"start_latitude": str(start_lat),
       	"start_longitude": str(start_lon),
        "end_latitude": str(end_lat),
        "end_longitude": str(end_lon),
        "seat_count": "2",
  		"fare_id": str(response_taxi[0]['fare']["fare_id"])
        }     
	try:
	
		response = requests.post("https://api.uber.com/v1.2/requests"
							,data = json.dumps(data1),headers=header)

		response = json.loads(response.text)
		
	except:
		bot.sendMessage(chat_id = update.message.chat_id, text ="error 7")
seven = CommandHandler('ride_requests', ride_requests)
disp.add_handler(seven)	

##########################################################################################3

def to_uber_console(bot, update):
	bot.sendMessage(chat_id = update.message.chat_id, text = '/to_see_the_Uber_products_available\n/exchange_to_access_token\n/about_user\n/Get_a_list_of_products_available\n/get_request_estimate\n/ride_requests')
	sign_in()
	exchange_to_access_token(bot, update)
	to_see_the_Uber_products_available(bot, update)
	Get_a_list_of_products_available(bot, update)
	about_user(bot, update)
	get_request_estimate(bot, update)
to_uber_console_handler = CommandHandler('to_uber_console', to_uber_console)
disp.add_handler(to_uber_console_handler)

def start_uber():
	
	ride_requests()


print("\t\t\tWelcome, to uber_console!\n")

def start(bot, update):
	try:
		bot.sendMessage(chat_id = update.message.chat_id, text = 'Hello world!')
	except:
		print('error')

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
	global num
	num = eval(update.message.text) 
	bot.sendMessage(chat_id = update.message.chat_id, text = num)



echo_handler = MessageHandler(Filters.text, echo)
disp.add_handler(echo_handler)

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


def change_status_vk(bot, update):
	import random
	response = requests.get('http://www.vktops.com/statusy-o-zhenshchinakh/')
	html = response.text
	soup = BeautifulSoup(html, 'html.parser')
	pop_status = soup.find_all('div', class_='text')
	access_token='cd6787446b1053d24d6cd50e4d3f520856f5e2af70ef99a0660323825361c9b9caf0f455da0a7c56d38d9'
	status_is = random.choice(pop_status).get_text()
	url = 'https://api.vk.com/method/status.set?access_token={}&text={}'.format(access_token, status_is)
	response = requests.get(url)
	bot.sendMessage(chat_id=update.message.chat_id, text = "changed to: "+status_is)

change_status_vk_handler = CommandHandler('change_status_vk', change_status_vk)
disp.add_handler(change_status_vk_handler)



#-------------------------------------------------------------
taxi_list_users = {}

def taxi_list(bot, update):
	global taxi_list_users
	if len(taxi_list_users) > 0: 
		for taxi_li in taxi_list_users:
			bot.sendMessage(chat_id = update.message.chat_id, text = '@'+taxi_li+'\nTime : ' + taxi_list_users[taxi_li]['time'][11:-4] + '\nFrom: ' + taxi_list_users[taxi_li]['from'])
	else:
		bot.sendMessage(chat_id = update.message.chat_id, text = "no one")

taxi_list_handler = CommandHandler('taxi_list', taxi_list)
disp.add_handler(taxi_list_handler)
#-------------------------------------------------------------
location_from = ''

header = {
		"Authorization":"Token nP6AFQcEjxivyOtuuoMd__Tv5MgB3FrBmF94MYcD",
		"Content-type":"aplication/json",
		"Accept-Language":"en_EN"	
			}

response = requests.get('https://api.uber.com/v1.2/products?latitude=37.7752315&longitude=-122.418075',
							headers=header)
response = response.text
products_1 = json.loads(response).get("products")

def taxi_request(bot, update):
	global taxi_list_users, location_from
	if location_from is not "KBTU" and location_from is not "DMiS":
		bot.sendMessage(chat_id = update.message.chat_id, text = "from where?\n/KBTU\n/DMiS\ntype on one of these")		
	else:
		if update.message.chat.username not in taxi_list_users:			
			taxi_list_users[update.message.chat.username] = { 
			'first_name' : update.message.chat.first_name 
			,'last_name' : update.message.chat.last_name
			, 'status':'unknown' 
			, 'cost': '750 KZT'
			, 'from' : location_from
			, 'time' : time.ctime()  
			}

			# here payd we'll take it from uber api responses
			
			bot.sendMessage(chat_id = update.message.chat_id, 
				text = update.message.chat.first_name + 
				' ' + update.message.chat.last_name + 
				'\nusername: @' + update.message.chat.username) + '\n' + products_1[0]
			# here must be requests for uber api
		else:
			bot.sendMessage(chat_id = update.message.chat_id, text = "you cannot do it again")		

taxi_request_handler = CommandHandler('taxi_request', taxi_request)
disp.add_handler(taxi_request_handler)

def KBTU(bot, update):
	global location_from
	location_from = 'KBTU'
	bot.sendMessage(chat_id = update.message.chat_id, text = 'your location is KBTU\n/taxi_request\n;)')

KBTU_handler = CommandHandler('KBTU', KBTU)
disp.add_handler(KBTU_handler)

def DMiS(bot, update):
	global location_from
	location_from = 'DMiS'
	bot.sendMessage(chat_id = update.message.chat_id, text = 'your location is DMiS\n/taxi_request\n;)')

DMiS_handler = CommandHandler('DMiS', DMiS)
disp.add_handler(DMiS_handler)


#-------------------------------------------------------------




def commands(bot, update):
	bot.sendMessage(chat_id = update.message.chat_id, text = '/to_uber_console\n/change_status_vk\n/start\n/quit\n/echo\n/cars\n/gear_mechanics\n/gear_automatics\n')


commands_handler = CommandHandler('help', commands)
disp.add_handler(commands_handler)



quit_handler = CommandHandler('quit', quit)
disp.add_handler(quit_handler)

print("is started")
updater.start_polling()