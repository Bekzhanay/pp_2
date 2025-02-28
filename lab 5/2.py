import re
str = "abbabadfadsfbadbasfasfbabbbfbbfabfbabbbbfsbfgsdbqbgabAFBA"
x = re.findall("ab{2,3}", str)
print(x)