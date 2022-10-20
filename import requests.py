from bs4 import BeautifulSoup
import requests
import csv
import os

def download_path():
    print('Enter the path to which you want to download the .csv file:')
    download_path = input()
    return download_path
path = download_path()+"\\file.csv"


with open(path, 'w+', newline='') as output:
    csv_writer = csv.writer(output)
    csv_writer.writerow(['Symbol', 'Definition', 'Example'])

req = requests.get("http://www.mathsisfun.com/math-symbols.html")
soup = BeautifulSoup(req.content,'lxml')

for row in soup.select('table.table-bordered tr'):
    cells = row.find_all('td')
    if len(cells) > 1:
        with open(path, 'a') as output:
            csv_writer = csv.writer(output)
            csv_writer.writerow([cells[0].text, cells[1].text, cells[2].text])