d = [0]
n = 0
while len(d)<=1000000:
    n+=1
    d.extend(list(str(n)))

for i in range(len(d)):
    d[i] = int(d[i])

print(d[1]*d[10]*d[100]*d[1000]*d[10000]*d[100000]*d[1000000])