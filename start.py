-----------------------------------------------------------------------------------------------------------------------------------------
import requests
import json
import os, sys
start_lat=37.7752315
start_lon=-122.418075
end_lat=74.121
end_lon=86.123
acess_token="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZXMiOlsicmVxdWVzdCIsInByb2ZpbGUiLCJoaXN0b3J5Il0sInN1YiI6Ijg4MjY5YmRlLWYwODEtNDlmNy1hZDhlLWVkZjk0YjdiMWU2ZiIsImlzcyI6InViZXItdXMxIiwianRpIjoiNDA2MmM2YzktOGZmNS00ZWFmLWEyOGYtOTc1NzYyMmE0ZmI2IiwiZXhwIjoxNDkwMTcwMTk3LCJpYXQiOjE0ODc1NzgxOTcsInVhY3QiOiI0am5XSW9jQkhseUszSXhWdGFSaHliVlRmQ0MycUciLCJuYmYiOjE0ODc1NzgxMDcsImF1ZCI6IlEwc1RtdXozZV9kT0FfeTZyQXE3MW9MVmFvSllQc29JIn0.V9pbRi-c4jZs3q3uIs8ngYES_PhEZrJudfy4E1TCm5gcrtnCwzBjaJiq0OrEgJaVUwYsSS72ZYVvjqUhz7pSHvWftd6QlwSEMa9WSZFZx096vugEblpB2kzlkdtzv-SV-wJbLR5a2aYQqKOdEbEHWvHZHqBu6zzksF8S_5jvz2Kj0MGjkSZNKrSO6rfU230B2B7Sabr9qVzBtpewcfWQPVNvrseIiYlZgdIDawhhw4bxnBB5nzISO79a1H9fYAfqmzqbq16KouO9QmWpDCGBacOY76jmTvsdQrdHRH6iOrM8x2VZDD7UX5juPjIlcGE-P2DMlFcH2-xzMkA6c-G-kg"
server_token="Y2Qa_qYmdjLty0zeLb6_hn-h2xdxhiv5xyAEI9ye"
client_id="Q0sTmuz3e_dOA_y6rAq71oLVaoJYPsoI"
client_secret="Fb1W_6uWbr5CLjFYcSmmTEsxeK9I0XImR-QkR17A"
redirect_url="http://localhost:4444"
auth_code="fV0Itn9YCyIP2oHRpfo1GaIQgfi60V"
product_id=""
accept_lang='en_EN'

------------------------------------------------------------------------------------------------------------------------------------------
+++++++++++++to see the Uber products available+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------------------------------------------------------------------------------

header1 = {
		"Authorization: Token {}".format(server_token)
     	"Content-Type: application/json" 
     	"Accept-Language: {}".format(accept_lang)
     	'https://api.uber.com/v1.2/products?latitude={}&longitude={}'.format(start_lat,start_lon)
     	}

print('[1] To see the Uber products available')
"https://login.uber.com/oauth/v2/authorize?response_type=code&client_id=Q0sTmuz3e_dOA_y6rAq71oLVaoJYPsoI&scope=request%20profile%20history&redirect_uri=http://localhost:80".format(client_id,redirect_url)
choose = str(input())

------------------------------------------------------------------------------------------------------------------------------------------
+++++++++++++exchanging to access token+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------------------------------------------------------------------------------

curl -F 'client_id=Q0sTmuz3e_dOA_y6rAq71oLVaoJYPsoI' \
     -F 'client_secret=Fb1W_6uWbr5CLjFYcSmmTEsxeK9I0XImR-QkR17A' \
     -F 'grant_type=authorization_code' \
     -F 'redirect_uri=http://localhost:4444' \
     -F 'code=fV0Itn9YCyIP2oHRpfo1GaIQgfi60V' \
     https://login.uber.com/oauth/v2/token | jq '.'

