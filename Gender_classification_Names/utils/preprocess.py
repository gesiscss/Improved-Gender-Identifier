import zipfile as zf
import tarfile as tf
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import os
import pandas as pd
import requests
from scipy.io import loadmat
import numpy as np

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
    
def get_names(x):
    if len(x)>0:
        return x[0]
    else:
        return ''
    
def extract_mat(mat_file, dataset):
    mat = loadmat(mat_file)  # load mat-file
    mdata = mat[dataset]  # variable in mat file
    mdtype = mdata.dtype
    ndata = {n: mdata[n][0, 0] for n in mdtype.names}
    columns = [n for n, v in ndata.items()]# if v.size == ndata['numIntervals']]

    dob = mdata['dob'][0,0][0]
    photo_taken = mdata['photo_taken'][0,0][0]
    full_path = [mdata['full_path'][0,0][0][n][0] for n in range(len(mdata['full_path'][0,0][0]))]
    gender = mdata['gender'][0,0][0]
    name = np.array(list(map(get_names, mdata['name'][0,0][0])))
    face_location = mdata['face_location'][0,0][0]
    face_score = mdata['face_score'][0,0][0]
    second_face_score = mdata['second_face_score'][0,0][0]
    #celeb_id = mdata['celeb_id'][0,0][0]

    metadf = pd.DataFrame({"dob": dob, "photo_taken":photo_taken, "full_path":full_path, "gender":gender, "name":name, "face_location":face_location, "face_score":face_score, "second_face_score":second_face_score})
                  #index=celeb_id)
    metadf['full_path'] = metadf['full_path'].apply(lambda x: x.split('/')[1])
    metadf.to_csv(f"{dataset}.csv")
    

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