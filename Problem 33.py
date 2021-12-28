l = []
for i in range(10,100):
    for j in range(i+1,100):
        num = [int(i) for i in str(i)]
        den = [int(i) for i in str(j)]
        for x in num:
            if x and x in den:
                num.remove(x)
                den.remove(x)
                if den[0] and num[0]/den[0] == i/j:
                    l.append((i,j))
                break
prod = 1
for i,j in l:
    prod*= i
    prod/= j

print(prod)