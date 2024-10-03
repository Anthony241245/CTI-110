
# Anthony Raynor
#9/26/2024
#P1HW2
# a program that does some basic math on numbers that are entered
print('This program calculates and displays travel expenses')
print()
#Get user comment
budget = int(input('Enter Budget: '))
print() 
# Get users travel destination
destination = str(input('Enter your travel destination: '))
print() 
# Ask user for amount they will spend on gas
gas = int(input('How much do you think you will spend on gas: '))
print()
#Ask user for amount they will spend on accommodation
accomodation = int(input('Approximately, how much will you need for accomodation/hotel: '))
print()
# Ask user for amount they will spend on food
food = int(input('Last, how much do you need for food: '))
print()
print()
# Add expenses
print('--------Travel Expenses---------')
print(f'Location: {destination}')
print(f'Initial Budget: {budget}')
print()
print(f'Fuel: {gas}')
print(f'Accomodation: {accomodation}')
print(f'Food: {food}')

print()
 

# Subtract expenses from budget

Balance = budget - accomodation - food - gas

# Display results

print(f'Remaining Balance: {Balance}')
