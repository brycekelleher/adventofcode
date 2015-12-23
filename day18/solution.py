#!/usr/bin/python

from itertools import product

grid_w = 100
grid_h = 100

def count_neighbours(state, nlist):
	return sum([1 if state[i] == True else 0 for i in nlist])

def valid_cell_addr(a):
	return (a[0] >= 0 and a[0] < grid_h) and (a[1] >= 0 and a[1] < grid_w)

cells = list(product(range(grid_h), range(grid_w)))
maskn = [i for i in product(range(-1, 2), range(-1, 2)) if i[0] != 0 or i[1] != 0]
celln = dict(zip(cells, [[(j[0] + i[0], j[1] + i[1]) for j in maskn if valid_cell_addr((j[0] + i[0], j[1] + i[1]))] for i in cells]))

def setup_initial_state():
	state = {}

	f = open('input')
	d = f.read()
	d = [i for i in d if i == '.' or i == '#']
	for i, j in zip(d, cells):
		state[j] = False
		if i == '#':
			state[j] = True
	#state[(0, 0)] = state[(0, grid_w - 1)] = state[(grid_h - 1, 0)] = state[(grid_h - 1, grid_w - 1)] = True
	return state

def next_generation(g):
	h = {}
	for i in cells:
		nc = count_neighbours(g, celln[i])
		h[i] = g[i]
		if g[i] == True and nc != 2 and nc != 3:
			h[i] = False
		if g[i] == False and nc == 3:
			h[i] = True

	#h[(0, 0)] = h[(0, grid_w - 1)] = h[(grid_h - 1, 0)] = h[(grid_h - 1, grid_w - 1)] = True
	return h

def display(s):
	for r in range(grid_h):
		print ['#' if s[(r, c)] == True else '.' for c in range(grid_w)]
	print ""

def count_on(s):
	return sum([1 if s[i] == True else 0 for i in cells])
	
state = setup_initial_state()
display(state)
for i in range(100):
	state = next_generation(state)
display(state)
print count_on(state)
