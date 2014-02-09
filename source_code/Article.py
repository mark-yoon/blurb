import wordUtils

class Article(object):
    vect = []
    URL = ""

    def __init__(self, art, URL):
        self.URL = URL
        self.vect = wordUtils.getWordVector(art)

