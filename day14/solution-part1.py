#!/usr/bin/python

data = []
time = []
dist = []

def index_min(a, l, h):
	if l == h:
		return l
	m = (l + h) / 2
	x = index_min(a, l, m)
	y = index_min(a, m + 1, h)

	if a[x] < a[y]:
		return x
	else:
		return y

f = open('input')
for l in f:
	s = l.split()
	n, s, t, r = s[0], int(s[3]), int(s[6]), int(s[13])
	print n, s, t, r
	data.append((s, t, r))
	time.append(0)
	dist.append(0)

def all_finished(a):
	return all([i >= 2503 for i in a])

while not all_finished(time):
	i = index_min(time, 0, len(time) - 1)
	t = data[i][1]
	r = data[i][2]
	if (time[i] + t >= 2503):
		t = 2503 - time[i]
		print 'result', time[i] + (data[i][0] * t)

	dist[i] += data[i][0] * t
	time[i] += t + r

	print t, r, 'time', time, 'dist', dist
print max(dist)
