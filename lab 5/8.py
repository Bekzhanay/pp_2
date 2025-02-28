import re
str = "AfGslkjfsdlkjAdfslkjfslkjdfA<vncalFkfjslkjgAldfkjg;dkfglKl'kjSkdjfLSKdjdflkA"
x = re.findall(r"[^A-Z]+", str)
print(x)