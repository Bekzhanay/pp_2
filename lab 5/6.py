import re
str = "sdli fhd sjfkl.,,sdhflskj----___dsfds.nmk.llsdfj-sdlfj"
x = re.sub(r"[,. ]", ":", str)
print(x)