import re
import pandas as pd
from create_dataset import df
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

X= df['data']
y = df['labels']

# X_train,X_test,y_train,y_test = train_test_split(X,pd.get_dummies(y),random_state=2)
X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=2)

model_names = ['LogisticRegression()']
pattern = '[A-Za-z0-9]+(?=\\s+)'
for model in model_names:
    """
    TO-DOs
    1) convert labels to numbers using pd.get_dummies() ?
    2) convert text data to numeric features.
    3) Add multiple models
    """
    pl = Pipeline([
        ('vectorizer',CountVectorizer()),
        ('clf',LogisticRegression())
    ])

    pl.fit(X_train,y_train)

    accuracy = pl.score(X_test,y_test)
    print("Acuuracy for {} is {}".format(model,accuracy))