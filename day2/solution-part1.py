import sys

def area(l, w, h):
	lw = l * w
	wh = w * h
	hl = h * l

	slack = lw
	slack = min(slack, wh)
	slack = min(slack, hl)

	return (2 * lw) + (2 * wh) + (2 * hl) + slack

f = sys.stdin
total = 0
for line in f:
	l, w, h = map(int, line.split('x'))
	total += area(l, w, h)

print total

