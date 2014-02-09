key = "33FD9081AE0D75A3717CCBBAAABBA66B:10:68797139"
numArticles = 100

def recommendFive():
    articles = []
    for i in range(numArticles / 10):
        urlcopy = url
        urlcopy = urlcopy + "&begin_date=" + getRandomDay()
        urlcopy = urlcopy + "&api-key=" + key
        page = urllib2.urlopen(urlcopy)
        html = page.read()
        page.close()
        jsonData = json.loads(html)
        docs = jsonData["response"]["docs"]
        for article in docs:
            pass
