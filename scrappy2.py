#python 3
# scrape this website url (https://www.rapidtables.com/math/symbols/index.html)
# download data in .xls
# read data in .xls
# print data in three columns

import requests
import os
import xlrd
url = 'https://www.rapidtables.com/math/symbols/index.html'
dir_name = 'math_symbols'
response = requests.get(url)
html = response.text
os.mkdir(dir_name)
head = html[html.find('<div class="indextable">'):html.find('<div class="clear"></div>')]
table = head[head.find('<table>'):head.find('</table>')]
rows = table.split('</tr>')
rows.pop()
for row in rows:
    row_split = row.split('</td>')
    row_split.pop()
    row_split_name = row_split[0]
    row_split_name = row_split_name[row_split_name.find('>')+1:]
    row_split_symbol = row_split[1]
    row_split_symbol = row_split_symbol[row_split_symbol.find('>')+1:]
    row_split_description = row_split[2]
    row_split_description = row_split_description[row_split_description.find('>')+1:]
    print(row_split_name,row_split_symbol,row_split_description)
    with open(dir_name + '/' + 'math_symbols.xls','a') as f:
        f.write(row_split_name + '\t' + row_split_symbol + '\t' + row_split_description + '\n')
print('Downloaded to ' + dir_name)
print('\n')
print('Opening ' + dir_name + '/' + 'math_symbols.xls')
time.sleep(2)
print('\n')
print('Printing')
print('\n')
wb = xlrd.open_workbook(dir_name + '/' + 'math_symbols.xls')
sh = wb.sheet_by_index(0)
for rownum in range(sh.nrows):
    print(sh.row_values(rownum))
    print('\n')

