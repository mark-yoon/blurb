def getWords():
    words = []
    with open("words.txt") as f:
        for line in f:
            words.append(line),
    return words

def getWordVector(article):
    wordList = getWords()
    articleWords = article.split(' ')
    wordVector = [0]*len(wordList)
    for word in articleWords:
        index = wordList.index(word)
        wordVector[index] = wordVector[index] + 1
    return wordVector