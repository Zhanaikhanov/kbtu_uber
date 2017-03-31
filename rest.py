import requests
import json
params = {
   "product_id": "a1111c8c-c720-46c3-8534-2fcdd730040d",
   "status": "processing",
   "vehicle": "null",
   "driver": "null",
   "location": "null",
   "eta": 5,
   "surge_multiplier": 1
}
headers = {'Content-Type': 'application/json',
'Authorization': 'Bearer UiqU7WQXJAjgSYqh3COfRimt5nw352KD6LNvns1FTdRXW_H_VHPHBFC3V6bYd1nVwOfCfl2afaFbEKpUm4NwFCKMHEI9DSibS8nc7p3WgdeJabRZz1CtzI9vvsNXplORHsB41zljDLyy7WKV5w'}

res = requests.put('https://sandbox-api.uber.com/v1.2/products', data=json.dumps(params), headers=headers)
print(res.text)

'''
curl -X PUT 'https://sandbox-api.uber.com/v1.2/sandbox/requests/a1111c8c-c720-46c3-8534-2fcdd730040d' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer Y2Qa_qYmdjLty0zeLb6_hn-h2xdxhiv5xyAEI9ye' \
  -d '{"status":"accepted"}'



  curl -X POST 'https://sandbox-api.uber.com/v1.2/requests' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer Y2Qa_qYmdjLty0zeLb6_hn-h2xdxhiv5xyAEI9ye' \
  -d '{ "fare_id": "abcd", "product_id": "a1111c8c-c720-46c3-8534-2fcdd730040d", "start_latitude": 37.761492, "start_longitude": -122.423941, "end_latitude": 37.775393, "end_longitude": -122.417546 }'
'''