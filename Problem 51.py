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

def duplicate(n):
    s = str(n)
    x,c = '',0
    for i in s[1:]:
        if s.count(i)>c:
            x = i
            c = s.count(i)
    firstd = False
    if s[0]==x:
        firstd = True
    return x,c,firstd

checked=[]
for i in pr:
    if i not in checked:
        l = []
        d,c,firstd = duplicate(i)
        if c in (3,5):
            a = 0
            if firstd:
                a = 1
            for j in range(a,10):
                l.append(int(str(i).replace(d,str(j))))
            checked.extend(l)
            temp = [k for k in l if k in pr]
            if len(temp)==8:
                print(temp)
                break