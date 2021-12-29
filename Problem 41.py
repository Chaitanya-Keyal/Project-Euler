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

for i in range(7654321,1233,-1):
    if sorted(str(i)) == list("123456789")[:len(str(i))] and isPrime(i):
        print(i)
        break
