import urllib2, csv
from bs4 import BeautifulSoup

output_file = open('accidents.csv', 'w')
writer = csv.writer(output_file)

url = 'https://www.mshp.dps.missouri.gov/HP68/search.jsp'

html = urllib2.urlopen(url).read()

soup = BeautifulSoup(html, "html.parser")

acc_table = soup.find('table', {'class': 'accidentOutput'})

row_list = acc_table.find_all('tr')

for row in row_list:

    cell_list = row.find_all('td')

    data = [cell.text.encode('utf-8').strip() for cell in cell_list]

    writer.writerow(data)