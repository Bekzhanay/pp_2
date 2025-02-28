import re
str = "asdFghjJkl;zxcBnm,x"
x = re.sub(r"([A-Z])", r" \1", str)
print(x)