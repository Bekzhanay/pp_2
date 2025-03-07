s = input()

with open(s, "r") as f:
    cnt = 0
    for x in f:
        cnt += 1

print("Number of lines:", cnt)