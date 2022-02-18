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

def smallestMultiple(start,end):
    l = [i for i in range(start,end+1) if isPrime(i)]
    n=1
    for i in l:
        temp = i
        while temp<=end:
            temp*=i
        n*=(temp/i)
    return n

print(smallestMultiple(1,20))