#Example similar to P4HW1
#Ask user how many grades
#Loop to run(that many)times
#Check to make sure grade is between 0-100
#add valid to list
#invalid scores not accepted
#List of available items
availableItems =["litter", "cat food", "feather", "collar", "toy",\
                 "litter box", "flea meds", "treats"]

num_items = int(input("How many items will you purchase: "))
#Empty list to hold valid responeses
cart = []

#Loop to get the items
for item in range(num_items):
    thisItem = input(f"enter item #{item + 1}: ")
    # Loop to ensure this item is in availableItems
    while thisItem not in availableItems:
        print(f"{thisItem} is not in stock!")
        thisItem = input(f"enter item #{item + 1} again: ")
    #Add the valid item to the cart
    cart.append(thisItem)

#loop to print each item in the cart
print()
print("Items we purchased are")
for product in cart:
    print(product)







