def isPenta(n):
    if ((24*n + 1)**0.5 + 1)%6:
        return False
    return True

def isHexa(n):
    if ((8*n + 1)**0.5 + 1)%4:
        return False
    return True

tri = []
for i in range(100000):
    tri.append((i*(i+1))//2)

for i in tri:
    if isPenta(i) and isHexa(i):
        print(i)