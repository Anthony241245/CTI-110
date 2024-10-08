#Anthony Raynor
#10/8/24
#P2LAb1
# Using Python's built-in math library
# write code that performs mathematical calculations and displays information to users

import math

print(f"The value of pi is {math.pi}\n")
print()
#Get radius from user

radius = float(input("What is the radius of the cirle? "))
print()
#Get the diamter
diameter = 2 * radius
#Display diameter with one decimal place
print(f"The dimaeter of the circle is {diameter:.1f}\n")
print()
#Get the cirumference
cirumfrenece = 2 * math.pi * radius
#Display the cirumference
print(f"The cirumference of the circle is {cirumfrenece:.2f}\n")
print()
#Get area of the circle
area = math.pi * radius**2
#Display the area
print(f"The area of the circle is {area:.3f}\n")



