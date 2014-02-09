import json
import urllib2
import random
import time

key = "33FD9081AE0D75A3717CCBBAAABBA66B:10:68797139"
numArticles = 100

def getRandomDay():
    year = str(random.randint(2000, 2013))
    month = str(random.randint(1, 12))
    if len(month) == 1:
        month = "0" + month
    day = str(random.randint(1, 28))
    if len(day) == 1:
        day = "0" + day
    return year + month + day

def getArticles():
    """Returns an array of first paragraphs of articles."""
    url = "http://api.nytimes.com/svc/search/v2/articlesearch.json?sort=oldest"
    articles = []
    for i in range(numArticles):
        urlcopy = url
        print i
        urlcopy = urlcopy + "&begin_date=" + getRandomDay()
        urlcopy = urlcopy + "&api-key=" + key
        page = urllib2.urlopen(urlcopy)
        html = page.read()
        page.close()
        jsonData = json.loads(html)
        docs = jsonData["response"]["docs"]
        for article in docs:
            articles.append(article["lead_paragraph"])
            articles.append(article["snippet"])
            articles.append(article["abstract"])
    return articles