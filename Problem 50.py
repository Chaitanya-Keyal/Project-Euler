import itertools
def isPrime(n):
    if n==2:
        return True
    elif n<2 or not n%2:
        return False
    else:
        for i in range(3,int(n**0.5)+1,2):
            if not n%i:
                return False
        return True
pr = []
for i in range(1000000):
    if isPrime(i):
        pr.append(i)

sumpr = list(itertools.accumulate(pr))

n,l=0,0

for i in range(l,len(sumpr)):
    for j in range(i-l-1,-1,-1):
        temp = sumpr[i]-sumpr[j]
        if temp > 1000000:
            break
        if temp in pr:
            l = i-j
            n = temp

print(n)