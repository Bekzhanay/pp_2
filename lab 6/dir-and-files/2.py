import os

def f(path):

    if not os.access(path, os.F_OK):
        print("File is not exist.")
        return


    if os.access(path, os.R_OK):
        print("File is readable.")
    else:
        print("File is not readable.")


    if os.access(path, os.W_OK):
        print("File is writable.")
    else:
        print("File is not writable.")

    if os.access(path, os.X_OK):
        print("File is executable.")
    else:
        print("File is not executable.")

path = input()
f(path)