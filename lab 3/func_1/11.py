def pal(st):
    ts = st.copy()
    ts.reverse()
    for i in range(len(st)):
        if st[i] != ts[i]:
            return False
    return True
s = list(input())
if pal(s):
    print(True)
else:
    print(False)