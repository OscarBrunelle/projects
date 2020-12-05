from PIL import ImageDraw
from PIL import Image
from builtins import input

picture = Image.open(r'C:\\Users\\oscar\\Desktop\\#Oscar\\Programmation\\puzzle python\\images\\reverse-separated.png')

width, height = picture.size
threshold = 20
black_threshold = 65

def is_different_color(pixel_color1, pixel_color2):
	total_diff = 0
	for i in range(3):
		diff = abs(pixel_color1[i] - pixel_color2[i])
		if diff > threshold:
			return True
		total_diff += abs(pixel_color1[i] - pixel_color2[i])
	if total_diff > threshold:
		return True
	return False

def is_border(pixel_array, bt, a, b):
	if (a == 0 or b == 0 or a == (len(pixel_array) - 1) or b == (len(pixel_array[0]) - 1)):
		return False
	pixel = pixel_array[a][b]
	leftpixel = pixel_array[a - 1][b]
	toppixel = pixel_array[a][b - 1]
	rightpixel = pixel_array[a + 1][b]
	bottompixel = pixel_array[a][b + 1]

	if (pixel[0] < bt and pixel[1] < bt and pixel[2] < bt):
		return False
	black_around = 0
	if (leftpixel[0] < bt and leftpixel[1] < bt and leftpixel[2] < bt):
		black_around += 1
	if (toppixel[0] < bt and toppixel[1] < bt and toppixel[2] < bt):
		black_around += 1
	if (rightpixel[0] < bt and rightpixel[1] < bt and rightpixel[2] < bt):
		black_around += 1
	if (bottompixel[0] < bt and bottompixel[1] < bt and bottompixel[2] < bt):
		black_around += 1
	if (black_around > 0 and black_around < 3):
		return True
	return False
	if is_different_color(pixel, pixel_array[a - 1][b]):
		return True
	if is_different_color(pixel, pixel_array[a][b - 1]):
		return True
	return False

def find_border(image, black_threshold = 65):
	width, height = image.size

	pixel_array = []
	for i in range(width):
		temp_arr = [0] * height
		pixel_array.append(temp_arr)

	for x in range(width):
		pixel_array_col = []
		for y in range(height):
			pixel_color = image.getpixel((x, y))
			pixel_array[x][y] = pixel_color
			print(str(x) + ' : ' + str(y))

	for x in range(width):
		for y in range(height):
			# new_color = (0, 0, 0)
			if (is_border(pixel_array, black_threshold, x, y)):
				image.putpixel((x, y), (255, 0, 255))

	image.save('results\\result.png')

find_border(picture, black_threshold)
user_input = input('Enter threshold: ')
if (type(user_input) != 'int'):
	user_input = int(user_input)
threshold = user_input
while(user_input > 0):
	threshold = user_input
	find_border(picture, black_threshold)
	user_input = input('Enter threshold: ')
	if (type(user_input) != 'int'):
		user_input = int(user_input)