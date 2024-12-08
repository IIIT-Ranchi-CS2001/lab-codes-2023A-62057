import math

side1=float(input("Enter first size : "))
side2=float(input("Enter second size : "))
side3=float(input("Enter third size : "))

s=(side1+side2+side3)/2

print("Perimeter of triangle is :",2*s)
print("Area of tringle is :",(s*(s-side1)*(s-side2)*(s-side3))**(0.5))

a1=math.degrees(math.acos(((side2**2)+(side3**2)-(side1**2))/(2*side2*side3)))
a2=math.degrees(math.acos(((side1**2)+(side3**2)-(side2**2))/(2*side1*side3)))
a3=math.degrees(math.acos(((side2**2)+(side1**2)-(side3**2))/(2*side2*side1)))

print("First angle is :",a1)
print("Second angle is :",a2)
print("Third angle is :",a3)

print("this is a test")