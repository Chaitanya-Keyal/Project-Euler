import math
def isPrime(n):
    if n==2:
        return True
    elif n<2 or not n%2:
        return False
    else:
        for i in range(3,int(math.sqrt(n))+1,2):
            if not n%i:
                return False
        return True

plist = []
for i in range(1001):
    if isPrime(i):
        plist.append(i)

d={}
for a in range(-999,1001):
    for b in plist:
        n=0
        while True:
            if isPrime((n*n)+(a*n)+b):
                n+=1
            else:
                break
        d[n]=(a,b)

print(d[max(d)][0]*d[max(d)][1])