#!/usr/bin/python

state = []
data = []
time = []
dist = []
score = []

# this is broken as it gives an extra tick in each state
def tick(i):
	if (state[i] == 'f'):
		if (time[i] == 0):
			time[i] = data[i][2]
			state[i] = 'r'
			return
		dist[i] += data[i][0]
		time[i] -= 1
	elif (state[i] == 'r'):
		if (time[i] == 0):
			time[i] = data[i][1]
			state[i] = 'f'
			return
		time[i] -= 1

# update the time, apply the current state, evaluate the state change
def tick2(i):
	time -= 1

	if (state[i] == 'f'):
		dist[i] += data[i][0]

	if (time[i] == 0 and state[i] == 'f'):
		state[i] = 'r'
		time[i] = data[i][2]
	if (time[i] == 0 and state[i] == 'r'):
		state[i] = 'f'
		time[i] = data[i][1]

f = open('input')
for l in f:
	s = l.split()
	n, s, t, r = s[0], int(s[3]), int(s[6]), int(s[13])
	print n, s, t, r
	data.append((s, t, r))
	state.append('f')
	time.append(t)
	dist.append(0)
	score.append(0)

#data[0] = (5, 5, 5)
for s in range(2503):
	for i in range(len(state)):
		tick2(i)
	lead = max(dist)
	for i in range(len(state)):
		if dist[i] == lead:
			score[i] += 1
	print "state", state, "time", time, "dist", dist, "score", score

