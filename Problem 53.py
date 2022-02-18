import math
c = 0
for i in range(23,101):
    for j in range(1,i):
        if math.factorial(i)/(math.factorial(j)*math.factorial(i-j))>1000000:
            c+=1
print(c)