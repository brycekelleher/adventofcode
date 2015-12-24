#!/usr/bin/python

def read_rules():
	rules = {}
	f = open('testrules')
	for l in f:
		s = l.split()
		i, o = s[0], s[2]
		if i not in rules:
			rules[i] = []
		rules[i].append(o)
	return rules

def read_molecule():
	f = open('input')
	return f.read()

def lookup_rule(s, rules):
	if s[0:1] in rules:
		return rules[s[0:1]]
	elif s[0:2] in rules:
		return rules[s[0:2]]
	else:
		return []

def check_match(s, rules):
	for i in rules.keys():
		if s.find(i) == 0:
			return True, i
	return False. None

def eval_molecule(m, rules):
	q = []
	q.append(("", m))
	while len(q):
		print q
		p, s = q.pop(0)

		# print the completed molecule
		if s == "":
			print p
			continue

		found, key = check_match(s, rules)
		if not found:
			q.append((p + s[0], s[1:]))
			continue
		rl = rules[key]
		for r in rl:
			q.append((p + r, s[len(r):]))


rules = read_rules()
molecule = read_molecule()
molecule = 'HOH'
print rules
print molecule

eval_molecule(molecule, rules)
