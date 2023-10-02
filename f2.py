r, c = [int(x) for x in input().split()]
grid = []
for i in range(r):
	grid.append(input().split())

cols = [row[i] for row in range(r)]
print(cols)