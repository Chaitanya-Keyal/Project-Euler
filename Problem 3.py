n = 600851475143
c = 2
f = 0
while(c**2 <= n):
    if not n%c:
        n/=c
        f = c
    else:
        if c==2:
            c+=1
        else:
            c+=2
if n>f:
    f = n

print(f)

