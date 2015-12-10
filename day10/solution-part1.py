import sys

def lookandsay(s):
	t = ""
	i = 0
	while (i < len(s)):
		r = i
		while r < len(s) and s[i] == s[r]:
			r += 1
		t += str(r - i) + s[i]
		i = r
	return t

def lookandsay_r(s):
	if not len(s):
		return ""
	r = 0
	while r < len(s) and s[0] == s[r]:
		r += 1
	return str(r) + s[0] + lookandsay2_r(s[r:])

s = '1113222113'
for i in range(40):
	s = lookandsay2(s)
print len(s)

for i in range(10):
	s = lookandsay2(s)
print len(s)

