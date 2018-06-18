import requests
from bs4 import BeautifulSoup

class Article:
    def __init__(self, title, link, content):
        self.title = title
        self.link = link
        self.content = content

# federais abertos e em andamento
url = 'https://www.acheconcursos.com.br/concursos-brasil'
#url = 'https://www.acheconcursos.com.br/concursos-abertos'
urls = [
        'https://www.acheconcursos.com.br/concursos-sao-paulo',
        'https://www.acheconcursos.com.br/concursos-rio-de-janeiro',
        'https://www.acheconcursos.com.br/concursos-rio-grande-do-sul',
        'https://www.acheconcursos.com.br/concursos-minas-gerais',
        'https://www.acheconcursos.com.br/concursos-espirito-santo',
        'https://www.acheconcursos.com.br/concursos-parana',
        'https://www.acheconcursos.com.br/concursos-distrito-federal',
        'https://www.acheconcursos.com.br/concursos-goias',
        'https://www.acheconcursos.com.br/concursos-santa-catarina',
        'https://www.acheconcursos.com.br/concursos-mato-grosso',
        'https://www.acheconcursos.com.br/concursos-mato-grosso-do-sul'
        ];
headers = {'User-Agent':'Mozilla/5.0'}
articles = []

html = requests.get(url)
bs = BeautifulSoup(html.text, 'html.parser')
# first list = concursos abertos = "concurso, inscriçoes ate, vagas(nao aparece no site),  salarios ate"
# second_list= concursos andamento = "concurso, provas em, resultados em"

unordered_lists = bs.find_all('ul', {'class':'ul_site_concursos'})
# should return two un_lists, first for 'concursos em aberto', second for 'concursos em andamento'
for unordered_list in unordered_lists:
    headers = []
    headers_html = unordered_list.find_all('li')[0]
    headers = [header.get_text() + ": " for header in headers_html.find_all('div')]
    list_items = unordered_list.find_all('li')[1:]
    for list_item in list_items:
        content = ''
        divs = list_item.find_all('div')
        anchor = divs[0].span.a
        title = anchor.get_text()
        link = anchor['href']
        limit_date = divs[1].get_text()
        vaccancies = divs[2].get_text()
        income = divs[3].get_text()
        content += headers[1] + limit_date + "\n"
        content += headers[2] + vaccancies + "\n"
        content += headers[3] + income
        articles.append(Article(title, link, content))


for article in articles:
    print(article.title)
    print(article.link)
    print(article.content)
