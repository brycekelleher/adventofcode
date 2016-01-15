def fs(n):
	counts = {}
	for i in range(1, n + 1):
		for j in range(i, n + 1, i):
			if not j in counts:
				counts[j] = 0
			counts[j] += i

		if counts[i] >= n:
			return i

		# the solution can't be i so remove it
		# deletion is O(1) from a dict so should be fast
		del counts[i]

def fs2(n):
	counts = {}
	for i in range(1, n + 1):
		for j in range(i, i * 51, i):
			if not j in counts:
				counts[j] = 0
			counts[j] += i * 11

		if counts[i] >= n:
			return i

		# the solution can't be i so remove it
		# deletion is O(1) from a dict so should be fast
		del counts[i]

#print find_solution2(2900000)
