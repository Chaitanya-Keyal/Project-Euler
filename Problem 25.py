l = [0,1]
i = 2
while True:
    temp = l[i-1]+l[i-2]
    l.append(temp)
    if temp>10**999:
        print(i)
        break
    i+=1