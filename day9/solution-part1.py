import sys
import itertools

dists = {}
places = set()

f = sys.stdin
for l in f:
	l = l.split()
	s, d, c = l[0], l[2], l[4]
	dists[(s, d)] = int(c)
	dists[(d, s)] = int(c)
	places.add(s)
	places.add(d)

def valid(l):
	return all([x in dists for x in zip(l[0:], l[1:])])

def distance(l):
	return sum([dists[x] for x in zip(l[0:], l[1:])])

for i in itertools.permutations(places):
	if valid(i):
		print distance(i), i 
