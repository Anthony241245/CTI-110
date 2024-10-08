#Using python built in libraries

#import the datetime library to use it in the program
import datetime

# Assign the currennt date and time to a variable
time = datetime.datetime.now()
month = time.month


month_word = time.strftime("%B")

# Display data/time
print(f"The current data and time is {time}")
print(f"The current Month is {month}")
print(f"The current Month is {month_word}")

today = datetime.datetime.today()
print(f"Today is {today}")

weekday = today.weekday()
print(f"The day of the week is {weekday}\n")

#Get the datatype of the variables
print(type(weekday))
print()
'''
#Get day of week from user as integer
weekday = int(input("Enter an integer 0-6 as the day of week: "))
'''
# If-else statements to determine the day of the week
if weekday == 0:
    weekday_word = "Monday"

elif weekday == 1:
    weekday_word = "Tuseday"

elif weekday == 2:
    weekday_word = "Wednesday"

elif weekday == 3:
    weekday_word = "Thursday"

elif weekday == 4:
    weekday_word = "Friday"

elif weekday == 5:
    weekday_word = "Saturday"

elif weekday == 6:
    weekday_word = "Sunday"

else:
    print("invalid day of week!!!")
    weekday_word = "INVALID"
    
print()
print(f"The day of the week is {weekday_word}")
