#!/usr/bin/python

def read_rules():
	rules = {}
	f = open('rules')
	for l in f:
		s = l.split()
		i, o = s[0], s[2]
		if i not in rules:
			rules[i] = []
		rules[i].append(o)
	return rules

def eval_molecule(s, rules):
	for i in range(len(s)):
		if s[i:i + 1] in rules
		if s[i:i + 2]

rules = read_rules()
print rules
