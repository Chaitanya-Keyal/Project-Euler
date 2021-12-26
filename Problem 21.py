def sumFact(n):
    sum = 0
    for i in range(1,(n//2)+1):
        if not n%i:
            sum+=i
    return sum
    
l = []
for i in range(1,10001):
    temp = sumFact(i)
    if sumFact(temp) == i and temp!=i:
        l.extend([i,temp])

L = []
for i in l:
    if i not in L:
        L.append(i)

print(sum(L))