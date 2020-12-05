from builtins import input
# from time import time
from myfunctions import *

red_fact = 4
# starting_time = time()

picture = Image.open(r'C:\\Users\\oscar\\Desktop\\#Oscar\\Programmation\\puzzle python\\images\\reverse-separated.png')
width,height = picture.size
picture.thumbnail((width / red_fact, height / red_fact))
width,height = picture.size
pieces = []

def detour_piece(image,x,y):
	i,j = x,y
	# for i in range(5):
	# 	for j in range(5):
	# 		color = (255,0,255)
	# 		picture.putpixel((x-i,y-j),color)
	(image,(min_x,min_y,max_x,max_y),filled_pixels) = floodfill(image, (x,y), (255,0,255), 0.1, 1)
	(image,(min_x,min_y,max_x,max_y),filled_pixels) = fillborders(image, (x,y), filled_pixels, (0,0,255))
	(image,(min_x,min_y,max_x,max_y),filled_pixels) = fillborders(image, (x,y), filled_pixels, (0,0,255))
	crop_x = max(0, min_x - 2)
	crop_y = max(0, min_y - 2)
	crop_width = min(width, max_x + 2)
	crop_height = min(height, max_y + 2)
	cropped_image = image.crop((crop_x,crop_y,crop_width,crop_height))
	cropped_image.save('images\\cropped\\' + str(len(pieces)) + '.png')
	pieces.append([min_x,min_y,max_x,max_y])
	return image

bg_threshold = 175
step = int(min(width / 25, height / 25))
x = step
y = step
while x < width:
	while y < height:
		pixel_color = picture.getpixel((x,y))
		color_average = (pixel_color[0] + pixel_color[1] + pixel_color[2]) / 3
		if (color_average < bg_threshold):
			if len(pieces) > 0:
				flag = True
				for piece in pieces:
					if (x >= piece[0] and x <= piece[2]) and (y >= piece[1] and y <= piece[3]):
						flag = False
						break
				if flag:
					picture = detour_piece(picture,x,y)
			else:
				picture = detour_piece(picture,x,y)
		y += step
	y = step
	x += step

# print("Time taken with reduction = " + str(red_fact) + ": " + str(time() - starting_time))
picture.show()
picture.save('results\\result_separate.png')