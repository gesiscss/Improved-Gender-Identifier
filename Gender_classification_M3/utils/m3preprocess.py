
# coding: utf-8



import zipfile as zf
import tarfile as tf
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import os
import pandas as pd
import requests
from PIL import Image
from io import BytesIO

# Extracting images from the zip archive
def extract_zip(path_to_data, path_to_output):
    files = zf.ZipFile(path_to_data, 'r')
    files.extractall(path_to_output)
    files.close()
    
def extract_tar(path_to_data, path_to_output):
    if path_to_data.endswith("tar.gz"):
        files = tf.open(path_to_data, "r:gz")
    else:
        files = tf.TarFile(path_to_data, 'r')
    files.extractall(path_to_output)
    files.close()
    

# Convert all the images in the RGB formate
def preprocess_images(file_name, height, width, skip = True):
    try:
        im = Image.open(file_name)
    except:
        print("Skipping unreadable image")
        return False
    extrema = im.convert("L").getextrema()
    if extrema[0] == extrema[1]:
        return False
    
    if skip == True:
        if im.size[0] + im.size[1] < 400:
            print(f'{file_name} is too small. Skip.')
            return
    resized_im = im.resize((height, width))
    resized_im.convert('RGB').save(file_name)
    return True
    


def extract_files(dataset, path_to_data, path_to_output):
    if dataset == 'twitter':
        extract_zip(path_to_data, path_to_output)
        for file in os.listdir(path_to_output + path_to_data[:-4]): 
            if file == 'Twitter.zip' or file == '_a_results32langs.zip':
                extract_zip(path_to_output+path_to_data[:-4]+'/'+file, path_to_output + path_to_data[:-4]+'/')
        path_to_images = path_to_output + path_to_data[:-4]+'/'+ 'Images/'
            
    elif dataset == 'gender_shade':
        extract_zip(path_to_data, path_to_output)
        for file in os.listdir(path_to_output):
            if file == 'PPB-2017.zip':
                extract_zip(path_to_output+file, path_to_output)  
        path_to_images = path_to_output + 'PPB-2017/'
    elif dataset == 'imdb' or dataset == 'wiki':
        extract_tar(path_to_data, path_to_output)
        if dataset == 'imdb':
            path_to_images = path_to_output + 'imdb_crop/'
        else:
            path_to_images = path_to_output + 'wiki/'
    else:
        extract_zip(path_to_data, path_to_output)
        if dataset == 'oui':
            path_to_images = path_to_output + 'OUI/'
        elif dataset == 'scholar':
            extract_zip(path_to_data, path_to_output)
            extract_zip(path_to_output+'scholar_images.zip', path_to_output+'scholar_images/')
            path_to_images = path_to_output+'scholar_images/'
        else:
            path_to_images = path_to_output
    print('Files successfully extracted to ', path_to_images)
    return path_to_images

def url_to_image(url, file_name):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.save(file_name)
    
    
def fill_image_names(path, scholar):
    for name in os.listdir(path):
        images = os.listdir(path+name)
        images = [int(image.split('image')[1][:-4]) for image in images] #extracting image numbers for sorting
        images.sort()
        image_names = [path + name + '/image'+ str(image_num) + '.jpg' for image_num in images[:5]]
        while len(image_names) < 5:
            image_names = image_names + [None]
        scholar.loc[scholar['Name'] == name, 'Image1':'Image5'] = image_names



def get_scholar_data(path_to_images, path_to_output):
    global scholar
    scholar = pd.DataFrame(columns=['Name', 'Gender', 'Image1', 'Image2', 'Image3', 'Image4', 'Image5'])
    scholar['Name'] = os.listdir(path_to_images+'scholar_female/') + os.listdir(path_to_images+'scholar_male/')
    scholar['Gender'][:len(os.listdir(path_to_images+'scholar_female/'))] = 'F'
    scholar['Gender'][len(os.listdir(path_to_images+'scholar_female/')):] = 'M'

    fill_image_names(path_to_images+'scholar_female/', scholar)
    fill_image_names(path_to_images+'scholar_male/', scholar)
    return scholar
