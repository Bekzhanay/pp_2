class Shape:
    def Area(self):  
        return 0
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def Area(self):  
        return self.length ** 2  
fig = Square(int(input("Square length: ")))
print(f"The area of the square: {fig.Area()}")