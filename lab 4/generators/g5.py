def down(n):
    for i in range(n, -1, -1):
      yield i
n = int(input("N:"))
for x in down(n):
   print(x)