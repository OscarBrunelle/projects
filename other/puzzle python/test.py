from myfunctions import *

picture = Image.open(r'C:\\Users\\oscar\\Desktop\\#Oscar\\Programmation\\puzzle python\\test images\\all+.jpg')
picture = floodfill(picture, (0,0), (255,0,255), 0.2)
picture.show()