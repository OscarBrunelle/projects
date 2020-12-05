import os
path = "C:\\Users\\oscar\Desktop\\#Oscar\Programmation\\ferrero\\"
for i in range(16):
	original_name = path + str(i) + ".png"
	new_name = path + "storage-" + str(i) + ".png"
	os.rename(original_name,new_name)