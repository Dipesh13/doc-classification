import re
import pandas as pd
import json
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
for key,value in model_names.items():
    """
    1) converted text data to numeric features.
    2) Added multiple models
    """
    pl = Pipeline([
        ('vectorizer',CountVectorizer()),
        ('clf',value)
    ])

    pl.fit(X_train,y_train)

    accuracy = pl.score(X_test,y_test)
    print("Acuuracy for {} is {}".format(key,accuracy))