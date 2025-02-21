def div(n):
    a = 1
    while a <= n:
        if a % 3 == 0 and a % 4 == 0:
            yield a
        a += 1
n = int(input("N: "))
for x in div(n):
    print(x)