{
  "last_authenticated": 1487412192,
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZXMiOlsicmVxdWVzdCIsInByb2ZpbGUiLCJoaXN0b3J5Il0sInN1YiI6Ijg4MjY5YmRlLWYwODEtNDlmNy1hZDhlLWVkZjk0YjdiMWU2ZiIsImlzcyI6InViZXItdXMxIiwianRpIjoiNDA2MmM2YzktOGZmNS00ZWFmLWEyOGYtOTc1NzYyMmE0ZmI2IiwiZXhwIjoxNDkwMTcwMTk3LCJpYXQiOjE0ODc1NzgxOTcsInVhY3QiOiI0am5XSW9jQkhseUszSXhWdGFSaHliVlRmQ0MycUciLCJuYmYiOjE0ODc1NzgxMDcsImF1ZCI6IlEwc1RtdXozZV9kT0FfeTZyQXE3MW9MVmFvSllQc29JIn0.V9pbRi-c4jZs3q3uIs8ngYES_PhEZrJudfy4E1TCm5gcrtnCwzBjaJiq0OrEgJaVUwYsSS72ZYVvjqUhz7pSHvWftd6QlwSEMa9WSZFZx096vugEblpB2kzlkdtzv-SV-wJbLR5a2aYQqKOdEbEHWvHZHqBu6zzksF8S_5jvz2Kj0MGjkSZNKrSO6rfU230B2B7Sabr9qVzBtpewcfWQPVNvrseIiYlZgdIDawhhw4bxnBB5nzISO79a1H9fYAfqmzqbq16KouO9QmWpDCGBacOY76jmTvsdQrdHRH6iOrM8x2VZDD7UX5juPjIlcGE-P2DMlFcH2-xzMkA6c-G-kg",
  "expires_in": 2592000,
  "token_type": "Bearer",
  "scope": "request profile history",
  "refresh_token": "Nnq2X7J0EROet27iHV0G2ZHJN8pyJV"
}

------------------------------------------------------------------------------------------------------------------------------------------
+++++++++++profile information about the authorized user.+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------------------------------------------------------------------------------

curl -X GET -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZXMiOlsicmVxdWVzdCIsInByb2ZpbGUiLCJoaXN0b3J5Il0sInN1YiI6Ijg4MjY5YmRlLWYwODEtNDlmNy1hZDhlLWVkZjk0YjdiMWU2ZiIsImlzcyI6InViZXItdXMxIiwianRpIjoiNDA2MmM2YzktOGZmNS00ZWFmLWEyOGYtOTc1NzYyMmE0ZmI2IiwiZXhwIjoxNDkwMTcwMTk3LCJpYXQiOjE0ODc1NzgxOTcsInVhY3QiOiI0am5XSW9jQkhseUszSXhWdGFSaHliVlRmQ0MycUciLCJuYmYiOjE0ODc1NzgxMDcsImF1ZCI6IlEwc1RtdXozZV9kT0FfeTZyQXE3MW9MVmFvSllQc29JIn0.V9pbRi-c4jZs3q3uIs8ngYES_PhEZrJudfy4E1TCm5gcrtnCwzBjaJiq0OrEgJaVUwYsSS72ZYVvjqUhz7pSHvWftd6QlwSEMa9WSZFZx096vugEblpB2kzlkdtzv-SV-wJbLR5a2aYQqKOdEbEHWvHZHqBu6zzksF8S_5jvz2Kj0MGjkSZNKrSO6rfU230B2B7Sabr9qVzBtpewcfWQPVNvrseIiYlZgdIDawhhw4bxnBB5nzISO79a1H9fYAfqmzqbq16KouO9QmWpDCGBacOY76jmTvsdQrdHRH6iOrM8x2VZDD7UX5juPjIlcGE-P2DMlFcH2-xzMkA6c-G-kg" \
     -H "Content-Type: application/json" \
     -H "Accept-Language: en_EN" \
     'https://api.uber.com/v1.2/me'

{
  "picture": "https://d1w2poirtb3as9.cloudfront.net/default.jpeg",
  "first_name": "Bektemir",
  "last_name": "Zhanaykhanov",
  "uuid": "88269bde-f081-49f7-ad8e-edf94b7b1e6f",
  "rider_id": "8MGuIYpjGSV7klm1AlfuTdTxCk1zhlvBecB5M7pXPwmbc47QvmgRHRE994hs0vv13qgYZAp2dS2XpcpdW4brXt7HL4eFQHeBbNz3YGE5FHlzF6uv6m5jL3mith6Zwb6hFQ==",
  "email": "bekablack.bz@gmail.com",
  "mobile_verified": true,
  "promo_code": "rcmkygh2ue"
}

------------------------------------------------------------------------------------------------------------------------------------------
++++++++++++++Get a list of products available++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------------------------------------------------------------------------------

