import requests, random
from bs4 import BeautifulSoup
access_token='3d6c7afe90826e3599ed3e22a4ce38849f57d0b6ec57fcc402c6d88e8811bf4fed7a4017b8ab6abdf669b&expires_in=86400&user_id=183399060'
# https://oauth.vk.com/authorize?client_id=5943662%20&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends,%20status&response_type=token&v=5.52

def set_status(text_status):
	global access_token
	textt = str(text_status)
	url = 'https://api.vk.com/method/status.set?access_token={}&text={}'.format(access_token, textt)
	response = requests.get(url).text
	print(response)



response = requests.get('http://www.vktops.com/statusy-o-zhenshchinakh/')
html = response.text
soup = BeautifulSoup(html, 'html.parser')
pop_status = soup.find_all('div', class_='text')

status_is = random.choice(pop_status).get_text()
set_status(status_is)