import math 

def string_list(str):
	l = str.split()
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
