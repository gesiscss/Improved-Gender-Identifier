
# Improved Gender Inference



## Requirements

* Keras (Using TensorFlow backend)

## About

GINN takes vision inputs specifically image of a person or web address of a image. Generally GINN identify faces from the image and take this single or multiple faces as a input and provides the gender of that face or faces with the probability of accuracy if it’s human otherwise it skip the prediction of image data.


## How to Use: 

This model takes an input image and gives the prediction as an output. You need to 
        a) Copy or clone this package (```git clone https://github.com/gesiscss/Improved-Gender-Identifier.git```) and follow the instructions.
        b) Preprocess (for a bunch of images) like resize to get them reshaped. Use the preprocess script to make the images right.


You can use this model to predict the gender using image or a bunch of images (same extension e.g., only jpg or png and so on ) as data in any format but need to mention the extension (e.g., jpg, png etc.). 

Image could be inputed mostly 2 different ways:

   * Web-link

   Simply provide the web address of the image or images as web link in the system (e.g., ```web_link = “https://github.com/gesiscss/Improved-Gender -Identifier/blob/master/Gender_classification_CNN/Data/a.jpeg”```).
   
   * Directory


   You need to create a directory called ```‘data’``` in your default directory or individually and keep your image or images in that directory in the system (e.g., ```[default directory] /data/```).


## Install





## Datasets


* IMDB Dataset



Source: ```https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/```

What is in the data: The IMDB dataset contains 460,723 facial images (with gender and age labels) of film stars, predominantly Hollywood actors and actresses. We have taken only the frontal faces which has the face score 4.5 or above and get 33,147 facial images.

Number of images:  33,147

Male images: 14370

Female images: 18777



* Wikipedia Dataset


Source: ```https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/```

What is in the data: Wikipedia dataset includes 62,328 (with gender and age labels) of celebrities from various fields, such as sports, politics, social events, and the film industry. We have taken only the frontal faces which has the face score 5 or above and get 3,209 facial images.

Number of images: 3,209

Male images: 1830

Female images: 1379



* Scholars Dataset (manual labeled at GESIS)


Source: (gesis)[https://gesis.org/]

What is in the data: Images of xx scholars which have been manually labeled by the coders at GESIS. 

Number of images: 3,324

Male images: 1,953

Female images: 1,371


## FAQs

## More Questions

## License


