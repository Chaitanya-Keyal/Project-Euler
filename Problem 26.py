def reciprocal(n):
    dec = []
    rem = []
    r = 1
    while True:
        r = 10 * (r%n)
        if not r or r in rem:
            break
        else:
            dec.append(r//n)
            rem.append(r)
    rep = 0
    if r:
        rep = len(dec[rem.index(r):])
    ans = "0."
    for i in dec[:-rep]:
        ans+=str(i)
    ans+="("
    for i in dec[-rep:]:
        ans+=str(i)
    ans += ")"
    return ans,rep

maxrep,maxquo,div=0,'',0
for i in range(1,1000):
    quo,rep = reciprocal(i)
    if rep>maxrep:
        maxquo,maxrep,div = quo,rep,i

print("Maximum Repeat: 1/",div,"=",maxquo,"\nRepeated Decimals =",maxrep)

