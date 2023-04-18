'''
Create an Abstract Base Class called Shape that include abstract methods area() and circumference(). 
Then derive two classes Circle and Rectangle from the Shape class and implement the area() and circumference() methods.
'''

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def circumference(self):
        pass


class Rectangle(Shape):
    def __init__(self, ln, bd):
        self.ln = ln
        self.bd = bd

    def area(self):
        return self.ln*self.bd

    def circumference(self):
        return 2*(self.ln+self.bd)


class Circle(Shape):
    def __init__(self, rad):
        self.rad = rad

    def area(self):
        return pi*self.rad**2

    def circumference(self):
        return 2*pi*self.rad


l = int(input("Rectangle: Enter the length:"))
b = int(input("Enter the breadth:"))
r = int(input("Circle:Enter the radius:"))
R = Rectangle(l, b)
C = Circle(r)

print("Area of Rectangle: ", R.area())
print("Circumference of Rectangle: ", R.circumference())
print("Area of Circle: ", C.area())
print("Circumference of Circle: ", C.circumference())
