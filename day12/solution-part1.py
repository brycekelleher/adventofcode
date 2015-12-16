import sys

s = sys.stdin.read()
s = "".join([" " if c in "{}[],:\"" else c for c in s])
s = s.split()
s = filter(lambda x: x.isdigit() or x[0] == '-', s)
s = map(int, s)
print sum(s)

