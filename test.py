import os
import pandas as pd
from create_dataset import df

x= df['data']
for i,a in enumerate(x):
    # print (a)
    print(len(a))
    # if len(a)==0:
    #     print("Remove file")

# label = []
# text_data = []
# for (dirname, dirs, files) in os.walk('.'):
#     for filename in files:
#         if filename.endswith('.txt'):
#             thefile = os.path.join(dirname,filename)
#             if (os.stat(thefile).st_size) > 10:
#                 with open(thefile,'rb') as fi:
#                     print(fi.read())
