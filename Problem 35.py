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

def circulate(n):
    l = []
    s = str(n)
    for i in range(len(s)):
        l.append(int(s[i:]+s[:i]))
    return l

l = []
for i in range(1000000):
    temp = circulate(i)
    for j in temp:
        if not isPrime(j):
            break
    else:
        l.extend(temp)

L = []
for i in sorted(l):
    if i not in L:
        L.append(i)

print(len(L),L)