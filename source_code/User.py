import numpy as np
import scipy as sp
import wordUtils
import MySQLdb
import json
import utils
from scipy.spatial.distance import cosine

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
    cur.execute("SELECT * FROM clients WHERE id='%s'" % ID)
    vect = cur.fetchall()
    return json.loads(vect[0][1])


def getSimilarity(vect1, vect2):
	return 1 - cosine(vect1, vect2)

def getMostSimilar(ID, articles): # What info do these articles contain?
	articles = sorted(articles, 
        key = lambda x: getSimilarity(getWeights(ID), utils.get_vector(x)))
    return articles[0:5]

def userUpdate(ID, article):
    vect = np.array(utils.get_vector(article))
    IDvect = np.array(getWeights(ID))
    newVect = vect + IDvect
    updateClient(ID, newVect)
