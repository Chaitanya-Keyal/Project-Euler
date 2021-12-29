def sides(n):
    l = []
    for c in range(1,n//2):
        for b in range(1,c):
            a = n-b-c
            if a*a +b*b == c*c and sorted((a,b,c)) not in l:
                l.append(sorted((a,b,c)))
    return len(l)

print(max(range(1,1001),key= sides))