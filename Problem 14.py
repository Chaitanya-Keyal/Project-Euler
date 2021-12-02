d = {n:0 for n in range(1000000)}
d[1] = 1
d[2] = 2 

for n in range(3,1000000):
    count = 0
    N = n
    while n>1:
        if n<N:
            d[N] = d[n]+count
            break
        if n%2:
            n = 3*n + 1
            count+=1
        else:
            n/=2
            count+=1
print (list(d.values()).index(max(d.values())))
        