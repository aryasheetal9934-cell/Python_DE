# WAP to create a class named Shape. include methods to calculate the ares and perimeter of different shapes
# e.g. squares,circles,triangle using inheritance and polymorphism . implement subclasses for easc shape and override
# the ares and perimeter methods accordingly.

import math

class Shape:
    def cal_ares(self):
        pass
    def cal_perimeter(self):
        pass

class Circles(Shape):
    def __init__(self,radius):
        self.radius=radius

    def cal_area(self):
        return math.pi*self.radius**2
    
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def cal_area(self):
        return self.length*self.width
    
    def cal_perimeter(self):
        return 2*(self.length+self.width)
    
class Triangle(Shape):
    def __init__(self,side1,side2,side3,height,base):
        self.side1=side1
        self.side2=side2
        self.side3=side3
        self.height=height
        self.base=base

    def cal_area(self):
        return 0.5*self.base*self.height

    def cal_perimeter(self):
        return self.side1+self.side2+self.side3
    
r=7
circle=Circles(r)
print(f"area of circle with radius{r}is: {circle.cal_area()}")
print(f"permimeter of cicles with radius {r} is: {circle.cal_perimeter()}")

l=5
w=3
rectangle=Rectangle(l,w)
print(f"Area of Rectangle with lenght{l} and widht {w} is :{rectangle.cal_area()}")
print(f"perimter of rectangle with lenght {l} and width {w} is {rectangle.cal_perimeter()}")
      

base=4
height=6
side1=4
side2=5
side3=6
triangle=Triangle(side1,side2,side3,height,base)
print(f"Area of triangle with base {base} and (height) is: {triangle.cal_area}")
print(f"perimeter of triangle with sides {side1},{side2},{side3} is: {triangle.cal_perimeter()}")