s = 0
for i in range(1000000):
    if str(i)[::-1]==str(i) and bin(i)[:1:-1]==bin(i)[2:]:
        s+=i
print(s)