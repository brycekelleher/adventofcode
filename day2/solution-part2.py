import sys

# could sort and take the first two elements. For 3 elements it should be simple enough
# to find the smallest element then find the smallest element again from the remaining two
#elements
#def smallest2(l, w, h):
#	if l <= w and l <= h:
#		x = l
#		y = min(w, h)
#	elif w <= l and w <= h:
#		x = w
#		y = min(l, h)
#	elif h <= l and h <= w:
#		x = h
#		y = min(l, w)
#
#	return (x, y)

def min3(x, y, z):
	r = x
	r = min(r, y)
	r = min(r, z)
	return r

def smallest_perimeter(l, w, h):
	lw = l + l + w + w
	wh = w + w + h + h
	hl = h + h + l + l

	return min3(lw, wh, hl)

#even simpler is to just subtract the largest value as the permeter is just an addition of the two smallest values
def smallest_perimeter2(l, w, h):
	return (2 * l) + (2 * w) + (2 * h) - 2 * (max(l, max(w, h)))

f = sys.stdin
total = 0
for line in f:
	l, w, h = map(int, line.split('x'))
	total += smallest_perimeter(l, w, h) + (l * w * h)

print total

