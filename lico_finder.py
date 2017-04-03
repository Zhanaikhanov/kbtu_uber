from PIL import Image
import os, sys, json
skin_file = sys.argv[1]

skin = Image.open(skin_file).convert('RGB')
pix = skin.load()
width, hight = skin.size

dojd_from_up = []
dojd_from_left = []
dojd_from_down = []
dojd_from_right = [] 

for x in range(0, width):
	for y in range(int(hight/4.0), hight):
		r, g, b = pix[x, y]
		if r > 235 and g > 235 and b > 235:
			continue
		else:
			dojd_from_up.append((x, y))
			break

for y in range(int(hight/4.0), hight):
	for x in range(0, width):
		r, g, b = pix[x, y]
		if r > 235 and g > 235 and b > 235:
			continue
		else:
			dojd_from_left.append((x, y))
			break

for x in range(0, width):
	for y in range(hight-int(hight/4.0),0, -1):
		r, g, b = pix[x, y]
		if r > 235 and g > 235 and b > 235:
			continue
		else:
			dojd_from_down.append((x, y))
			break

for y in range(0, hight):
	for x in range(width-int(width/4.0), 0, -1):
		r, g, b = pix[x, y]
		if r > 235 and g > 235 and b > 235:
			continue
		else:
			dojd_from_right.append((x, y))
			break

from_up = 0
from_left = 0
from_down = 0
from_right = 0



min = dojd_from_up[0][1]
for x, y in dojd_from_up:
	if y < min:
		min = y
print('from up ->', min)
from_up = min

min = dojd_from_left[0][0]
for x, y in dojd_from_left:
	if x < min:
		min = x
print('from left ->', min)
from_left = min

max = dojd_from_down[0][1]
for x, y in dojd_from_down:
	if y > max:
		max = y
print('from down ->', max)
from_down = max

max = dojd_from_right[0][0]
for x, y in dojd_from_right:
	if x > max:
		max = x
print('from right ->', max)
from_right = max


print('red lines..')
par_im = Image.open(sys.argv[2]).convert("RGB").resize((300, 300))
par_pix = par_im.load()
par_width, par_hight = par_im.size

tolwina = 5 #int(input('tolwina -> '))
for y in range(from_up-tolwina, from_up):
	for x in range(0, par_width):
		r, g, b = par_pix[x ,y]
		r = 255
		g = b = 0
		par_pix[x, y] = r, g, b

for y in range(from_down-tolwina ,from_down ) :
	for x in range(0, par_width):
		r, g, b = par_pix[x ,y]
		r = 255
		g = b = 0
		par_pix[x, y] = r, g, b

for x in range(from_left-tolwina, from_left):
	for y in range(0, par_hight):
		r, g, b = par_pix[x ,y]
		r = 255
		g = b = 0
		par_pix[x, y] = r, g, b

for x in range(from_right-tolwina, from_right):
	for y in range(0, par_hight):
		r, g, b = par_pix[x ,y]
		r = 255
		g = b = 0
		par_pix[x, y] = r, g, b		
print('red lines done')
print('eyes...')

for y in range(from_up, int( from_up+(from_down-from_up)/2) ):
	for x in range( from_left + int((from_right - from_left)/4.0 ), from_right - int((from_right - from_left)/4.0) ):
		r, g, b = par_pix[x, y]
		if r!=0 and g!=0 and b!=0 and 0.8 < r / g < 1.2 and 0.8 < r / b < 1.2 and 0.8 <  g / b < 1.2 or ( b < 30 and g < 30 and r < 40):
			print(x, y)
			r = b = 0
			g = 255
		par_pix[x, y] = r, g, b 	

eyes_from_up = []
eyes_from_down = []
scale = 9


for x in range(from_left, from_right-9):
	for y in range(from_up,  int( from_up+(from_down-from_up)/2)-9 ):
		total = 0
		for w in range(x, x+scale):
			for h in range(y, y+scale):
				r, g, b = par_pix[w, h]
				if g==255 and r==0 and b==0:

					total+=1
		if total/(scale)**2 >= 0.3:
			
			eyes_from_up.append((x, y))


for x in range(from_left, from_right):
	for y in range(int( from_up+(from_down-from_up)/2), from_up, -1):
		r, g, b = par_pix[x, y]
		if r == 0 and g == 255 and b == 0:
			eyes_from_down.append((x, y))

min = eyes_from_up[0][1]
for x, y in eyes_from_up:
	if y < min:
		min = y
eye_pos_up = min

max = eyes_from_down[0][1]
for x, y in eyes_from_down:
	if y > max:
		max = y
eye_pos_down = max


for y in range(eye_pos_up-tolwina, eye_pos_up):
	for x in range(from_left, from_right-5):
		r, g, b = par_pix[x, y]
		b = 255
		g = r = 0
		par_pix[x, y] = r, g, b

for y in range(eye_pos_down, eye_pos_down+tolwina):
	for x in range(from_left, from_right-5):
		r, g, b = par_pix[x, y]
		b = 255
		g = r = 0
		par_pix[x, y] = r, g, b
