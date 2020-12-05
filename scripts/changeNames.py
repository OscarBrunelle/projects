import os, shutil

for root, directories, files in os.walk(r"C:\Users\Oscar\AndroidStudioProjects\Laboratoire4Equipedefoot\app\src\main\res\drawable"):
    for file in files:
        if os.path.splitext(file)[1] == ".png":
            shutil.copy(os.path.join(root, file), os.path.join(r"C:\Users\Oscar\AndroidStudioProjects\Laboratoire4Equipedefoot\app\src\main\res\drawable\result","".join(file.lower().split(" "))))
    break
