import zipfile as zf
import tarfile as tf
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import os
import pandas as pd
import requests

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
    

def extract_files(dataset, path_to_data, path_to_output):
    if dataset == 'twitter':
        extract_zip(path_to_data, path_to_output)
        for file in os.listdir(path_to_output + path_to_data[:-4]):
            if file == '_a_results32langs.zip':
                extract_zip(path_to_output+path_to_data[:-4]+'/'+file, path_to_output + path_to_data[:-4]+'/')
                
    elif dataset == 'imdb' or dataset == 'wiki':
        extract_tar(path_to_data, path_to_output)
#             if dataset == 'imdb':
#                 path_to_images = path_to_output + 'imdb_crop/'
#             else:
#                 path_to_images = path_to_output + 'wiki/'
    else:
        extract_zip(path_to_data, path_to_output)