import sys

state = {}

#function map
func = dict(zip(['1', '0', 't'], [lambda x: True, lambda x: False, lambda x: not x]))
#def execute(i):
#	state[(x, y)] = func[i[0]](state[(x, y)])

def rect_test(xy, xy0, xy1):
	return (int(xy0[0]) <= xy[0] <= int(xy1[0])) and (int(xy0[1]) <= xy[1] <= int(xy1[1]))

def execute_instruction(xy, i):
	func

def execute(xy, p):
	for i in p:
		if not rect_test(xy, i[1], i[2]):
			continue
		f = func[i[0]]
		state[xy] = f(state[xy])

f = sys.stdin
p = []
for l in f:
	s =  l.replace(","," ").split()
	if 'on' in l:
		p.append( ('1', ( s[2], s[3] ), ( s[5], s[6] ) ) )
	if 'off' in l:
		p.append( ('0', ( s[2], s[3] ), ( s[5], s[6] ) ) )
	if 'toggle' in l: 
		p.append( ('t', ( s[1], s[2] ), ( s[4], s[5] ) ) )

for x in range(500, 750):
	for y in range(500, 750):
		state[(x, y)] = False
		execute((x, y), p)
count = 0
for l in state.keys():
	if state[l] is True:
		count += 1

print state
print count
