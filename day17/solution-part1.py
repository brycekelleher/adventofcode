#!/usr/bin/python
from itertools import combinations

f = open('input')
n = map(int, f.read().split())
count = 0
for i in range(len(n)):
	c = combinations(n, i)
#print list(c)
	for j in c:
		if sum(j) == 150:
			count += 1
print count
