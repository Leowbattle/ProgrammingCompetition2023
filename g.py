# import sys
# from math import ceil

# def f(x):
# 	return 10 * (x ** 0.5)

# x, y_low, y_high = [int(x) for x in input().split()]

# i = 0
# x2 = x
# while ceil(x2) < y_low:
# 	x2 = f(x2)
# 	if x2 > y_high:
# 		print("impossible")
# 		sys.exit()
# 	i += 1

# print(i, end=' ')

# while ceil(x2) < y_high:
# 	x2 = f(x2)
# 	if x2 < 100 and y_high >= 100:
# 		print("inf")
# 		sys.exit()
# 	i += 1

# print(i)

from math import ceil

def f(x):
	return 10 * (x ** 0.5)

def within(x, low, high):
	return x >= low and x <= high

x, y_low, y_high = map(int, input().split())

lower_bound = 0 if within(x, y_low, y_high) else -1
upper_bound = -1 if y_high < 100 else 'inf'

iterations = 0
while lower_bound == -1 or upper_bound == -1:
	iterations += 1
	x = f(x)

	if within(ceil(x), y_low, y_high) and lower_bound == -1:
		lower_bound = iterations
	elif not within(ceil(x), y_low, y_high) and lower_bound != -1:
		upper_bound = iterations - 1

	if x > y_high:
		break

if lower_bound == -1:
	print('impossible')
else:
	print(f'{lower_bound} {upper_bound}')
