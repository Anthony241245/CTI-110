# Anthony Raynor
# 11/26/24
# P5HW
# Using function to create a game
import random
def create_character():

    name = input("Enter character name: ")
    health = random.randint(135000,15000)
    inventory = []
    weapons = ["Fishing Rod", "Chains", "Ben's knives", "yo-yo", "Sword", "Boxing gloves", "Axe", "Claws", "Clubs", "Solitaire Cards", "Umbrella Sword", "Whips", "Needles", "Fans", "Ouroboros", "Aramasa" , "Blowgun" ]
    random_weapon = random.choice(weapons)
    strength = random.randint(100, 150)
    nen_type = ["Conjuration", "Manipulation", "Emission", "Transmutation", "Enhancement", "Specialization"]
    random_nen_type = random.choice(nen_type)
    print(f"Your Nen type is {nen_type}")
    print(f"Your weapon is {weapons}")
    
    



    
    

    

    character = {
        "Name":name,
        "Health":health,
        "Items":inventory,
        "Weapons": random_weapon,
        "Strength": strength,
        "Nen_type": random_nen_type,
    }
    return character 

def create_character2():

    name = input("Enter character2 name: ")
    health = random.randint(13500,15000)
    inventory = [""]
    weapons = ["Fishing Rod", "Chains", "Ben's knives", "yo-yo", "Sword", "Boxing gloves", "Axe", "Claws", "Clubs", "Solitaire Cards", "Umbrella Sword" , "Whips", "Needles", "Fans", "Ouroboros", "Aramasa", "Blowgun" ]
    random_weapon = random.choice(weapons)
    strength = random.randint(100, 150)
    nen_type = ["Conjuration", "Manipulation", "Emission", "Transmutation", "Enhancement", "Specialization"]
    random_nen_type = random.choice(nen_type)
    print(f"Your Nen type is {nen_type}")
    print(f"Your weapon is {weapons}")
    
    



    
    

    

    character = {
        "Name":name,
        "Health":health,
        "Items":inventory,
        "Weapons": random_weapon,
        "Strength": strength,
        "Nen_type": random_nen_type,
    }
    return character 



def show_stats(character):
    #Character is dictionary
    print()
    print(f"{character['Name']}'s Stats")
    print(f"Health: {character['Health']}")
    print(f"Items: {character['Items']}")
    print(f"Weapons: {character['Weapon']}")
    print(f"Strength:{character['Strength']}")
    print(f"Nen_type:{character['Nen_type']}")
    print()




def battle(char1, char2):
    print("Battle Start!")
    print(f"{char1['Name']} vs {char2['Name']}\n")


    turn = 0
    while char1["Health"] > 0 and char2['Health'] > 0:
        character = [char1, char2]
        current_player = char1 if turn % 2 == 0 else char2
        opponent = char2 if turn % 2 == 0 else char1
        random.shuffle(character)
        print(f"{current_player['Name']}'s turn!")
        print(f"1. Attack\n2. Defend\n3. Special Move")
        choice = input("Choose your action (1/2/3): ")

        if choice == "1":
            damage = random.randint(50, current_player)
       









def main():
    print("Hunter x Hunter Turn based Fighting Game")
    print()
    # Call create_character
    char1 = create_character()
    show_stats(char1)
    char2 = create_character2()
    show_stats(char2)
    battle(char1, char2)
    # Call create villain functions



if __name__ == "__main__":
    main()