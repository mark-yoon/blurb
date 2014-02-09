import numpy as np
import scipy as sp
import wordUtils

class User(object):
	vector = []
	userID = 0

	def __init__(self, weights, ID):
		vector = [0]*2000
		userID = ID

	def updateVector(self, article, like):
		updateWeight = (int(like)-0.5)*2
		for word in article:
			vector[word] = vector[word] + updateWeight

	def getMostSimilar(self, articles): # What info do these articles contain?
		mostSimilar = -1
		mostSimilarArticle = None
		for art in articles:
			y = getSimilarity(art, self.vector)
			if y > mostSimilar:
				mostSimilar = y
				mostSimilarArticle = art
		return art


def getSimilarity(vect1, vect2):
	return (numpy.dot(vect1, vect2)/
		(numpy.dot(vect1, vect1) * numpy.dot(vect2, vect2)))

def getMostSimilar(user, articles): # What info do these articles contain?
	mostSimilar = -1
	mostSimilarArticle = None
	for art in articles:
		y = getSimilarity(art, user.vector)
		if y > mostSimilar:
			mostSimilar = y
			mostSimilarArticle = art
	return art
