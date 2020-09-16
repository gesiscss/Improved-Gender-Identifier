# Scraping Images from Google Images using selenium
This subfolder provides code for scraping a given list of names in a pandas data frame and saves n images that contain exactly one face using dlib.

It works as a web environment: the actual scraping is done on a (Windows) machine with a GUI (for selenium) while the face recognition runs on a powerful Ubuntu machine.

The result is a folder containing one folder for each name. Each folder consists of all scraped images (for debugging) plus a subfolder called *oneFace* containing the n (*N_FACE_IMAGES_TO_SCRAPE*) images that only show one face (according to the dlib detector) as a copy. 

## scrapeImages.py
Scrapes Google images for a given CSV file. The function *query_confidence_values* takes the path of an image and queries the service that is implemented by *service_isFace.py*.

Depends on configuration file *scrape_config.py*:
- PATH_CHROMEDRIVER: the path to a working chromedriver installation
- PIC_UPLOAD_URL: the URL of the web service recognizing the image
- MALE_PATHS/FEMALE_PATHS: a tuple of two fields: one for the path to the input csv file and the second one for the path to the output folder of all downloaded images.
- N_FACE_IMAGES_TO_SCRAPE: number of images that contain exactly one face. Scraping stops when this number is reached.
- N_THRESHOLD_CONF_VALUE: minimum threshold for dlib's detector to accept image.

It also creates a glossary to match IDs (=position in original CSV) in the output folder of all downloaded images.

## checkIfFace.py
Contains a function that calculates confidence values of being a face as well as the number of faces given an image or a path to an image. Uses dlib.

## dist_face_detection_scores.py
Since I could not find a documentation of how dlib's face detector confidence scores are distributed (probably -1 to 1) I wrote a script to calculate a distribution of them. That is in this file.

## service_isFace.py
A Flask service to evaluate if an uploaded image contains faces and their confidence values. Expects a POST request including an image upload and responds the number of detected faces and their respective confidence values(done by checkIfFace.py) as JSON.

