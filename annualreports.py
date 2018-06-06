# encoding=utf8
import requests
from bs4 import BeautifulSoup
import os
import string
import urllib2

names = list(string.ascii_uppercase)

dir_links = []
for name in names:
    url = 'http://www.annualreports.com/Companies?a='+name
    r = requests.get(url, allow_redirects=False)

    html = r.text
    soup = BeautifulSoup(html, "html5lib")

    links = []
    for a in soup.find_all('a', href=True):
        links.append(a['href'])

    links = [link for link in links if link]
    links = [link for link in links if link != '/']
    links = links[1:-6]
    dir_links.append(links)

sum = 0
for down in dir_links:
    sum +=(len(down))
print("total no of companies is {}".format(sum))

link_count = 0
for down in dir_links:
    for c_name in down:
        download_folder = os.path.join(os.getcwd(),os.path.basename(c_name))
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)
        url = 'http://www.annualreports.com/'+c_name
        r = requests.get(url, allow_redirects=False)

        html = r.text
        soup = BeautifulSoup(html, "html5lib")

        path = 'http://www.annualreports.com'
        links = []
        for a in soup.find_all('a', href=True):
            links.append(a['href'])

        for link in links:
            link = path+link
            if link.endswith('.pdf'):
                link_count += 1
                response = urllib2.urlopen(link)
                download_path = os.path.join(download_folder,os.path.basename(link))
                file = open(download_path,'wb')
                file.write(response.read())
                file.close()
                print("Completed {}".format(link))

print("total no of pdfs is {}".format(link_count))
