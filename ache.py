import requests
from bs4 import BeautifulSoup

class Article:
    def __init__(self, title, link, content):
        self.title = title
        self.link = link
        self.content = content

url = 'https://www.acheconcursos.com.br/concursos-brasil'
headers = {'User-Agent':'Mozilla/5.0'}
articles = []

html = requests.get(url)
bs = BeautifulSoup(html.text, 'html.parser')
abertos = bs.find('div', {'class':'tbl_concursos_inc'})
ul = abertos.ul
items = ul.find_all('li')[1:]
for li in items:
    content = ''
#    print(li.prettify())
    divs = li.find_all('div')[1:]
    limit_date = divs[0].get_text()
    vaccancies = divs[1].get_text()
    income = divs[2].get_text()
    content += "Fim inscrições: " + limit_date + "\n"
    content += "Vagas: " + vaccancies + "\n"
    content += "Salário: " + income
#    print(content)

    anchors = li.find_all('a')
    for anchor in anchors:
        title = anchor.get_text()
        link = anchor['href']
        articles.append(Article(title, link, content))

for article in articles:
    print(article.title)
    print(article.link)
    print(article.content)
