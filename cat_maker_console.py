from PIL import Image, ImageDraw
im = Image.open('cat.jpg').convert('L')
#print(im.getpixel((101, 100)))
width, hight = im.size
#print(x, y)

# .*@#$%&
for y in range(0, hight, 10):	
	for x in range(0, width, 5):
		if im.getpixel((x, y)) < 5:
			print('$', end='')			
		elif im.getpixel((x, y)) < 50:
			print('*', end='')			
		elif im.getpixel((x, y)) < 	100:
			print('@', end='')			
		else:
			print(' ', end='')
	print('\n', end='')