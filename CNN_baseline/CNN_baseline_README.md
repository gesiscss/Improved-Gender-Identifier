# CNN_baseline running process
The notebook path is 'Combined Code/Overall_code.ipynb'
## Information about CNN_baseline model :
#### Architecture
CNN_baseline is a CNN model with 5 convolution 2D with 64, 32, 16, 8, and 4 filters respectively. The filters have size 3X3 and stride 1X1. After each conv2D, Maxpooling was used with size 2X2 and stride 2X2. And ReLU was used as activation function.
Before the fully connnected layer, there is a flatten layer that convert the output of the last conv2D to one vector , which will be used as input to the output layer (size 1X100). Finally the output layer (1X2).
#### Training rate
To adjust the learning rate throughout training, ADADELTA (An Adaptive Learning Rate Method) was used.
### Training data
The model was trained with images comming from 2 differents datasets:
1. IMDB dataset: all the images that have face score ≥ 4.5 (33,147 images were used)
2. Wikipedia  dataset: all the images that have face score ≥ 5 (3,209 images were used)


In total the model was trained with 36,356 images
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
4. crope the faces
5. Resize the croped image to 100 X 100
6. Convert image to grayscale
7. Reshape the image
## Running CNN_baseline:
1. The prediction are made in CNN_baseline function which takes as input image_path.
2. The resulted gender is based on the confidence score (the threshold is 50%)
3. The CNN_baseline return image name and the gender
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
