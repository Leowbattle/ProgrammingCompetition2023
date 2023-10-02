n, w = [int(x) for x in input().split()]
dams = [(w, 0, [])]

for i in range(1, n + 1):
	d, c, u = [int(x) for x in input().split()]
	dams[d][2].append(i)
	dams.append((c, u, []))

def func(i):
	if dams[i][2] == []:
		return dams[i][0] - dams[i][1]
	
	m = dams[i][0] - dams[i][1]
	for j in dams[i][2]:
		f = func(j)
		if f < m:
			m = f

	return m

w2 = func(0)
if w2 > w:
	w2 = w
print(w2)