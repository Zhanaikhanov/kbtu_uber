from PIL import Image, ImageDraw, ImageFont
img = Image.open('cat.jpg').convert('L')
text = 'S'
color = (0, 0, 120)
new_img = Image.new("RGB",(100,100),color)
ImageDraw.Draw(new_img).text((2, -2), text)
new_img.save('cat.jpg')