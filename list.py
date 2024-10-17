#In-class example using lists
'''
#Create an empty list
myfam = []

#Add values to the list
myfam.append("Mallory")
myfam.append("Mandy")
myfam.append("Natelie")
myfam.append("Brant")
myfam.append("Yoshi")

#Display list
print(myfam)

#Print item at index 3
print(myfam[3])

#Print items from index 1 to 3(must give 4)(up to, but not including 3)
#Add one to your ending index
print(myfam[1:4])

#Remove item from list by its value
myfam.remove('Yoshi')
print(myfam)
#Remove item from list by its index
myfam.pop(2)

print(f"\n\n Remove Natelie")
print(myfam)
'''
num1 = int(input("gimme a number: "))
num2 = int(input("gimme a number: "))
num3 = int(input("gimme a number: "))
num4 = int(input("gimme a number: "))

#Creat the list with the values in it
numbers = [num1, num2, num3, num4]
print(numbers)

#Functions use list

#Gives back the number of items in the list
print(f"There are {len(numbers)} items in the list")

#Highest nuumber
print(f"The highest value in the lists is {max(numbers)}")

#Get the sum of all numbers
print(f"The sum of values in the list is {sum(numbers)}")

#Get average
average = sum(numbers)/len(numbers)

#display average
print(f"The Average of values in the list is {average}")
