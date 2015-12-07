import sys

#def check_repeats(s): return len(filter(lambda x: x[0] == x[2], [s[x-2] + s[x-1] + s[x] for x in range(2, len(s))])) >= 1
def check_repeats(s): return len(filter(lambda x: x[0] == x[1], zip(s, s[2:]))) >= 1
def check_pairs(s): return any(filter(lambda x: x >= 2, map(lambda x: s.count(x), [s[x-1] + s[x] for x in range(1, len(s))]))) 
def check(l): return len(filter(lambda x: check_repeats(x) and check_pairs(x), l))
print check(sys.stdin.read().split())

