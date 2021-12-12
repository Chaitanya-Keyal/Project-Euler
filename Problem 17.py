l = '''one
two
three
four
five
six
seven
eight
nine
ten
eleven
twelve
thirteen
fourteen
fifteen
sixteen
seventeen
eighteen
nineteen
twenty
thirty
forty
fifty
sixty
seventy
eighty
ninety
hundred
and'''.splitlines()
temp = 0
for i in range(9):
    temp+=len(l[i])

temp1 = 0
for i in range(19):
    temp1+=len(l[i])

temp2 = 0
for i in range(19,27):
    temp2 += len(l[i])*10 + temp
temp2+=temp1

temp3 = 0
for i in range(9):
    temp3 += len(l[27])*100 + len(l[28])*99 + len(l[i])*100 + temp2

sum = temp2 + temp3 + len("onethousand")

print(sum)
