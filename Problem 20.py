f = 1
for i in range(1,101):
    f*=i

f = str(f)
sum = 0
for i in f:
    sum+=int(i)

print(sum)