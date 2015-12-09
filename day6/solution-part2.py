import sys

state = {}

#function map
func = dict(zip(['1', '0', 't'], [lambda x: x + 1, lambda x: max(0, x - 1), lambda x: x + 2]))

def coord(x, y):
	return (int(x), int(y))

def rect_test(xy, xy0, xy1):
	return (xy0[0] <= xy[0] <= xy1[0]) and (xy0[1] <= xy[1] <= xy1[1])

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
		p.append( ('1', coord( s[2], s[3] ), coord( s[5], s[6] ) ) )
	if 'off' in l:
		p.append( ('0', coord( s[2], s[3] ), coord( s[5], s[6] ) ) )
	if 'toggle' in l: 
		p.append( ('t', coord( s[1], s[2] ), coord( s[4], s[5] ) ) )

for x in range(1000):
	for y in range(1000):
		state[(x, y)] = 0
		execute((x, y), p)
count = 0
for l in state.keys():
	count += state[l]

print count
