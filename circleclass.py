'''
Write a Python class named Circle constructed by a
radius and two methods which will compute the area and the perimeter of
a given circle
'''

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius**2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

# Example usage
circle = Circle(5)
print("Area:", circle.area())
print("Perimeter:", circle.perimeter())
