string = input()
it = iter(string)
rit = reversed(string)
s = ""
for x in rit:
    s += x

if string == s:
    print("Palindrome")
else:
    print("Not palindrome")