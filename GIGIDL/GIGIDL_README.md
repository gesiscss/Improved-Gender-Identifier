# GIGIDL running process

The notebook path is 'Combined Code/Overall_code_new.ipynb'

## Requirements

numpy,  pandas, keras, PIL, dlib, face_recognition, sklearn, os, cv2, sys

## Data

All datasets are saved here: 175.238.89:/bigdisk/gender_inference/Unpruned_data/ in .zip or .tar format. They should not be modified or de-archived. Following data is used:

* wiki: 62304 images as a .tar.bz archive
* IMDB: 460723 images as a .tar archive
* Twitter: 3326 images as a .zip archive
* Scholar: 2 csv files with image URLs
* OUI: 19370 images as a .zip archive
* Gender Shade: 1270 images as a .zip archive

#### You have to create a folder called "Data" and put the original data in this folder.

## Image Processing:
1. De-archive the images and store a path to images 
2. Save image URLs to the list "images" (they might be in one folder or several folders)
3. Detect faces in the image and return face_frames
4. Resize image to 100 X 100
5. Convert image to grayscale
6. Reshape the image
## Running GIGIDL:
1. The prediction are made in GIGIDL function which takes as input image_path.
2. The resulted gender is based on the confidence score (the threshold is 50%)
3. The GIGIDL return image name and the gnder
4. The resulted output contains image name, predicted gender. Results are saved in "Data" folder in CSV format.
## Extracting annotations:

### The format of annotation files:

* imdb and wiki: .mat files where gender is indicated as 1.0 if male and 0.0 if female
* twitter: a .csv file for each folder of images where gender is indicated as 'indicated_gender' equal to 'male or 'female' and 'orga' (this is after processing, only those annotations are taken where 'indicated_gender:confidence' >= 0.8)
* gender_shade: a .csv file where gender is indicated with 'Female' or 'Male'
* scholar: a .xlsx file with 2 sheets for male and female where gender is indicated with 'F' or 'M'
* OUI: 5 .txt documents with :  user_id, original_image, face_id and gender 

### The process for extracting annotations:
####  OUI: 
1. we read each file as Dataframe first and then append all the files to one dataframe. 
2. After that we create new column: "Image_name" each row of this column has the following format: 'user_id'+'/'+ 'face_id'+'.'+'original_image'( format the image name in the annotation dataframe to be the same as images)
3. we delete all the columns except for "Image_name" and "gender"

## Calculating performance measurements

1. The metadf from annotations and predicted results are merged into one dataframe
2. The confusion matrix (from sklearn) is printed based on true and predicted values (columns 'predicted_gender' and 'gender' respectively)
3. The classification report (from sklearn) is created and overall precision, recall and f-1 score are calculated as weighted average metrics.
