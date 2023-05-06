import requests
from bs4 import BeautifulSoup

url = 'https://minfin.com.ua/currency/nbu/'

source = requests.get(url)
main_text = source.text
soup = BeautifulSoup(main_text)

table = soup.find('table', {'class' : 'table-auto'}) #если указать только find, то отобразилось бы только первое совпадение, если findAll - то все
tr = table.find('td', {'class' : 'responsive-hide'})
tr = tr.text

tr = tr[:7]
doll = 'Курс доллара: ' + str(tr)

print(doll)
#print(table)