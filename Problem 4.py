def isPalindrome(n):
    s = str(n)
    if s==s[::-1]:
        return True
    else:
        return False

r = 0
for i in range(999,100,-1):
    for j in range(999,100,-1):
        temp = i*j
        if isPalindrome(temp) and temp>r:
             r = temp

print(r)
