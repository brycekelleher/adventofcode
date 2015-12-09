import sys

csize = msize = i = 0
s = sys.stdin.read()
#s = r'"njro\x68qgbx\xe4af\"\\suan"'
print s
while (i < len(s)):
	if s[i:i+2] == r'\"':
		csize += 2
		msize += 1
		i += 2
	elif s[i:i+2] == r'\\':
		csize += 2
		msize += 1
		i += 2
	elif s[i:i+2] == r'\x':
		csize += 4
		msize += 1
		i += 4
	elif s[i] == '"':
		csize += 1
		i += 1
	elif not s[i].isspace():
		csize += 1
		msize += 1
		i += 1
	else:
		i += 1

print csize - msize
