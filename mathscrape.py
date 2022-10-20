
import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.rapidtables.com/math/symbols/Basic_Math_Symbols.html"

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html5lib')

# print(soup.prettify())

table = soup.find('table', attrs = {'class':'table table-bordered'})

# print(table.prettify())

table_rows = table.find_all('tr')

# print(table_rows)

with open('math_symbols.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Symbol', 'Name', 'Description', 'Example'])
    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text for i in td]
        writer.writerow(row)