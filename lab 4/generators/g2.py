def even(n):
    for i in range(0, n + 1, 2):
        print(i, end=", ")
n = int(input("N: "))
even(n)