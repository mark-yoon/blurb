import math

def string_list(strn):
	l = strn.split()
	lst = []
	for s in l:
		lst.append(s.lower())
	st = set(lst)
	return list(st)

#vect1 and vect2 must be the same length
def cosine_similarity(vect1,vect2):
	sum_ = 0.0
	len1 = 0.0
	len2 = 0.0
	if len(vect1) != len(vect2):
		return 0.0
	else:
		for i in range(len(vect1)):
			sum_ = sum_ + float(vect1[i] * vect2[i])
			len1 = len1 + float(vect1[i] * vect1[i])
			len2 = len2 + float(vect2[i] * vect2[i])
		return sum_/(math.sqrt(len1) * math.sqrt(len2))

def get_words(lst,n):
	semi_final_list = []
	
	for strn in lst:
		if strn != None :
			for s in string_list(strn) :
				semi_final_list.append(s)
	
	final_set = set(semi_final_list)
	new_dictionary = {}
	cut = int(float(n) * 0.25)
	final_list = []

	for st in final_set:
		new_dictionary[st] = 0
	
	for st in semi_final_list:
		new_dictionary[st] = new_dictionary[st] + 1
	
	for hi in new_dictionary.keys():
		if new_dictionary[hi] < cut:
			final_list.append(hi)

	write_to_file(final_list)

def write_to_file(lst):
	f = open("words.txt", "w")
	for w in lst:
		w = w.encode("ascii", "ignore")
		f.write(w+"\n")

def remove_non_alpha_numerics(file1,file2):
	f = open (file1)
	g = open (file2, "w")
	for l in f :
		l = l.replace("\n","")
		if l.isalpha() or l.isalnum() :
			g.write(l+"\n")

def get_vector(strn):
	f = open("words.txt")
	res = []
	for line in f:
		line = line.replace("\n","")
		res.append(strn, line)
	return res

def count(strn,word):
	if strn == None:
		return 0
	count = 0
	l = strn.split()
	for w in l:
		if w[len(w)-1] == ',' || w[len(w)-1] == '\'' || w[len(w)-1] == '\"':
			w = w[:(len(w) - 1)]
		if w == word:
			count = count + 1
	return count

