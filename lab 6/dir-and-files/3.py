from colorama import Fore, Back, Style

import os

def f(path):
    if not os.access(path, os.F_OK):
        return False
    return True

path = input()

if f(path):
    with os.scandir(path) as it:
        for x in it:
            if (x.is_dir()):
                print(Fore.WHITE + "Directories: " + x.name)
            else:
                print(Fore.RED + "Files: " + x.name)
else:
    print("No such path exist")

print(Style.RESET_ALL)