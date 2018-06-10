from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

from feedgen.feed import FeedGenerator

url = 'http://www.flograppling.com'

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

def getTitle(anchor):
    title = anchor.find('div', {'class': 'title'})
    if title == None:
        content_feed = anchor.find('div', {'class': 'content-feed'})
        headings = content_feed.find_all('h4')
        title = headings[0].get_text().strip()
    else:
        title = title.get_text().strip()
    return title

def getDate(anchor):
    try:
        date = anchor.find('div', {'class': 'flo-footnote'})
        date = date.get_text()
        return date
    except AttributeError as e:
        return None

def getLink(anchor):
    fullLink = url + anchor['href']
    return fullLink

def buildListArticles(articles):
    fullList = []
    for article in articles:
        anchor = getAnchor(article)
        if anchor != None:
            title = getTitle(anchor)
            date = getDate(anchor)
            link = getLink(anchor)
            fullList.append((title, date, link))
    return fullList

def parseContent(html):
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        contentList = bs.find('ul', {"class": "list-medium-content"})
        articles = getArticles(contentList)
        if articles != None:
            return buildListArticles(articles)
    except AttributeError as e:
        return []

try:
    html = urlopen(url)
except HTTPError as e:
    print(e)
except URLError as e:
    print('Server not found')
else:
    results = parseContent(html)
    fg = FeedGenerator()
    fg.title('Flo')
    fg.link(href=url, rel='alternate')
    fg.description('Flo')
    for result in results:
        (title, date, link) = result
        fe = fg.add_entry()
        fe.title(title)
        fe.link(href=link)
    fg.rss_str(pretty=True)
    fg.rss_file('flo.xml')
