class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        self.lenght = 0
    def area(self):
        return self.lenght**2
shape = Shape()
square = Square(Shape)
square.lenght = int(input())
print(square.area())
print(shape.area())