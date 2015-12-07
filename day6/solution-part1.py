import sys


#function map
func = dict(zip(['1', '0', 't'], [lambda x: True, lambda x: False, lambda x: not x]))
def execute(i):
	state[(x, y)] = func[i[0]](state[(x, y)])

f = sys.stdin
x = y = 0
houses = {}
houses[(x, y)] = True
for l in f():
	if c is '>':
		x += 1
	if c is '<':
		x -= 1
	if c is '^':
		y += 1
	if c is 'v':
		y -= 1
	houses[(x, y)] = True

print len(houses.keys())

