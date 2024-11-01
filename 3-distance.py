from math import sqrt

class Point:
    def __init__(self, x : int | float, y : int | float):
        self.x = x
        self.y = y

    def __eq__(self, value):
        return self.x == value.x and self.y == value.y
    
    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)
    
    # def __sub__(self, other):
    #     return Point(0,0)

    # def __mult__(self, other):
    #     return 1
    
    def __str__(self):
        return f"({self.x},{self.y})"

def dist(point1 : Point, point2 : Point) -> float:
    return 0

def length(*args : Point) -> float:
    return 0

a = Point(5,11)
b = Point(2,7)
c = Point(-2,4)

print(a+b)
print(a-b)
print(a*c)
print(dist(a,b))
print(length(a,b,c,a))

