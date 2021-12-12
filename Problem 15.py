def fact(n):
    f = 1
    for i in range(n,1,-1):
        f*=i
    return f

print(fact(20+20)/(fact(20)*fact(20)))
