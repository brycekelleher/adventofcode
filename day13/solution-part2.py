names = set()
rules = dict()

from itertools import permutations, izip, imap

def rotatel(x, i): return x[i:] + x[:i]
def rotater(x, i): return x[-i:] + x[:-i]

def h(x):
	return rules[(x[0], x[1])]

def score(x):
	xr = list(reversed(x))
	return sum(imap(h, izip(x, rotatel(x, 1)))) + sum(imap(h, izip(xr, rotatel(xr, 1))))
	
def score2(x):
	xr = list(reversed(x))
	return sum(imap(h, izip(x, x[1:]))) + sum(imap(h, izip(xr, xr[1:])))

f = open("input")
for l in f:
	l = l.split()
	s, m, v, d = l[0], l[2], int(l[3]), l[10].replace(".", "")
	
	names.add(s)
	names.add(d)

	if m == 'lose':
		v = -v

	rules[(s, d)] = v

print max(list(imap(score2, permutations(list(names)))))

	
	


