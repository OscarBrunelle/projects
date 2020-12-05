import myfunctions
from PIL import ImageDraw
from PIL import Image

intial_picture = Image.open(r'C:\\Users\\oscar\\Desktop\\#Oscar\\Programmation\\puzzle python\\test images\\all+.jpg')
picture = Image.open(r'C:\\Users\\oscar\\Desktop\\#Oscar\\Programmation\\puzzle python\\test images\\all+.jpg')
initial_width, initial_height = picture.size
newwidth = 100
picture.thumbnail((newwidth, int(initial_height / (initial_width / newwidth))))
width, height = picture.size
center = (int(0.5 * width)), (int(0.5 * height))

def floodfill(pixel_pos, fill_color, tolerance):
	if (pixel_pos[0] < 0 or pixel_pos[1] < 0 or pixel_pos[0] >= width or pixel_pos[1] >= height):
		print("Error: Pixel position is out of the image.")
		return
	selected_color = picture.getpixel(pixel_pos)
	queued = [pixel_pos]
	done_pixels = []
	for i in range(width):
		done_pixels.append([0] * height)
	done_pixels[pixel_pos[0]][pixel_pos[1]] = True
	number_done = 0
	while (len(queued) > 0):
		pos = queued.pop(0)
		same_color = floodfill_call(pos, selected_color, fill_color, tolerance)
		if same_color:
			next_pixels = [
				(pos[0], pos[1] - 1),
				(pos[0] + 1, pos[1]),
				(pos[0], pos[1] + 1),
				(pos[0] - 1, pos[1])
			]
			for pixel in next_pixels:
				if not(pixel[0] < 0 or pixel[1] < 0 or pixel[0] >= width or pixel[1] >= height):
					if done_pixels[pixel[0]][pixel[1]] != True:
						queued.append(pixel)
					done_pixels[pixel[0]][pixel[1]] = True
		number_done += 1
		print("Done: " + str(number_done) + "; Queued: " + str(len(queued)))
		if number_done > width * height:
			break

def floodfill_call(pixel_pos, selected_color, fill_color, tolerance):
	pixel_color = picture.getpixel(pixel_pos)
	for i in range(3):
		c = selected_color[i]
		if not(pixel_color[i] >= c - (255 * tolerance) and pixel_color[i] <= c + (255 * tolerance)):
			picture.putpixel(pixel_pos, (255, 255, 255))
			return False
	picture.putpixel(pixel_pos, fill_color)
	return True

# floodfill((0, 0), (0, 0, 0), 0.2)
# picture.show()
# floodfill(center, (255, 255, 255), 0.4)
# picture.show()

pixel_array = []
for i in range(width):
	temp_arr = [0] * height
	pixel_array.append(temp_arr)

treshold = 20
def is_different_color(pixel_color1, pixel_color2):
	total_diff = 0
	for i in range(3):
		diff = abs(pixel_color1[i] - pixel_color2[i])
		if diff > treshold:
			return True
		total_diff += abs(pixel_color1[i] - pixel_color2[i])
	if total_diff > treshold:
		return True
	return False

def is_border(a, b):
	if (a == 0 or b == 0 or a == (len(pixel_array) - 1) or b == (len(pixel_array[0]) - 1)):
		return False
	pixel = pixel_array[a][b]
	leftpixel = pixel_array[a - 1][b]
	toppixel = pixel_array[a][b - 1]
	rightpixel = pixel_array[a + 1][b]
	bottompixel = pixel_array[a][b + 1]

	bt = 65
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

for x in range(width):
	pixel_array_col = []
	for y in range(height):
		pixel_color = picture.getpixel((x, y))
		pixel_array[x][y] = pixel_color
		print(str(x) + " : " + str(y))

# border_image = Image.new("RGBA", (width,height), (255, 0, 0, 0))
for x in range(width):
	for y in range(height):
		# new_color = (0, 0, 0)
		if (is_border(x, y)):
			picture.putpixel((x, y), (255, 0, 255))
		# 	new_color = (255, 255, 255)
		# picture.putpixel((x, y), new_color)

# border_image = border_image.resize((initial_width, initial_height))
# intial_picture.paste(border_image, (0,0))
# intial_picture.show()
picture.save('results\\test-result.jpg')