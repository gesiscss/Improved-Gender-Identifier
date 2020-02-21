
# Improved Gender Inference



## Requirements

* Keras (Using TensorFlow backend)

## About

GIGIDL takes vision inputs specifically image of a person or web address of a image. Generally GIGIDL identify faces from the image and take this single or multiple faces as a input and provides the gender of that face or faces with the probability of accuracy if it’s human otherwise it skip the prediction of image data.


## Training

To train our model we have used full dataset of IMDB and WIKI together (after cleaning total 36,356 images of  human). We have used 10-fold cross-validation to minimize the bias and got 98.28 % training accuracy.



## How to Use: 

This model takes an input image and gives the prediction as an output. You need to 
        a) Copy or clone this package (```git clone https://github.com/gesiscss/Improved-Gender-Identifier.git```) and follow the instructions.
        b) Preprocess (for a bunch of images) like resize to get them reshaped. Use the preprocess script to make the images right.


You can use this model to predict the gender using image or a bunch of images (same extension e.g., only jpg or png and so on ) as data in any format but need to mention the extension (e.g., jpg, png etc.). 

Image could be inputed mostly 2 different ways:

   * Web-link

   Simply provide the web address of the image or images as web link in the system (e.g., ```web_link = “https://github.com/gesiscss/Improved-Gender -Identifier/blob/master/GIGIDL/Data/a.jpeg”```).
   
   * Directory


   You need to create a directory called ```‘data’``` in your default directory or individually and keep your image or images in that directory in the system (e.g., ```[default directory] /data/```).


## Install





## Datasets


* IMDB Dataset



Source: https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/

What is in the data: The IMDB dataset contains 460,723 facial images (with gender and age labels) of film stars, predominantly Hollywood actors and actresses. We have taken only the frontal faces which has the face score 4.5 or above and get 33,147 facial images.

Number of images:  33,147

Male images: 14370

Female images: 18777



* Wikipedia Dataset


Source: https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/

What is in the data: Wikipedia dataset includes 62,328 (with gender and age labels) of celebrities from various fields, such as sports, politics, social events, and the film industry. We have taken only the frontal faces which has the face score 5 or above and get 3,209 facial images.

Number of images: 3,209

Male images: 1830

Female images: 1379



* Scholars Dataset (manual labeled at GESIS)


Source: https://gesis.org/

What is in the data: Images of xx scholars which have been manually labeled by the coders at GESIS. 

Number of images: 3,324

Male images: 1,953

Female images: 1,371


## Comparison:

* CNN performed better than M3 to predict IMDB and WIKI datasets as CNN trained on IMDB+WIKI datasets.

* For scholar dataset, M3 have performed better as M3 trained on social network images and this dataset is contained different scholars images from different parts of the world.

* Quality of OUI dataset is very bad especially females as all the images have collected by doing continuous shot of front camera using mobile app randomly which is not the similar quality like social network profile. So, M3 have performed worst for OUI dataset.

* As M3 have trained on particularly twitter profile so for twitter dataset it’s normal to show better results.

* Every performance have huge differences between male and female images. We have checked the reasons and got some problems which need to be minimized to get better performance for female and that is, 

        a) Bad performance for coloured data 
        b) Better performance when the canvas is not coloured i.e. noisy 
        c) More better when the canvas is perfectly white. For example, we have tried to predict using gender shade datasets which is very noisy and coloured female images only and got accuracy 0.67 when for all female it was 0.58 using GIGIDL. Then we removed the images which background is so much noisy and coloured and remained only coloured but white background then we have got accuracy 0.71 i.e. the performance have improved depending on the background colour.

## Note: 

Quality images means low resolution, background is noisy, face is not frontal, side view or multiple objects in the image, have eye glass, cap or cloths top to the head and so on.



## Limitations

We have some limitations in our training model i.e.,

        a) Accuracy for females is lower than the accuracy for males.
        b) Predictions for dark, low resolutions and less contrast images is lower.
        c) For the people of east asia prediction accuracy is also lower.



## FAQs

## More Questions

## License


