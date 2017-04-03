from PIL import Image
import json 
import os, sys
skin_file = sys.argv[1]
image = Image.open(skin_file).convert('RGB').resize((300, 300))
width, hight = image.size
pix = image.load()

count_of_black = 0
center_x = 150
center_y = 150

for y in range(0, 300):
	for x in range(0, 300):
		r, g, b = pix[x ,y]
		r = int(r * 0.7)
		g = int(g * 0.7)
		b = int(b * 0.7)
		pix[x, y] = r, g, b

radius = 5
eye_color = []
try:
	while radius < 150:
		for y in range(center_y-radius, center_y+radius):
			for x in range(center_x-radius, center_x+radius):
				r, g, b = pix[x, y]
				if r < 30 and g < 30 and b < 30 and ((x - center_x)**2+(y - center_y)**2)**0.5 <= radius:
					#print(x, y)
					count_of_black+=1
					eye_color.append((r, g, b))
		radius+=1
		if count_of_black > 30 :
			print(radius)
			break


	eye_from_up = []
	for x in range(center_x - radius, center_x + radius):
		for y in range(center_y - radius, center_y + radius):
			r, g, b = pix[x, y]
			if (r, g, b) in eye_color:
				eye_from_up.append((x, y))


	min = eye_from_up[0][1]
	for x, y in eye_from_up:	
		if y<min:
			min = y
	from_up = min
	from_down = from_up + 5

	left_eye_center_y = int(from_up + (from_down - from_up)/2.0) 
	right_eye_center_y = int(from_up + (from_down - from_up)/2.0)

	left_eye_center_x = int(   center_x -  (radius**2 - (center_x - from_up)**2)**0.5    )
	right_eye_center_x = int(   center_x +  (radius**2 - (center_x - from_up)**2)**0.5    ) 



	print(right_eye_center_x, right_eye_center_y)
	for y in range(0, width):
		for x in range(0, hight):
			r, g, b = pix[x, y]
			if ( (x - left_eye_center_x)**2 + (y - left_eye_center_y)**2 )**0.5 < 20 or ( (x - right_eye_center_x)**2 + (y - right_eye_center_y)**2 )**0.5 < 20:
				r = b = 0
				g = 255
			pix[x, y] = r, g, b
except:
	print('no eyes')



image.save('wall_finder.jpg')
os.system('firefox wall_finder.jpg')
