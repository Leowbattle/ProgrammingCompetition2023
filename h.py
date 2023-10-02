l, m = map(int, input().split())
out, price = "", 100001
for i in range(m):
	inp = input().split(',')
	n = inp[0]
	p, c, t, r = map(int, inp[1:])
	if (10080*c*t) / (t+r) >= l:
		if p < price:
			price = p
			out = n
		elif p == price:
			if out == "":
				out = n
			else:
				out += "\n" + n
if out == "":
	print("no such mower")
else:
	print(out)