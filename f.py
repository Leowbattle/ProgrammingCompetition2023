rows, cols = map(int, input().split(' '))
grid = []
for i in range(rows):
	grid.append(list(input()))

for y in range(rows-2, -1, -1):
	for x in range(cols):
		if grid[y][x] != 'a':
			continue
		for next_row in range(y+1, rows):
			if grid[next_row][x] != '.':
				grid[y][x] = '.'
				grid[next_row - 1][x] = 'a'
				break
		else:
			grid[y][x] = '.'
			grid[rows - 1][x] = 'a'

for i in grid:
	print(''.join(i))