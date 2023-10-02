while (True):
	inp = int(input())
	if inp == 0:
		break
	i = 0
	s = 0
	while i < inp:
		s += i
		if s >= inp-1:
			print(i)
			break
		i+=1