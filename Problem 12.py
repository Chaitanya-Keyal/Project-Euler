import math


def countFact(n):
    count = 2
    for i in range(2,math.ceil(math.sqrt(n))):
        if not n%i:
            count+=2
        if n==i*i:
            count-=1
    return count

n,i = 1,0
while countFact(n)<500:
    i+=1
    n = (i*(i+1))//2

print(n)
