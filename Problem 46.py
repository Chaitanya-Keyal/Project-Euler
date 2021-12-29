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

pr = [2]
n = 3

while True:
    if isPrime(n):
        pr.append(n)
    else:
        for i in pr:
            if int(((n-i)//2)**0.5) == ((n-i)//2)**0.5:
                break
        else:
            print(n)
            break
    n+=2