#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


'''#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################
'''

### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess



print ("\nNaive bayes classifier: \n")

from sklearn.naive_bayes import GaussianNB

clf = GaussianNB()

t0 = time()
clf.fit(features_train, labels_train)
print ("training time:", round(time()-t0, 3), "s")

t1 = time()
print (clf.score(features_test, labels_test))
print ("scoring time:", round(time()-t1, 3), "s")

prettyPicture(clf, features_test, labels_test, "NaiveBayesClassifier")

print ("\nSVM classifier: \n")

from sklearn import svm

## clf = svm.SVC(kernel="linear")
clf = svm.SVC(kernel="rbf", C=10000.0)

print ("C = ", getattr(clf, 'C'))


t0 = time()
clf.fit(features_train, labels_train)
print ("training time:", round(time()-t0, 3), "s")

t1 = time()
print (clf.score(features_test, labels_test))
print ("scoring time:", round(time()-t1, 3), "s")
prettyPicture(clf, features_test, labels_test, "SVMClassifier")

print ("\nDecision trees classifier: \n")

from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier(min_samples_split=40)

t0 = time()
clf.fit(features_train, labels_train)
print ("training time:", round(time()-t0, 3), "s")

t1 = time()
print (clf.score(features_test, labels_test))
print ("scoring time:", round(time()-t1, 3), "s")

prettyPicture(clf, features_test, labels_test, "DecisionTreesClassifier")

print ("\nK nearest neighbors classifier: \n")

from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KDTree
clf = KNeighborsClassifier(n_neighbors=3, algorithm='kd_tree', leaf_size=10)

t0 = time()
clf.fit(features_train, labels_train)
print ("training time:", round(time()-t0, 3), "s")

t1 = time()
print (clf.score(features_test, labels_test))
print ("scoring time:", round(time()-t1, 3), "s")

prettyPicture(clf, features_test, labels_test, "KNNClassifier")
print ("\nRandom forest classifier: \n")

from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier()

t0 = time()
clf.fit(features_train, labels_train)
print ("training time:", round(time()-t0, 3), "s")

t1 = time()
print (clf.score(features_test, labels_test))
print ("scoring time:", round(time()-t1, 3), "s")

prettyPicture(clf, features_test, labels_test, "RandomForestClassifier")
print ("\nAdaboost classifier: \n")

from sklearn.ensemble import AdaBoostClassifier

clf = AdaBoostClassifier()

t0 = time()
clf.fit(features_train, labels_train)
print ("training time:", round(time()-t0, 3), "s")

t1 = time()
print (clf.score(features_test, labels_test))
print ("scoring time:", round(time()-t1, 3), "s")

prettyPicture(clf, features_test, labels_test, "AdaBoostClassifier")

'''try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass'''
