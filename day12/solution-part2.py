import sys
import json

def process_dict(x):
	total = 0
	if 'red' in x.values():
		return 0
	for k in x.keys():
		total += eval_json(x[k])
	return total

def process_list(x):
	total = 0;
	for i in x:
		total += eval_json(i)
	return total

def process_int(x):
	return x

def process_float(x):
	pass

def process_unicode(x):
	if x.isdigit() or (x[0] =='-' and x[1:].isdigit()):
		return int(x)
	else:
		return 0

def eval_json(j):
	total = 0
	if type(j) == dict:
		total += process_dict(j)
	elif type(j) == list:
		total += process_list(j)
	elif type(j) == unicode:
		total += process_unicode(j)
	elif type(j) == int:
		total += process_int(j)
	elif type(j) == float:
		process_float(j)
	else:
		print "unkown argument"

	return total

s = sys.stdin.read()
j = json.loads(s)
print eval_json(j)
