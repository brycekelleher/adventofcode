import sys

f = sys.stdin
floor = 0
for c in f.read():
	if c is '(':
		floor += 1
	if c is ')':
		floor -= 1

print floor

