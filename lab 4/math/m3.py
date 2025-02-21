import math
def f(l, n):
    p = n * l
    pi = math.pi
    ang = math.tan(pi / n) 
    a = l / (2 * ang)
    s = (a * p) / 2
    print(f"The area of the polygon is: {s:.0f}")
number = int(input("Input number of sides: "))
lengh = int(input("Input the length of a side: "))
f(lengh, number)