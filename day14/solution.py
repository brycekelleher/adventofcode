#!/usr/bin/python

data = []
dist = []

f = open('input')
for l in f:
	s = l.split()
	n, s, t, r = s[0], int(s[3]), int(s[6]), int(s[13])
	print n, s, t, r

