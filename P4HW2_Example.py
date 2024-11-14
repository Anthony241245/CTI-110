#Example similar to P4W using loops
#While loop to control the program
#Create variables to hold total
numItems = 0
totalCost = 0
#Variable to control the loop
product = input("Enter product name or 'exit' to terminate: ")

#While loop
while product.lower() != "exit":
    #Increment numItems by 1
    numItems += 1
    cost = float(input(f"Enter cost for {product}: "))
    totalCost += cost
    print()
    product = input("Enter product name or 'exit' to terminate: ")
#loop breaks here
print(f"Total number of items purchased: {numItems}")
print(f"Total cost of items purchased: ${totalCost}")

