import hashlib

i = 0
while True:
	h = hashlib.md5('iwrupvqb' + str(i)).hexdigest()
	if (h[:6] == '000000'):
		break
	i += 1

print i
