# Anthony Raynor
# 11/26/24
# P5HW
# Using function to create a game
import random
def create_character():


    weapon_damage = {
    "Fishing Rod": random.randint(5, 50),
    "Chains": random.randint(15, 65),
    "Ben's knives": random.randint(10, 35),
    "yo-yo": random.randint(5, 60),
    "Sword": random.randint(15, 70),
    "Boxing gloves": random.randint(10, 90),
    "Axe": random.randint(10, 67),
    "Claws": random.randint(10, 50),
    "Clubs": random.randint(10, 45),
    "Solitaire Cards": random.randint(5, 90),
    "Umbrella Sword": random.randint(5, 55),
    "Whips": random.randint(17, 42),
    "Needles": random.randint(15, 25),
    "Fans": random.randint(15, 60),
    "Ouroboros": random.randint(90,150),
    "Aramasa": random.randint(85,100),
    "Blowgun": random.randint(5, 56),
}

    name = input("Enter character name: ")
    health = random.randint(1300,1500)
    weapon = random.choice(list(weapon_damage.keys()))
    weapons = ["Fishing Rod", "Chains", "Ben's knives", "yo-yo", "Sword", "Boxing gloves", "Axe", "Claws", "Clubs", "Solitaire Cards", "Umbrella Sword", "Whips", "Needles", "Fans", "Ouroboros", "Aramasa" , "Blowgun" ]
    random_weapon = random.choice(weapons)
    damage_range = weapon_damage[weapon]
    strength = random.randint(100, 150)
    nen_type = ["Conjuration", "Manipulation", "Emission", "Transmutation", "Enhancement", "Specialization"]
    random_nen_type = random.choice(nen_type)
    print(f"Your Nen type is {random_nen_type}")
    print(f"Your weapon is {random_weapon} with a damage range {damage_range}")
    
    
    

    

    
    

    

    character = {
        "Name":name,
        "Health":health,
        "Weapons": random_weapon,
        "Strength": strength,
        "Damage_Range": damage_range,
        "Nen_type": random_nen_type,
    }


    return character 

def create_character2():

    weapon_damage = {
    "Fishing Rod": random.randint(5, 50),
    "Chains": random.randint(15, 65),
    "Ben's knives": random.randint(10, 35),
    "yo-yo": random.randint(5, 60),
    "Sword": random.randint(15, 70),
    "Boxing gloves": random.randint(10, 90),
    "Axe": random.randint(10, 67),
    "Claws": random.randint(10, 50),
    "Clubs": random.randint(10, 45),
    "Solitaire Cards": random.randint(5, 90),
    "Umbrella Sword": random.randint(5, 55),
    "Whips": random.randint(17, 42),
    "Needles": random.randint(15, 25),
    "Fans": random.randint(15, 60),
    "Ouroboros": random.randint(90,150),
    "Aramasa": random.randint(85,100),
    "Blowgun": random.randint(5, 56),
}

    name = input("Enter character2 name: ")
    health = random.randint(1300,1500)
    weapons = ["Fishing Rod", "Chains", "Ben's knives", "yo-yo", "Sword", "Boxing gloves", "Axe", "Claws", "Clubs", "Solitaire Cards", "Umbrella Sword", "Whips", "Needles", "Fans", "Ouroboros", "Aramasa" , "Blowgun" ]
    weapon = random.choice(list(weapon_damage.keys()))
    random_weapon = random.choice(weapons)
    damage_range = weapon_damage[weapon]
    strength = random.randint(100, 150)
    nen_type = ["Conjuration", "Manipulation", "Emission", "Transmutation", "Enhancement", "Specialization"]
    random_nen_type = random.choice(nen_type)
    print(f"Your Nen type is {random_nen_type}")
    print(f"Your weapon is {random_weapon} with a damage range {damage_range}")
    
    



    
    

    

    character = {
        "Name":name,
        "Health":health,
        "Weapons": random_weapon,
        "Strength": strength,
        "Damage Range": damage_range,
        "Nen_type": random_nen_type,
    }
    return character 



def show_stats(character):
    #Character is dictionary
    print()
    print(f"{character['Name']}'s Stats")
    print(f"Health: {character['Health']}")
    print(f"Weapons: {character['Weapons']}")
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
        print(f"1. Attack\n2. Defend\n3. Special Move\n4. Special_nen_damage\n5. dodge")
        choice = input("Choose your action (1/2/3/4/5): ")

        if choice == "1":
            damage = random.randint(50, current_player['Strength'])
            opponent["Health"] -= damage
            print(f"{current_player['Name']} attacked with {current_player['Weapons']}! {opponent['Name']} took {damage} damage.") 
            # Rework Healing
        elif choice == "2":
            heal = random.randint(1, 25)
            current_player["Health"] += heal
            print(f"{current_player['Name']} has healed {heal} hp")

        elif choice == "3":
            Special_weapon_damage = random.randint(80, 200)
            opponent["Health"] -= Special_weapon_damage
            print(f"{current_player['Name']} used {current_player['Weapons']} {opponent['Name']} took {Special_weapon_damage} damage.")

        elif choice =="4":
            Special_nen_damage = random.randint(100,250)
            opponent["Health"] -= Special_nen_damage
            print(f"{current_player['Name']} used {current_player['Nen_type']} ability {opponent['Name']} took {Special_nen_damage} damage.")
            # Rework dodged attacked
        elif choice =="5":
                if random.randint(1, 115) <= 20:
                    print(f"{opponent['Name']} dodged the attacked!")
                
        
        print(f"\n{char1['Name']} Health: {char1['Health']} | {char2['Name']} Health: {char2['Health']}\n")
        turn +=1


    if char1['Health'] >= 0:
            print(f"{char1['Name']}has won the battle with {char1['Health']}HP")
        
    else:
         print(f"{char2['Name']} wins the battle with {char2['Health']}HP")



       









def main():

    while True:
        print("Hunter x Hunter Turn based Fighting Game")
        print()
        # Call create_character
        print("Create Character 1")
        char1 = create_character()
        show_stats(char1)
        print("Create Character 2")
        char2 = create_character2()
        show_stats(char2)

        battle(char1, char2)
    # Call create villain functions
        rematch = input("Do you want to play again? yes or no: ").lower()
        if rematch != "yes":
            print("Thank you for playing!")
            break


if __name__ == "__main__":
    main()