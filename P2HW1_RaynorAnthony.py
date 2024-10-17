# Anthony Raynor
#10/17/2024
#P2HW1
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
print('-----------Travel Expenses----------')
print(f"{'Location:':<20}{destination}")
print(f"{'Initial Budget:':<20}${budget:,.2f}")
print(f"{'Fuel:':<20}${gas:,.2f}")
print(f"{'Accomodation:':<20}${accomodation:,.2f}")
print(f"{'Food:':<20}${food:,.2f}")
print("-" *36)

print()
 

# Subtract expenses from budget

Balance = budget - accomodation - food - gas

# Display results

print(f"{'Remaing Balance:':<20}${Balance:,.2f}")
