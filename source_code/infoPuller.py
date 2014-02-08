import json
import urllib2
import random

key = "33FD9081AE0D75A3717CCBBAAABBA66B:10:68797139"
numArticles = 1

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
        url = url + "&begin_date=" + getRandomDay()
        url = url + "&api-key=" + key
        page = urllib2.urlopen(url)
        html = page.read()
        jsonData = json.loads(html)
        docs = jsonData["response"]["docs"]
        print docs
        for article in docs:
            articles.append(article["lead_paragraph"])
    print articles[0]
    return articles