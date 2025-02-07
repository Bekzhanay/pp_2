a = int(input())
x = lambda k : k // 2
k = 0
for i in range(2, x(a) + 1):
    if (a % i == 0):
        k = k + 1

if (k <= 0):
    print("Prime")
else:
    print("Not prime")