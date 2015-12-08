import sys

# take a name as input
# evaluate the rule and apply the result
def evaluate(name, env, rules):
	# evaluate the operands
	operands = []
	for o in rules[name][1:]:
		if o.isdigit():
			operands.append(int(o))
		elif o in env:
			operands.append(env[o])
		else:
			operands.append(evaluate(o, env, rules))

	# get the operator
	op = rules[name][0]

	# apply the operator
	if op is 'VALUE' : env[name] = operands[0]
	if op is 'AND'   : env[name] = operands[0] & operands[1]
	if op is 'OR'    : env[name] = operands[0] | operands[1]
	if op is 'LSHIFT': env[name] = operands[0] << operands[1]
	if op is 'RSHIFT': env[name] = operands[0] >> operands[1]
	if op is 'NOT'   : env[name] = 65535 - operands[0]
	if op is 'ASSIGN': env[name] = operands[0]

	env[name] &= 0xffff

	print name, "=", op, rules[name][1:]
	print name, "=", env[name], "(", name, "=", op, operands, ")"
	return env[name]

def read_rules():
	rules = {}
	f = sys.stdin
	for l in f:
		l = l.split()
		if 'AND' in  l: rules[l[-1]] = 'AND', l[0], l[2]
		if 'OR' in  l: rules[l[-1]] = 'OR', l[0], l[2]
		if 'NOT' in  l: rules[l[-1]] = 'NOT', l[1]
		if 'LSHIFT' in  l: rules[l[-1]] = 'LSHIFT', l[0], l[2]
		if 'RSHIFT' in  l: rules[l[-1]] = 'RSHIFT', l[0], l[2]
		if l[0].isdigit() and l[1] == '->': rules[l[-1]] = 'VALUE', l[0]
		if l[0].isalpha() and l[1] == '->': rules[l[-1]] = 'ASSIGN', l[0]


	return rules

env = {}
rules = read_rules()
b = evaluate('a', env, rules)
env.clear()
env['b'] = b
print evaluate('a', env, rules)