curl -X GET -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZXMiOlsicmVxdWVzdCIsInByb2ZpbGUiLCJoaXN0b3J5Il0sInN1YiI6Ijg4MjY5YmRlLWYwODEtNDlmNy1hZDhlLWVkZjk0YjdiMWU2ZiIsImlzcyI6InViZXItdXMxIiwianRpIjoiNDA2MmM2YzktOGZmNS00ZWFmLWEyOGYtOTc1NzYyMmE0ZmI2IiwiZXhwIjoxNDkwMTcwMTk3LCJpYXQiOjE0ODc1NzgxOTcsInVhY3QiOiI0am5XSW9jQkhseUszSXhWdGFSaHliVlRmQ0MycUciLCJuYmYiOjE0ODc1NzgxMDcsImF1ZCI6IlEwc1RtdXozZV9kT0FfeTZyQXE3MW9MVmFvSllQc29JIn0.V9pbRi-c4jZs3q3uIs8ngYES_PhEZrJudfy4E1TCm5gcrtnCwzBjaJiq0OrEgJaVUwYsSS72ZYVvjqUhz7pSHvWftd6QlwSEMa9WSZFZx096vugEblpB2kzlkdtzv-SV-wJbLR5a2aYQqKOdEbEHWvHZHqBu6zzksF8S_5jvz2Kj0MGjkSZNKrSO6rfU230B2B7Sabr9qVzBtpewcfWQPVNvrseIiYlZgdIDawhhw4bxnBB5nzISO79a1H9fYAfqmzqbq16KouO9QmWpDCGBacOY76jmTvsdQrdHRH6iOrM8x2VZDD7UX5juPjIlcGE-P2DMlFcH2-xzMkA6c-G-kg" \
     -H "Content-Type: application/json" \
     -H "Accept-Language: en_EN" \
     'https://api.uber.com/v1.2/products?latitude=37.7752315&longitude=-122.418075' | jq '.'


{
  "products": [
    {
      "upfront_fare_enabled": true,
      "capacity": 2,
      "product_id": "26546650-e557-4a7b-86e7-6a3942445247",
      "image": "http://d1a3f4spazzrp4.cloudfront.net/car-types/mono/mono-uberx.png",
      "cash_enabled": false,
      "shared": true,
      "short_description": "POOL",
      "display_name": "POOL",
      "product_group": "rideshare",
      "description": "Share the ride, split the cost."
    },
    {
      "upfront_fare_enabled": true,
      "capacity": 4,
      "product_id": "a1111c8c-c720-46c3-8534-2fcdd730040d",
      "image": "http://d1a3f4spazzrp4.cloudfront.net/car-types/mono/mono-uberx.png",
      "cash_enabled": false,
      "shared": false,
      "short_description": "uberX",
      "display_name": "uberX",
      "product_group": "uberx",
      "description": "THE LOW-COST UBER"
    },
    {
      "upfront_fare_enabled": true,
      "capacity": 4,
      "product_id": "57c0ff4e-1493-4ef9-a4df-6b961525cf92",
      "image": "http://d1a3f4spazzrp4.cloudfront.net/car-types/mono/mono-uberselect.png",
      "cash_enabled": false,
      "shared": false,
      "short_description": "SELECT",
      "display_name": "SELECT",
      "product_group": "uberx",
      "description": "A STEP ABOVE THE EVERY DAY"
    },
    {
      "upfront_fare_enabled": true,
      "capacity": 6,
      "product_id": "821415d8-3bd5-4e27-9604-194e4359a449",
      "image": "http://d1a3f4spazzrp4.cloudfront.net/car-types/mono/mono-uberxl2.png",
      "cash_enabled": false,
      "shared": false,
      "short_description": "uberXL",
      "display_name": "uberXL",
      "product_group": "uberxl",
      "description": "LOW-COST RIDES FOR LARGE GROUPS"
    },
    {
      "upfront_fare_enabled": true,
      "capacity": 4,
      "product_id": "d4abaae7-f4d6-4152-91cc-77523e8165a4",
      "image": "http://d1a3f4spazzrp4.cloudfront.net/car-types/mono/mono-black.png",
      "cash_enabled": false,
      "shared": false,
      "short_description": "BLACK",
      "display_name": "BLACK",
      "product_group": "uberblack",
      "description": "THE ORIGINAL UBER"
    },
    {
      "upfront_fare_enabled": true,
      "capacity": 6,
      "product_id": "8920cb5e-51a4-4fa4-acdf-dd86c5e18ae0",
      "image": "http://d1a3f4spazzrp4.cloudfront.net/car-types/mono/mono-suv.png",
      "cash_enabled": false,
      "shared": false,
      "short_description": "SUV",
      "display_name": "SUV",
      "product_group": "suv",
      "description": "ROOM FOR EVERYONE"
    },
    {
      "upfront_fare_enabled": true,
      "capacity": 4,
      "product_id": "ff5ed8fe-6585-4803-be13-3ca541235de3",
      "image": "http://d1a3f4spazzrp4.cloudfront.net/car-types/mono/mono-uberx.png",
      "cash_enabled": false,
      "shared": false,
      "short_description": "ASSIST",
      "display_name": "ASSIST",
      "product_group": "uberx",
      "description": "uberX with extra assistance"
    },
    {
      "upfront_fare_enabled": true,
      "capacity": 4,
      "product_id": "2832a1f5-cfc0-48bb-ab76-7ea7a62060e7",
      "image": "http://d1a3f4spazzrp4.cloudfront.net/car-types/mono/mono-wheelchair.png",
      "cash_enabled": false,
      "shared": false,
      "short_description": "WAV",
      "display_name": "WAV",
      "product_group": "uberx",
      "description": "WHEELCHAIR ACCESSIBLE VEHICLES"
    },
    {
      "upfront_fare_enabled": false,
      "capacity": 4,
      "product_id": "3ab64887-4842-4c8e-9780-ccecd3a0391d",
      "image": "http://d1a3f4spazzrp4.cloudfront.net/car-types/mono/mono-taxi.png",
      "cash_enabled": false,
      "shared": false,
      "short_description": "TAXI",
      "display_name": "TAXI",
      "product_group": "taxi",
      "description": "TAXI WITHOUT THE HASSLE"
    }
  ]
}

