def f(a, b, h):
    res = ((a + b) / 2) * h
    print(f"Expected Output: {res}")

a = int(input("Height: "))
b = int(input("Base, first value: "))
h = int(input("Base, second value: "))
f(a, b, h)