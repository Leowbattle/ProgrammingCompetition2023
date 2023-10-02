n = int(input())
s = input()
l = int(s[::-1], 2)

buffer = 0
x = 0
while(n > 0):
	if l & 1 == 1:
		x += 1
		buffer = 2
	elif buffer > 0:
		buffer -= 1
		x += 1
	l=l>>1
	n -= 1

print(x)

# DONE