------------------------------------------------------------------------------------------------------------------------------------------
+++++++++++++++++++Request a Ride Estimate+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------------------------------------------------------------------------------

curl  -X POST -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZXMiOlsicmVxdWVzdCIsInByb2ZpbGUiLCJoaXN0b3J5Il0sInN1YiI6Ijg4MjY5YmRlLWYwODEtNDlmNy1hZDhlLWVkZjk0YjdiMWU2ZiIsImlzcyI6InViZXItdXMxIiwianRpIjoiNDA2MmM2YzktOGZmNS00ZWFmLWEyOGYtOTc1NzYyMmE0ZmI2IiwiZXhwIjoxNDkwMTcwMTk3LCJpYXQiOjE0ODc1NzgxOTcsInVhY3QiOiI0am5XSW9jQkhseUszSXhWdGFSaHliVlRmQ0MycUciLCJuYmYiOjE0ODc1NzgxMDcsImF1ZCI6IlEwc1RtdXozZV9kT0FfeTZyQXE3MW9MVmFvSllQc29JIn0.V9pbRi-c4jZs3q3uIs8ngYES_PhEZrJudfy4E1TCm5gcrtnCwzBjaJiq0OrEgJaVUwYsSS72ZYVvjqUhz7pSHvWftd6QlwSEMa9WSZFZx096vugEblpB2kzlkdtzv-SV-wJbLR5a2aYQqKOdEbEHWvHZHqBu6zzksF8S_5jvz2Kj0MGjkSZNKrSO6rfU230B2B7Sabr9qVzBtpewcfWQPVNvrseIiYlZgdIDawhhw4bxnBB5nzISO79a1H9fYAfqmzqbq16KouO9QmWpDCGBacOY76jmTvsdQrdHRH6iOrM8x2VZDD7UX5juPjIlcGE-P2DMlFcH2-xzMkA6c-G-kg" \
     -H "Content-Type: application/json" -d \
     '{"product_id": "821415d8-3bd5-4e27-9604-194e4359a449", "start_latitude":"37.775232", "start_longitude": "-122.4197513", "end_latitude":"37.7899886", "end_longitude": "-122.4021253","seat_count": "2"}' \
      https://api.uber.com/v1.2/requests/estimate

{
  "fare": {
    "value": 12.22,
    "fare_id": "55c714203169a03cf816e280976fd5c1920f1574dd92a8a21cda19156b23ce06",
    "expires_at": 1487578856,
    "display": "$12.22",
    "currency_code": "USD"
  },
  "trip": {
    "distance_unit": "mile",
    "duration_estimate": 600,
    "distance_estimate": 2.39
  },
  "pickup_estimate": 6
}

------------------------------------------------------------------------------------------------------------------------------------------
+++++++++++++++++++Ride Requests+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------------------------------------------------------------------------------

