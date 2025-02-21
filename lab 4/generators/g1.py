def sq(N):
    for i in range(1, N + 1):
        yield i ** 2
n = int(input())
for x in sq(n):
    print(x)