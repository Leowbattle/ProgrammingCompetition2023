x = int(input())
out = []

# while x > 0:
# 	for i in range(x, 0, -1):
# 		if str(i) == str(i)[::-1]:
# 			x -= i
# 			out.append(i)
# 			break

if str(x) == str(x)[::-1]:
	out.append(x)

else:
	m = x
	for i in range(x, -1, -1):
		if str(i) == str(i)[::-1]:
			m -= i
			out.append(i)
			if m <= 0 or len(out) >= 10:
				break
	# while x > 9:
	# 	n = int('9' * (len(str(x)) - 1))
	# 	x -= n
	# 	out.append(n)

	# if x > 0:
	# 	out.append(x)

print(len(out))
print('\n'.join(map(str, out)))