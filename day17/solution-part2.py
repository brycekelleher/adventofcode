#!/usr/bin/python
from itertools import combinations
from itertools import groupby

f = open('input')
n = map(int, f.read().split())
count = 0
valid = []
for i in range(len(n)):
	c = combinations(n, i)
	for j in c:
		if sum(j) == 150:
			valid.append(j)
			count += 1
valid = sorted(valid, cmp=lambda x, y: len(x) - len(y))
lengths = [len(x) for x in valid]
for k, g in groupby(lengths):
	print k, list(g)

