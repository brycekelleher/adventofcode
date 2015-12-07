import sys

def check_bad_strings(s): return all(map(lambda x: x not in s, ['ab', 'cd', 'pq', 'xy'])) 
#def check_vowels(s): return len(filter(lambda x: x in 'aeiou', list(s))) >= 3
def check_vowels(s): return len([x for x in s if x in 'aeiou']) >= 3
#def check_doubles(s): return any(map(lambda x: x in s, [x + x for x in "abcdefghijklmnopqrstuvwxyz"]))
def check_doubles(s): return any(map(lambda x: x[0] == x[1], zip(s, s[1:])))
def check(l): return len(filter(lambda x: check_bad_strings(x) and check_vowels(x) and check_doubles(x), l))
print check(sys.stdin.read().split())
