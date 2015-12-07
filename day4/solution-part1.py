import hashlib

i = 0
while True:
	h = hashlib.md5('iwrupvqb' + str(i)).hexdigest()
	print h
	if (h[:5] == '00000'):
		break
	i += 1

print i
