names = set()
rules = dict()

from itertools import permutations, izip, imap

#def score(x):
#	sum = 0
#	for l, i, r in izip(x[-1:] + x[:-1], x, x[1:] + x[:1]):
#		sum += rules[(i, l)] + rules[(i, r)]
#	return sum

def g(x):
	l, i, r = x[0], x[1], x[2]
	return rules[(i, l)] + rules[(i, r)]

def score(x):
	return sum(imap(g, izip(x[-1:] + x[:-1], x, x[1:] + x[:1])))
	

f = open("input")
for l in f:
	l = l.split()
	s, m, v, d = l[0], l[2], int(l[3]), l[10].replace(".", "")
	
	names.add(s)
	names.add(d)

	if m == 'lose':
		v = -v

	rules[(s, d)] = v

print max(list(imap(score, permutations(list(names)))))

	
	


