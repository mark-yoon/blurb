numberOfWords = 2000

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
