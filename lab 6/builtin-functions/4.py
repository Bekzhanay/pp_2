import time

num = int(input())
milsec = int(input())
sec = milsec / 1000
time.sleep(sec)
sqrt = num ** 0.5
txt = f"Square root of {num} after {sec} is {sqrt}"
print(txt)