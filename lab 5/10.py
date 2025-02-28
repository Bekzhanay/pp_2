import re
camel = "camelCaseExample"
snake = re.sub(r"([^a-z]+)", r"_\1", camel)
snake = snake.lower()
print(snake)