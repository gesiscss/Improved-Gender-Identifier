
# coding: utf-8

# In[ ]:
import sys
import json
import zipfile as zf
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import random
import os


def extract_files(input_path): 
    # extracting the files from the zip archive
    files = zf.ZipFile(input_path, 'r')
    files.extractall(input_path.split(input_path.split('/')[-1])[0])
    files.close()

def preprocess_images(file_name, height, width):
    # resizing and converting all the images to the RGB format
    im = Image.open(file_name)
    if im.size[0] + im.size[1] < 400: #smaller images are not suitable for M3
        print(f'{file_name} is too small. Skip.')
        return
    resized_im = im.resize((height, width))
    resized_im.convert('RGB').save(file_name)
        

# Generate random numbers
def randomNumber(Numberlength):
    for x in range(Numberlength):
        number= random.randint(1,10001)
    return number


input_path = sys.argv[1]
output_path = sys.argv[2]
extract_files(input_path)
output_file = input_path[:-4] + '.csv'
files_path = input_path[:-4]+'/'
data = {}
data['images'] = []
for Imagename in os.listdir(files_path): # Get the images from directory
    try:
        if "jpg" in Imagename or 'png' in Imagename:
            Image_location=files_path+Imagename # Get the image loacation of each image
            preprocess_images(Image_location, 224, 224)
            data['images'].append({
                "description":"", 
                "id": Imagename,
                "img_path": Image_location, 
                "lang": "en", 
                "name": "", 
                "screen_name": ""
            })
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        
with open(output_path + 'data.jsonl', 'w') as json_file: 
    # json file for m3 is created  
    json.dump(data, json_file)

