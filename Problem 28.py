'''
forward diagonal is (sum of squares till 1001)+(500) because 
bottom half is even squares plus one and upper half is odd squares

backward diagonal excluding center 1 is 1^2 + 3^2 + 3^2 + 5^2 + 5^2 + 7^2...
                                    (or: 1^2 + 1001^2 + 2(3^2 + 5^2 + 7^2...)) because
bottom half is 1^2 + 2,3^2 + 4, 5^2 + 6... and
upper half is 3^2 - 2, 5^2 - 4, 7^2 - 6...
'''
'''
n = 1001
res = (n//2)
res += (n*(n+1)*((2*n)+1))//6

res+= 1*1 + n*n
temp = 0
for i in range(3,n,2):
    temp+=i*i

res+=2*temp

print(res)
'''
'''
or
sum of corners of each square is 4n^2 - 6(n-1)
'''
n=1001
print(sum(4*i*i - 6*(i-1) for i in range(3,n+1,2))+1)