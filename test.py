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
access_token='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZXMiOlsiaGlzdG9yeSIsImhpc3RvcnlfbGl0ZSIsInBsYWNlcyIsInByb2ZpbGUiLCJyaWRlX3dpZGdldHMiXSwic3ViIjoiODgyNjliZGUtZjA4MS00OWY3LWFkOGUtZWRmOTRiN2IxZTZmIiwiaXNzIjoidWJlci11czEiLCJqdGkiOiI4Mjg4YmI5Yy1iZmM4LTQwODAtYjFiNy00NmIwZTYzZmJhMGEiLCJleHAiOjE0OTA1MDUxNzQsImlhdCI6MTQ4NzkxMzE3NCwidWFjdCI6Im1DRFgxaVFCNmJTOFVaSjVqOWFzZnY1YmZEOHJsTCIsIm5iZiI6MTQ4NzkxMzA4NCwiYXVkIjoiUTBzVG11ejNlX2RPQV95NnJBcTcxb0xWYW9KWVBzb0kifQ.hEoWPVqNZEiLP9LtBDazjUqTMVl9HGzk1i0ZWB64sv7zciwtxA8B2JocfVqPrYlFAjtsVfonxI2VPzvem-bmASX-r3sYDDUxBt9x1eS4pY2tGxVqIXvUGrra7ypfded4cXuS_lMDzs80h2C5L1CJXpictVjqspdZnHZGIQ84nZRxuYmno-uu79TG6nK1hmgr00SVb43aGap8AxB0t-G9QuGpVvdTa7BuFDPLJGMucZmpaVvjgMlO4-xu8qnemGQXQo4Le3Rq8l66ML-lYL10cu7MPIwJK5vywmQugbe7lcaz7RAI8q4SYhf7RWLauhC95faFrnts9nIa72V35nFX_w'
server_token="Y2Qa_qYmdjLty0zeLb6_hn-h2xdxhiv5xyAEI9ye"
client_id="Q0sTmuz3e_dOA_y6rAq71oLVaoJYPsoI"
client_secret="Fb1W_6uWbr5CLjFYcSmmTEsxeK9I0XImR-QkR17A"
redirect_url="http://localhost:80"
product_id=""
accept_lang='en_EN'
choose = [{'capacity': 2, 'shared': True, 'product_id': '26546650-e557-4a7b-86e7-6a3942445247', 'product_group': 'rideshare', 'short_description': 'POOL', 'display_name': 'POOL', 'image': 'http://d1a3f4spazzrp4.cloudfront.net/car-types/mono/mono-uberx.png', 'upfront_fare_enabled': True, 'cash_enabled': False, 'description': 'Share the ride, split the cost.'}]
header = {
       "Authorization": "Bearer {}".format(access_token),
       "Content-Type": "application/json"
       }
body = {
        "product_id": "821415d8-3bd5-4e27-9604-194e4359a449", 
    	"start_latitude":"37.775232", 
    	"start_longitude": "-122.4197513",
     	"end_latitude":"37.7899886",
      	"end_longitude": "-122.4021253",
        "seat_count": "2",
        "fare_id":"55c714203169a03cf816e280976fd5c1920f1574dd92a8a21cda19156b23ce06"
        }    

response = requests.post("https://api.uber.com/v1.2/requests", data = json.dumps(body), headers = header)	
print(response.text)