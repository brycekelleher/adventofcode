import sys

instructions = sys.stdin.read().strip('\n')
houses = {}

def execute(i):
	moves  = {'>': (1, 0), '<': (-1, 0), '^': (0, 1), 'v': (0, -1)}
	x = y = 0
	houses[(x, y)] = True
	for c in i:
		x += moves[c][0]
		y += moves[c][1]
		houses[(x, y)] = True

execute([instructions[x] for x in range(len(instructions)) if x % 2 == 0])
execute([instructions[x] for x in range(len(instructions)) if x % 2 == 1])

print len(houses.keys())

