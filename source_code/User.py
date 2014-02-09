import numpy as np
import scipy as sp
import wordUtils
import MySQLdb
import json

def newClient(ID, weights):
    db = MySQLdb.connect(host="localhost",
                             user="root",
                             passwd="password",
                             db="hackathonbb2014")
    cur = db.cursor()
    cur.execute("INSERT INTO clients VALUES ('%s', '%s')" 
                              % (ID, json.dumps(weightsv)))
    db.commit()

def updateClient(ID, weights):
    db = MySQLdb.connect(host="localhost",
                         user="root",
                         passwd="password",
                         db="hackathonbb2014")
    cur = db.cursor()
    cur.execute("UPDATE clients SET ID='%s', VECTOR1='%s' WHERE ID='%s'" 
                  % (ID, json.dumps(weights), ID))
    db.commit()

def getWeights(ID):
    db = MySQLdb.connect(host="localhost",
                         user="root",
                         passwd="password",
                         db="hackathonbb2014")
    cur = db.cursor()
    cur.execute("SELECT FROM clients WHERE id=%s" % ID)
    vect = cur.fetchall()
    return json.loads(vect[0][1])


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
