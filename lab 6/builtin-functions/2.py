txt = input()
cntup = 0
cntlow = 0
for i in txt:
    if i.isupper():
        cntup += 1
    elif i.islower():
        cntlow += 1
print("Uppercase letters: ", cntup)
print("Lowercase letters: ", cntlow)