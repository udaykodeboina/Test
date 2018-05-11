#to find area and perimeter of a circle
import math#import math module
class circle():#creating a circle class 
    def __init__(self,radius):#creating a user defined function init
        self.radius=radius
    def area(self):#creating a user defined function area
        return math.pi*(self.radius**2)
    def perimeter(self):#creating a user defined function perimeter
        return 2*math.pi*self.radius
 
r=int(input("Enter radius of circle: "))#enter radius of a circle which is int type
obj=circle(r)#creating a object for circle class
print("Area of circle:",round(obj.area(),2))#perform area and print area of circle
print("Perimeter of circle:",round(obj.perimeter(),2))#perform perimeter and print erimeter of a circle
