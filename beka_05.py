from PIL import Image, ImageDraw, ImageFont
im = Image.new('RGB', (600, 600), (0, 0, 120))
imDrawer = ImageDraw.Draw(im)
width =600
def font_drawer(x = 20, y = 20, text_word = 'Salem', size_of = 40, font_name = 'Lobster/Lobster.otf'):
	global width
	fnt = ImageFont.truetype(font_name, size_of)
	text_size = fnt.getsize(text_word)
	words = text_word.split(' ')
	string_text = 0
	text_words = ''
	te = []
	print(text_size)
	for word in words:
		if fnt.getsize(word)[0] > width-x:
			
			for num in range(len(word)-2,0,-1):
				first = word[0: num] 
				
				if fnt.getsize(first)[0] < width-x:
					word = first + '-\n' + word[num:]
					te.append(word)
					print(word)
					break
					 
		elif int(fnt.getsize(word)[0]+string_text) < width-x:
			#print(word, fnt.getsize(word)[0])
			string_text += fnt.getsize(word)[0]
			te.append(word)
		else:
			string_text = 0
			word = '\n'+word 
			#print(word)
			te.append(word)
			
	text_words = ' '.join(te)
	#print(text_words)
	imDrawer.text((x, y), text=text_words, font = fnt)			

font_drawer(20, 20, 'abcdefghjklmnopqrst', 70)



im.save('beak.jpg')