# -*- coding: utf-8 -*-
import argparse
import re
import pandas as pd
import json
import pickle
import os
from sklearn.pipeline import Pipeline
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
parser.add_argument('-foldername', help='name of the txt file containing the article')
args = parser.parse_args()
model_name = args.modelname
foldername = args.foldername

def model_pred(model_name,foldername):
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
    modelpath = os.path.join(os.getcwd(), 'models')
    model = os.path.join(modelpath, model_name)
    with open(model + '.pickle', 'rb') as fi:
        model = pickle.load(fi)

    filepath = os.path.join(os.getcwd(), foldername)
    for file in os.listdir(filepath):
        with open(os.path.join(filepath,file),'rb') as f:
            data = [f.read()]
        label = model.predict(data)
        print (file,label[0])

    # df_test = pd.read_csv("test.csv")
    # out_df.to_csv('pred-'+model_name+'.csv',index = False)

if __name__ == '__main__':
    model_pred(model_name,foldername)