import math
def pandigital(n):
    for i in range(1, math.floor(math.sqrt(n)) + 1):
        if not n%i:
            if sorted(str(n) + str(i) + str(n // i)) == list("123456789"):
                return True
    return False

print(sum(i for i in range(1,10000) if pandigital(i)))