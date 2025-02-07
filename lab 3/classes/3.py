class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self):
        self.length = int(input("Length: "))
        self.width = int(input("Width: "))
    def area(self):
        return self.length * self.width


shape = Shape()
print(f"Shap's area: {shape.area()}")

rectangle = Rectangle()
print(f"Rectangle's area: {rectangle.area()}")