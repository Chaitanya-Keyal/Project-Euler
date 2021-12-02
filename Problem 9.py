import math
def isSquare(n):
    if math.sqrt(n) == int(math.sqrt(n)):
        return True
    else:
        return False

prod = 1
for i in range(400,1,-1):
    for j in range(400,1,-1):
        temp = i*i+j*j
        if isSquare(temp):
            k = int(math.sqrt(temp))
            if (i + j + k) == 1000:
                print(i,j,k)
                prod = i*j*k
                break

print(prod)