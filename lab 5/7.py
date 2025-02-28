import re
snake = "snake_case_askdkj"
capital = snake.upper()
camel = ""
i = 0
while(i!=len(snake)):
    if(snake[i]=="_"):
        camel += snake[i] + capital[i+1]
        i += 2
    else:
        camel += snake[i]
        i += 1
camel = re.sub("_", "", camel)
print(camel)