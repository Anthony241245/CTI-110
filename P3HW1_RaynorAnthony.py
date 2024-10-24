# 10/24/2024
# Anthony Raynor
#P3HW1
# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
sum_of_grades = mod_1 + mod_2 + mod_3 + mod_4 + mod_5 + mod_6
print()
# TO DO: determine lowest, highest , sum and average for grades
lowest = min(grades)
highest = max(grades)

print('-----------Results-----------')
print(f"{'Lowest Grade:':<20}{min(grades)}")
print(f"{'Highest Grade:':<20}{max(grades)}")
print(f"{'Sum of Grades:':<20}{sum_of_grades:,.1f}")
average = sum(grades)/len(grades)
print(f"{'Average:':<20}{average:,.2f}")
print("-" * 40)
# determine letter grade for average


if average >=90:
    print('Your grade is: A')

elif average >=80:
     print('Your grade is: B')

elif average >=70:
     print('Your grade is: C')

elif average >=60:
     print('Your grade is: D')

else:
    print('Your grade is: F') 




