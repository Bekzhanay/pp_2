import os

l = input().split()

with open("file_name.txt", "w") as f:
   f.write(" ".join(l))