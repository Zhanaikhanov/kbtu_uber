from PIL import Image, ImageDraw
im = Image.open('carl.jpg').convert('RGB')
#print(im.getpixel((101, 100)))
width, hight = im.size
#color = (0, 0, 0)
#new_im = Image.new("RGB", (1200, hight), color)
pix = im.load()

center_x, center_y = int(width/2.0), int(hight/2.0)
max_black = int( (center_y**2+center_x**2)**0.5 )
print(max_black)

radius = 0
t=0
for y in range(0, hight):
	for x in range(0, width):
		radius = int(((x-center_x)**2+(y-center_y)**2)**0.5)
		coef = 1.0/max_black
		power = 1 - 1.1*coef*radius
		r, g, b = pix[x, y]
		#==================
		r = int(r * power)  
		g = int(g * power)	
		b = int(b * power)
		#==================
		pix[x, y] = r, g, b
		
im.save('sepia.jpg')	
