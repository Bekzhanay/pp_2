def unique(ls):
    lst = []
    for i in range(len(ls)):
        k = ls.count(ls[i])
        if k == 1:
            lst.append(ls[i])
    print(lst)
l = list(input())
unique(l)