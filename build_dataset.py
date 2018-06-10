# encoding=utf8
import requests
from bs4 import BeautifulSoup
import os

sport_name = ['football','sport/cricket','sport/tennis']
months = ['2018/may/','2018/apr/']
days = [i for i in range(10,31)]
count= []

for s_name in sport_name:
    f = 0
    if s_name == 'football':
        download_folder = os.path.join(os.getcwd(), s_name)
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)
        # print (download_folder)
    else:
        new_path = s_name.split('/')[-1]
        download_folder = os.path.join(os.getcwd(),new_path)
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)
        # print (download_folder)
    for month in months:
        for day in days:
            url = 'https://www.theguardian.com/'+s_name+'/'+month+str(day)+'/all'
            # print(url)
            r = requests.get(url, allow_redirects=False)

            html = r.text
            soup = BeautifulSoup(html, "html5lib")

            links = []
            for a in soup.find_all('a', href=True):
                link_test = a['href'].split('/')
                if '2018' in link_test and 'may' in link_test and str(day) in link_test:
                    links.append(a['href'])

            # print(links)
            links = list(set(links))
            for link in links:
                res = requests.get(link, allow_redirects=False)
                html1 = res.text
                soup1 = BeautifulSoup(html1, "html5lib")
                download_path = os.path.join(download_folder, os.path.basename(link))
                file = open(download_path+'.txt','wb')
                for p in soup1.find_all('p'):
                    # print(p.text)
                    file.write(p.text.encode('utf-8'))
                file.close()
                print("Completed {}".format(link))
                f+=1
        count.append(f)

print(dict(zip(sport_name,count)))