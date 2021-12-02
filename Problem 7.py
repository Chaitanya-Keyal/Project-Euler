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

i,counter = 1,0
while counter<10001:
    i+=1
    if isPrime(i):
        counter += 1

print(i)
