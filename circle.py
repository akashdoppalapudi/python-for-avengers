import math
class Circle:
    def __init__(self,radius):
        self.radius = radius
        
    def circumference(self):
        c = 2*math.pi*self.radius
        return c

    def area(self):
        a = math.pi * self.radius**2
        return a

    def __str__(self):
        return "circle of radius " + str(self.radius)

    def __del__(self):
        print("Circle of radius", self.radius, "is deleted.")


circle1 = Circle(5)
print(circle1)
print(circle1.circumference())
print(circle1.area())
del circle1