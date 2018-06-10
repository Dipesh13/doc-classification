import re
import pandas as pd
import json
import pickle
import os
from create_dataset import df
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from config import model_names

X= df['data']
y = df['labels']

X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=2)

# with open('config.json','rb') as fi:
#     model_names = json.load(fi)

pattern = '[A-Za-z0-9]+(?=\\s+)'
path = os.path.join(os.getcwd(),'models')
if not os.path.exists(path):
    os.makedirs(path)
for key,value in model_names.items():
    """
    Done: Add alpha numeric pattern for tokenization(This removes punctuation as well).
    Done: Predict on new data(+tranform new data? no need)
    1) lower case before writing to df ? build_dataset.py
    2) remove stop words before writing to df? build_dataset.py
    3) read from config file
    """
    pl = Pipeline([
        ('vectorizer',CountVectorizer(token_pattern=pattern)),
        ('clf',value)
    ])

    pl.fit(X_train,y_train)

    accuracy = pl.score(X_test,y_test)
    print("Acuuracy for {} is {}".format(key,accuracy))
    destination = os.path.join(path,key)
    with open(destination + '.pickle', 'wb') as fo:
        pickle.dump(pl,fo)