import math

a=int(input("Enter first coefficient : "))
b=int(input("Enter second coefficient : "))
c=int(input("Enter third coefficient : "))

D=(b**2)-(4*a*c)

if D==0:
    print("Both roots are real and equal.")
    print("R1=R2=",(-b)/(2*a))
elif D>0:
    print("Roots are real and unequal")
    print("R1=",(-b+math.sqrt(D))/(2*a))
    print("R2=",(-b-math.sqrt(D))/(2*a))
else:
    print("Roots are imaginary")
    print("Real part = ",(-b)/(2*a))
    print("Imaginary part = ",math.sqrt(-D)/(2*a))