from PIL import Image, ImageDraw, ImageFont
im = Image.open('carl.jpg')
imDrawer = ImageDraw.Draw(im)
width, hight = im.size
def font_drawer(x = 20, y = 'up', text_word = 'Salem', size_of = 40, font_name = 'Lobster/Lobster.otf'):
	global width, hight
	width -= 70
	font_hight = 0
	fnt = ImageFont.truetype(font_name, size_of)
	text_size = fnt.getsize(text_word)
	words = text_word.split(' ')
	full = ''
	tu = int(len(text_word)/(text_size[0]/width) )
	for i in range(len(text_word)):
		full+=text_word[i]
		if i % tu == 0 and i!= 0:
			if text_word[i]==' ' or text_word[i+1]==' ' or text_word[i-1]==' ':
				full+='\n'
				font_hight += text_size[1]
			else:
				full+='-\n'
				font_hight += text_size[1]

	font_hight += text_size[1]
	print(full)
	if y == 'up':
		y = 20
	elif y == 'down':
		y = hight - font_hight - 40
	imDrawer.text((x, y), text=full, font = fnt)			

font_drawer(30, 'up', 'У меня 29 по Programming Technologies', 40)
font_drawer(30, 'down', 'По Programming Technologies, Карл!!', 40)

im.save('beak.jpg')