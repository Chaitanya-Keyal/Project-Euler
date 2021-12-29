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

for i in range(1000,10000):
    if isPrime(i):
        for j in range(1,5000):
            if i + 2*j <10000:
                t1 = i + j
                t2 = t1 + j
                if isPrime(t1) and isPrime(t2) and sorted(str(i))==sorted(str(t1))==sorted(str(t2)):
                    print(i,t1,t2)