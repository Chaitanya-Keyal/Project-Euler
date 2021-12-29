ans = ''
for i in range(2,10):
    for j in range(1,10**(9//i)):
        s = ''.join([str(j*k) for k in range(1,i+1)])
        if sorted(s)==list('123456789'):
            ans = max(s,ans)
print(ans)