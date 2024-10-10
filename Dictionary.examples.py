#Anthony Raynor
#In-class example on dictionaries

#Create a dictionary
rose_bush = {"rose_color":"purple", "price":25.12, "max_height":60, "is_perennial":True}

#Get value, given the key
print(F'${rose_bush["price"]:.2f}')

#Get another value, given the key
print(f"Is the rose bush a pernnial? {rose_bush['is_perennial']}")
#Get value
print(F'rosh bush color is {rose_bush["rose_color"]}')

#Add a key value pair
rose_bush["water_needed"] = "4 oz per day"
#Print the entire dictionary
print(rose_bush)
#Add a key value pair
rose_bush.update({"leaf_color":"green", "sun_needed":6})
print("\n\n")
#Print dictionary update
print(rose_bush)
print('\n\n')
#Remove item from dictionary
del rose_bush["leaf_color"]
print(rose_bush)
print()
#Print all keys in dictionary
print(rose_bush.keys())
print()
#Ask the user to give key in the dictionary
answer = input("Enter a key from the dictionary: ")

#Give the value associated with the user's answer
print(F"The value for {answer} is {rose_bush[answer]}")




