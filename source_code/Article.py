import wordUtils

class Article(object):
    vect = []
    URL = ""

    def __init__(self, art, URL):
        self.URL = URL
        self.art = wordUtils.getWordVector(art)