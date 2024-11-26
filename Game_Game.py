# Anthony Raynor
# 11/26/24
# P5HW
# Using function to create a game
import random
def create_character():

    name = input("Enter character name: ")
    health = float(input("Enter {name}'s health: "))
    inventory = []
    weapons = []
    strength = float(input("Enter {name}'s strength: "))


    character = {
        "Name":name,
        "Health":health,
        "Items":inventory,
        "Weapons": weapons,
        "Strength": strength
    }
    return character 













def main():
    print("Game is starting...")
    print()
    # Call create_character
    char1 = create_character()
    print()
    print(char1)



if __name__ == "__main__":
    main()