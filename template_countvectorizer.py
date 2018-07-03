import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

df = pd.DataFrame({'labels':[1,2,3],'data':['pizza','hey there','I want a pizza']})

X= df['data']
y = df['labels']

X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=2)

vectorizer = CountVectorizer()

vec_text = vectorizer.fit_transform(X)
print(vectorizer.get_feature_names())
print(vec_text.data)
# for a,b in zip(vectorizer.get_feature_names(),vec_text.data):
#     print(a,b)