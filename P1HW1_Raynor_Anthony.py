# Anthony
# 9/24/2024
# Get integer integer input from the user and perform math calculations

#Display output to user

print('---------Calcuulating Exponents--------------')
print()
print()

# Get info from the user
baseValue = int (input ('Enter an integer as the base value: '))

 #Get exponent
exponent = int(input('Enter an integer as the exponent: '))
print()
print()

# Calculate the value of the exponents math

result = baseValue ** exponent
#Display the results of the math
print (baseValue, 'raised to th power of', exponent, 'is', result, '! !')
print()
print()
print('---------Addition and Subtraction--------------')
print()
print()
#Get user info
startingInteger = int(input('Enter a starting integer: '))
add = int(input('Enter an integer to add: '))
subtract = int(input('Enter an integer to subtract: '))
print()
print()
#Calculate math

result2 = startingInteger + add - subtract
#Display the results
print(startingInteger, '+', add ,' - ', subtract, 'is equal to', result2)
