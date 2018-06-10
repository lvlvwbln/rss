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

def getAnchor(article):
    try:
        anchor = article.a
        return anchor
    except AttributeError as e:
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
            for article in articles:
                #anchor = article.a
                anchor = getAnchor(article)
                if anchor != None:
                    title = anchor.find('div', {'class': 'title'})
                    if title == None:
                        content_feed = anchor.find('div', {'class': 'content-feed'})
                        headings = content_feed.find_all('h4')
                        title = headings[0].get_text().strip()
                    else:
                        title = title.get_text().strip()
                    print(title)

                    date = anchor.find('div', {'class': 'flo-footnote'})
                    date = date.get_text()
                    print(date)

                    link = anchor['href']
                    #print(link)
                    full_link = url + link
                    print(full_link)
    except AttributeError as e:
        print(e)
