# Scraping Images from Google Images using selenium

# checkIfFace.py
Contains a function that calculates confidence values of being a face as well as the number of faces given an image or a path to an image. Uses dlib.

# dist_face_detection_scores.py
Since I could not find a documentation of how dlib's face detector confidence scores are distributed (probably -1 to 1) I wrote a script to calculate a distribution of them. That is in this file.