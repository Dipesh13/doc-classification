import os
import pandas as pd

label = []
text_data = []
for (dirname, dirs, files) in os.walk('.'):
    for filename in files:
        if filename.endswith('.txt'):
            thefile = os.path.join(dirname,filename)
            if (os.stat(thefile).st_size) !=0:
                # print(dirname.split('/')[1],thefile.split('/')[-1])
                with open(thefile,'rb') as fi:
                    label.append(dirname.split('/')[1])
                    text_data.append(fi.read())

dataset = dict(zip(label,text_data))
# print(dataset.keys())

# df = pd.DataFrame(dataset,index=[0])
# print(df.T)

df = pd.DataFrame(
    {'labels': label,
     'data': text_data
    })

df = df[['labels', 'data']]
print(df)