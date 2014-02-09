import time
import infoPuller

key = "33FD9081AE0D75A3717CCBBAAABBA66B:10:68797139"
numArticles = 100
url = "http://api.nytimes.com/svc/search/v2/articlesearch.json?sort=oldest"

def getArticles(amt):
    articles = []
    for i in range(amt / 10):
        urlcopy = url
        urlcopy = urlcopy + "&begin_date=" + getRandomDay()
        urlcopy = urlcopy + "&api-key=" + key
        page = urllib2.urlopen(urlcopy)
        html = page.read()
        page.close()
        jsonData = json.loads(html)
        docs = jsonData["response"]["docs"]
        articles = articles + docs
    return articles

def getTodayArticles():
    today = (time.strftime("%Y%m%d"))
    urlcopy = url + "&begin_date=" + today + "&api-key=" + key
    page = urllib2.urlopen(urlcopy)
    html = page.read()
    page.close()
    jsonData = json.loads(html)
    docs = jsonData["response"]["docs"][0:5]
    return docs
