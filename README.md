### Improved-Gender-Identifier using eigenfaces and SVMs

People's name and Picture are in the data set which is preprocessed excerpt of the “Labeled Faces in the Wild”, aka LFW:

    http://vis-www.cs.umass.edu/lfw/lfw-funneled.tgz (233MB). 
 
or easily we can import data by running the code 'from sklearn.datasets import fetch_lfw_people' in python

In the file Pridiction_from_Image.ipynb the whole code exists and by running this code we have got overall, 

precision (0.87)   recall (0.85)  f1-score (0.85) 

For the citation of Scikit-learn,

Scikit-learn: Machine Learning in Python, Pedregosa et al., JMLR 12, pp. 2825-2830, 2011.


# DATA
Our data is preprocessed (can be downloaded from ) and have two file, one is picture and another is text file.

5749 number of peoples picture we have in our data.

Different people have different number of pictures.

There have 2 kinds of text file, in one text file there have name along with ()

In another text file assigning one name for people's multiple picture.

# Train & Test Split of data

We have divided the whole dataset as training(75%) and test(25%) for both images(X_train, X_test) and label(y_Train, y_test) using a stratified k fold.

### Building a model

# Compute a PCA (eigenfaces) on the face dataset (treated as unlabeled dataset): unsupervised feature extraction / dimensionality reduction.

Extracting the top 150 eigenfaces from 966 faces needed time to do 7.997s

Projecting the input data on the eigenfaces orthonormal basis needed time to do 0.047s

We have applied PCA on both train and test data sets.

# After that train a SVM classification model using 'rbf' kernel

The best estimator found by grid search:

SVC(C=1000.0, cache_size=200, class_weight='balanced', coef0=0.0,
  decision_function_shape='ovr', degree=3, gamma=0.005, kernel='rbf',
  max_iter=-1, probability=False, random_state=None, shrinking=True,
  tol=0.001, verbose=False)
  
 and done in 61.614s
 
 # Predictions
 
 Then we have applied the model on test data and got the results.
 
 After that we showed the pictures and the confusion matrix.

