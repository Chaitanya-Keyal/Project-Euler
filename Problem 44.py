def isPenta(n):
    if ((24*n + 1)**0.5 + 1)%6:
        return False
    return True

i = 1
while True:
    for j in range(i-1,0,-1):
        a = i*(3*i-1)//2
        b = j*(3*j-1)//2
        if isPenta(a+b) and isPenta(a-b):
            print(a-b)
            break
    else:
        i+=1
        continue
    break