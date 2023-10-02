n = int(input())
ndigits = len(str(n)) // 2

ps = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(1, 10 ** ndigits):
	p = int(str(i) + str(i)[::-1])
	ps.append(p)

print(ps)