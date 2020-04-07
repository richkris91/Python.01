import requests
import json
site = requests.get('https://wp.pl')
print(site.text)
data = requests.get('http://api.openrates.io/2000-01-03')
# data_str = data.text
data_json = data.json()
# print(type(data.text))
# print(type(data.json))
print(data.json['rates']['PLN'])
# import requests
# import bs4
# lx_html = requests.get('https://www.olx.pl/motoryzacja/samochody/')
# parser = bs4.BeautifulSoup(olx_html.text, 'html.parser')
# obrazki = parser.find_all('img')
#for obrazek in obrazki:
#    adres = obrazek.get('src')
#    nazwa = obrazek.get('alt')
#    obrazek = requests.get(adres).content
#    with open('pics'w)
#contents = requests.get('https://www.olx.pl/motoryzacja/samochody/')
#pics = parser.find_all('jpg')
