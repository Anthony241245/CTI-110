# Using functions in Python

# Define a function that adds number
def add_nums(num1, num2, num3):
    result = num1 + num2 + num3
    print(result)
    


def main():
    # Min logic goes here
    print("The main is running...")
    # Call the add_numbers function
    add_nums(3,5,1)
    add_nums(0,0,0)
    add_nums("egg","bacon","bread")

# Call the main function
if __name__ == "__main__":
    main()