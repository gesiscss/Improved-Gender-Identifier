Modified on 09.06.2020



# M3 running process

The notebook path is 'Combined Code/Full_model.ipynb'

## Requirements

numpy
pandas
json
pathlib
m3inference
collections
urllib.request
re
os
csv 
sys
string 
operator
sklearn
io
scipy.io

## Data

All datasets are saved here: 175.238.89:/bigdisk/gender_inference/Unpruned_data/ in .zip or .tar format. They should not be modified or de-archived. 
Following data is used:
* wiki: 62304 images as a .tar.bz archive
* IMDB: 460723 images as a .tar archive
* Twitter: 3326 images as a .zip archive
* Scholar: 2 csv files with image URLs 
* OUI: 19370 images as a .zip archive
* Gender Shade: 1270 images as a .zip archive


## Input variables

You should specify the following variables to run code:
* dataset (twitter, wiki, imdb, gender_shade, scholar or oui)
* path_to_data (path to the archive)
* path_to_output (path to where the images should be extracted to and where the intermediate results will be stored)


## Image Processing:

1. De-archive the images and store a path to images with extract_files function from 'utils/m3preprocess.py'
2. Save image URLs to the list "images" (they might be in one folder or several folders)
3. Pre-process images (change the size and convert to RGB) using function preprocess_images from 'utils/m3preprocess.py' and store image names and paths to the dictionary "data". *The json is saved at path_to_output+'data.jsonl'*

## Running M3:

1. The prediction are made in M3_inference function which takes as input path_to_output and path to json.
2. First all predictions are made with m3.infer(data['images']). *Predictions are saved at path_to_output+'predictions.json'*
3. The resulted gender is based on the confidence score (the threshold is 50%) 
4. The resulted output contains file name, predicted gender and boolean variable 'is_org' which indicates if there are more than one faces on an image. *Result is saved at path_to_output+'result.csv'*

## Extracting annotations:

The format of annotation files:
* imdb and wiki: .mat files where gender is indicated as 1.0 if male and 0.0 if female
* twitter: a .csv file for each folder of images where gender is indicated as 'indicated_gender' equal to 'male or 'female' and 'orga' (this is after processing, only those annotations are taken where 'indicated_gender:confidence' >= 0.8)
* gender_shade: a .csv file where gender is indicated with 'Female' or 'Male'
* scholar: a .xlsx file with 2 sheets for male and female where gender is indicated with 'F' or 'M'
* oui: 

here the process for extracting annotations will be described

## Calculating performance measurements

1. The metadf from annotations and predicted results are merged into one dataframe
2. The column with true gender column is modified to contain values 'female' or 'male'
3. The confusion matrix (from sklearn) is printed based on true and predicted values (columns 'predicted_gender' and 'gender' respectively)
4. The classification report (from sklearn) is created and overall precision, recall and f-1 score are calculated as weighted average metrics. 
5. The confusion matrix and overall scores are saved to 'performance_result.csv'











