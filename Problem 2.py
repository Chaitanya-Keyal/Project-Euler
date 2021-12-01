a,b=1,2
sum = 0
while a<4000000:
    if not a%2:
        sum+=a
    a,b = b,a+b
print(sum)