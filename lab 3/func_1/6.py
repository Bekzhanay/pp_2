def reverse(s):
    new_str = ""
    listik = s.split()
    listik.reverse()
    new_str = " ".join(listik)
    print(new_str)

str = input() 
reverse(str)