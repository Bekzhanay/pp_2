import random
print("Hello!, What is your name?")
name = input()
print(f"Well, {name}, I am thinking of a number between 1 and 20.")
print("Take a guess")
n = random.randrange(1, 20)
num = list(map(int, input().split()))

for i in range(20):
    if num[i] == n:
        print(f"Good job, {name}! You guessed my number in {len(num)} guesses!")
        break
    elif num[i] > n:
        print("Your guess is too large.")
        print("Take a guess.")
        x = int(input())
        num.append(x)
    else:
        print("Your guess is too low.")
        print("Take a guess.")
        y = int(input())
        num.append(y)