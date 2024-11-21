'''
# Using functions in Python

# Define a function that adds number
def add_nums(num1, num2, num3):
    result = num1 + num2 + num3
    return result
    


def main():
    # Min logic goes here
    print("The main is running...")
    # Call the add_numbers function
    resut1 = add_nums(3,5,1)
    print(resut1)
    print(add_nums(resut1,1,1))
    

# Call the main function
if __name__ == "__main__":
    main()
    '''

# Value-returning functions
import random

def getHabitat(animal):
    if animal in ["turtle", "fish", "anemone", "urchin" "jellyfish", "shark"]:
        return "ocean"
    if animal in ["iguana", "spider", "camel", "fox",  "snake"]:
        return "desert"
    if animal in ["lemur", "monkey", "tiger", "parrot" "panda", "panther", "lion"]:
        return "jungle"
    



def getFriends(habitat, numFriends):
    friends = []
    if habitat == "ocean":     
        oceanList = ["turtle", "fish", "anemone", "urchin" "jellyfish", "shark"]
        # Loop run numFriends times
        for i in range(numFriends):
             # Adding a random oceanList item to the friends list
             friends.append(random.choice(oceanList))
        return friends

    if habitat == "desert":     
        desertList = ["iguana", "spider", "camel", "fox",  "snake"]
            # Loop run numFriends times
        for i in range(numFriends):
                 # Adding a random oceanList item to the friends list
            friends.append(random.choice(desertList))
        return friends

    if habitat == "jungle":     
        jungleList = ["lemur", "monkey", "tiger", "parrot" "panda", "panther", "lion"]
        # Loop run numFriends times
        for i in range(numFriends):
             # Adding a random oceanList item to the friends list
            friends.append(random.choice(jungleList))
        return friends
           
      
        
     





# Define main
def main():
    run_again = "yes"
    while run_again.lower() =="yes":
        print("🐍🦁🐦🦚🦎")
        animal = input("Enter your favorite animal: ")
        habitat = getHabitat(animal)
        print(f"{animal} lives in the {habitat}")
        print()
        numFriends = int(input(f"How mnay friends for the {animal}?: "))
        #Call getFriends function
        friendsList = getFriends(habitat, numFriends)
        print(f"The animal has the following frinds: ")
        #Loop to display all items in friendsList
        for i in friendsList:
            print(i)
        print()
        run_again = input("Would you like to run again? Type 'yes' or 'no': ")
        
    
# Call the main
if __name__ == "__main__":
    main()