def append_of_files():
    with open("first.txt", "r") as firstfile, open("second.txt", "a") as secondfile:
        for line in firstfile:
            secondfile.write(line)