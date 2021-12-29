import itertools
def property(n):
    s = str(n)
    if not int(s[1:4]) % 2:
        if not int(s[2:5]) % 3:
            if not int(s[3:6]) % 5:
                if not int(s[4:7]) % 7:
                    if not int(s[5:8]) % 11:
                        if not int(s[6:9]) % 13:
                            if not int(s[7:10]) % 17:
                                return True
    return False

print(sum([int(''.join(i)) for i in itertools.permutations("1234567890") if sorted(''.join(i))==list("0123456789") and property(int(''.join(i)))]))
