def primefact(n):
    l = []
    while not n%2:
        n/=2
        l.append(2)
    
    for i in range(3,int(n**0.5)+1,2):
        while not n%i:
            n/=i
            l.append(i)
    
    if n>2:
        l.append(int(n))
    
    d = {}
    for i in l:
        d[i]=l.count(i)
    
    return d

i = 209
while True:
    i+=1
    for j in range(4):
        if len(primefact(i+j))!=4:
            break
    else:
        print(i)
        break