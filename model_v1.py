import re
import pandas as pd
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


X= df['data']
y = df['labels']

X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=2)

classifiers = [
    LogisticRegression(),
    KNeighborsClassifier(2),
    SVC(kernel="linear", C=0.025),
    SVC(gamma=2, C=1),
    DecisionTreeClassifier(max_depth=5),
    RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
    MLPClassifier(alpha=1),
    AdaBoostClassifier(),
    GaussianNB()
]

names = ["Logistic Regression",
         "Nearest Neighbors",
         "Linear SVM",
         "RBF SVM",
         "Decision Tree",
         "Random Forest",
         "Neural Net",
         "AdaBoost"
         "Naive Bayes"
         ]

model_names = dict(zip(names,classifiers))

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