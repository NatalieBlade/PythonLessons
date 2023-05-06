import requests
from bs4 import BeautifulSoup

# url = 'https://www.gismeteo.ru/weather-phuket-6002/2-weeks/'
#
# source = requests.get(url)
# main_text = source.text
# soup = BeautifulSoup(main_text)
#
# section = soup.find('a', {'class':'white subnav_link'})
#
# print(section)


# url = 'https://ria.ru/location_Pkhuket/'
#
# source = requests.get(url)
# main_text = source.text
# soup = BeautifulSoup(main_text)
#
# section = soup.findAll('a', {'class':'list-item__title color-font-hover-only'})
#
# print(section)


url = 'http://www.finmarket.ru/currency/rates/'

source = requests.get(url)
main_text = source.text
soup = BeautifulSoup(main_text)

table = soup.find('table', {'class' : 'karramba'})
tr = table.find('tr', {'class' : 'bold'})
tr = tr.find('td', {'class':'green'})
tr = tr.text

#print(tr)

doll = 'Курс доллара на сегодня: ' + str(tr) + ' по сравнению со вчерашним днем'

print(doll)