#!/usr/bin/python

def base26_add(n, c):
	print "n", n, "c", c
	if n == [] and c == 0:
		return []
	elif n == [] and c != 0:
		return [c]
	else:
		q, r = divmod(n[0] + c, 26)
		print "q", q, "r", r
		return [r] + base26_add(n[1:], q)

def base26to10(n):
	return sum([(ord(c) - ord('a')) * pow(26 ,i) for i, c in enumerate(reversed(n))])

def base10to26(n):
	r = ""
	while(n):
		r = chr((n % 26) + ord('a')) + r
		n /= 26
	return r

def check_straights(s):
	a = 'abcdefghijklmnopqrstuvwxyz'
	return any([i[0] + i[1] + i[2] in s for i in zip(a, a[1:], a[2:])])

def check_letters(s):
	return not any([i in s for i in 'iol'])

def check_pairs(s):
	s = s + '$'
	return sum([1 if i[0] == i[1] and i[0] != i[2] else 0 for i in zip(s[0:], s[1:], s[2:])]) >= 2

def new_password(s):
	while True:
		n = base26to10(s)
		s = base10to26(n + 1)
		if (check_straights(s) and check_letters(s) and check_pairs(s)):
			return s
s = 'cqjxjnds'
s = new_password(s)
print s
s = new_password(s)
print s

