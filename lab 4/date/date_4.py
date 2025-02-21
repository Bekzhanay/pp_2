import datetime
date1 = input()
date2 = input()
d1 = datetime.datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')
d2 = datetime.datetime.strptime(date2, '%Y-%m-%d %H:%M:%S')
x = abs((d2 - d1).total_seconds())
print(f"Difference: {x}")