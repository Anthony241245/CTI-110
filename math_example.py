#In-class examples of math equations

#import random libarary for use in the program
import random



'''
#Get value of side from user

side1 = float(input('Enter value for side 1: '))

side2 = float(input('Enter value for side 2: '))
'''

#Generate random values for side1 and side2
side1 = random.randint(1,100)
side2 = random.randint(1,50)

#Calaculate the hypotenuse
hypotenuse = (side1**2) + (side2**2)

#Display the results to the user
print(f"The hypotenuse of an right triangle with the sides {side1} and {side2} is {hypotenuse}")
