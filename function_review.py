# Review of Functions
import random

def death_calc(name, age):
    average_lifespan = 80
    approx_years_left = average_lifespan - age
    print(f"Using an average lifespan of {average_lifespan}, {name} has {approx_years_left} years left to change the world for the better!!")
    possible_demise = ["choked on a grapefruit", "attacked by rabid owl", "sneezed too hard", "bunny pushed you down stairs"]
    cause = random.choice(possible_demise)
    return cause


def main():
    cause = death_calc(input("Enter your name: "), int(input("Enter your age: ")))
    print("💀💀💀💀💀💀")
    print(f"Cause of demise: {cause}")

    print("+--------+")
    print("|        |")
    print("|  RIP   |")
    print("|        |")
    print("+--------+")
    print("\n\n\nGAME OVER")


# Call the main
if __name__ == "__main__":
    main()
