from PIL import ImageDraw
from PIL import Image

# mode: 0 normal, 1 overflood (fills 1 pixel around), 2 only borders
def floodfill(image, pixel_pos, fill_color = (255,0,255), tolerance = 0.2, mode = 0):
	width,height = image.size
	if (pixel_pos[0] < 0 or pixel_pos[1] < 0 or pixel_pos[0] >= width or pixel_pos[1] >= height):
		print("Error: Pixel position is out of the image.")
		return

	min_x = pixel_pos[0]
	min_y = pixel_pos[1]
	max_x = pixel_pos[0]
	max_y = pixel_pos[1]
	selected_color = image.getpixel(pixel_pos)
	queued = [pixel_pos]
	filled_pixels = []
	done_pixels = []
	for i in range(width):
		done_pixels.append([0] * height)

	done_pixels[pixel_pos[0]][pixel_pos[1]] = True
	number_done = 0
	while (len(queued) > 0):
		pos = queued.pop(0)
		return_val = floodfill_call(image, pos, selected_color, fill_color, tolerance, mode)
		if return_val == 0:
			if pos[0] < min_x:
				min_x = pos[0]
			elif pos[0] > max_x:
				max_x = pos[0]
			if pos[1] < min_y:
				min_y = pos[1]
			elif pos[1] > max_y:
				max_y = pos[1]
			filled_pixels.append(pos)

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
		elif return_val == 1:
			filled_pixels.append(pos)
		number_done += 1
		# print("Done: " + str(number_done) + "; Queued: " + str(len(queued)))
		if number_done > width * height:
			break
	return (image,(min_x,min_y,max_x,max_y),filled_pixels)

def floodfill_call(image, pixel_pos, selected_color, fill_color, tolerance, mode):
	pixel_color = image.getpixel(pixel_pos)

	for i in range(3):
		c = selected_color[i]
		t = 255 * tolerance
		if not(pixel_color[i] <= c + t):#not(pixel_color[i] >= c - t and pixel_color[i] <= c + t):
			if mode == 1:
				image.putpixel(pixel_pos, fill_color)
				return 1
			elif mode == 2:
				image.putpixel(pixel_pos, fill_color)
				return 2
			return -1
	
	if mode == 0 or mode == 1:
		image.putpixel(pixel_pos, fill_color)
	return 0

def fillborders(image, pixel_pos, filled_pixels, fill_color = (255,0,255)):
	width,height = image.size
	if (pixel_pos[0] < 0 or pixel_pos[1] < 0 or pixel_pos[0] >= width or pixel_pos[1] >= height):
		print("Error: Pixel position is out of the image.")
		return

	min_x = pixel_pos[0]
	min_y = pixel_pos[1]
	max_x = pixel_pos[0]
	max_y = pixel_pos[1]
	selected_color = image.getpixel(pixel_pos)
	queued = [pixel_pos]
	new_filled_pixels = []
	done_pixels = []
	for i in range(width):
		done_pixels.append([0] * height)

	done_pixels[pixel_pos[0]][pixel_pos[1]] = True
	number_done = 0
	while (len(queued) > 0):
		pos = queued.pop(0)
		# if image.getpixel(pos) != selected_color:
		# 	print(image.getpixel(pos))
		return_val = fillborders_call(image, pos, filled_pixels, selected_color, fill_color)
		if return_val == 0:
			if pos[0] < min_x:
				min_x = pos[0]
			elif pos[0] > max_x:
				max_x = pos[0]
			if pos[1] < min_y:
				min_y = pos[1]
			elif pos[1] > max_y:
				max_y = pos[1]

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
		# print("Done: " + str(number_done) + "; Queued: " + str(len(queued)))
		if number_done > width * height:
			break
	return (image,(min_x,min_y,max_x,max_y),new_filled_pixels)

def fillborders_call(image, pixel_pos, filled_pixels, selected_color, fill_color):
	pixel_color = image.getpixel(pixel_pos)
	if pixel_color != selected_color:
		return -1

	neighbours = [
		(pixel_pos[0], pixel_pos[1] - 1),
		(pixel_pos[0] + 1, pixel_pos[1]),
		(pixel_pos[0], pixel_pos[1] + 1),
		(pixel_pos[0] - 1, pixel_pos[1])
	]
	for neighbour in neighbours:
		flag = -1
		for filled_pixel in filled_pixels:
			if filled_pixel == neighbour:
				flag = True
				break
		neighbour_color = image.getpixel(neighbour)
		if not(flag) and neighbour_color != selected_color:
			image.putpixel(pixel_pos, fill_color)
			index = 0
			# for filled_pixel in filled_pixels:
			# 	if filled_pixel == pixel_pos:
			# 		filled_pixels.remove(index)
			# 		break
			# 	index += 1
			return 0

	return 0