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

def truncate(n):
    l = []
    s = str(n)
    for i in range(len(s)):
        try:
            l.extend([int(s[i:]),int(s[:-i])])
        except:
            l.append(int(s[i:]))
    return sorted(l,reverse=True)

l = []
for i in range(8,1000000):
    temp = truncate(i)
    for j in temp:
        if not isPrime(j):
            break
    else:
        l.append(i)

print(len(l),sum(l))