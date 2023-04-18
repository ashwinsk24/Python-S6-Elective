'''
Create an Abstract Base Class called Polygon that include abstract methods area() and display(). 
Then derive 3 classes Square, Circle and Rectangle from the Shape class and implement the area() method.
Write a Python program to implement above concept.
'''

from abc import ABC, abstractmethod
from math import pi


class Polygon(ABC):
    @abstractmethod
    def area(self):
        pass

    def display(self):
        print("Area:")


class Rectangle(Polygon):
    def __init__(self, ln, bd):
        self.ln = ln
        self.bd = bd

    def area(self):
        return self.ln*self.bd


class Square(Polygon):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2


class Circle(Polygon):
    def __init__(self, rad):
        self.rad = rad

    def area(self):
        return pi*self.rad**2


l = int(input("Rectangle: Enter the length:"))
b = int(input("Enter the breadth:"))
s = int(input("Square: Enter the side:"))
r = int(input("Circle:Enter the radius:"))

R = Rectangle(l, b)
C = Circle(r)
S = Square(s)

print("\nArea of Rectangle: ", R.area())
print("Area of Square: ", S.area())
print("Area of Circle: ", C.area())