curl  -X POST -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZXMiOlsicmVxdWVzdCIsInByb2ZpbGUiLCJoaXN0b3J5Il0sInN1YiI6Ijg4MjY5YmRlLWYwODEtNDlmNy1hZDhlLWVkZjk0YjdiMWU2ZiIsImlzcyI6InViZXItdXMxIiwianRpIjoiNDA2MmM2YzktOGZmNS00ZWFmLWEyOGYtOTc1NzYyMmE0ZmI2IiwiZXhwIjoxNDkwMTcwMTk3LCJpYXQiOjE0ODc1NzgxOTcsInVhY3QiOiI0am5XSW9jQkhseUszSXhWdGFSaHliVlRmQ0MycUciLCJuYmYiOjE0ODc1NzgxMDcsImF1ZCI6IlEwc1RtdXozZV9kT0FfeTZyQXE3MW9MVmFvSllQc29JIn0.V9pbRi-c4jZs3q3uIs8ngYES_PhEZrJudfy4E1TCm5gcrtnCwzBjaJiq0OrEgJaVUwYsSS72ZYVvjqUhz7pSHvWftd6QlwSEMa9WSZFZx096vugEblpB2kzlkdtzv-SV-wJbLR5a2aYQqKOdEbEHWvHZHqBu6zzksF8S_5jvz2Kj0MGjkSZNKrSO6rfU230B2B7Sabr9qVzBtpewcfWQPVNvrseIiYlZgdIDawhhw4bxnBB5nzISO79a1H9fYAfqmzqbq16KouO9QmWpDCGBacOY76jmTvsdQrdHRH6iOrM8x2VZDD7UX5juPjIlcGE-P2DMlFcH2-xzMkA6c-G-kg" \
     -H "Content-Type: application/json" -d \
     '{"product_id": "821415d8-3bd5-4e27-9604-194e4359a449", "start_latitude":"37.775232", "start_longitude": "-122.4197513", "end_latitude":"37.7899886", "end_longitude": "-122.4021253", "seat_count": "2", "fare_id":"55c714203169a03cf816e280976fd5c1920f1574dd92a8a21cda19156b23ce06"}' \
      https://api.uber.com/v1.2/requests | jq '.'

{
  "meta": {},
  "errors": [
    {
      "status": 422,
      "code": "invalid_fare_id",
      "title": "Invalid fare id: 55c714203169a03cf816e280976fd5c1920f1574dd92a8a21cda19156b23ce06"
    }
  ]
}



{
  "status": "processing",
  "product_id": "821415d8-3bd5-4e27-9604-194e4359a449",
  "destination": {
    "latitude": 37.7899886,
    "longitude": -122.4021253
  },
  "driver": null,
  "pickup": {
    "latitude": 37.775232,
    "longitude": -122.4197513
  },
  "request_id": "0aec0061-1e20-4239-a0b7-78328e9afec8",
  "eta": null,
  "location": null,
  "vehicle": null,
  "shared": false
}

------------------------------------------------------------------------------------------------------------------------------------------
+++++++++++++++Get the request details For a ride+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------------------------------------------------------------------------------
Get the request details for a ride.

curl -H 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZXMiOlsicmVxdWVzdCIsInByb2ZpbGUiLCJoaXN0b3J5Il0sInN1YiI6Ijg4MjY5YmRlLWYwODEtNDlmNy1hZDhlLWVkZjk0YjdiMWU2ZiIsImlzcyI6InViZXItdXMxIiwianRpIjoiNDA2MmM2YzktOGZmNS00ZWFmLWEyOGYtOTc1NzYyMmE0ZmI2IiwiZXhwIjoxNDkwMTcwMTk3LCJpYXQiOjE0ODc1NzgxOTcsInVhY3QiOiI0am5XSW9jQkhseUszSXhWdGFSaHliVlRmQ0MycUciLCJuYmYiOjE0ODc1NzgxMDcsImF1ZCI6IlEwc1RtdXozZV9kT0FfeTZyQXE3MW9MVmFvSllQc29JIn0.V9pbRi-c4jZs3q3uIs8ngYES_PhEZrJudfy4E1TCm5gcrtnCwzBjaJiq0OrEgJaVUwYsSS72ZYVvjqUhz7pSHvWftd6QlwSEMa9WSZFZx096vugEblpB2kzlkdtzv-SV-wJbLR5a2aYQqKOdEbEHWvHZHqBu6zzksF8S_5jvz2Kj0MGjkSZNKrSO6rfU230B2B7Sabr9qVzBtpewcfWQPVNvrseIiYlZgdIDawhhw4bxnBB5nzISO79a1H9fYAfqmzqbq16KouO9QmWpDCGBacOY76jmTvsdQrdHRH6iOrM8x2VZDD7UX5juPjIlcGE-P2DMlFcH2-xzMkA6c-G-kg' \
'https://api.uber.com/v1.2/requests/current' | jq '.'

{
  "meta": {},
  "errors": [
    {
      "status": 404,
      "code": "no_current_trip",
      "title": "User is not currently on a trip."
    }
  ]
}
------------------------------------------------------------------------------------------------------------------------------------------