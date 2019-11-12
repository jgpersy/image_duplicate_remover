from Tkinter import Tk
from tkFileDialog import askdirectory
from PIL import Image
import os.path
import hashlib

number_of_duplicates = 0

#Set of hash values for images
hashes = set()

#Hides unnecessary TK root window
Tk().withdraw()

#User selects desired folder
folder = askdirectory()

#Hash every image from its byte form, delete image if hash is a duplicate
#Else, store it in the set

for filename in os.listdir(folder):

    #If file is any of following image types
    if filename.endswith(".jpeg") or filename.endswith(".jpg") or \
    filename.endswith(".png") or filename.endswith(".bmp"):

        image_path = os.path.join(folder, filename)
        
        img = Image.open(image_path)

        #Produce hash of the image's byte representation
        img_hash = hashlib.md5(img.tobytes()).digest()

        #Print hashes for shits and giggles if you want, simply uncomment below
        #print(img_hash)

        
        if img_hash in hashes:
            os.remove(image_path)
            
            ##register a duplicate
            number_of_duplicates += 1
            
        else:
            hashes.add(img_hash)
            
    #If file isn't an image
    else:
        continue


result_message = "Deleted " + str(number_of_duplicates) + " duplicates"
print(result_message)
