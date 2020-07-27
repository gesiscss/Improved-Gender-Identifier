# Scraping Images from Google Images using selenium

# checkIfFace.py
Contains a function that calculates confidence values of being a face as well as the number of faces given an image or a path to an image. Uses dlib.

# dist_face_detection_scores.py
Since I could not find a documentation of how dlib's face detector confidence scores are distributed (probably -1 to 1) I wrote a script to calculate a distribution of them. That is in this file.

# service_isFace.py
A Flask service to evaluate if an uploaded image contains faces and their confidence values. Expects a POST request including an image upload and responds the number of detected faces and their respective confidence values(done by checkIfFace.py) as JSON.