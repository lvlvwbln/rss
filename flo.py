import requests
from bs4 import BeautifulSoup

# ul.list-medium-content

url = "http://www.flograppling.com"
result = requests.get(url)
c = result.content
soup = BeautifulSoup(c, "lxml")
ulist = soup.find('ul', {"class": "list-medium-content"})
#print(ulist.prettify())
# link is on an ANCHOR href attribute inside LI
# a.href
# title: div.title span
# date : div.flo-footnote span
print(ulist.li.a['href'])
title = ulist.li.a.div.find('div', {"class": "title"})
print(title.span.string)
date = ulist.li.a.div.find('div', {"class": "flo-footnote"})
print(date.span.string)
#print(len(ulist.li))
testedois = ulist.find_all('li')
for item in testedois:
   # print(item.a['href'])
    divs = item.a.find_all('div', {"class": "title"})
    #print(title.prettify())
    for div in divs:
        print(div.span.string)
