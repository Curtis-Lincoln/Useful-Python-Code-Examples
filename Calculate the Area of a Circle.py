#Calculating the Area of a Circle
CONSTANT_PI = 3.14159

def circle_area(radius_in):
    area_out = CONSTANT_PI * radius_in**2
    return area_out

radius = int(input("Enter the radius of the circle: "))
area = circle_area(radius)
print("The area of the circle is", area)
