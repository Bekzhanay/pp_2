def hist(ls):
    for i in range(len(ls)):
        s = ""
        for j in range(ls[i]):
            s = s + "*"
        print(s)
l = list(map(int, input().split()))
hist(l)