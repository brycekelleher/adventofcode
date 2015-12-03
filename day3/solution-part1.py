import sys

f = sys.stdin
x = y = 0
houses = {}
houses[(x, y)] = True
for c in f.read():
	if c is '>':
		x += 1
	if c is '<':
		x -= 1
	if c is '^':
		y += 1
	if c is 'v':
		y -= 1
	houses[(x, y)] = True

print len(houses.keys())

