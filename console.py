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

##########################################################################################3

def to_see_the_Uber_products_available():
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
		print("==========================================================================")
		print("[ "+ str(i_1) +" ]"+"description :"+ i["description"] + "\n\t\t\t\t\t" + "capacity :" + str(i["capacity"]) )
		i_1 += 1
	print("==========================================================================")
	print("\n")	
	
##########################################################################################3

def exchange_to_access_token():
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
	print('\n'+access_token+'\n')
	
##########################################################################################3

def about_user():
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
		print("\n\n\n\n\n==========================================================================")	
		print("\t\t Hello "+f_name+" "+l_name+"!")
		print("==========================================================================")
		print("\t\t your promo code is ---->: "+response.get("promo_code"))
		print("==========================================================================")
		print("\t\t      your email is ---->: "+response.get("email"))
		print("==========================================================================")
	except:
		print("error 4")

##########################################################################################3

def Get_a_list_of_products_available():
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
			print("\n==========================================================================")	
			print("[ "+ str(i_1) +" ]"+"\t\t description :"+i["description"]+" / "+i["short_description"])
			print("==========================================================================")
			print("[ "+ str(i_1) +" ]"+"\t\t PRODUCT_ID : "+i["product_id"])
			print("==========================================================================")
			print("[ "+ str(i_1) +" ]"+"\t\t product group: "+i["product_group"])
			print("==========================================================================\n")
			choose.append(i)
			i_1+=1
	except:
		print("error 5")

##########################################################################################3

def get_request_estimate():
	global choose,start_lat,start_lon,end_lat,end_lat, num, response_taxi
	num = int(input("\nTake taxi (type num [ ? ]) >>>"))-1
	print("Your taxi is :",num+1)
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
        "seat_count": "2"
        }
	
     
	try:
		response = requests.post("https://api.uber.com/v1.2/requests/estimate"
							,data = json.dumps(data1),headers=header)
		response = json.loads(response.text)
		print("\n\t\t<-----Your choice----->\n|==========================================================================")	
		print("|\t\t Display: "+response["fare"]["display"])
		print("|==========================================================================")
		print("|\t\t distance_unit: "+response["trip"]["distance_unit"])
		print("|==========================================================================")
		print("|\t\t duration_estimate: "+str(response["trip"]["duration_estimate"]) )
		print("|==========================================================================")
		print("|\t\t distance_estimate: "+str(response["trip"]["distance_estimate"]) )
		print("|==========================================================================")
		print("|\t\t pick up estimate: "+str(response["pickup_estimate"]) )
		print("|=========================================================================\n")
		response_taxi.append(response)
	except:
		print("error 6")

##########################################################################################3

def ride_requests():

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
		print("error 7")

##########################################################################################3

def start():
	sign_in()
	to_see_the_Uber_products_available()
	exchange_to_access_token()
	about_user()
	Get_a_list_of_products_available()
	get_request_estimate()
	ride_requests()


print("\t\t\tWelcome, to uber_console!\n")
'''
number = int(input("""
[ 1 ] 
[ 2 ] sign_in
[ 3 ] to see the Uber products available
	[ 4 ] exchange to access token
	[ 5 ] about user
	[ 6 ] Get a list of products available
	[ 7 ] get request estimate
	[ 8 ] ride requests
[ 9 ] exit
>>>
"""))

number1 = int(input("""
[ 1 ] sign_in
[ 2 ] to see the Uber products available
[ 3 ] exit
	"""))
'''
start()