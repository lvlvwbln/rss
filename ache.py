import requests
from bs4 import BeautifulSoup

url = 'https://www.acheconcursos.com.br/concursos-brasil'
headers = {'User-Agent':'Mozilla/5.0'}

html = requests.get(url)
bs = BeautifulSoup(html.text, 'html.parser')
abertos = bs.find('div', {'class':'tbl_concursos_inc'})
ul = abertos.ul
items = ul.find_all('li')[1:]
for li in items:
    anchors = li.find_all('a')
    for anchor in anchors:
        title = anchor.get_text()
        link = anchor['href']
        print(title)
        print(link)