#=============================
left_eye_center = []
right_eye_center = []

eyes_from_left = []
eyes_from_right = []
eye_pos_left = 0
eye_pos_right = 0

for y in range(eye_pos_up, eye_pos_down):
	for x in range(from_left, int(from_left + (from_right - from_left)/2.0) ):
		r, g, b = par_pix[x, y]
		if r == 0 and g == 255 and b == 0:
			eyes_from_left.append((x, y))

for y in range(eye_pos_up, eye_pos_down):
	for x in range(int(from_left + (from_right - from_left)/2.0), from_left, -1):
		r, g, b = par_pix[x, y]
		if r==0 and g == 255 and b == 0:
			eyes_from_right.append((x, y))

max = eyes_from_left[0][0]
for x, y in eyes_from_left:
	if x > max:
		max = x
eye_pos_left = max

min = eyes_from_right[0][1]
for x, y in eyes_from_right:
	if x < min:
		min = x
eye_pos_right = min

for x in range(eye_pos_left-tolwina, eye_pos_left):
	for y in range(eye_pos_up, eye_pos_down):
		r, g, b = par_pix[x, y]
		r = g = 0
		b = 255
		par_pix[x, y] = r, g ,b

for x in range(eye_pos_right, eye_pos_right+tolwina):
	for y in range(eye_pos_up, eye_pos_down):
		r, g, b = par_pix[x, y]
		r = g = 0
		b = 255
		par_pix[x, y] = r, g ,b
left_eye_center.append( ( int(eye_pos_left + (eye_pos_right-eye_pos_left)/2.0) , int(eye_pos_up + (eye_pos_down-eye_pos_up)/2.0 ) ) )
radiusL = ((eye_pos_right-eye_pos_left)**2 + (eye_pos_down-eye_pos_up)**2)**0.5
#=============================

eyes_from_left = []
eyes_from_right = []
eye_pos_left = 0
eye_pos_right = 0

for y in range(eye_pos_up, eye_pos_down):
	for x in range(int(from_left + (from_right - from_left)/2.0), from_right ):
		r, g, b = par_pix[x, y]
		if r == 0 and g == 255 and b == 0:
			eyes_from_left.append((x, y))

for y in range(eye_pos_up, eye_pos_down):
	for x in range(from_right, int(from_left + (from_right - from_left)/2.0), -1):
		r, g, b = par_pix[x, y]
		if r==0 and g == 255 and b == 0:
			eyes_from_right.append((x, y))

min = eyes_from_left[0][0]
for x, y in eyes_from_left:
	if x < min:
		min = x
eye_pos_left = min

max = eyes_from_right[0][1]
for x, y in eyes_from_right:
	if x > max:
		max = x
eye_pos_right = max

for x in range(eye_pos_left-tolwina, eye_pos_left):
	for y in range(eye_pos_up, eye_pos_down):
		r, g, b = par_pix[x, y]
		r = g = 0
		b = 255
		par_pix[x, y] = r, g ,b

for x in range(eye_pos_right, eye_pos_right+tolwina):
	for y in range(eye_pos_up, eye_pos_down):
		r, g, b = par_pix[x, y]
		r = g = 0
		b = 255
		par_pix[x, y] = r, g ,b
right_eye_center.append( ( int( eye_pos_left + (eye_pos_right-eye_pos_left)/2.0) , int(eye_pos_up + (eye_pos_down-eye_pos_up)/2.0 ) ) )
#=============================
radiusR = ((eye_pos_right-eye_pos_left)**2 + (eye_pos_down-eye_pos_up)**2)**0.5
radius = 0
if radiusR > radiusL:
	radius = radiusR
else:
	radius = radiusL

for y in range(from_up, from_up + int( (from_down - from_up)/2.0) ): 
	for x in range(from_left, int(from_left+(from_right-from_left)/2.0) ):
		#print(((x - left_eye_center[0][0])**2+(y - left_eye_center[0][1])**2)**0.5, radius)
		
		if ((x - left_eye_center[0][0])**2+(y - left_eye_center[0][1])**2)**0.5 < radius:
			r, g, b = par_pix[x, y]
			g = 255
			r = b = 0
			par_pix[x, y] = r, g ,b

for y in range(from_up, from_up + int( (from_down - from_up)/2.0) ): 
	for x in range(int(from_left+(from_right-from_left)/2.0), from_right):
		if ((x - right_eye_center[0][0])**2+(y - right_eye_center[0][1])**2)**0.5 < radius:
			r, g, b = par_pix[x, y]
			g = 255
			r = b = 0
			par_pix[x, y] = r, g ,b
#print(left_eye_center[0][0], left_eye_center[0][1])
#print(radius)
#=============================

print('eyes done')
print('saving...')
par_im.save('lico.jpg')
skin.save('lico_found.jpg')
print('opening..')
os.system('firefox lico.jpg')