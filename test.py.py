import http.server
import socketserver
from http import client
import requests
import json
import os
data_file = open('data.txt' , 'r')
auth_code = ''
start_lat=37.7752315
start_lon=-122.418075
end_lat=74.121
end_lon=86.123
access_token=''
server_token="Y2Qa_qYmdjLty0zeLb6_hn-h2xdxhiv5xyAEI9ye"
client_id="Q0sTmuz3e_dOA_y6rAq71oLVaoJYPsoI"
client_secret="Fb1W_6uWbr5CLjFYcSmmTEsxeK9I0XImR-QkR17A"
redirect_url="http://localhost:80"
product_id=""
accept_lang='en_EN'
choose = {}