#import requests
#from bs4 import BeautifulSoup

# ul.list-medium-content

#url = "http://www.flograppling.com"
#result = requests.get(url)
#c = result.content
#soup = BeautifulSoup(c, "lxml")
#ulist = soup.find('ul', {"class": "list-medium-content"})
##print(ulist.prettify())
## link is on an ANCHOR href attribute inside LI
## a.href
## title: div.title span
## date : div.flo-footnote span
#print(ulist.li.a['href'])
#title = ulist.li.a.div.find('div', {"class": "title"})
#print(title.span.string)
#date = ulist.li.a.div.find('div', {"class": "flo-footnote"})
#print(date.span.string)
##print(len(ulist.li))
#testedois = ulist.find_all('li')
#for item in testedois:
#   # print(item.a['href'])
#    divs = item.a.find_all('div', {"class": "title"})
#    #print(title.prettify())
#    for div in divs:
#        print(div.span.string)

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

url = 'http://www.flograppling.com'

def getTitle(unList):
    try:
        title = unList.li.a.div.find('div', {"class": "title"})
        #return title
        return title.get_text()
    except AttributeError as e:
        return None
    return None

def getDate(unList):
    try:
        date = unList.li.a.div.find('div', {"class": "flo-footnote"})
        return date.get_text()
    except AttributeError as e:
        return None
    return None

def getArticles(unList):
    try:
        articles = unList.find_all('li')
        return articles
    except AttributeError as e:
        return None
    return None

try:
    html = urlopen(url)
except HTTPError as e:
    print(e)
except URLError as e:
    print('Server not found')
else:
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        unList = bs.find('ul', {"class": "list-medium-content"})
        articles = getArticles(unList)
        if articles == None:
            print('no articles')
        else:
            #print(articles)
            #print(articles[0].prettify())
            anchor = articles[0].a
            title = anchor.find('div', {'class': 'title'})
            title = title.get_text()
            print(title)
            date = anchor.find('div', {'class': 'flo-footnote'})
            date = date.get_text()
            print(date)
    except AttributeError as e:
        print(e)
