#Anthony Raynor
#10/10/2024
#P2LAB2
#write code that uses a dictionary to store user input and displays output to the user

#Create a dictionary

cars ={"Camaro":18.21, "Prius":52.36, "Model S":110, "Silverado":26}
#Variable that hold only keys from dicitionary
keys = cars.keys()
#SHow all the keys to the user
print(keys)

print()
selected_car = input("Enter a vehicle to see it's mpg: ")
#Display the seletced car and it's mpg
print(f"The{selected_car} gets {cars[selected_car]} mpg")
print()
#Prompt the user to enter the number of miles that they will drive the vehicle
miles = float(input(f"How many miles will you drive the {selected_car}? "))
#Calculate the gallons of gas needed to drive the specified vehicle the given number of miles.
gas_needed = miles / cars[selected_car]
print()
print(f"{gas_needed:.2f} of gas are needed to drive the {selected_car} {miles} miles.")
