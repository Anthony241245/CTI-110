#Anthony Raynor
#P4HW1
#11/12/24


scores = int(input("How many scores do you want to enter?: "))
grade = []

for grades in range(scores):
    thisScore = int(input(f"Enter score #{grades + 1}: "))
    while thisScore < 0 or thisScore > 100:
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        thisScore = int(input(f"Enter score # {grades + 1} again: "))
    grade.append(thisScore)
print()
print()
print("------------Results-----------")
lowest = min(grade)
print(f"{'Lowest Grade:':<20}{min(grade)}")
print(f"{'Modified List:':<20}{grade}")
grade.remove(lowest)
average = sum(grade)/len(grade)
print(f"{'Scores Average:':<20}{average:,.2f}")
if average >=90:
    print('Grade: A')

elif average >=80:
     print('Grade : B')

elif average >=70:
     print('Grade : C')

elif average >=60:
     print('Grade : D')

else:
    print('Grade : F') 
