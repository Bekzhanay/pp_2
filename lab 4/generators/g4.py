def sq(n):
   a = 1
   while a <= n:
      x = a ** 2
      yield x
      a += 1
n = int(input("N:"))
for x in sq(n):
   print(x)