import sys
import itertools

dists = {}
places = []

f = sys.stdin
for l in f:
	l = l.split()
	s, d, c = l[0], l[2], l[4]
	dists[(s, d)] = int(c)
	dists[(d, s)] = int(c)
	if s not in places:
		places.append(s)
	if d not in places:
		places.append(d)

def valid(l):
	return all( [(l[x], l[x+1]) in dists for x in range(len(l) - 1)] )

def distance(l):
	return sum([dists[(l[i], l[i+1])] for i in range(len(l) - 1)])

for i in itertools.permutations(range(len(places))):
	i = [places[x] for x in i]
	if valid(i):
		print distance(i), i 
