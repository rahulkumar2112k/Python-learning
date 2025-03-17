import math


def circle_calculation(radius):
    area=math.pi*radius**2
    circumference=2*math.pi*radius
    # return area,circumference
    return round(area,4),round(circumference,4) #rounding to 4 decimal point 


Radius=int(input("Enter a radius :"))

A , C=circle_calculation(Radius)

print("Area of circle : ",A)
print("Circumference of circle :",C)
