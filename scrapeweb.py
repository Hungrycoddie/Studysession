#python 3
#make the code simpler 
#use BeautifulSoup
#save in csv file and add target location 
#add input for url

import requests
import csv
from bs4 import BeautifulSoup

url = input("Enter a website to extract the URL's from: ")

r  = requests.get("http://" +url)

data = r.text

soup = BeautifulSoup(data)

with open("output.csv", "w") as f:
    writer = csv.writer(f)
    for link in soup.find_all('a'):
        writer.writerow([link.get('href')])
        print(link.get('href'))