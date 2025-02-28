import re
str = "AadskfjsklfAjslkdfjsdlfGajfkdlfjDSFalfskjAKgljsldfjlFAKlklkFLKSDJFLASJFLKSDJFLKJ"
x = re.findall("[A-Z]{1}[a-z]+", str)
print(x)