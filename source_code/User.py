numberOfWords = 2000

class User(object):
	vector = []
	def __init__(self, weights):
		vector = [0]*2000

	def updateVector(self, article, like):
		updateWeight = (int(like)-0.5)*2
		for word in article:
			vector[word] = vector[word] + updateWeight
