def sumFact(n):
    sum = 0
    for i in range(1,(n//2)+1):
        if not n%i:
            sum+=i
    return sum

l = []
for i in range(28124):
    if sumFact(i)>i:
        l.append(i)

ints = [i for i in range(1,28123)]

for i in range(len(l)):
    for j in range(i,28123):
        temp = l[i] + l[j]
        if temp<28123:
            ints[temp-1]=0
        else:
            break

ints = [i for i in ints if i != 0]
print(ints)
print(sum(ints))