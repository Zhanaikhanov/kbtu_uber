from PIL import Image, ImageDraw, ImageFont
im = Image.open('carl.jpg')
imDrawer = ImageDraw.Draw(im)
width, hight = im.size
def font_drawer(x = 20, y = 'up', text_word = 'Salem', size_of = 40, font_name = 'Lobster/Lobster.otf'):
	global width, hight
	width -= 70
	font_hight = 0
	font_width = 0
	fnt = ImageFont.truetype(font_name, size_of)
	text_size = fnt.getsize(text_word)
	words = text_word.split(' ')
	full = ''
	for word in words:
		full += word
		font_width = fnt.getsize(full)[0]
		if fnt.getsize(word)[0] + font_width > width - x:
			full += ' \n'
			font_hight += fnt.getsize(full)[1]
		full += ' '

	print(full)

	if y == 'up':
		y = 20
	elif y == 'down':
		y = hight - font_hight - 40
	imDrawer.text((x, y), text=full, font = fnt)			

font_drawer(70, 'up', 'У меня 29 по Programming Technologies', 40)
font_drawer(70, 'down', 'По Programming Technologies, Карл!!', 40)

im.save('beak.jpg')