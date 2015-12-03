import sys

f = sys.stdin
floor = 0
position = 1
for c in f.read():
	if c is '(':
		floor += 1
	if c is ')':
		floor -= 1
	if floor == -1:
		break
	position += 1

print position

