# from math import comb

# a_uniq, b_uniq, a_reuse, b_reuse = [int(x) for x in input().split()]
# print(a_reuse * b_reuse + comb(a_uniq, b_uniq))

au, bu, ar, br = [int(x) for x in input().split()]

ans = ar * br
if ar == 0 and br == 0:
	ans += min(au, bu)

if ar > 0:
	ans += bu

if br > 0:
	ans += au

print(ans)
