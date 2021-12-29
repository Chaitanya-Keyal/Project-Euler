import math as m
ans = 0
for n in range(3,1000000):
    if sum([m.factorial(int(i)) for i in str(n)]) == n:
        ans+=n
print(ans)