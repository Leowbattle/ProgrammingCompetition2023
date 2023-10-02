import math
t = int(input())
for i in range(t):
	n = int(input())
	a = {}
	for j in range(n):
		key = input().split()[1]
		if key in a:
			a[key] += 1
		else:
			a[key] = 1
	out = 1
	for key in a.keys():
		out *= a[key]+1
	print(out-1)