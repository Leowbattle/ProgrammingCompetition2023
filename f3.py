rows, cols = map(int, input().split(' '))
grid = []
for i in range(rows):
	grid.append(list(input()))

for col in range(cols):
	bottom = rows-1
	for y in range(rows-1, -1, -1):
		if grid[y][col] == "#":
			bottom = y-1
		elif grid[y][col] == "a":
			grid[y][col] = "."
			grid[bottom][col] = "a"
			bottom -= 1

for i in grid:
	print("".join(i))