# -*- coding: utf-8 -*-
import argparse
import re
import pandas as pd
import json
import pickle
import os
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

parser = argparse.ArgumentParser(description='model name to load the pickle file')
parser.add_argument('-modelname', help='name of the classifier',default="Linear SVM")
parser.add_argument('-filename', help='name of the txt file containing the article')
args = parser.parse_args()
model_name = args.modelname
filename = args.filename

def model_pred(model_name,filename):
    """Test based on model name (defaults to Linear SVM) for predictions.

    Following models are available

    "Logistic Regression",
    "Nearest Neighbors",
    "Linear SVM",
    "RBF SVM",
    "Decision Tree",
    "Random Forest",
    "Neural Net",
    "AdaBoost"
    "Naive Bayes"

    """

    filepath = os.path.join(os.getcwd(), filename)
    with open(filepath,'rb') as f:
        data = f.read()
    modelpath = os.path.join(os.getcwd(), 'models')
    model = os.path.join(modelpath,model_name)
    with open(model+'.pickle', 'rb') as fi:
        pl = pickle.load(fi)

    # pattern = '[A-Za-z0-9]+(?=\\s+)'
    # vectorizer = CountVectorizer(token_pattern=pattern)
    # pred_data = vectorizer.transform(data)
    # label = pl.predict(pred_data)
    # print (label)

    # df_test = pd.read_csv("test.csv")
    # out_df.to_csv('pred-'+model_name+'.csv',index = False)

if __name__ == '__main__':
    model_pred(model_name,filename)