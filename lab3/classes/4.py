class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"x = {self.x}\ny = {self.y}")

    def move(self, newx, newy):
        self.x = newx
        self.y = newy
    
    def dist(self, point2):
        return ((self.x-point2.x)**2 + (self.y-point2.y)**2)**0.5
    
x, y = map(int, input("enter coordinates of point1: ").split())
x1, y1 = map(int, input("enter coordinates of point2: ").split())
point1 = Point(x, y)
point2 = Point(x1, y1)

point1.show()
point2.show()

x2, y2 = map(int, input("change coordinates of point1: ").split())
point1.move(x2, y2)
point1.show()

print(f"distance between points: {point1.dist(point2)}")