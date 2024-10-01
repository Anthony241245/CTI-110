#This program simulates shopping and display receipt

#Get info for item1
item1 = input("Enter first item: ")
quantity1 = int(input(f"Enter the quantity of {item1}: "))
price1 = float(input(f"Enter the price of {item1}: "))
print()
print()
#Get info for item2
item2 = input("Enter second item: ")
quantity2 = int(input(f"Enter the quantity of {item2}: "))
price2 = float(input(f"Enter the price of {item2}: "))
print()
print()
#Get info for item3
item3 = input("Enter third item: ")
quantity3 = int(input(f"Enter the quantity of {item3}: "))
price3 = float(input(f"Enter the price of {item3}: "))
print()
#Display top of receipt
print("Thanks for shopping at Yoshi's Fizness")
print("-" * 25)
print()
item ="ITEM"
quantity="QUANTITY"
item_total="ITEM TOTAL"
print(f"{item:<20}{quantity:<15}{item_total}")
print()
print(f"{item1:<20}{quantity1:<15}${price1 * quantity1:.2f}\n")
print(f"{item2:<20}{quantity2:<15}${price2 * quantity2:.2f}\n")
print(f"{item3:<20}{quantity3:<15}${price3 * quantity3:.2f}\n")
#Calaculte subtotal
subtotal=(quantity1 * price1) + (quantity2 * price2) + (quantity3 * price3)
print(f"subtotal: ${subtotal:.2f}")


tax = 0.07 * subtotal
print(f"tax: ${tax:.2f}")
total = tax + subtotal
print(f"total: ${total:.2f}")

