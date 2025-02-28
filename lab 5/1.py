import re
str = "dsabflkhasdkjasdlksdfl"
str1 = "bcd"
x = re.findall("ab*", str)
y = re.findall("ab*", str1)
print(x)
print(y)