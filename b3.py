import math
x = int(input())
out = []
i = x // 2
j = (x // 2) - 1
while x > 0:
	if str(i) == str(i)[::-1] and x - i > 0:
		x -= i
		out.append(i)
	else: i += 1
	if str(j) == str(j)[::-1] and x - j > 0:
		x -= j
		out.append(j)
	else: j -= 1

print(len(out))
print('\n'.join(map(str, out)))