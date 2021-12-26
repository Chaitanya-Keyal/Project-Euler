import calendar
c = 0
for i in range(1901,2001):
    for j in range(1,13):
        if calendar.weekday(i,j,1)==6:
            c+=1
print(c)