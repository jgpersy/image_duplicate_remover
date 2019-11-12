import sys
import os.path
from PIL import Image
import hashlib

#Sets the default image folder to the current dir
#Also allows folder to be given via argument

hashes = set()
number_of_duplicates = 0

IMAGE_FOLDER_PATH = os.getcwd()

if len(sys.argv) > 1:
    IMAGE_FOLDER_PATH = sys.argv[1]

    if not os.path.exists(IMAGE_FOLDER_PATH):
        print("Error: Path is not valid or does not exist")
        print("Please provide a filepath as a parameter or leave blank to use the current directory")
        sys.exit()

#Verify if user wants to use the folder
user_input = raw_input("Using " + IMAGE_FOLDER_PATH + " as image folder, are you sure? Y/N \n")

#Exit if the user doesn't want to proceed
if user_input == "Y" or user_input == "y":
    print("OK proceeding to delete duplicates in " + IMAGE_FOLDER_PATH)
else:
    print("Exiting")
    sys.exit()

#print out folder and perform Yes/no check 

print(IMAGE_FOLDER_PATH)

print("Processing folder " + IMAGE_FOLDER_PATH)


for filename in os.listdir(IMAGE_FOLDER_PATH):

    #If file is any of following image types
    if filename.endswith(".jpeg") or filename.endswith(".jpg") or \
    filename.endswith(".png") or filename.endswith(".bmp"):

        image_path = os.path.join(IMAGE_FOLDER_PATH, filename)
        
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

