class Point:
    def __init__(self):
        self.p1 = int(input("x: "))
        self.p2 = int(input("y: "))
    def show(self):
        print(f"Point A: ({self.p1}, {self.p2})")

    def move(self):
        self.p3 = int(input("x1: "))
        self.p4 = int(input("y1: "))
        print(f"Point B: ({self.p3}, {self.p4})")

    def dist(self):
        self.sum = (self.p3 - self.p1)**2 + (self.p4 - self.p2)**2
        self.dt = self.sum**0.5
        print(f"Distance between A and B: {self.dt:.1f}")

point = Point()
point.show()
point.move()
point.dist()