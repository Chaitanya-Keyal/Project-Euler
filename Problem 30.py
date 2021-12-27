def psum(n):
    return sum(int(i)**5 for i in str(n))

print(sum(i for i in range(2, 6*9**5) if i == psum(i)))
