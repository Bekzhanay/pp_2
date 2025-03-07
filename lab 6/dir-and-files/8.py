import os

for x in range(65, 91):
    file_name = chr(x) + ".txt"
    if os.access(file_name, os.F_OK):
        os.remove(file_name)
    else:
        pass